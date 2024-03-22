<template>
    <div class="modal-overlay">
        <div class="modal" tabindex="-1">
            <img src="img/interface.png" id="alert-icon">
            <p>Insira os valores para realizar</p>
            <p>a cotação.</p>
            <button class="close-btn" @click="$emit('close')">Fechar</button>
        </div>
    </div>
</template>

<script>
    export default{
        name: 'Modal',
    }
</script>

<style scoped>
    .modal-overlay {
        display: flex;
        justify-content: center;
        align-items: center;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.5); /* Fundo semi-transparente */
    }

    .modal {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background-color: #fff;
        padding: 45px 45px;
        border-radius: 5px;
    }

    #alert-icon {
        width: 50px;
        margin: 0 0 20px 0;
    }

    p {
        font-family: Helvetica;
        color: #2c2c44;
        font-size: 25px;
    }

    .close-btn {
        background-color: turquoise;
        color: #2c2c44;
        font-weight: bold;
        font-size: 15px;
        border: none;
        border-radius: 5px;
        padding: 5px 10px;
        width: 150px;
        cursor: pointer;
        margin: 0 auto;
        justify-content: center;
        margin: 20px 0 0 0;
    }
</style>