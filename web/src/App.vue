<template>
  <div
    id="app"
    class="container"
  >
    <h2>Fire Emblem Three Houses RNGCurse</h2>
    <Character />
    <ClassList />
    <Results />
  </div>
</template>

<script>
import Character from './components/Character.vue';
import ClassList from './components/ClassList.vue';
import Results from './components/Results.vue';

export default {
  name: 'app',
  components: {
    Character,
    ClassList,
    Results,
  },
};
</script>

<style>
input[type="number"] {
  width: 80px;
}
</style>
