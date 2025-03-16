<template>
  <div class="login-container">
    <h2>Farmer Login</h2>
    <form @submit.prevent="login">
      <input v-model="email" type="email" placeholder="Email" required />
      <input v-model="password" type="password" placeholder="Password" required />
      <button type="submit">Login</button>
    </form>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
  </div>
</template>

<script>
import axios from "axios";
import { ref } from "vue";
import { useRouter } from "vue-router";
import { jwtDecode } from 'jwt-decode';
export default {
  name : 'loginPage',
  setup() {
    const email = ref("");
    const password = ref("");
    const errorMessage = ref("");
    const router = useRouter();
    const login = async () => {
      try {
        console.log("Logging in with:", email.value, password.value);
        const res = await axios.post("http://127.0.0.1:5000/farmers/login", {
          email: email.value,
          password: password.value,
        });
        const token = res.data.token;
        localStorage.setItem("token", token);
        const decodedToken = jwtDecode(token);
        localStorage.setItem("farmer_id", decodedToken.id);
        router.push(`/farmers/dashboard/${decodedToken.id}`);
      } catch (error) {
        console.error("Login error:", error);
        errorMessage.value = "Invalid email or password.";
      }
    };

    return { email, password, errorMessage, login };
  }
};
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
input {
  width: 100%;
  padding: 12px;
  margin: 10px 0;
  border: 1px solid #ccc;
  border-radius: 5px;
}
button {
  background: #2E8B57;
  color: white;
  padding: 12px;
  border: none;
  width: 100%;
  font-size: 16px;
  border-radius: 5px;
  cursor: pointer;
}
.error {
  color: red;
}
</style>
