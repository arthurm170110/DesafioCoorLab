<template>
    <div id="information">
        <div v-if="!city || !date" id="message">
            <h2>Nenhum dado selecionado.</h2>
        </div>
        <div v-else id="data-information">
            <h3>Estas são as melhores alternativas de</h3>
            <h4>viagem para a data selecionada</h4>
            <div class="block">
               <img src="img/dinheiro-na-entrega.png" id="hand2-icon"> 
            </div>
            <div class="block-text">
                <br>
                <p1>TG Transportes</p1>
                <br>
                <p2>Leito: 13 Completo</p2>
                <br>
                <p2>Tempo estimado: 6h</p2>
            </div>
            <div class="block-price">
                <br>
                <p3>Preço</p3>
                <br>
                <br>
                <p4>R$ 1.250,00</p4>
            </div>
            <div class="block">
                <img src="img/relogio.png" id="clock-icon">
            </div>
            <div class="block-text">
                <br>
                <p1>Pássaro Ver</p1>
                <br>
                <p2>Pltrona: 2 convencional</p2>
                <br>
                <p2>Tempo estimado: 6h</p2>
            </div>
            <div class="block-price">
                <br>
                <p3>Preço</p3>
                <br>
                <br>
                <p4>R$ 650,00</p4>
            </div>
            <button @click="reloadPage">Limpar</button>
      </div>
    </div>
</template>

<script>
    export default {
        name: 'Information',
        props: ['city', 'date'],
        data() {
            return {
                showMessage: true,
            }
        },
        methods: {
            reloadPage() {
                location.reload();
            }
        }
    }
</script>

<style scope>

    #data-information {
        margin-left: 370px;
    }
    #message {
        margin-left: 500px;
    }

    h2, h3, h4 {
        color: #2c2c44;
        font-size: 20px;
    }

    h3 {
        margin: 30px 0 0 0;
    }

    #clock-icon {
        width: 40px;
        margin: 22px 0 0 20px;
        filter: invert(1);
    }

    #hand2-icon {
        width: 45px;
        justify-content: center;
        margin: 20px 0 0 20px;
        filter: invert(1); 
    }

    .block{
        background-color: turquoise;
        border-radius: 5px 0 0 5px;
        width: 15%;
        height: 15vh;
        margin: 10px 0 0 0;
    }

    .block-text{
        background-color: #f0f0f0;
        border-radius: 5px 5px 5px 0;
        width: 58%;
        height: 15vh;
        margin: -91px 0 0 80px;

    }

    .block-price {
        background-color: #f0f0f0;
        border-radius: 5px;
        width: 25%;
        height: 15vh;
        margin: -91px 0 0 400px;
    }

    p1, p2 {
        font-family: Helvetica;
        font-size: 15px;
        color: #2c2c44;
        margin-left: 40px;
    }
    p1, p3 {
        font-weight: bold;
    }

    p3,p4 {
        font-family: Helvetica;
        font-size: 15px;
        color: #2c2c44;
        margin-left: 20px;
    }

    button {
        margin: 50px 0 0 425px;
        background-color: #f4a434; 
        color: #2c2c44; 
        font-family: Helvetica; 
        font-size: 15px; 
        padding: 8px 30px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-weight: bold;
    }

    button:hover {
        background-color: #f4a434;
        color:white;
    }


</style>