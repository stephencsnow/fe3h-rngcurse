/* eslint no-shadow: ["error", { "allow": ["state"] }] */
const state = {
  characterName: '',
  characterLvl: 1,
  characterHp: null,
  characterStr: null,
  characterMag: null,
  characterDex: null,
  characterSpd: null,
  characterLck: null,
  characterDef: null,
  characterRes: null,
  characterCha: null,
};

const getters = {
  getCharacterName: state => state.characterName,
  getCharacterLvl: state => state.characterLvl,
  getCharacterHp: state => state.characterHp,
  getCharacterStr: state => state.characterStr,
  getCharacterMag: state => state.characterMag,
  getCharacterDex: state => state.characterDex,
  getCharacterSpd: state => state.characterSpd,
  getCharacterLck: state => state.characterLck,
  getCharacterDef: state => state.characterDef,
  getCharacterRes: state => state.characterRes,
  getCharacterCha: state => state.characterCha,
  getCharacter(state) {
    return {
      character: state.characterName,
      level: state.characterLvl,
      stats: {
        hp: state.characterHp,
        strength: state.characterStr,
        magic: state.characterMag,
        dexterity: state.characterDex,
        speed: state.characterSpd,
        luck: state.characterLck,
        defense: state.characterDef,
        resistance: state.characterRes,
        charm: state.characterCha,
      },
    };
  },
};

const actions = {};

const mutations = {
  setCharacterName(state, characterName) {
    state.characterName = characterName;
  },
  setCharacterLvl(state, characterLvl) {
    state.characterLvl = parseInt(characterLvl, 10);
  },
  setCharacterHp(state, characterHp) {
    state.characterHp = parseInt(characterHp, 10);
  },
  setCharacterStr(state, characterStr) {
    state.characterStr = parseInt(characterStr, 10);
  },
  setCharacterMag(state, characterMag) {
    state.characterMag = parseInt(characterMag, 10);
  },
  setCharacterDex(state, characterDex) {
    state.characterDex = parseInt(characterDex, 10);
  },
  setCharacterSpd(state, characterSpd) {
    state.characterSpd = parseInt(characterSpd, 10);
  },
  setCharacterLck(state, characterLck) {
    state.characterLck = parseInt(characterLck, 10);
  },
  setCharacterDef(state, characterDef) {
    state.characterDef = parseInt(characterDef, 10);
  },
  setCharacterRes(state, characterRes) {
    state.characterRes = parseInt(characterRes, 10);
  },
  setCharacterCha(state, characterCha) {
    state.characterCha = parseInt(characterCha, 10);
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
