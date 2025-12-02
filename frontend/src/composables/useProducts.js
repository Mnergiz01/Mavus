import { ref, computed } from 'vue'
import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000/api'

// Shared state
const products = ref([])
const categories = ref([])
const isLoading = ref(false)

export function useProducts() {
  // Fetch products
  async function fetchProducts() {
    try {
      isLoading.value = true
      const response = await axios.get(`${API_URL}/products/`)
      products.value = response.data.results || response.data
    } catch (error) {
      console.error('Error fetching products:', error)
      products.value = []
    } finally {
      isLoading.value = false
    }
  }

  // Fetch categories
  async function fetchCategories() {
    try {
      const response = await axios.get(`${API_URL}/categories/`)
      categories.value = response.data.results || response.data
    } catch (error) {
      console.error('Error fetching categories:', error)
      categories.value = []
    }
  }

  // Get parent categories (categories without a parent)
  const parentCategories = computed(() => {
    if (!Array.isArray(categories.value)) return []
    return categories.value.filter(cat => !cat.parent)
  })

  // Get all category slugs including children for filtering
  function getAllCategorySlugs(categorySlug) {
    if (!Array.isArray(categories.value)) return [categorySlug]
    const category = categories.value.find(c => c.slug === categorySlug)
    if (!category) return [categorySlug]

    const slugs = [categorySlug]
    if (category.children && category.children.length > 0) {
      category.children.forEach(child => {
        slugs.push(child.slug)
        slugs.push(...getAllCategorySlugs(child.slug))
      })
    }
    return slugs
  }

  // Get unique metal types from products
  const metalTypes = computed(() => {
    if (!Array.isArray(products.value)) return []
    const types = new Set()
    products.value.forEach(p => {
      if (p.metal_type) types.add(p.metal_type)
    })
    return Array.from(types)
  })

  // Get unique karats from products
  const karats = computed(() => {
    if (!Array.isArray(products.value)) return []
    const karatSet = new Set()
    products.value.forEach(p => {
      if (p.karat) karatSet.add(p.karat)
    })
    return Array.from(karatSet).sort((a, b) => parseInt(a) - parseInt(b))
  })

  // Get featured products
  const featuredProducts = computed(() => {
    if (!Array.isArray(products.value)) return []
    return products.value.filter(p => p.is_featured)
  })

  // Get best seller products
  const bestSellerProducts = computed(() => {
    if (!Array.isArray(products.value)) return []
    return products.value.filter(p => p.is_best_seller)
  })

  // Get recommended products
  const recommendedProducts = computed(() => {
    if (!Array.isArray(products.value)) return []
    return products.value.filter(p => p.is_recommended)
  })

  // Find product by slug
  function findProductBySlug(slug) {
    if (!Array.isArray(products.value)) return null
    return products.value.find(p => p.slug === slug)
  }

  // Find category by slug
  function findCategoryBySlug(slug) {
    if (!Array.isArray(categories.value)) return null
    return categories.value.find(c => c.slug === slug)
  }

  return {
    products,
    categories,
    isLoading,
    parentCategories,
    metalTypes,
    karats,
    featuredProducts,
    bestSellerProducts,
    recommendedProducts,
    fetchProducts,
    fetchCategories,
    getAllCategorySlugs,
    findProductBySlug,
    findCategoryBySlug
  }
}
