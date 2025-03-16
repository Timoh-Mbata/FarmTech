import { createRouter, createWebHistory } from 'vue-router';
import F_Register from '@/components/farmers/F_Register.vue';
import loginPage from '@/components/farmers/F_Login.vue';
import FarmersDashboard from '@/components/farmers/F_Dashboard.vue';
import farmersProducts from '@/components/farmers/F_Products.vue';
import F_Orders from '@/components/farmers/F_Orders.vue';
import FarmersProfile from '@/components/farmers/F_Profile.vue';
import HomePage from '@/HomePage.vue';
import buyersOrders from '@/components/buyers/buyersOrders.vue';
import AdminsOrders from '@/components/admin/AdminsOrders.vue';
import MainMarket from '@/components/farmers/MainMarket.vue';
const routes = [
  {path : '/', component: HomePage},
  { path: '/farmers/register', component: F_Register },
  { path: '/farmers/login', component: loginPage },
  { path: '/farmers/dashboard/:id', component: FarmersDashboard },
  { path: '/farmers/products', component: farmersProducts },
  {path: '/farmers/orders',component :F_Orders},
  {path: '/farmers/profile',component :FarmersProfile},
  {path: '/admin/orders',component : AdminsOrders},
  {path: '/buyers/orders',component : buyersOrders},
  {path: '/Market' ,component: MainMarket},
];
const router = createRouter({
  history: createWebHistory(),
  routes
});
export default router;
