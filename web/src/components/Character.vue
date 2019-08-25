<template>
  <div>
    <h2>Character</h2>
    <b-form-select
      @input="setCharacterName"
      :options="characters"
      :value=this.name
      class="mb-2 mr-sm-2 mb-sm-0"
    >
    </b-form-select>
    <b-form-group
      label="Stats"
      label-size="lg"
      label-class="font-weight-bold pt-0"
    >
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
