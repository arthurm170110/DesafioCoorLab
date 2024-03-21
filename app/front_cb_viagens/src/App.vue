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

    .main-container {
    margin: 50px;
    min-height: 250px;
  }

  h1 {
    color: white;
  }

  h2 {
    text-align: center;
    font-size: 42px;
    margin-bottom: 30px;
    color: #222;
  }
</style>
