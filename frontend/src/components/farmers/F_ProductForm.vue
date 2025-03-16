<template>
    <div>
      <h2>Manage Products</h2>
      <form @submit.prevent="saveProduct">
        <input v-model="product.name" placeholder="Product Name" />
        <input type="number" v-model="product.price" placeholder="Price (Ksh)" />
        <input v-model="product.description" placeholder="Description" />
        <button type="submit">{{ isEditing ? "Update" : "Add" }} Product</button>
      </form>
      <ul>
        <li v-for="p in products" :key="p.id">
          {{ p.name }} - {{ p.price }} Ksh
          <button @click="editProduct(p)">Edit</button>
          <button @click="deleteProduct(p.id)">Delete</button>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    data() {
      return { products: [], product: {}, isEditing: false };
    },
    async mounted() {
      this.products = (await axios.get("/products")).data;
    },
    methods: {
      async saveProduct() {
        if (this.isEditing) {
          await axios.put(`/products/${this.product.id}`, this.product);
        } else {
          await axios.post("/products", this.product);
        }
        this.product = {}; this.isEditing = false; this.$router.go(0);
      },
      editProduct(p) { this.product = { ...p }; this.isEditing = true; },
      async deleteProduct(id) { await axios.delete(`/products/${id}`); this.$router.go(0); }
    }
  };
  </script>
  