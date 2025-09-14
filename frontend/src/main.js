import { createApp } from "vue"
import { createPinia } from "pinia"
import App from "./App.vue"
import router from "./router"

import "./index.css" // TailwindCSS

const app = createApp(App)

// Global state management
app.use(createPinia())

// Vue Router
app.use(router)

app.mount("#app")
