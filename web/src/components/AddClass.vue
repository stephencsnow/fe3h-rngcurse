<template>
  <div>
    <b-form
      @submit="onSubmit"
      inline
      class="my-2"
    >
      <b-form-select
        v-model="className"
        :options="classes"
        id="class-input"
        class="mr-2"
      >
        <template v-slot:first>
          <option
            :value="null"
            disabled
          >Class</option>
        </template>
      </b-form-select>

      <label
        for="levelup-input"
        class="mr-2"
      >Level Ups:</label>
      <b-input
        type="number"
        inputmode="numeric"
        v-model="levelUps"
        id="levelup-input"
        class="mr-2"
      ></b-input>

      <b-form-checkbox
        v-model="isCurrent"
        class="mr-2"
      >
        Current
      </b-form-checkbox>
      <b-button
        type="submit"
        variant="outline-primary"
      >Add</b-button>
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
      className: null,
      levelUps: null,
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
      this.className = null;
      this.levelUps = null;
      this.isCurrent = false;
    },
  },
};
</script>

<style>
</style>
