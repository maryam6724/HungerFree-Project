<template>
  <div class="min-h-screen bg-gray-900 text-white font-sans">
    <div class="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8 pt-20">
      <h1 class="text-5xl font-extrabold mb-8 animate-fade-in-down bg-gradient-to-r from-green-400 to-teal-300 text-transparent bg-clip-text">Restaurant Command Center</h1>

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div class="lg:col-span-1">
          <div class="dashboard-card border-green-500/50 animate-fade-in-up" style="animation-delay: 0.2s;">
            <h2 class="text-2xl font-bold text-white mb-4">Create a New Donation</h2>
            <form @submit.prevent="addDonation" class="space-y-4">
              <input v-model="foodItem" type="text" placeholder="Food Item (e.g., Vegetable Curry)" class="input-field" required />
              <input v-model="quantity" type="text" placeholder="Quantity (e.g., 5 kg)" class="input-field" required/>
              <button type="submit" class="w-full px-4 py-3 bg-gradient-to-r from-green-500 to-teal-500 text-white font-semibold rounded-lg hover:from-green-600 hover:to-teal-600 shadow-lg hover:shadow-green-500/40 transition-all transform hover:scale-105">Add Donation</button>
            </form>
          </div>
        </div>

        <div class="lg:col-span-2">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="dashboard-card border-green-500/50 animate-fade-in-up" style="animation-delay: 0.4s;">
              <h3 class="text-xl font-bold text-white mb-4">Available</h3>
              <div v-if="donations.filter(d => d.status === 'available').length > 0" class="max-h-80 overflow-y-auto pr-2">
                <ul class="space-y-3">
                  <li v-for="d in donations.filter(d => d.status === 'available')" :key="d.id" class="list-item">
                    <div>
                      <strong class="text-lg text-gray-100">{{ d.food_item }}</strong>
                      <p class="text-gray-400">Quantity: {{ d.quantity }}</p>
                    </div>
                    <span :class="statusBadgeClass(d.status)" class="status-badge">{{ d.status }}</span>
                  </li>
                </ul>
              </div>
              <p v-else class="empty-state">No donations are currently available.</p>
            </div>

            <div class="dashboard-card border-yellow-500/50 animate-fade-in-up" style="animation-delay: 0.6s;">
              <h3 class="text-xl font-bold text-white mb-4">Requested</h3>
              <div v-if="donations.filter(d => d.status === 'requested').length > 0" class="max-h-80 overflow-y-auto pr-2">
                <ul class="space-y-3">
                  <li v-for="d in donations.filter(d => d.status === 'requested')" :key="d.id" class="list-item">
                    <div>
                      <strong class="text-lg text-gray-100">{{ d.food_item }}</strong>
                      <p class="text-gray-400">NGO: {{ d.ngo_name || 'Pending' }}</p>
                    </div>
                    <button @click="updateDonation(d.id, 'accepted')" class="action-button bg-green-500 hover:bg-green-600 shadow-green-500/30">Accept</button>
                  </li>
                </ul>
              </div>
              <p v-else class="empty-state">No pending requests.</p>
            </div>

            <div class="dashboard-card border-blue-500/50 animate-fade-in-up" style="animation-delay: 0.8s;">
              <h3 class="text-xl font-bold text-white mb-4">Accepted</h3>
              <div v-if="donations.filter(d => d.status === 'accepted').length > 0" class="max-h-80 overflow-y-auto pr-2">
                <ul class="space-y-3">
                  <li v-for="d in donations.filter(d => d.status === 'accepted').sort((a,b) => new Date(b.created_at) - new Date(a.created_at))" :key="d.id" class="list-item">
                    <div>
                      <strong class="text-lg text-gray-100">{{ d.food_item }}</strong>
                      <p class="text-gray-400">NGO: {{ d.ngo_name }}</p>
                    </div>
                    <button @click="updateDonation(d.id, 'completed')" class="action-button bg-blue-500 hover:bg-blue-600 shadow-blue-500/30">Complete</button>
                  </li>
                </ul>
              </div>
              <p v-else class="empty-state">No donations accepted yet.</p>
            </div>

            <div class="dashboard-card border-gray-500/50 animate-fade-in-up" style="animation-delay: 1s;">
              <h3 class="text-xl font-bold text-white mb-4">Completed</h3>
              <div v-if="donations.filter(d => d.status === 'completed').length > 0" class="max-h-80 overflow-y-auto pr-2">
                <ul class="space-y-3">
                  <li v-for="d in donations.filter(d => d.status === 'completed').sort((a,b) => new Date(b.created_at) - new Date(a.created_at))" :key="d.id" class="list-item">
                     <div>
                      <strong class="text-lg text-gray-100">{{ d.food_item }}</strong>
                      <p class="text-gray-400">NGO: {{ d.ngo_name }}</p>
                    </div>
                    <span :class="statusBadgeClass(d.status)" class="status-badge">{{ d.status }}</span>
                  </li>
                </ul>
              </div>
              <p v-else class="empty-state">No completed donations.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
// The script remains unchanged
import { ref, onMounted, onUnmounted } from "vue"
import api from "@/service/api"
import io from 'socket.io-client'

const donations = ref([])
const foodItem = ref("")
const quantity = ref("")
const socket = io('https://hungerfree-5r2b.onrender.com')

const fetchDonations = async () => {
  const res = await api.get("/donations")
  donations.value = res.data
}

const addDonation = async () => {
  await api.post("/donations", { food_item: foodItem.value, quantity: quantity.value })
  foodItem.value = ""
  quantity.value = ""
  fetchDonations()
}

const updateDonation = async (id, status) => {
  await api.put(`/donations/${id}`, { status })
  fetchDonations()
}

const statusBadgeClass = (status) => {
  const classes = {
    available: 'bg-green-500/20 text-green-300',
    requested: 'bg-yellow-500/20 text-yellow-300',
    accepted: 'bg-blue-500/20 text-blue-300',
    completed: 'bg-gray-500/20 text-gray-400',
  };
  return classes[status] || 'bg-gray-700 text-gray-300';
};

onMounted(() => {
  fetchDonations()
  socket.on('donation_update', () => {
    fetchDonations()
  })
})

onUnmounted(() => {
  socket.disconnect()
})
</script>

<style scoped>
/* Dashboard specific styles */
.dashboard-card {
  @apply bg-gray-800/50 backdrop-blur-sm border rounded-2xl p-6 shadow-2xl;
}
.input-field {
  @apply w-full p-3 bg-gray-800 border-2 border-gray-700 rounded-lg focus:outline-none 
         focus:border-green-500 focus:ring-1 focus:ring-green-500 transition-all text-white;
}
.list-item {
  @apply bg-gray-800 rounded-xl p-4 flex justify-between items-center transition-all 
         hover:shadow-lg hover:bg-gray-700/80 transform hover:-translate-y-1;
}
.empty-state {
  @apply text-gray-500 text-center py-8;
}
.action-button {
  @apply px-4 py-2 text-white text-sm font-semibold rounded-md transition-all shadow-md hover:shadow-lg;
}
.status-badge {
  @apply px-3 py-1 text-xs font-semibold rounded-full;
}

/* Animations */
@keyframes fade-in-down {
  from { opacity: 0; transform: translateY(-20px); }
  to { opacity: 1; transform: translateY(0); }
}
@keyframes fade-in-up {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
.animate-fade-in-down { animation: fade-in-down 0.8s ease-out forwards; }
.animate-fade-in-up { animation: fade-in-up 0.8s ease-out forwards; }
</style>