import { defineStore } from 'pinia'           ;

export const search = defineStore('search', 
{
  state: () => (
    {
    text: "", 
    load: false,
    }),
  actions: {
   async loadSearch(value) 
    {
        this.text = value; 
    }
  }
});