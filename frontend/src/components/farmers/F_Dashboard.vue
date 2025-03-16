<template>

  <div class="dashboard-container">
    <aside class="side-bar">
      <nav>
        <ul>
          <li><router-link to="/farmers/products">Post Products</router-link></li>
          <li><router-link to="/farmers/orders">View Orders</router-link></li>
          <li><router-link to="/farmers/notifications">View Notifications</router-link></li>
          <li><router-link to="/farmers/chat">Message</router-link></li>
          <li><router-link to="/farmers/sales">View Sales</router-link></li>
          <li><router-link to="/farmers/profile">Profile</router-link></li>
        </ul>
      </nav>
    </aside>
    <main class="dashboard-content">
      <h2>Farmer Dashboard</h2>
      <div v-if="farmer">
        <p><strong>ID:</strong> {{ farmer.id }}</p>
        <p><strong>Name:</strong> {{ farmer.name }}</p>
        <p><strong>Email:</strong> {{ farmer.email }}</p>
        <p><strong>Phone:</strong> {{ farmer.phone }}</p>
        <p><strong>Location:</strong> {{ farmer.location }}</p>
      </div>
      <div v-else>
        <p>Loading...</p>
      </div>
      <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    </main>
  </div>
</template>

<script>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";

export default {
  name: "FarmersDashboard",
  setup() {
    const route = useRoute();
    const router = useRouter();
    const farmer = ref(null);
    const errorMessage = ref("");

    const fetchFarmerData = async () => {
      try {
        const token = localStorage.getItem("token");
        if (!token) {
          router.push("/farmers/login");
          return;
        }
        // Ensure route parameter name matches your router configuration
        const farmerId = route.params.id;
        const res = await axios.get(`http://127.0.0.1:5000/farmers/${farmerId}`, {
          headers: { Authorization: token }
        });
        farmer.value = res.data;
      } catch (error) {
        console.error("Error fetching farmer data:", error);
        errorMessage.value = "Failed to load dashboard data.";
      }
    };

    onMounted(() => {
      fetchFarmerData();
    });

    return { farmer, errorMessage };
  }
};
</script>

<style scoped>
.dashboard-container {
  display: flex;
  min-height: 100vh;
}

/* Sidebar styling */
.side-bar {
  width: 240px;
  background-color: #2e8b57;
  color: #fff;
  padding: 20px;
}

.side-bar nav ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.side-bar nav li {
  margin-bottom: 15px;
}

.side-bar nav li a {
  color: #fff;
  text-decoration: none;
  font-size: 16px;
  transition: color 0.3s;
}

.side-bar nav li a:hover {
  color: #d4d4d4;
}

/* Main content styling */
.dashboard-content {
  flex: 1;
  padding: 20px;
  background-color: #f7f7f7;
}

.error {
  color: red;
}
</style>
