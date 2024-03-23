<template>
    <div id="sidebar">
        <div id="icon-text">
            <img src="img/calculator.png" id="calc-icon">
            <h1>Calculadora de Viagem</h1>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Sidebar',
    }

</script>


<style scoped>
    #sidebar {
        background-color: #2c2c44;
        padding: 20px 20px;
        box-sizing: border-box;
        width: 22%;
        height: 100vh;
        position: fixed;
    }

    #icon-text {
        display: flex;
        align-items: center;
    }

    #calc-icon {
        width: 25px;
        margin-right: 10px;
        filter: invert(1);
    }

    h1{
        font-size: 20px;
        white-space: nowrap;
    }

</style>