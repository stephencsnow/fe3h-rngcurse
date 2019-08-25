import Vue from 'vue';
import Vuex from 'vuex';
import character from './modules/character';
import classes from './modules/classes';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    character,
    classes,
  },
});
