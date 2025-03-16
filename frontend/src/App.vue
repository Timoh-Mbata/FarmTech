<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link>
      <router-link to="/farmers/login">Login</router-link>
      <router-link to="/farmers/register">Register</router-link>
      <router-link to="/farmers/dashboard">Dashboard</router-link>
    </nav>

    <router-view></router-view>

    <footer>
      <p>&copy; 2025 Agriculture Distribution Platform. All rights reserved.</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
}

nav {
  background: #4CAF50;
  padding: 10px;
  display: flex;
  justify-content: center;
  gap: 15px;
}

nav a {
  color: white;
  text-decoration: none;
  font-weight: bold;
}

nav a:hover {
  text-decoration: underline;
}

footer {
  margin-top: 20px;
  padding: 10px;
  background: #f1f1f1;
  color: #333;
}
</style>
