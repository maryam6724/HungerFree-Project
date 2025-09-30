# 🍲 HungerFree

HungerFree is a food donation and request platform that connects restaurants with NGOs to reduce food wastage and fight hunger.  
Restaurants can donate surplus food, while NGOs can request and receive meals efficiently.

---

## 📑 Table of Contents
- [Features](#-features)
- [Technologies Used](#-technologies-Used)
- [Architecture Diagram](#-architecture-diagram)
- [Installation](#️-installation)
- [Usage](#️-usage)
- [API Documentation](#-api-documentation)
- [Environment Configuration](#-environment-configuration)
- [Screenshots / Demo](#-screenshots--demo)
- [Future Enhancements](#-future-enhancements)


---

## 🌟 Features
- 🔐 **Secure Authentication** (JWT-based signup/login for Restaurants & NGOs)  
- 🏪 **Restaurant Dashboard**: Add and manage food donations  
- 🏢 **NGO Dashboard**: Browse available donations and request meals  
- 🤝 **Donation Workflow**: NGO requests → Restaurant accepts → Delivery  
- 📱 **Responsive UI** built with Vue 3 + TailwindCSS  
- 🗄 **Supabase PostgreSQL Database** integration  
- 🌍 **Flask REST API** with CORS support  

---

## 🛠 Technologies Used

- **Frontend:** Vue 3, Vite, TailwindCSS, Vue Router  
- **Backend:** Flask, Flask-JWT-Extended, Flask-CORS  
- **Database:** Supabase PostgreSQL, SQLAlchemy  
- **Deployment:** Render(backend), Vercel (frontend)  
- **Tools:** GitHub

---

![HungerFree Architecture Diagram](./Architecture%20Diagram.png)


---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/hungerfree.git
cd hungerfree
```

### 2. Backend Setup
```bash
cd backend
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Mac/Linux

pip install -r requirements.txt
```


### Create .env file inside backend/
```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@db.<project-id>.supabase.co:5432/postgres
JWT_SECRET_KEY=your_secret_key
```


### Run backend
```bash
python app.py

Backend runs at: http://localhost:5000
```

### 3. Frontend Setup
```bash
cd frontend
npm install
npm run dev

Frontend runs at: http://localhost:5173
```

---

## ▶️ Usage

1. Go to `http://localhost:5173`
2. Signup as a **Restaurant** or **NGO**
3. **Restaurants** → Add surplus food donations
4. **NGOs** → View list of donations and request items
5. **Restaurants** → Accept or reject NGO requests

---

## 📡 API Documentation
```bash
Auth
POST /auth/signup → Register Restaurant/NGO
POST /auth/login → Login, receive JWT

Donations
POST /donations/add → Restaurant adds donation
GET /donations/list → NGO fetches available donations
POST /donations/request/<id> → NGO requests donation
POST /donations/accept/<id> → Restaurant accepts request
```
---

## 🌍 Environment Configuration
```bash
Required environment variables (backend/.env):
DATABASE_URL=postgresql://postgres:password@db.supabase.co:5432/postgres
JWT_SECRET_KEY=mysecret

DATABASE_URL → Supabase PostgreSQL connection string
JWT_SECRET_KEY → Secret key for JWT signing
```
----

[Screenshots / Demo](#-screenshots--demo)

## 📸 Screenshots / Demo

### Home Page
![Home Page Screenshot](frontend/public/Home.png)

### Sgn Up Page
![NGO Dashboard](frontend/public/SignUp.png)

### Restaurant Dashboard
![Restaurant Dashboard](frontend/public/Restaurant.png)

### NGO Dashboard
![NGO Dashboard](frontend/public/NGO.png)

---

## 🚀 Future Enhancements
Here are some planned improvements for HungerFree:
✅ Real-time Notifications
Push alerts when a donation is requested or accepted
✅ Geo-location Support
Match NGOs with the nearest Restaurants
✅ Analytics Dashboard
Track food donated, meals served, and reduce wastage stats
✅ Multi-language Support
Make the platform accessible for wider communities
