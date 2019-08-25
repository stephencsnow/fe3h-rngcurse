<template>
  <div>
    <b-form
      @submit="onSubmit"
      inline
    >
      <label
        class="mr-sm-2"
        for="class-input"
      >Class:</label>
      <b-form-select
        class="mb-2 mr-sm-2 mb-sm-0"
        v-model="className"
        :options="classes"
        id="class-input"
      >
      </b-form-select>

      <label
        class="mr-sm-2"
        for="levelup-input"
      >Level Ups:</label>
      <b-input
        class="sm-2 mr-sm-2 mb-sm-0"
        type="number"
        v-model="levelUps"
        id="levelup-input"
      ></b-input>

      <b-form-checkbox
        v-model="isCurrent"
        class="mb-2 mr-sm-2 mb-sm-0"
      >
        Current class
      </b-form-checkbox>
      <b-button
        type="submit"
        variant="primary"
      >Add class</b-button>
    </b-form>
  </div>
</template>

<script>
import { mapActions } from 'vuex';
import json from '../data/classes.json';

export default {
  name: 'AddClass',
  data() {
    return {
      classes: json,
      className: '',
      levelUps: 0,
      isCurrent: false,
    };
  },
  methods: {
    ...mapActions({
      addNewClass: 'addNewClass',
    }),
    onSubmit(evt) {
      evt.preventDefault();
      const newClass = {
        name: this.className,
        isCurrent: this.isCurrent,
        levelUps: parseInt(this.levelUps, 10),
      };
      this.addNewClass(newClass);

      this.resetForm();
    },
    resetForm() {
      this.className = '';
      this.levelUps = 0;
      this.isCurrent = false;
    },
  },
};
</script>

<style>
</style>
