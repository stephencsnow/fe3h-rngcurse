/* eslint no-shadow: ["error", { "allow": ["state"] }] */
const state = {
  classes: [],
};

const getters = {
  getClasses: state => state.classes,
  getFormattedClasses(state) {
    return state.classes.map((_class) => {
      const formattedClass = {
        name: _class.name,
        level_ups: _class.levelUps,
        is_current: _class.isCurrent,
      };

      return formattedClass;
    });
  },
};

const actions = {
  addNewClass({ commit }, newClass) {
    commit('addClass', newClass);
  },
};

const mutations = {
  addClass: (state, newClass) => state.classes.push(newClass),
};

export default {
  state,
  getters,
  actions,
  mutations,
};
