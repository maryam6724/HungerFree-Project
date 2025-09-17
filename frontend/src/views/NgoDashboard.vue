<template>
  <div class="min-h-screen bg-gray-900 text-white font-sans">
    <div class="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8 pt-20">
      <h1 class="text-5xl font-extrabold text-white mb-8 animate-fade-in-down">
        <span class="bg-gradient-to-r from-purple-400 to-blue-400 text-transparent bg-clip-text">NGO Operations Hub</span>
      </h1>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div class="dashboard-card border-green-500/50 animate-fade-in-up" style="animation-delay: 0.2s;">
          <h2 class="text-2xl font-bold text-white mb-4">Available Donations</h2>
          <div v-if="donations.filter(d => d.status === 'available').length > 0" class="max-h-96 overflow-y-auto pr-2">
            <ul class="space-y-3">
              <li v-for="d in donations.filter(d => d.status === 'available')" :key="d.id" class="list-item">
                 <div class="flex-grow">
                  <strong class="text-lg text-gray-100">{{ d.food_item }}</strong>
                  <p class="text-sm text-gray-400">Quantity: {{ d.quantity }}</p>
                  <p class="text-sm text-gray-400">From: {{ d.restaurant_name }}</p>
                </div>
                <button v-if="d.status === 'available'" @click="requestDonation(d.id)" class="action-button bg-green-500 hover:bg-green-600 shadow-green-500/30">
                  Request
                </button>
              </li>
            </ul>
          </div>
          <p v-else class="empty-state">No donations are available. Check back soon for new opportunities.</p>
        </div>
        
        <div class="dashboard-card border-blue-500/50 animate-fade-in-up" style="animation-delay: 0.4s;">
          <h2 class="text-2xl font-bold text-white mb-4">My Requests</h2>
          <div v-if="myRequests.length > 0" class="max-h-96 overflow-y-auto pr-2">
            <ul class="space-y-3">
              <li v-for="d in myRequests" :key="d.id" class="list-item">
                <div class="flex-grow">
                  <strong class="text-lg text-gray-100">{{ d.food_item }}</strong>
                  <p class="text-sm text-gray-400">Quantity: {{ d.quantity }}</p>
                  <p class="text-sm text-gray-400">From: {{ d.restaurant_name }}</p>
                </div>
                <span :class="statusBadgeClass(d.status)" class="status-badge">
                  {{ d.status }}
                </span>
              </li>
            </ul>
          </div>
          <p v-else class="empty-state">You haven't made any requests yet. Find a donation to get started.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
// The script remains unchanged
import { ref, onMounted, onUnmounted, computed } from "vue"
import api from "@/service/api"
import io from 'socket.io-client'

const donations = ref([])
const socket = io('https://hungerfree-5r2b.onrender.com')

const fetchDonations = async () => {
  const res = await api.get("/donations")
  donations.value = res.data.sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
}

const requestDonation = async (id) => {
  await api.put(`/donations/${id}/request`, {})
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

const myRequests = computed(() => {
  const statusOrder = { requested: 1, accepted: 2, completed: 3 };
  return donations.value
    .filter(d => ['requested', 'accepted', 'completed'].includes(d.status))
    .sort((a, b) => {
      if (statusOrder[a.status] !== statusOrder[b.status]) {
        return statusOrder[a.status] - statusOrder[b.status];
      }
      return new Date(b.created_at) - new Date(a.created_at);
    });
});

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
.list-item {
  @apply bg-gray-800 rounded-xl p-4 flex justify-between items-center transition-all 
         hover:shadow-lg hover:bg-gray-700/80 transform hover:-translate-y-1;
}
.empty-state {
  @apply text-gray-500 text-center py-12 px-4;
}
.action-button {
  @apply px-4 py-2 text-white text-sm font-semibold rounded-md transition-all shadow-md hover:shadow-lg;
}
.status-badge {
  @apply px-3 py-1 text-xs font-semibold rounded-full min-w-[80px] text-center;
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