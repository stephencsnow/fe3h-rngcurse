<template>
  <div>
    <b-form-group>

      <b-form-group
        label-cols-sm="3"
        label="Character:"
        label-align-sm="right"
        label-for="char-input"
      >
        <b-form-select
          @input="setCharacterName"
          :options="characters"
          :value=this.name
          id="char-input"
          class="col-sm-2"
        >
        </b-form-select>
      </b-form-group>

      <b-form-group
        label-cols-sm="3"
        label="Level:"
        label-align-sm="right"
        label-for="lvl-input"
      >
        <b-form-input
          @input="setCharacterLvl"
          :value=this.lvl
          :state="validLevel"
          type="number"
          inputmode="numeric"
          id="lvl-input"
        ></b-form-input>
      </b-form-group>

      <b-form-group
        label-cols-sm="3"
        label="HP:"
        label-align-sm="right"
        label-for="hp-input"
      >
        <b-form-input
          @input="setCharacterHp"
          :value=this.hp
          type="number"
          inputmode="numeric"
          id="hp-input"
        ></b-form-input>
      </b-form-group>

      <b-form-group
        label-cols-sm="3"
        label="Str:"
        label-align-sm="right"
        label-for="str-input"
      >
        <b-form-input
          @input="setCharacterStr"
          :value=this.str
          type="number"
          inputmode="numeric"
          id="str-input"
        ></b-form-input>
      </b-form-group>

      <b-form-group
        label-cols-sm="3"
        label="Mag:"
        label-align-sm="right"
        label-for="mag-input"
      >
        <b-form-input
          @input="setCharacterMag"
          :value=this.mag
          type="number"
          inputmode="numeric"
          id="mag-input"
        ></b-form-input>
      </b-form-group>

      <b-form-group
        label-cols-sm="3"
        label="Dex:"
        label-align-sm="right"
        label-for="dex-input"
      >
        <b-form-input
          @input="setCharacterDex"
          :value=this.dex
          type="number"
          inputmode="numeric"
          id="dex-input"
        ></b-form-input>
      </b-form-group>

      <b-form-group
        label-cols-sm="3"
        label="Spd:"
        label-align-sm="right"
        label-for="spd-input"
      >
        <b-form-input
          @input="setCharacterSpd"
          :value=this.spd
          type="number"
          inputmode="numeric"
          id="spd-input"
        ></b-form-input>
      </b-form-group>

      <b-form-group
        label-cols-sm="3"
        label="Lck:"
        label-align-sm="right"
        label-for="lck-input"
      >
        <b-form-input
          @input="setCharacterLck"
          :value=this.lck
          type="number"
          inputmode="numeric"
          id="lck-input"
        ></b-form-input>
      </b-form-group>

      <b-form-group
        label-cols-sm="3"
        label="Def:"
        label-align-sm="right"
        label-for="def-input"
      >
        <b-form-input
          @input="setCharacterDef"
          :value=this.def
          type="number"
          inputmode="numeric"
          id="def-input"
        ></b-form-input>
      </b-form-group>

      <b-form-group
        label-cols-sm="3"
        label="Res:"
        label-align-sm="right"
        label-for="res-input"
      >
        <b-form-input
          @input="setCharacterRes"
          :value=this.res
          type="number"
          inputmode="numeric"
          id="res-input"
        ></b-form-input>
      </b-form-group>

      <b-form-group
        label-cols-sm="3"
        label="Cha:"
        label-align-sm="right"
        label-for="cha-input"
      >
        <b-form-input
          @input="setCharacterCha"
          :value=this.cha
          type="number"
          inputmode="numeric"
          id="cha-input"
        ></b-form-input>
      </b-form-group>

    </b-form-group>
  </div>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex';
import json from '../data/characters.json';

export default {
  name: 'Character',
  data() {
    return {
      characters: json,
    };
  },
  methods: {
    ...mapMutations([
      'setCharacterName',
      'setCharacterLvl',
      'setCharacterHp',
      'setCharacterStr',
      'setCharacterMag',
      'setCharacterDex',
      'setCharacterSpd',
      'setCharacterLck',
      'setCharacterDef',
      'setCharacterRes',
      'setCharacterCha',
    ]),
  },
  computed: {
    ...mapGetters({
      name: 'getCharacterName',
      lvl: 'getCharacterLvl',
      hp: 'getCharacterHp',
      str: 'getCharacterStr',
      mag: 'getCharacterMag',
      dex: 'getCharacterDex',
      spd: 'getCharacterSpd',
      lck: 'getCharacterLck',
      def: 'getCharacterDef',
      res: 'getCharacterRes',
      cha: 'getCharacterCha',
    }),
    validLevel() {
      return parseInt(this.lvl, 10) >= 1 && parseInt(this.lvl, 10) <= 99 ? null : false;
    },
  },
};
</script>

<style scoped>
</style>
