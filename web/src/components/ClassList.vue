<template>
  <div>
    <h3>Classes</h3>
    <span>Add class history for this character.</span>
    <b-list-group>
      <template v-for="characterClass in getClasses">
        <b-list-group-item
          v-bind:key="characterClass.name"
          class="d-flex justify-content-between align-items-center"
          :active="characterClass.isCurrent"
        >
          {{ characterClass.name }}
          <b-badge
            variant="info"
            pill
          >{{ characterClass.levelUps }}</b-badge>
        </b-list-group-item>
      </template>
    </b-list-group>
    <AddClass />
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import AddClass from './AddClass.vue';

export default {
  name: 'ClassList',
  components: {
    AddClass,
  },
  computed: mapGetters(['getClasses']),
};
</script>

<style>
</style>
