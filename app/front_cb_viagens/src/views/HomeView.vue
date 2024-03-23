<template>
<div class="componente">
  <Title/>
  <div id="box-home">
    <Form @formSubmitted="updateData" @dataSubmitted="dataFastCheap"/>
    <Information :city="city" :date="date" :fastest="fastest" :cheapest="cheapest"/>
  </div>
</div> 
</template>

<script>
  import Title from '@/components/Title.vue'
  import Form from '@/components/Form.vue'
  import Information from '@/components/Information.vue'

  export default {
    name: 'HomeView',
    components: {
      Title,
      Form,
      Information,
    },
    data() {
      return {
        city: '',
        date: '',
        fastest: null,
        cheapest: null,
      }
    },
    methods: {
      updateData(data) {
        this.city = data.city
        this.date = data.date
      },
      dataFastCheap(data) {
        this.fastest = data.fastest
        this.cheapest = data.cheapest

      }
    }
  }

</script>

<style scoped>

  #box-home {
    margin: 0 50px 0 400px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
    margin-left: 400px;
    min-height: 400px;
    border-radius: 2px;
    display: flex;
    align-items: center;
  }

  #return {
    margin-left: 500px;
  }
</style>
