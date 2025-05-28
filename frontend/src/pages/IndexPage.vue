<template>
  <div class="q-pa-md row items-start q-gutter-md">

    <q-card  v-for="(hero,index) in heroes" v-bind:key="index" class="my-card q-card--bordered">
        <q-img
        :src="getImage(hero.name)"
        style="height: 200px; object-fit:contain; object-position: top; "
        ratio="1.5"
      />
        <q-card-section>
          <div class="row">
            <div class="col-12 text-h6">{{hero.name}}</div>
          </div>
          <div class="row">
            <div class="col-8 text-subtitle2">{{hero.real_name}}</div>
            <div class="col-4"><q-chip :color="hero.universe=='marvel'?'red':'blue'" text-color="white" text="bold">{{ hero.universe.toUpperCase() }}</q-chip></div>
          </div>
          
        </q-card-section>
  
        <q-card-section class="q-pt-none truncar-texto">
          {{ hero.biography }}
        </q-card-section>
        <q-card-section class=" col-12 q-gutter-xl flex justify-center" >
          <q-btn
            class="col-4"
            round
            icon="visibility"  
            color="info"
            @click="showCharacter(hero)"
          />
           <q-btn  
             class="col-4"
             round
             icon   = "edit"
             color  = "accent"
            @click  = "updateCharacter(hero)"  
           />
          <q-btn
            class="col-4"  
             round
             icon   = "delete"
             color  = "negative"
            @click  = "deleteCharacter(hero)"  
           />
        </q-card-section>
    </q-card>
    <q-page-sticky position="bottom-right" :offset="[40, 40]">
            <q-btn fab icon="add" color="positive" @click="createCharacter()" />
    </q-page-sticky>
  </div>
</template>
<script>
import { api } from 'src/boot/axios'
import { Dialog } from 'quasar'
import AddHeroForm from 'src/components/dialog/AddHeroForm.vue'
import { search } from 'src/store/searchStore'
import { watch } from 'vue'
import Swal from 'sweetalert2'

export default {
  data() {
    return {
      heroes: [],
      allHeroes: [],
      searchStore : search() 
    }
  },
  created() {
    this.loadHeroes()
    watch(() => this.searchStore.text, (newValue) => {
      if (newValue && newValue.length >= 3) {
        this.heroes = this.allHeroes.filter(hero =>
          hero.name.toLowerCase().includes(newValue.toLowerCase())
        )
      } else {
        this.heroes = [...this.allHeroes]
      }
    })
  },
  watch: {
    // observar cambios en el query param "universo"
    '$route.query.universo': {
      handler(newVal, oldVal) {
        oldVal
        console.log('universo cambió:', newVal)
        this.loadHeroes()
      },
      immediate: false,
    },
  },
  methods: {
    async loadHeroes() {
      const universo = this.$route.query.universo
      console.log('Cargando héroes con universo:', universo)
      var prm = {}
      if(this.$route.query.universo)
        prm.universe = universo 
      
      const response = await api.get('/heroes', {
        params: prm
      })
      this.heroes = response.data
      this.allHeroes = [...response.data]
    },
    async createCharacter() {
      Dialog.create({
        component: AddHeroForm,
        componentProps:
            {
              typeForm: 1
            }
      }).onOk(() => {
        this.loadHeroes()
      })
    },
    async updateCharacter(hero) {
      Dialog.create({
        component: AddHeroForm,
        componentProps:
            {
              character:hero,
              typeForm: 2
            }
      }).onOk(() => {
        this.loadHeroes()
      })
    },
    async showCharacter(hero) {
      Dialog.create({
        component: AddHeroForm,
        componentProps:
            {
              character:hero,
              typeForm: 3
            }
      }).onOk(() => {
        console.log('Nuevo lugar agregado, recargando mapa...')
      })
    },
    async deleteCharacter(hero){
      console.log('Eliminando héroe:', hero.name);
      
      api.delete(`/hero/${encodeURIComponent(hero.name)}`)
      .then(() => {
        this.loadHeroes()
        Swal.fire({
          icon: 'success',
          title: 'Héroe eliminado',
          text: `El héroe ${hero.name} ha sido eliminado correctamente.`,
          confirmButtonText: 'Aceptar'
        })
      })
      .catch(error => {
        console.error('Error al eliminar el héroe:', error)
        Swal.fire({
          icon: 'error',
          title: 'Error al eliminar',
          text: `No se pudo eliminar el héroe ${hero.name}. Por favor, inténtalo de nuevo más tarde.`,
          confirmButtonText: 'Aceptar'
        })
      })
    },
    getImage(name) {
    const fileName = name.replace(' ', '_').replace('-', '_').toLowerCase()
    try {
      console.log(fileName);
      
      return new URL(`../assets/images/${fileName}_1.jpg`, import.meta.url).href
    } catch (e) {
      e
      console.error('No se encontró imagen para:', fileName)
      return '' // o una imagen por defecto
    }
}
  }
}
</script>

<style lang="sass" scoped>
.my-card
  width: 100%
  max-width: 250px
.truncar-texto 
    width: 200px
    overflow: hidden
    white-space: nowrap
    text-overflow: ellipsis
  
</style>
