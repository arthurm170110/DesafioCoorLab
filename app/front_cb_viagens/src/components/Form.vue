<template>
    <div id="form" class="componente">
        <div id="form-text">
            <img src="img/dinheiro-na-entrega.png" id="hand-icon">
            <h1>Calcule o Valor da Viagem</h1>
        </div>
        <div>
            <form id="form-city" @submit.prevent="checkForm">
                <div class="input-container">
                    <label for="destiny">Destino</label>
                    <select name="destiny" id="destiny" v-model="city">
                        <option value="">Selecione o destino</option>
                        <option v-for="city in uniqueCities" :key="city" :value="city">{{ city }}</option>
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
                showModal: false,
                transports: null,
                uniqueCities: [],
                fastest: null,
                cheapest: null,
            }
        },
        methods: {
            checkForm() {
                if (this.city == '' || this.date == '') {
                    this.showModal = true
                } else {
                    this.$emit('formSubmitted', { city: this.city, date: this.date });
                    this.getFastCheap();
                }
            },
            async getTranports() {
                const response = await fetch('http://localhost:3000/transport/');
                const data = await response.json();

                this.transports = data;

                this.uniqueCities = data.reduce((unique, item) => {
                    return unique.includes(item.city) ? unique : [...unique, item.city];
                }, []).sort();
            },
            async getFastCheap(){
                const response = await fetch(`http://localhost:3000/transport/city/${this.city}/`);
                const data = await response.json();

                this.fastest = data.fastest;
                this.cheapest = data.cheapest;

                this.$emit('dataSubmitted', { fastest: this.fastest, cheapest: this.cheapest });
                
            }
        },
        mounted() {
            this.getTranports();
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
        color: #2c2c44;
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

    option {
        color: #999999;
        font-size: 15px;
        font-family: Helvetica;
    }

</style>
