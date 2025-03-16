<template>
  <div class="dashboard">
    <h2>Manage Products</h2>
    <!-- Add / Edit Product Form -->
    <form @submit.prevent="saveProduct" enctype="multipart/form-data">
      <input type="text" v-model="product.name" placeholder="Product Name" required />
      <input type="number" v-model="product.price" placeholder="Price (Ksh)" required />
      <input type="text" v-model="product.description" placeholder="Description" required />
      <input type="file" @change="handleFileUpload" accept="image/*, video/*" />
      <button type="submit">{{ isEditing ? "Update" : "Add" }} Product</button>
    </form>
    <!-- Products List -->
    <ul class="product-list">
      <li v-for="p in products" :key="p.id">
        <span>{{ p.name }} - {{ p.price }} Ksh</span>

        <!-- Display media (Image or Video) -->
        <img v-if="p.media_url && isImage(p.media_url)" :src="p.media_url" alt="Product Image" />
        <video v-if="p.media_url && isVideo(p.media_url)" :src="p.media_url" controls></video>

        <div class="actions">
          <button @click="editProduct(p)">Edit</button>
          <button @click="deleteProduct(p.id)">Delete</button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name:'farmersProducts',
  data() {
    return {
      product: { name: '', price: '', description: '' },
      file: null,
      products: [],
      isEditing: false
    };
  },
  async mounted() {
    await this.fetchProducts();
  },
  methods: {
    async fetchProducts() {
      const farmerId = localStorage.getItem("farmer_id");
      if (!farmerId) {
        return alert("Farmer ID missing!");
      }
      try {
        const response = await axios.get(`http://127.0.0.1:5000/farmers/${farmerId}/products`);
        this.products = response.data;
      } catch (error) {
        console.error("Error fetching products", error);
      }
    },
    handleFileUpload(event) {
      this.file = event.target.files[0];
    },
    async saveProduct() {
      const farmerId = localStorage.getItem("farmer_id");
      if (!farmerId) {
        return alert("Farmer ID missing!");
      }
      try {
        const formData = new FormData();
        formData.append("name", this.product.name);
        formData.append("price", this.product.price);
        formData.append("description", this.product.description);
        if (this.file) {
          formData.append("file", this.file);
        }
        if (this.isEditing) {
          // Update an existing product
          await axios.put(`http://127.0.0.1:5000/products/${this.product.id}`, formData, {
            headers: { "Content-Type": "multipart/form-data" }
          });
          alert("Product updated!");
        } else {
          // Create a new product for the farmer
          await axios.post(`http://127.0.0.1:5000/farmers/${farmerId}/products`, formData, {
            headers: { "Content-Type": "multipart/form-data" }
          });
          alert("Product added!");
        }
        // Reset form and state
        this.product = { name: '', price: '', description: '' };
        this.file = null;
        this.isEditing = false;
        await this.fetchProducts();
      } catch (error) {
        console.error("Error saving product", error);
        alert("Error saving product");
      }
    },
    editProduct(p) {
      // Fill the form with selected product data and switch to edit mode
      this.product = { ...p };
      this.isEditing = true;
    },
    async deleteProduct(productId) {
      try {
        await axios.delete(`http://127.0.0.1:5000/products/${productId}`);
        alert("Product deleted!");
        await this.fetchProducts();
      } catch (error) {
        console.error("Error deleting product", error);
        alert("Error deleting product");
      }
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
.dashboard {
  max-width: 600px;
  margin: auto;
  text-align: center;
}
form {
  margin-bottom: 20px;
}
input {
  display: block;
  margin: 10px auto;
  padding: 8px;
  width: 80%;
}
button {
  background-color: green;
  color: white;
  padding: 8px 12px;
  border: none;
  cursor: pointer;
  margin: 5px;
}
button:hover {
  background-color: darkgreen;
}
.product-list {
  list-style: none;
  padding: 0;
}
.product-list li {
  background: #f4f4f4;
  padding: 10px;
  margin: 5px 0;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.product-list li span {
  font-weight: bold;
}
.actions {
  margin-top: 10px;
}
img {
  max-width: 100px;
  max-height: 100px;
  margin: 10px 0;
}
video {
  max-width: 150px;
  max-height: 100px;
  margin: 10px 0;
}
</style>
