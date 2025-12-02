#!/bin/bash
# Deployment script for Mavus project

set -e  # Exit on error

echo "==== Mavus Deployment Script ===="
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Configuration
PROJECT_DIR="/var/www/mavus"
REPO_URL="your-git-repository-url"  # Git repository URL'nizi buraya ekleyin
BRANCH="main"

echo -e "${YELLOW}1. Pulling latest code from Git...${NC}"
cd $PROJECT_DIR
git pull origin $BRANCH

echo -e "${YELLOW}2. Activating virtual environment...${NC}"
source $PROJECT_DIR/venv/bin/activate

echo -e "${YELLOW}3. Installing/updating Python dependencies...${NC}"
pip install -r requirements.txt --upgrade

echo -e "${YELLOW}4. Running Django migrations...${NC}"
python manage.py migrate --noinput

echo -e "${YELLOW}5. Collecting static files...${NC}"
python manage.py collectstatic --noinput

echo -e "${YELLOW}6. Building frontend...${NC}"
cd $PROJECT_DIR/frontend
npm install
npm run build

echo -e "${YELLOW}7. Restarting Gunicorn service...${NC}"
sudo systemctl restart gunicorn

echo -e "${YELLOW}8. Restarting NGINX...${NC}"
sudo systemctl restart nginx

echo -e "${GREEN}==== Deployment completed successfully! ====${NC}"
echo ""
echo "Your application is now live!"
