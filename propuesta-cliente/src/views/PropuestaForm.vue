<template>
  <div class="propuesta-crear">
    <h1>Formulario para agregar Propuestas</h1>
    <form action="">
        <label for="">Propuesta</label>
        <input type="text" v-model="propuestas.propuesta">
        <button @click.prevent="guardarPropuesta" type="button" name="button">Agregar Propuesta</button>
    </form>
  </div>
</template>
<script>
import axios from 'axios'
export default{
    name:'propuesta-crear',
    data(){
        return {
            propuestas:{id:null,propuesta:''}
        }
    },
    methods:{
        guardarPropuesta(){
            var datos={
                propuesta:this.propuestas.propuesta
            }
        
            axios.post('http://127.0.0.1:8000/api/',datos).
            then((respuesta)=>{
                console.log(respuesta)
            })
        }
    }
}
</script>