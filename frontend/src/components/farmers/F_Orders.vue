<template>
  <div>
    <h2>My Orders</h2>
    <div v-if="orders.length === 0">No orders available.</div>
    <ul>
      <li v-for="order in orders" :key="order.id">
        <strong>Product:</strong> {{ order.product_name }} <br>
        <strong>Quantity:</strong> {{ order.quantity }} <br>
        <strong>Total Price:</strong> ${{ order.total_price }} <br>
        <strong>Status:</strong> {{ order.status }}
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
      buyerId: localStorage.getItem("buyer_id"),
    };
  },
  methods: {
    async fetchOrders() {
      try {
        const response = await axios.get(`http://127.0.0.1:5000/orders/buyer/${this.buyerId}`, {
          headers: { Authorization: localStorage.getItem("token") }
        });
        this.orders = response.data;
      } catch (error) {
        console.error("Error fetching orders:", error);
      }
    }
  },
  mounted() {
    this.fetchOrders();
  }
};
</script>
