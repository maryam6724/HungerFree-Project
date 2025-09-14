// src/stores/auth.js
import { defineStore } from "pinia";

export const useAuthStore = defineStore("auth", {
  state: () => {
    const userItem = localStorage.getItem("user");
    return {
      token: localStorage.getItem("token") || null,
      user: userItem && userItem !== "undefined" ? JSON.parse(userItem) : null,
    };
  },

  getters: {
    isAuthenticated: (state) => !!state.token,
    userRole: (state) => state.user?.role || null,
  },

  actions: {
    // Login action (save token + user)
    login(token, user) {
      this.token = token;
      this.user = user;
      localStorage.setItem("token", token);
      localStorage.setItem("user", JSON.stringify(user));
    },

    // Logout action (clear everything)
    logout() {
      this.token = null;
      this.user = null;
      localStorage.removeItem("token");
      localStorage.removeItem("user");
    },
  },
});
