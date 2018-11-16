<template>
  <div class="propuestas">
    <h1>Pagina de Listado de propuestas</h1>
    <router-link :to="{name:'propuesta-crear'}">Agregar una nueva propuesta logica</router-link>
    <table border="1">
        <tr>
            <td>ID </td>
            <td>Propuesta </td>
            <td>Respuesta </td>
        </tr>
        <tr v-for="propuesta in propuestas">
            <td>{{propuesta.id}} </td>
            <td>{{propuesta.propuesta}} </td>
            <td>{{propuesta.respuesta}} </td>
        </tr>
    </table>
  </div>
</template>
<script>
import axios from 'axios'
export default{
    mounted(){
        axios.get('http://127.0.0.1:8000/api/all/').then((respuesta)=>{
            this.propuestas=respuesta.data
        })

    },
    data(){
        return {
            propuestas:[]
        }
    }
}
</script>