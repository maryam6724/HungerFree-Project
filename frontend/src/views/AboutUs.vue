<template>
  <div class="relative min-h-screen flex items-center justify-center bg-gray-900 p-4 overflow-hidden pt-20">
    <div class="absolute inset-0 z-0 bg-gradient-to-br from-gray-900 via-purple-900/50 to-gray-900">
      <div class="stars"></div>
      <div class="twinkling"></div>
    </div>

    <div class="relative z-10 bg-black/30 backdrop-blur-xl border border-green-500/20 p-8 rounded-2xl shadow-2xl shadow-green-500/20 w-full max-w-4xl animate-fade-in-up">
      <div class="text-center">
        <h1 class="text-4xl font-bold text-white mb-6">About HungerFree</h1>
        <p class="text-lg text-gray-200 leading-relaxed mb-6">
          HungerFree is a community-driven platform that bridges the gap between
          <span class="font-semibold text-green-300">restaurants</span> with surplus food
          and <span class="font-semibold text-green-300">NGOs</span> serving people in need.
          Our mission is simple: <span class="italic">no food should go to waste, and no one should go hungry.</span>
        </p>
        <p class="text-lg text-gray-200 leading-relaxed mb-6">
          Restaurants can donate their excess food with just a few clicks, and NGOs can request
          and track donations in real time. Together, we can build a sustainable ecosystem where
          every meal finds a plate.
        </p>
        <p class="text-lg text-gray-200 leading-relaxed">
          HungerFree isn’t just a project—it’s a movement towards compassion, sustainability,
          and community support. Join us and be a part of this change.
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
// no special logic needed
</script>

<style scoped>
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
