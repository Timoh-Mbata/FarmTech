<template>
    <div class="market-container">
      <h1>Marketplace</h1>
      <div class="product-grid">
        <div class="product-card" v-for="product in products" :key="product.id">
          <div class="media">
            <img
              v-if="product.media_url && isImage(product.media_url)"
              :src="product.media_url"
              alt="Product Image"
            />
            <video
              v-if="product.media_url && isVideo(product.media_url)"
              :src="product.media_url"
              controls
            ></video>
          </div>
          <div class="info">
            <h3>{{ product.name }}</h3>
            <p>{{ product.description }}</p>
            <p><strong>{{ product.price }} Ksh</strong></p>
            <button @click="addToCart(product)">Add to Cart</button>
          </div>
        </div>
      </div>
      </div>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    name : 'MainMarket',
    data() {
      return {
        // List of all products posted by farmers
        products: [],
        // Simple cart array for buyers
        cart: []
      };
    },
    async mounted() {
      await this.fetchProducts();
    },
    methods: {
      async fetchProducts() {
        try {
          // Assumes that your backend returns all products from the farmer's posts
          const response = await axios.get("http://127.0.0.1:5000/products");
          this.products = response.data;
        } catch (error) {
          console.error("Error fetching products", error);
        }
      },
      addToCart(product) {
        // Simple cart functionality – you can later expand this to use Vuex or localStorage
        this.cart.push(product);
        alert(`${product.name} added to cart!`);
      },
      isImage(url) {
        return url && url.match(/\.(jpeg|jpg|png|gif)$/i);
      },
      isVideo(url) {
        return url && url.match(/\.(mp4|avi)$/i);
      }
    }
  };
  </script>
  
  <style scoped>
  .market-container {
    max-width: 1200px;
    margin: auto;
    padding: 20px;
  }
  
  .product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    grid-gap: 20px;
  }
  
  .product-card {
    border: 1px solid #ddd;
    border-radius: 4px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }
  
  .product-card .media {
    width: 100%;
    height: 200px;
    background: #f9f9f9;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .product-card .media img,
  .product-card .media video {
    max-width: 100%;
    max-height: 100%;
  }
  
  .product-card .info {
    padding: 10px;
    text-align: center;
  }
  
  .product-card .info button {
    background-color: blue;
    color: white;
    border: none;
    padding: 8px 12px;
    cursor: pointer;
    margin-top: 10px;
  }
  
  .product-card .info button:hover {
    background-color: darkblue;
  }
  </style>
  