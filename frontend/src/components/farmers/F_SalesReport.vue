<template>
    <div class="sales-reports">
      <h2 class="text-2xl font-bold mb-4">Farmers Sales Reports</h2>
      
      <!-- Sales Chart -->
      <canvas ref="salesChart"></canvas>
      
      <!-- Sales Table -->
      <table class="table-auto w-full mt-6 border-collapse border border-gray-200">
        <thead>
          <tr class="bg-gray-100">
            <th class="border px-4 py-2">Farmer Name</th>
            <th class="border px-4 py-2">Product</th>
            <th class="border px-4 py-2">Quantity</th>
            <th class="border px-4 py-2">Total Price</th>
            <th class="border px-4 py-2">Date</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="sale in sales" :key="sale.id" class="text-center">
            <td class="border px-4 py-2">{{ sale.farmer }}</td>
            <td class="border px-4 py-2">{{ sale.product }}</td>
            <td class="border px-4 py-2">{{ sale.quantity }}</td>
            <td class="border px-4 py-2">{{ sale.total_price }}</td>
            <td class="border px-4 py-2">{{ sale.date }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import { ref, onMounted } from 'vue';
  import Chart from 'chart.js/auto';
  
  export default {
    setup() {
      const sales = ref([]);
      const salesChart = ref(null);
  
      const fetchSalesData = async () => {
        try {
          const response = await axios.get('http://127.0.0.1:5000/farmers/${farmerId}'); // Replace with actual API
          sales.value = response.data;
          renderChart();
        } catch (error) {
          console.error('Error fetching sales data:', error);
        }
      };
  
      const renderChart = () => {
        if (!salesChart.value) return;
        const ctx = salesChart.value.getContext('2d');
        new Chart(ctx, {
          type: 'bar',
          data: {
            labels: sales.value.map(sale => sale.date),
            datasets: [{
              label: 'Total Sales',
              data: sales.value.map(sale => sale.total_price),
              backgroundColor: 'rgba(54, 162, 235, 0.6)'
            }]
          }
        });
      };
  
      onMounted(fetchSalesData);
  
      return { sales, salesChart };
    }
  };
  </script>
  
  <style scoped>
  .sales-reports {
    max-width: 800px;
    margin: auto;
    padding: 20px;
  }
  </style>
  