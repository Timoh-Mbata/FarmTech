<template>
  <div class="home">
    <!-- Hero Section -->
    <header class="hero">
      <div class="overlay">
        <h1>Empowering Farmers, Connecting Markets</h1>
        <p>Your one-stop platform for seamless agricultural trade</p>
        <router-link to="/farmers/register" class="cta-button">Join the Community</router-link>
        <router-link to="/Market" class="cta-button">Explore Markets</router-link>
      </div>
    </header>

    <!-- Features Section -->
    <section class="features">
      <div class="feature">
        <img src="@/assets/cart.png" alt="Buy & Sell">
        <h2>Buy & Sell with Ease</h2>
        <p>Farmers can showcase their produce, and buyers can connect directly—no middlemen, just fair trade.</p>
      </div>
      
      <div class="feature">
        <img src="@/assets/analysis.png" alt="Insights">
        <h2>Real-time Market Insights</h2>
        <p>Stay ahead with real-time agricultural trends, pricing updates, and expert insights to make informed decisions.</p>
      </div>
      
      <div class="feature">
        <img src="@/assets/credit-card.png" alt="Secure Transactions">
        <h2>Secure & Transparent Transactions</h2>
        <p>Trust is our priority! Verified buyers and sellers ensure safe transactions with complete transparency.</p>
      </div>
    </section>

    <!-- Call to Action Section -->
    <section class="cta-section">
      <h2>Join Thousands of Farmers and Buyers</h2>
      <p>Unlock new opportunities in agriculture with our trusted distribution network.</p>
      <router-link to="/farmers/register" class="cta-button">Get Started Now</router-link>
    </section>
  </div>
</template>

<script>
export default {
  name: 'HomePage'
}
</script>

<style scoped>
/* General Styles */
.home {
  font-family: 'Poppins', sans-serif;
  text-align: center;
}

/* Hero Section */
.hero {
  position: relative;
  background: url('@/assets/287531350249b526398157d6d0d9c01c.jpg') center/cover no-repeat;
  height: 400px;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  color: white;
}

.overlay {
  background: rgba(0, 0, 0, 0.6);
  padding: 40px;
  border-radius: 10px;
}

.hero h1 {
  font-size: 2.5rem;
  margin-bottom: 10px;
}

.hero p {
  font-size: 1.2rem;
  margin-bottom: 20px;
}

/* CTA Button */
.cta-button {
  display: inline-block;
  padding: 10px 20px;
  background: #28a745;
  color: white;
  text-decoration: none;
  border-radius: 8px;
  font-weight: bold;
  transition: background 0.3s ease-in-out;
}

.cta-button:hover {
  background: #218838;
}

/* Features Section */
.features {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  padding: 50px 20px;
  gap: 30px;
}

.feature {
  background: white;
  padding: 20px;
  max-width: 320px;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  text-align: center;
  transition: transform 0.3s ease-in-out;
}

.feature:hover {
  transform: translateY(-5px);
}

.feature img {
  width: 60px;
  margin-bottom: 15px;
}

/* CTA Section */
.cta-section {
  background: #f8f9fa;
  padding: 50px 20px;
}

.cta-section h2 {
  font-size: 2rem;
  margin-bottom: 10px;
}

.cta-section p {
  font-size: 1.2rem;
  margin-bottom: 20px;
}
</style>
