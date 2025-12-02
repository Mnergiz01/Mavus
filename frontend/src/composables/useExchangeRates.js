import { ref } from 'vue'
import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000/api'

// Shared state
const exchangeRates = ref(null)
const ratesLoading = ref(false)

export function useExchangeRates() {
  async function fetchExchangeRates() {
    try {
      ratesLoading.value = true
      const response = await axios.get(`${API_URL}/exchange-rates/`)
      // Extract rates from response data
      exchangeRates.value = response.data.rates
    } catch (error) {
      console.error('Error fetching exchange rates:', error)
    } finally {
      ratesLoading.value = false
    }
  }

  return {
    exchangeRates,
    ratesLoading,
    fetchExchangeRates
  }
}
