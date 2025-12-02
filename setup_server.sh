#!/bin/bash
# Initial server setup script for Mavus project

set -e  # Exit on error

echo "==== Mavus Server Setup Script ===="
echo "This script will set up your Ubuntu/Debian server for Django + Vue.js deployment"
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root (use sudo)"
    exit 1
fi

echo -e "${YELLOW}1. Updating system packages...${NC}"
apt update && apt upgrade -y

echo -e "${YELLOW}2. Installing required packages...${NC}"
apt install -y python3 python3-pip python3-venv postgresql postgresql-contrib nginx git curl

echo -e "${YELLOW}3. Installing Node.js and npm...${NC}"
curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
apt install -y nodejs

echo -e "${YELLOW}4. Creating project directory...${NC}"
mkdir -p /var/www/mavus
mkdir -p /var/log/gunicorn
mkdir -p /var/run/gunicorn

echo -e "${YELLOW}5. Setting up PostgreSQL database...${NC}"
echo "Please enter database details:"
read -p "Database name [mavus_production]: " DB_NAME
DB_NAME=${DB_NAME:-mavus_production}

read -p "Database user [mavus_user]: " DB_USER
DB_USER=${DB_USER:-mavus_user}

read -sp "Database password: " DB_PASSWORD
echo ""

sudo -u postgres psql << EOF
CREATE DATABASE $DB_NAME;
CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';
ALTER ROLE $DB_USER SET client_encoding TO 'utf8';
ALTER ROLE $DB_USER SET default_transaction_isolation TO 'read committed';
ALTER ROLE $DB_USER SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;
\q
EOF

echo -e "${GREEN}Database created successfully!${NC}"

echo -e "${YELLOW}6. Setting up Python virtual environment...${NC}"
cd /var/www/mavus
python3 -m venv venv
source venv/bin/activate

echo -e "${YELLOW}7. Cloning repository...${NC}"
read -p "Enter your Git repository URL: " REPO_URL
git clone $REPO_URL /var/www/mavus/temp
mv /var/www/mavus/temp/* /var/www/mavus/
mv /var/www/mavus/temp/.* /var/www/mavus/ 2>/dev/null || true
rm -rf /var/www/mavus/temp

echo -e "${YELLOW}8. Installing Python dependencies...${NC}"
pip install -r requirements.txt

echo -e "${YELLOW}9. Creating .env file...${NC}"
cat > /var/www/mavus/.env << EOF
SECRET_KEY=$(python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')
DEBUG=False
DB_NAME=$DB_NAME
DB_USER=$DB_USER
DB_PASSWORD=$DB_PASSWORD
DB_HOST=localhost
DB_PORT=5432
ALLOWED_HOSTS=your-domain.com,www.your-domain.com,$(curl -s ifconfig.me)
CORS_ALLOWED_ORIGINS=https://your-domain.com,https://www.your-domain.com
EOF

echo -e "${GREEN}.env file created!${NC}"
echo "Please edit /var/www/mavus/.env and update your domain name"

echo -e "${YELLOW}10. Setting up Gunicorn service...${NC}"
cp /var/www/mavus/systemd_gunicorn.service /etc/systemd/system/gunicorn.service
systemctl daemon-reload
systemctl enable gunicorn
systemctl start gunicorn

echo -e "${YELLOW}11. Setting up NGINX...${NC}"
cp /var/www/mavus/nginx.conf /etc/nginx/sites-available/mavus
ln -s /etc/nginx/sites-available/mavus /etc/nginx/sites-enabled/
nginx -t

echo -e "${YELLOW}12. Installing Let's Encrypt for SSL...${NC}"
apt install -y certbot python3-certbot-nginx

echo -e "${YELLOW}13. Running Django migrations...${NC}"
cd /var/www/mavus
source venv/bin/activate
python manage.py migrate
python manage.py collectstatic --noinput

echo -e "${YELLOW}14. Building frontend...${NC}"
cd /var/www/mavus/frontend
npm install
npm run build

echo -e "${YELLOW}15. Setting permissions...${NC}"
chown -R www-data:www-data /var/www/mavus
chmod +x /var/www/mavus/deploy.sh

echo -e "${YELLOW}16. Restarting services...${NC}"
systemctl restart gunicorn
systemctl restart nginx

echo ""
echo -e "${GREEN}==== Setup completed successfully! ====${NC}"
echo ""
echo "Next steps:"
echo "1. Edit /var/www/mavus/.env and update your domain name"
echo "2. Edit /etc/nginx/sites-available/mavus and update your domain name"
echo "3. Point your domain to this server's IP: $(curl -s ifconfig.me)"
echo "4. Run: sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com"
echo "5. Create Django superuser: cd /var/www/mavus && source venv/bin/activate && python manage.py createsuperuser"
echo ""
echo "Your application should now be accessible at http://$(curl -s ifconfig.me)"
