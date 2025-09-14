<template>
  <div class="relative min-h-screen w-full overflow-hidden bg-[#0a0a2a] text-gray-200 ">
    <div class="absolute inset-0 z-0 ">
      <div class="gradient-bg ">
        <svg xmlns="http://www.w3.org/2000/svg">
          <defs>
            <filter id="goo">
              <feGaussianBlur in="SourceGraphic" stdDeviation="10" result="blur" />
              <feColorMatrix in="blur" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 18 -8" result="goo" />
              <feBlend in="SourceGraphic" in2="goo" />
            </filter>
          </defs>
        </svg>
        <div class="gradients-container">
          <div class="g1"></div>
          <div class="g2"></div>
          <div class="g3"></div>
          <div class="g4"></div>
          <div class="g5"></div>
        </div>
      </div>
    </div>

    <div class="relative z-10 container mx-auto flex flex-col items-center justify-center min-h-screen px-6 py-12 pt-20">
      <section class="text-center w-full max-w-4xl animate-fade-in-down">
        <h1 class="text-6xl md:text-8xl font-black mb-6 tracking-tighter">
          <span class="bg-gradient-to-br from-cyan-300 via-purple-400 to-pink-500 text-transparent bg-clip-text">
            HungerFree
          </span>
        </h1>
        <p class="text-lg md:text-xl text-gray-300 mb-10 max-w-3xl mx-auto font-light">
          A revolutionary platform where compassion meets action. We unite restaurants and NGOs to transform surplus food into hope, building a world free from hunger and waste.
        </p>

        <div class="flex flex-wrap justify-center gap-6">
          <button
            @click="handleGetStarted"
            class="transform transition-all duration-300 hover:scale-105 bg-gradient-to-r from-purple-600 to-blue-500 text-white font-bold px-10 py-4 rounded-xl shadow-lg hover:shadow-purple-500/50"
          >
            Start Your Mission
          </button>
          <router-link
            v-if="!authStore.isAuthenticated"
            to="/login"
            class="transform transition-all duration-300 hover:scale-105 bg-white/10 backdrop-blur-md text-white font-semibold px-10 py-4 rounded-xl shadow-lg hover:shadow-cyan-400/30"
          >
            Member Login
          </router-link>
        </div>
      </section>

      <section class="mt-24 w-full max-w-6xl">
        <div class="grid md:grid-cols-3 gap-8 text-center">
          <div class="card group animate-fade-in-up" style="animation-delay: 0.2s;">
            <div class="text-purple-400 mb-5">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-14 w-14 mx-auto transition-transform duration-300 group-hover:scale-110" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h6m-6 4h6m-6 4h6" /></svg>
            </div>
            <h3 class="text-2xl font-bold text-white mb-3">For Restaurants</h3>
            <p class="text-gray-400">
              Become a hero in your community. Effortlessly donate surplus food, slash waste, and elevate your brand's social impact.
            </p>
          </div>

          <div class="card group animate-fade-in-up" style="animation-delay: 0.4s;">
            <div class="text-blue-400 mb-5">
               <svg xmlns="http://www.w3.org/2000/svg" class="h-14 w-14 mx-auto transition-transform duration-300 group-hover:scale-110" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M15 21v-1a6 6 0 00-5.176-5.97m0 0A_._2_._2 0 014 9.354a4 4 0 115.292 0M15 21a6 6 0 00-9-5.197" /></svg>
            </div>
            <h3 class="text-2xl font-bold text-white mb-3">For NGOs</h3>
            <p class="text-gray-400">
              Amplify your reach. Access a real-time network of food donations to efficiently nourish the communities you serve.
            </p>
          </div>
          
          <div class="card group animate-fade-in-up" style="animation-delay: 0.6s;">
            <div class="text-cyan-400 mb-5">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-14 w-14 mx-auto transition-transform duration-300 group-hover:scale-110" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13 10V3L4 14h7v7l9-11h-7z" /></svg>
            </div>
            <h3 class="text-2xl font-bold text-white mb-3">For Society</h3>
            <p class="text-gray-400">
              A collective movement. Witness the power of community as we create a sustainable, waste-free, and hunger-free future, together.
            </p>
          </div>
        </div>
      </section>

      <footer class="text-center text-gray-500 mt-24">
        <p>&copy; {{ new Date().getFullYear() }} HungerFree. Redefining Compassion.</p>
      </footer>
    </div>
  </div>
