<template>
    <div>
      <h2>All Orders</h2>
      <div v-if="orders.length === 0">No orders available.</div>
      <ul>
        <li v-for="order in orders" :key="order.id">
          <strong>Farmer ID:</strong> {{ order.farmer_id }} <br>
          <strong>Buyer ID:</strong> {{ order.buyer_id }} <br>
          <strong>Product:</strong> {{ order.product_name }} <br>
          <strong>Quantity:</strong> {{ order.quantity }} <br>
          <strong>Status:</strong> {{ order.status }} <br>
          <button @click="deleteOrder(order.id)">Delete Order</button>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        orders: [],
      };
    },
    methods: {
      async fetchOrders() {
        try {
          const response = await axios.get("http://127.0.0.1:5000/orders", {
            headers: { Authorization: localStorage.getItem("token") }
          });
          this.orders = response.data;
        } catch (error) {
          console.error("Error fetching orders:", error);
        }
      },
      async deleteOrder(orderId) {
        try {
          await axios.delete(`http://127.0.0.1:5000/orders/${orderId}`, {
            headers: { Authorization: localStorage.getItem("token") }
          });
          this.fetchOrders(); // Refresh after deletion
        } catch (error) {
          console.error("Error deleting order:", error);
        }
      }
    },
    mounted() {
      this.fetchOrders();
    }
  };
  </script>
  