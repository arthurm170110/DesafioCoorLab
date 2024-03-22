<template>
  <div>
    <Navbar/>
    <Sidebar/>
    <router-view/>
  </div>
</template>

<script>
  import Navbar from './components/Navbar.vue'
  import Sidebar from './components/Sidebar.vue'

  export default {
    name: 'App',
    components: {
      Navbar,
      Sidebar,
    }
  }

</script>

<style>
   * {
    font-family: Helvetica;
    padding: 0;
    margin: 0;
    box-sizing: border-box;
  }

  h1 {
    color: white;
  }

</style>
