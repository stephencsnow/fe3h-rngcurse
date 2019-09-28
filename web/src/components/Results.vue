<template>
  <div>
    <b-alert
      v-model="showAlert"
      variant="danger"
      dismissible
    >
      {{ errorMsg }}
    </b-alert>
    <b-button
      type="submit"
      @click="calculate"
    >Submit</b-button>
    <b-modal
      id="results-modal"
      hide-footer
      title="Results"
    >
      <div>
        <b-table
          :items="tableItems"
          :fields="tableFields"
          :tbody-tr-class="rowClass"
        ></b-table>
      </div>
    </b-modal>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import axios from 'axios';

export default {
  data() {
    return {
      showAlert: false,
      errorMsg: null,
      tableItems: [],
      tableFields: ['stat', {
        key: 'percentile',
        formatter: value => `${value.toFixed()}th`,
      }, {
        key: 'percent_of_level_ups', label: '% of Level Ups', formatter: value => `${value.toFixed()}%`,
      }],
    };
  },
  methods: {
    calculate() {
      const data = {
        ...this.character,
        classes: this.formattedClasses,
      };
      axios.post(
        'http://localhost:5000/calculate', data,
      ).then((response) => {
        this.tableItems = this.formatResponse(response.data);
        this.$bvModal.show('results-modal');
      })
        .catch((error) => {
          this.showAlert = true;
          this.errorMsg = error;
        });
    },
    formatResponse(data) {
      return [
        {
          stat: 'HP',
          ...data.hp,
        },
        {
          stat: 'Str',
          ...data.strength,
        },
        {
          stat: 'Mag',
          ...data.magic,
        },
        {
          stat: 'Dex',
          ...data.dexterity,
        },
        {
          stat: 'Spd',
          ...data.speed,
        },
        {
          stat: 'Lck',
          ...data.luck,
        },
        {
          stat: 'Def',
          ...data.defense,
        },
        {
          stat: 'Res',
          ...data.resistance,
        },
        {
          stat: 'Cha',
          ...data.charm,
        },
      ];
    },
    rowClass(item, type) {
      if (!item) return;
      if (item.percentile.toFixed() <= 25) return 'table-danger';
      if (item.percentile.toFixed() >= 75) return 'table-success';
    },
  },
  computed: {
    ...mapGetters({
      character: 'getCharacter',
      formattedClasses: 'getFormattedClasses',
    }),
  },
};
</script>

<style>
</style>
