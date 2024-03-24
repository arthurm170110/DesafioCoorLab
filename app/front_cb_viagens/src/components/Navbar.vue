<template>
    <div id="container">
        <div id="navbar">
            <img src="img/logo.png" alt="Logo" id="logo"> 
        </div>
        <div id="nav">
        </div> 
    </div>
    
</template>

<script>
    export default {
        name: 'Navbar',
    }
</script>

<style scoped>

    #container {
        display: flex;
    }

    #nav {
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.8);
        flex-grow: 1;
        
    }
    #navbar {
        background-color: #2c2c44;
        border-bottom: 4px solid #2c2c44;
        padding: 20px 20px;
        box-sizing: border-box;
        width: 22%;
    }

    #logo {
        width: 175px;
        margin: auto;
        margin-left: 0;
    }
</style>