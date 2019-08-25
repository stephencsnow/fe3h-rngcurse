<template>
  <div id="app">
    <Character />
    <ClassList />
    <b-button
      type="submit"
      @click="calculate"
    >Submit</b-button>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import axios from 'axios';
import Character from './components/Character.vue';
import ClassList from './components/ClassList.vue';

export default {
  name: 'app',
  components: {
    Character,
    ClassList,
  },
  methods: {
    calculate() {
      const data = {
        ...this.character,
        classes: this.formattedClasses,
      };
      console.log(data);
      axios.post(
        'http://localhost:5000/calculate', data,
      ).then((response) => {
        console.log(response);
      });
    },
  },
  computed: {
    ...mapGetters({
      character: 'getCharacter',
      formattedClasses: 'getFormattedClasses',
    }),
  },
};
</script>

<style>
</style>