</template>

<script setup>
// The script remains unchanged
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';

const router = useRouter();
const authStore = useAuthStore();

const handleGetStarted = () => {
  if (authStore.isAuthenticated) {
    if (authStore.userRole === 'restaurant') {
      router.push('/restaurant');
    } else if (authStore.userRole === 'ngo') {
      router.push('/ngo');
    }
  } else {
    router.push('/signup');
  }
};
</script>

<style>
/* Enhanced animations and new premium styles */
@keyframes fade-in-down {
  from { opacity: 0; transform: translateY(-30px) scale(0.95); }
  to { opacity: 1; transform: translateY(0) scale(1); }
}

@keyframes fade-in-up {
  from { opacity: 0; transform: translateY(30px) scale(0.95); }
  to { opacity: 1; transform: translateY(0) scale(1); }
}

.animate-fade-in-down { animation: fade-in-down 1s ease-out forwards; }
.animate-fade-in-up { animation: fade-in-up 1s ease-out forwards; }

.card {
  background: rgba(15, 15, 45, 0.5);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 2rem;
  border-radius: 1.5rem;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.card:hover {
  transform: translateY(-10px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2), 0 0 30px rgba(128, 90, 213, 0.3);
}

/* Animated Gradient Background from https://codepen.io/AYIDouble/pen/RwrXMLz */
.gradient-bg {
  width: 100vw;
  height: 100vh;
  position: relative;
  overflow: hidden;
  background: #0a0a2a;
  top: 0;
  left: 0;
}
.gradients-container {
  filter: url(#goo) blur(40px);
  width: 100%;
  height: 100%;
}
@keyframes moveInCircle {
  0% { transform: rotate(0deg); }
  50% { transform: rotate(180deg); }
  100% { transform: rotate(360deg); }
}
@keyframes moveVertical {
  0% { transform: translateY(-50%); }
  50% { transform: translateY(50%); }
  100% { transform: translateY(-50%); }
}
@keyframes moveHorizontal {
  0% { transform: translateX(-50%) translateY(-10%); }
  50% { transform: translateX(50%) translateY(10%); }
  100% { transform: translateX(-50%) translateY(-10%); }
}
.g1, .g2, .g3, .g4, .g5 { position: absolute; mix-blend-mode: screen; }
.g1 { background: radial-gradient(circle at center, rgba(139, 114, 192, 0.3) 0, rgba(128, 90, 213, 0) 50%) no-repeat; width: 30vw; height: 30vw; top: calc(50% - 15vw); left: calc(50% - 15vw); transform-origin: center center; animation: moveVertical 30s ease infinite; }
.g2 { background: radial-gradient(circle at center, rgba(122, 196, 149, 0.3) 0, rgba(74, 222, 128, 0) 50%) no-repeat; width: 30vw; height: 30vw; top: calc(50% - 15vw); left: calc(50% - 15vw); transform-origin: calc(50% - 400px); animation: moveInCircle 20s reverse infinite; }
.g3 { background: radial-gradient(circle at center, rgba(127, 161, 202, 0.3) 0, rgba(96, 165, 250, 0) 50%) no-repeat; width: 30vw; height: 30vw; top: calc(50% - 15vw + 200px); left: calc(50% - 15vw - 500px); transform-origin: calc(50% + 400px); animation: moveInCircle 40s linear infinite; }
.g4 { background: radial-gradient(circle at center, rgba(221, 180, 147, 0.3) 0, rgba(251, 146, 60, 0) 50%) no-repeat; width: 30vw; height: 30vw; top: calc(50% - 15vw); left: calc(50% - 15vw); transform-origin: calc(50% - 200px); animation: moveHorizontal 40s ease infinite; }
.g5 { background: radial-gradient(circle at center, rgba(226, 160, 194, 0.3) 0, rgba(244, 114, 182, 0) 50%) no-repeat; width: 40vw; height: 40vw; top: calc(50% - 20vw); left: calc(50% - 20vw); transform-origin: calc(50% - 800px) calc(50% + 200px); animation: moveInCircle 20s ease infinite; }
</style>