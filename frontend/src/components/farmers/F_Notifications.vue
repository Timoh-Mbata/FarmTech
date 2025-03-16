<template>
    <div>
      <h2>Notifications</h2>
      <ul>
        <li v-for="notification in notifications" :key="notification.id">
          {{ notification.message }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    data() { return { notifications: [] }; },
    async mounted() { this.notifications = (await axios.get("/notifications")).data; }
  };
  </script>
  