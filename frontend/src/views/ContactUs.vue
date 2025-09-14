<template>
  <div class="relative min-h-screen flex items-center justify-center bg-gray-900 p-4 overflow-hidden pt-20">
    <div class="absolute inset-0 z-0 bg-gradient-to-br from-gray-900 via-purple-900/50 to-gray-900">
      <div class="stars"></div>
      <div class="twinkling"></div>
    </div>

    <div class="relative z-10 bg-black/30 backdrop-blur-xl border border-green-500/20 p-8 rounded-2xl shadow-2xl shadow-green-500/20 w-full max-w-2xl animate-fade-in-up">
      <h1 class="text-3xl font-bold text-white mb-6 text-center">Contact Us</h1>
      <p class="text-center text-gray-300 mb-8">
        Have questions or want to collaborate with HungerFree? Get in touch with us.
      </p>

      <form class="space-y-6">
        <div>
          <label class="block text-gray-300 mb-2">Name</label>
          <input type="text" placeholder="Your name"
            class="w-full border border-gray-700 rounded-lg p-3 bg-gray-900 text-gray-200 focus:ring-2 focus:ring-green-400 focus:outline-none" />
        </div>

        <div>
          <label class="block text-gray-300 mb-2">Email</label>
          <input type="email" placeholder="you@example.com"
            class="w-full border border-gray-700 rounded-lg p-3 bg-gray-900 text-gray-200 focus:ring-2 focus:ring-green-400 focus:outline-none" />
        </div>

        <div>
          <label class="block text-gray-300 mb-2">Message</label>
          <textarea rows="4" placeholder="Write your message..."
            class="w-full border border-gray-700 rounded-lg p-3 bg-gray-900 text-gray-200 focus:ring-2 focus:ring-green-400 focus:outline-none"></textarea>
        </div>

        <button type="submit"
          class="w-full bg-gradient-to-r from-green-500 to-teal-400 hover:from-green-600 hover:to-teal-500 text-white py-3 rounded-lg font-semibold transition">
          Send Message
        </button>
      </form>

      <div class="mt-10 text-center text-gray-400">
        <p>Email: <span class="font-medium text-blue-400">support@hungerfree.org</span></p>
        <p>Phone: <span class="font-medium text-blue-400">+91 98765 43210</span></p>
      </div>
    </div>
  </div>
</template>

<script setup>
// static form, later you can hook it to backend/email service
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
