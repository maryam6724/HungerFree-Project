<template>
  <div class="relative min-h-screen flex items-center justify-center bg-gray-900 p-4 overflow-hidden pt-20">
     <div class="absolute inset-0 z-0 bg-gradient-to-br from-gray-900 via-purple-900/50 to-gray-900">
      <div class="stars"></div>
      <div class="twinkling"></div>
    </div>
    
    <div class="relative z-10 bg-black/30 backdrop-blur-xl border border-green-500/20 p-8 rounded-2xl shadow-2xl shadow-green-500/20 w-full max-w-md animate-fade-in-up">
      <h2 class="text-4xl font-bold mb-4 text-center text-white">Join the Movement</h2>
      <p class="text-center text-green-200 mb-8">Create an account to begin your impact.</p>

      <form @submit.prevent="handleSignup" class="space-y-6">
        <div class="relative group">
           <span class="absolute inset-y-0 left-0 flex items-center pl-4 text-gray-500 group-focus-within:text-green-400 transition-colors">
             <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" /></svg>
          </span>
          <input v-model="name" type="text" placeholder="Your Full Name or Organization" class="input-field" required />
        </div>

        <div class="relative group">
          <span class="absolute inset-y-0 left-0 flex items-center pl-4 text-gray-500 group-focus-within:text-green-400 transition-colors">
             <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 12a4 4 0 10-8 0 4 4 0 008 0zm0 0v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9m4.5-1.206a8.959 8.959 0 01-4.5 1.207" /></svg>
          </span>
          <input v-model="email" type="email" placeholder="Email Address" class="input-field" required />
        </div>

        <div class="relative group">
          <span class="absolute inset-y-0 left-0 flex items-center pl-4 text-gray-500 group-focus-within:text-green-400 transition-colors">
             <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" /></svg>
          </span>
          <input v-model="password" :type="showPassword ? 'text' : 'password'" placeholder="Create a Secure Password" class="input-field pr-12" required />
          <span class="absolute inset-y-0 right-0 flex items-center pr-4 text-gray-500 group-focus-within:text-green-400 transition-colors cursor-pointer" @click="showPassword = !showPassword">
            <svg v-if="showPassword" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.878 9.878L3 3m6.878 6.878L21 21" />
            </svg>
            <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
            </svg>
          </span>
        </div>

        <select v-model="role" class="input-field appearance-none" required>
          <option disabled value="">Select Your Role</option>
          <option value="restaurant">I'm a Restaurant</option>
          <option value="ngo">I'm an NGO</option>
        </select>

        <button
          type="submit"
          class="w-full bg-gradient-to-r from-blue-500 to-teal-400 hover:from-blue-600 hover:to-teal-500 text-white font-bold py-3 rounded-lg shadow-lg shadow-green-500/30 hover:shadow-teal-400/40 transition-all duration-300 transform hover:scale-105"
        >
          Create My Account
        </button>
      </form>

      <p class="text-center mt-8 text-gray-400">
        Already a member?
        <router-link to="/login" class="text-blue-400 font-semibold hover:text-blue-300 transition-colors">Login Here</router-link>
      </p>
    </div>
  </div>
</template>

<script setup>
// The script remains unchanged
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth";

const name = ref("");
const email = ref("");
const password = ref("");
const role = ref("");
const showPassword = ref(false);
const router = useRouter();
const authStore = useAuthStore();

const handleSignup = async () => {
  try {
    const res = await fetch("https://hungerfree-5r2b.onrender.com/auth/signup", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name: name.value,
        email: email.value,
        password: password.value,
        role: role.value,
      }),
    });

    const data = await res.json();
    if (!res.ok) throw new Error(data.error || "Signup failed");
    const user = data.user || { role: data.role, name: data.name, email: data.email };
    authStore.login(data.token, user);
    const userRole = user.role;
    if (userRole === "restaurant") router.push("/restaurant");
    if (userRole === "ngo") router.push("/ngo");
  } catch (err) {
    alert(err.message);
  }
};
</script>

<style scoped>
.input-field {
  @apply w-full pl-12 pr-4 py-3 bg-gray-900/50 border-2 border-gray-700 rounded-lg text-white placeholder-gray-500
         focus:outline-none focus:border-green-500 focus:ring-2 focus:ring-green-500/50 transition-all duration-300;
}
select.input-field {
  @apply pl-4;
}
@keyframes move-twink-back { from { background-position: 0 0; } to { background-position: -10000px 5000px; } }
.stars {
  position: absolute; top: 0; left: 0; right: 0; bottom: 0; width: 100%; height: 100%; display: block;
  background: transparent url('https://www.script-tutorials.com/demos/360/images/stars.png') repeat top center;
  z-index: 0;
}
.twinkling {
  position: absolute; top: 0; left: 0; right: 0; bottom: 0; width: 100%; height: 100%; display: block;
  background: transparent url('https://www.script-tutorials.com/demos/360/images/twinkling.png') repeat top center;
  z-index: 1;
  animation: move-twink-back 200s linear infinite;
}
.animate-fade-in-up { 
  animation: fade-in-up 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) forwards; 
}
@keyframes fade-in-up {
  from { opacity: 0; transform: translateY(40px) scale(0.95); }
  to { opacity: 1; transform: translateY(0) scale(1); }
}
</style>