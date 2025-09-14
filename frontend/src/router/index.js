// import { createRouter, createWebHistory } from "vue-router"
// import Login from "../views/Login.vue"
// import Signup from "../views/Signup.vue"
// import RestaurantDashboard from "../views/RestaurantDashboard.vue"
// import NgoDashboard from "../views/NgoDashboard.vue"

// const routes = [
//   { path: "/", redirect: "/login" },
//   { path: "/login", component: Login },
//   { path: "/signup", component: Signup },
//   { 
//     path: "/restaurant", 
//     component: RestaurantDashboard, 
//     meta: { requiresAuth: true, role: "restaurant" } 
//   },
//   { 
//     path: "/ngo", 
//     component: NgoDashboard, 
//     meta: { requiresAuth: true, role: "ngo" } 
//   }
// ]

// const router = createRouter({
//   history: createWebHistory(),
//   routes
// })

// // -------------------------
// // Navigation Guard
// // -------------------------
// router.beforeEach((to, from, next) => {
//   const token = localStorage.getItem("token")
//   const userRole = localStorage.getItem("role") // store role at login/signup

//   if (to.meta.requiresAuth) {
//     if (!token) {
//       return next("/login")
//     }
//     if (to.meta.role && to.meta.role !== userRole) {
//       return next("/login")
//     }
//   }
//   next()
// })

// export default router
// src/router/index.js
import { createRouter, createWebHistory } from "vue-router";
import { useAuthStore } from "@/stores/auth";

import Home from "@/views/Home.vue";
import Login from "@/views/Login.vue";
import Signup from "@/views/Signup.vue";
import RestaurantDashboard from "@/views/RestaurantDashboard.vue";
import NGODashboard from "@/views/NGODashboard.vue";

const routes = [
  { path: "/", name: "Home", component: Home },

  { path: "/login", name: "Login", component: Login },
  { path: "/signup", name: "Signup", component: Signup },

  {
    path: "/restaurant",
    name: "RestaurantDashboard",
    component: RestaurantDashboard,
    meta: { requiresAuth: true, role: "restaurant" },
  },
  {
    path: "/ngo",
    name: "NGODashboard",
    component: NGODashboard,
    meta: { requiresAuth: true, role: "ngo" },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// 🔒 Global Navigation Guard
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();

  if (to.meta.requiresAuth) {
    if (!authStore.isAuthenticated) {
      // not logged in → send to login
      return next("/login");
    }

    if (to.meta.role && authStore.userRole !== to.meta.role) {
      // wrong role → redirect home
      return next("/");
    }
  }

  next();
});

export default router;
