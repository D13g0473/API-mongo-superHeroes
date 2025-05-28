<template>
    <!-- notice dialogRef here -->
    <q-dialog  ref="dialogRef" @hide="onDialogHide" maximized >
      <q-card class="q-dialog-plugin custom-card" style="width: auto; background-color: transparent;">
        <center>
          <div class="container row justify-center pc-sa q-mt-xl">
              <div elevated class="q-ma-sm q-card--bordered col-12">
                <q-card>
                    <q-card-section  >
                        <div class="text-h6">
                          <center>
                            {{ title }}
                          </center>
                        </div>
                    </q-card-section >
                    <q-separator class="q-mb-sm"></q-separator>
                    <q-form @submit="onSubmit" >
                    <q-card-section horizontal >

                            <div class="col-6 q-mb-xl q-ml-sm">
                              <q-carousel
                                v-model="slide"
                                animated
                                navigation
                                infinite
                                :autoplay="autoplay"
                                arrows
                                transition-prev="slide-right"
                                transition-next="slide-left"
                                @mouseenter="autoplay = false"
                                @mouseleave="autoplay = true"
                                style="height: 500px; max-width: 100%;"
                              >
                                <q-carousel-slide
                                  v-for="(img, index) in images"
                                  :key="index"
                                  :name="index + 1"
                                >
                                  <img :src="img" style="width: 60%; height: 70%; object-fit:contain;" />
                                </q-carousel-slide>
                              </q-carousel>
                            </div>
                        <q-card-section>
                           
                            <div class="row q-pb-sm">
                            <div class="col-12 flex justify-center" style="height: 50px;">
                                      <q-item>
                                        <q-input
                                            style   = "min-width: 25vw; height: 56px;"
                                            v-model = "name"
                                            type    = 'text'
                                            label   = 'Nombre de Personaje'
                                            :disable="(typeForm==3)"
                                            required
                                            filled
                                            dense
                                        />
                                      </q-item>
                            </div>
                            <div class="col-12 flex justify-center" style="height: 50px;">
                                      <q-item>
                                        <q-select
                                          style          = "min-width: 25vw; height: 56px;"
                                          v-model        = "selectedGroup"
                                          :options       = "groups"
                                          :label         = "'Seleccione Universo'"
                                          option-label   = "name"
                                          option-value   = "value"
                                          :disable="(typeForm==3)" 
                                          required
                                          filled
                                          dense
                                        />  
                                      </q-item>
                            </div>
                            <div class="col-12 flex justify-center" style="height: 50px;">
                                      <q-item>
                                        <q-input
                                            style = "min-width: 25vw; height: 56px;"
                                            v-model= "secreteName"
                                            type='text'
                                            label='Identidad Secreta'
                                            :disable="(typeForm==3)"
                                            required
                                            filled
                                            dense
                                        />
                                      </q-item>
                            </div>
                            <div v-if="listOfEquipmen.length && selectedEquipmen.length" class="col-12 flex justify-center" style="height: 50px;">
                                      <q-item>
                                        <q-select
                                          style   = "min-width: 25vw; height: 56px;"
                                          filled
                                          use-chips
                                          stack-label
                                          v-model="selectedEquipmen"
                                          multiple
                                          :options="listOfEquipmen"
                                          :disable= "(typeForm==3)"
                                          dense
                                        />
                                      </q-item>
                            </div>
                            <div v-if="!(typeForm==3)" class="col-12 flex justify-center" style="height: 50px;">
                                      <q-item>
                                        <q-input
                                            style   = "min-width: 20vw; height: 56px;"
                                            v-model = "equipment"
                                            type    = 'text'
                                            label   = 'Equipo'
                                            filled
                                            dense
                                        />
                                        <q-btn
                                          label="Agregar"
                                          color="info"
                                          style   = "min-width: 5vw; height: 30px;"
                                          @click="addEquipment"
                                        />
                                      </q-item>
                            </div>
                            <div class="col-12 flex justify-center" style="height: 50px;">
                                      <q-item>
                                        <q-input
                                            style   = "min-width: 25vw; height: 56px;"
                                            v-model = "year"
                                            type    = 'number'
                                            label   = 'Año de aparición'
                                            :disable= "(typeForm==3)"
                                            required
                                            filled
                                            dense
                                        />
                                      </q-item>
                            </div>
                            <div class="col-12 flex justify-center" style="height: 50px;">
                                      <q-item>
                                        <q-input
                                            style   = "min-width: 25vw;"
                                            v-model ="biography"
                                            type    ='textarea'
                                            label   ='Biografia'
                                            :disable="(typeForm==3)"
                                            required
                                            filled
                                            dense
                                        />
                                      </q-item>
                            </div>
                          </div>
                        </q-card-section>
                    </q-card-section >
                    <q-card-section>
                            <div class="q-pt-xl col-12 q-gutter-xl flex justify-center" >
                                <q-btn
                                  :label="typeForm==3?'Cerrar':'Cancelar'" 
                                  @click="onCancelClick" 
                                  :color="typeForm==3?'info':'grey'"
                                />
                                 <q-btn  
                                   v-if = "!(typeForm==3)"
                                   :label="'Guardar'" 
                                   type="submit"
                                   color="green" 
                                 />
                            </div>
                        </q-card-section>
                    </q-form>
                </q-card>
            </div>
          </div>
        </center>
      </q-card>
    </q-dialog>
  </template>
  
  <script>
