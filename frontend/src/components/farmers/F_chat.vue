<template>
    <div>
      <h2>Chat with Agrovets and clients </h2>
      <div v-for="msg in messages" :key="msg.id">{{ msg.sender }}: {{ msg.text }}</div>
      <input v-model="newMessage" placeholder="Type message..." />
      <button @click="sendMessage">Send</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    data() { return { messages: [], newMessage: "" }; },
    async mounted() { this.messages = (await axios.get("/chat")).data; },
    methods: {
      async sendMessage() {
        await axios.post("/chat", { text: this.newMessage });
        this.newMessage = ""; this.$router.go(0);
      }
    }
  };
  </script>
  