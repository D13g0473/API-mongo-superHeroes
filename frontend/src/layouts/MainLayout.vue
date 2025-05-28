<template>
  <q-layout view="lHh Lpr lFf"  >
    <q-header elevated class="bg-secondary">
      <q-toolbar class="col">
        <div class="col col-4  q-gutter-sm">
            <q-btn
              icon="home"
              href="#"
            />
            <q-btn
            label="Marvel"
            class="bg-negative"
            style="font-weight: bolder;"
            href="#?universo=marvel"
          />
          <q-btn
            label="DC"
            class="bg-primary"
            style="font-weight: bolder;"
            href="#?universo=dc"
          />
        </div> 
        <div class="col col-4">

        </div>
        <div class="col col-4">
          <q-input dark dense standout v-model="text" input-class="text-right" class="q-ml-md">
          <template v-slot:append>
            <q-icon v-if="(text == '')" name="search" />
            <q-icon v-else name="clear" class="cursor-pointer" @click="text = ''" />
          </template>
          </q-input>
        </div>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup>
  import { ref, watch } from 'vue'
  import { search } from "../store/searchStore"; 
  const text = ref('')
  const searchStore      = search();

  watch(text , (text)=>{
    if(text.length >= 3)
      searchStore.loadSearch(text)
      if(text.length === 0)
      searchStore.loadSearch('')

  })

</script>
