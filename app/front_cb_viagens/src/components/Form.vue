<template>
    <div id="form">
        <div id="form-text">
            <img src="img/dinheiro-na-entrega.png" id="hand-icon">
            <h1>Calcule o Valor da Viagem</h1>
        </div>
        <div>
            <form id="form-city" @submit.prevent="checkForm">
                <div class="input-container">
                    <label for="destiny">Destino</label>
                    <select name="destiny" id="destiny" v-model="city">
                        <option value="São Paulo">São Paulo</option>
                        <option value="Rio de Janeiro">Rio de Janeiro</option>
                        <option value="Belo Horizonte">Belo Horizonte</option>
                        <option value="Curitiba">Curitiba</option>
                        <option value="Porto Alegre">Porto Alegre</option>
                    </select>
                </div>
                <div class="input-container">
                    <label for="date">Data</label>
                    <input type="date" id="date" name="date" v-model="date">
                </div>
                <div class="input-container">
                    <input type="submit" class="submit-btn" value="Buscar">
                </div>    
            </form>
        </div>
        <Modal v-show="showModal" @close="showModal = false">
        </Modal>
    </div>
</template>

<script>
    import Modal from './Modal.vue'

    export default {
        name: 'Form',
        components: {
            Modal,
        },
        data() {
            return {
                city: '',
                date: '',
                showModal: false
            }
        },
        methods: {
            checkForm() {
                if (this.city == '' || this.date == '') {
                    this.showModal = true
                } else {
                    this.$emit('formSubmitted', { city: this.city, date: this.date });
                }
            }
        }
    }
</script>

<style scoped>

    #form{
        margin: 15px;
        background-color: #f0f0f0;
        border-radius: 5px;
        width: 25%;
        height: 61vh;
        position: fixed;
    }

    #form-text{
        display: flex;
        align-items: center;
        margin: 80px 25px 25px 25px;
    }

    .input-container {
        display: flex;
        flex-direction: column;
        display: flex;
        margin: 25px;
        
    }

    label{
        font-weight: bold;
        font-size: 15px;
        color: #999999;
        margin-bottom: 10px;
    }

    input,select {
        height: 30px;
        border: 1px solid #ccc; 
        border-radius: 5px;
    }

    .submit-btn {
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
        transition: .5s;
    }

    .submit-btn:hover {
        background-color: turquoise;
        color: white;
    }

    h1{
        color: #2c2c44;
        font-size: 20px;
    }

    #hand-icon {
        width: 25px;
        margin-right: 5px;
    }

</style>
