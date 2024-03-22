<template>
    <div id="titulo-home">
      <div id="titulo">
            <img src="img/caminhao-de-entrega.png" id="car-icon">
            <h1>Calculadora de Viagem</h1>
      </div>
  </div>
</template>


<script>

    export default {
        name: 'Title',    
    }

</script>

<style scoped>
    #titulo-home {
    margin: 50px 50px 0 400px;
    background-color: #2c2c44;
    border-radius: 5px;
  }

  h1 {
    font-size: 25px;
  }

  #titulo {
    display: flex;
    align-items: center;
    margin-left: 40px;
    padding: 10px 0;
  }

  #car-icon {
    width: 40px;
    margin-right: 15px;
    filter: invert(1);
  }
</style>