//   import { onMounted } from "vue";
  import { useDialogPluginComponent }         from 'quasar';
  import { api } from 'src/boot/axios';
  import { ref } from 'vue'
  import Swal from 'sweetalert2'




  export default {
    props: {
       character: {
          type: Object,
          required: false,
       },
       typeForm:{
          type:Number,
          required:true
       }
    },
  
    emits: [
      ...useDialogPluginComponent.emits
    ],
    // components: {
    //     FormScheme          : defineAsyncComponent(() => import('components/assets/FormScheme.vue'))
    // }, 
    setup (props) 
    {
      const { dialogRef, onDialogHide, onDialogOK, onDialogCancel } = useDialogPluginComponent()
      // REQUIRED; must be called inside of setup()
      // dialogRef      - Vue ref to be applied to QDialog
      // onDialogHide   - Function to be used as handler for @hide on QDialog
      // onDialogOK     - Function to call to settle dialog with "ok" outcome
      //                    example: onDialogOK() - no payload
      //                    example: onDialogOK({ /*.../* }) - with payload
      // onDialogCancel - Function to call to settle dialog with "cancel" outcome
      const secreteName     = ref('') ;
      const year            = ref(0)  ;
      const name            = ref('') ;
      const selectedEquipmen= ref([]) ; 
      const listOfEquipmen  = ref([]) ;
      const equipment       = ref("") ;
      const groups          =     [
                                    {name:'MARVEL', value: 'marvel'},
                                    {name:'DC'    , value: 'dc'}
                                  ];
      const title           = "Cargar personaje";                   
      const selectedGroup   = ref(null);  
      const biography       = ref("");
      const images = ref([])

      const allImages = import.meta.glob('./../../assets/images/*', { eager: true, import: 'default' })

      const loadImages = (characterName) => {
        const normalized = characterName.replace(' ', '_').replace('-', '_').toLowerCase()
        images.value = []
      
        for (const path in allImages) {
          const fileName = path.split('/').pop().split('.')[0] // sin extensión
          if (fileName.startsWith(normalized)) {
            images.value.push(allImages[path])
          }
        }
      }
      const post = async (body)=>
      {
        const response = await api.post("/hero", body)
          Swal.fire({
            icon: 'success',
            title: '¡Personaje creado!',
            text: response.data.message || 'El personaje fue creado correctamente.'
          })
      }

      const update = async (body)=>
      {
        const response = await api.put(`/hero/${encodeURIComponent(body.name)}`, body)
          Swal.fire({
            icon: 'success',
            title: '¡Personaje editado!',
            text: response.data.message || 'El personaje fue actualizado correctamente.'
          })
      }

      const onSubmit = async () => {
          const body = {
            name: name.value,
            real_name: secreteName.value,
            year: year.value,
            universe: selectedGroup.value?.value,
            biography: biography.value,
            equipment: selectedEquipmen.value,
            images: "imagen_data.jpg"
          }
        
           
          try {
          
                if (props.typeForm==1) 
                  await post(body)
          
                if (props.typeForm==2) 
                await update(body)  
          
                onDialogOK()
              }
          catch (err) 
              {
                console.log(err);

                Swal.fire({
                  icon: 'error',
                  title: 'Error',
                  text: err.response?.data?.error || 'Ocurrió un error al guardar el personaje.'
                })
              }
        }

      const addEquipment = ()=>{
          listOfEquipmen.value.push(equipment.value)
          selectedEquipmen.value.push(equipment.value)
          equipment.value = ""
      }  
      console.log(props.character);
      
      if((props.typeForm==2) || (props.typeForm==3) )
      {
        secreteName.value       = props.character.real_name;
        year.value              = props.character.year;
        name.value              = props.character.name;
        selectedEquipmen.value  = props.character.equipment;
        listOfEquipmen.value    = props.character.equipment;
        biography.value         = props.character.biography;

        selectedGroup.value     = groups.find(universe =>( universe.value == props.character.universe));
        loadImages(props.character.name)
      }

      return {
        name                  , 
        selectedGroup         ,
        secreteName           ,
        slide     : ref(1)    ,
        equipment             ,
        autoplay  : ref(true) ,
        biography             ,
        listOfEquipmen        ,
        year                  ,
        groups                ,
        dialogRef             ,
        title                 ,
        addEquipment          ,
        onDialogHide          ,
        selectedEquipmen      ,
        images                ,
        onOKClick () 
        {
          onDialogOK()
        },
        onSubmit,
        onCancelClick: onDialogCancel

      }
    }
  }
  </script>

  <style>

.custom-card{
  box-shadow:none

}
</style>