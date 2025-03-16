<template>
  <div class="container">
    <!-- Farmer Profile Section -->
    <div class="profile-card">
      <img :src="profile?.profileImage || 'default-image.jpg'" alt="Profile Image">
      <div class="profile-info">
        <h2>{{ farmer.name }}</h2>
        <p class="location">{{ farmer.location }}</p>
        <a :href="`tel:${farmer.contact}`" class="contact-link">📞 Contact Farmer</a>
      </div>
    </div>

    <!-- Farmer's Products Section -->
    <div class="section">
      <h3>🌿 Products Offered</h3>
      <div class="product-grid">
        <div v-for="product in farmer.products" :key="product.id" class="product-card">
          <img :src="product.image" alt="Product Image" class="product-image" />
          <h4>{{ product.name }}</h4>
          <p class="price">${{ product.price }}</p>
          <button class="add-to-cart">🛒 Add to Cart</button>
        </div>
      </div>
    </div>

    <!-- Farmer Reviews Section -->
    <div class="section">
      <h3>⭐ Reviews</h3>
      <div v-if="farmer?.reviews?.length">
        <div v-for="review in farmer.reviews" :key="review.id" class="review-card">
          <p class="review-buyer">{{ review.buyer }}</p>
          <p class="review-text">{{ review.comment }}</p>
        </div>
      </div>
      <p v-else class="no-reviews">No reviews yet.</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { onMounted, ref } from "vue";
export default {
  name : 'FarmersProfile',
  setup() {
    const farmer = ref(null);
    const farmerId = localStorage.getItem("farmer_id"); // Get stored farmer ID
    const fetchFarmerData = async () => {
      try {
        const res = await axios.get(`http://127.0.0.1:5000/farmers/${farmerId}`, {
          headers: { Authorization: `Bearer ${localStorage.getItem("token")}` }
        });
        farmer.value = res.data;
      } catch (error) {
        console.error("Error fetching farmer data:", error);
      }
    };

    onMounted(fetchFarmerData);

    return { farmer };
  }
};
</script>

<style scoped>
/* General Container */
.container {
  width: 80%;
  margin: auto;
  font-family: Arial, sans-serif;
}

/* Profile Section */
.profile-card {
  display: flex;
  align-items: center;
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
}

.profile-image {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  margin-right: 20px;
}

.profile-info h2 {
  margin: 0;
  font-size: 22px;
}

.location {
  color: gray;
}

.contact-link {
  display: inline-block;
  margin-top: 8px;
  color: #007bff;
  text-decoration: none;
}

.contact-link:hover {
  text-decoration: underline;
}

/* Products Section */
.section {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
}

h3 {
  font-size: 20px;
  margin-bottom: 15px;
}

.product-grid {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
}

.product-card {
  width: 200px;
  padding: 10px;
  border-radius: 8px;
  border: 1px solid #ddd;
  text-align: center;
}

.product-image {
  width: 100%;
  height: 120px;
  object-fit: cover;
  border-radius: 5px;
}

.price {
  color: green;
  font-weight: bold;
}

.add-to-cart {
  background: green;
  color: white;
  padding: 5px 10px;
  border: none;
  cursor: pointer;
  border-radius: 4px;
  margin-top: 5px;
}

.add-to-cart:hover {
  background: darkgreen;
}

/* Reviews Section */
.review-card {
  padding: 10px;
  border-bottom: 1px solid #ddd;
}

.review-buyer {
  font-weight: bold;
}

.review-text {
  color: #555;
}

.no-reviews {
  color: gray;
  font-style: italic;
}
</style>
