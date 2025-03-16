<template>
  <div class="container">
    <div class="registerFarmer">
      <h2>Register as a Farmer</h2>
      <form @submit.prevent="registerFarmer">
        <input v-model="farmer.name" placeholder="Name" required />
        <input v-model="farmer.email" type="email" placeholder="Email" required />
        <input v-model="farmer.phone" type="tel" placeholder="Phone" required />
        <input v-model="farmer.location" placeholder="Location" required />
        <input v-model="farmer.password" type="password" placeholder="Password" required />
        <button type="submit">Register</button>
      </form>
      <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      farmer: {
        name: '',
        email: '',
        phone: '',
        location: '',
        password: ''
      },
      errorMessage: ''
    };
  },
  methods: {
    async registerFarmer() {
      try {
        console.log("Sending Data:", this.farmer);
        const response = await axios.post(
          'http://127.0.0.1:5000/farmers/register',
          this.farmer,
          { headers: { "Content-Type": "application/json" } }
        );
        alert(response.data.message);
        this.$router.push('/farmers/login');
      } catch (error) {
        console.error("Error:", error.response ? error.response.data : error);
        this.errorMessage = error.response ? error.response.data.error : 'Registration failed';
      }
    }
  }
};
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
.registerFarmer {
  background: white;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
  width: 100%;
  max-width: 400px;
  text-align: center;
}
input {
  width: 100%;
  padding: 10px;
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
