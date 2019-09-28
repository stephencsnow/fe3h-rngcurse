<template>
  <div
    id="app"
    class="container"
  >
    <GithubFork />
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
import GithubFork from './components/GithubFork.vue';

export default {
  name: 'app',
  components: {
    Character,
    ClassList,
    Results,
    GithubFork,
  },
};
</script>

<style>
input[type="number"] {
  width: 80px;
}
</style>
