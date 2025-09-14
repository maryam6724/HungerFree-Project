<template>
  <nav class="fixed w-full top-0 z-50 bg-black/30 backdrop-blur-xl border-b border-white/10 shadow-lg">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-20">
        <router-link to="/" class="text-3xl font-black tracking-tighter transition-transform hover:scale-105">
           <span class="bg-gradient-to-r from-cyan-400 via-purple-400 to-pink-500 text-transparent bg-clip-text">
            HungerFree
          </span>
        </router-link>

        <div class="flex items-center gap-4">
          <template v-if="isAuthenticated">
            <span class="text-gray-300 hidden sm:block">Welcome, <strong class="font-medium">{{ authStore.user?.name }}</strong>!</span>
            
            <router-link
              :to="dashboardLink"
              class="nav-link"
            >
              My Dashboard
            </router-link>

            <button
              @click="handleLogout"
              class="action-button bg-gradient-to-r from-orange-500 to-red-500 hover:from-orange-600 hover:to-red-600 shadow-red-500/30"
            >
              Logout
            </button>
          </template>

          <template v-else>
            <router-link to="/login" class="nav-link">
              Login
            </router-link>
            <router-link to="/about" class="nav-link">
              About Us
            </router-link>
            <router-link to="/contact" class="nav-link">
              Contact Us
            </router-link>
            <router-link
              to="/signup"
              class="action-button bg-gradient-to-r from-purple-500 to-blue-500 hover:from-purple-600 hover:to-blue-600 shadow-blue-500/30"
            >
              Get Started
            </router-link>
          </template>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { computed } from 'vue';
import { useAuthStore } from "@/stores/auth";
import { useRouter } from "vue-router";

const authStore = useAuthStore();
const router = useRouter();

// Expose store state as a reactive property
const isAuthenticated = computed(() => authStore.isAuthenticated);

// Determine the correct dashboard link based on user role
const dashboardLink = computed(() => {
  const role = authStore.user?.role;
  if (role === 'restaurant') return '/restaurant';
  if (role === 'ngo') return '/ngo';
  return '/'; // Fallback link
});

// Logout function
const handleLogout = () => {
  authStore.logout();
  router.push("/login");
};
</script>

<style scoped>
.nav-link {
  @apply text-gray-300 font-medium px-3 py-2 rounded-md text-sm hover:bg-white/10 transition-colors duration-300;
}

.action-button {
  @apply text-white font-semibold px-5 py-2 rounded-lg shadow-lg hover:shadow-xl transition-all duration-300 transform hover:scale-105;
}
</style>