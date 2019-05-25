<template>
  <section class="container">
    <select v-model="generationSelection" @change="generationChanged($event)">
      <option v-for="g in generations" v-bind:value="g.value">
        {{g.text}}
      </option>
    </select>

    <div>
      <ul>
        <li v-for="hm in hms">
          <input type="checkbox" :id="hm.name" :value="hm.name" v-model="hmSelection" @change="hmChanged">
          <label :for="hm">{{hm.name}}</label>
        </li>
      </ul>
    </div>

    <ul>
      <li v-for="p in pokemon">
        <pokemon :name="p.name"/>
      </li>
    </ul>
  </section>
</template>

<script>
import intersection from 'lodash'

import Pokemon from '~/components/Pokemon.vue'
import json from '~/hm_data.json'
import allPokemon from '~/all_pokemon.json'

export default {
  components: {
    Pokemon
  },

  data() {
    return {
      checkedNames: [],
      pokemon: [],
      generations: [
        {text: "Gen 1 (RBY)", value: "gen1"},
        {text: "Gen 2 (GSC)", value: "gen2"},
        {text: "Gen 3", value: "gen3"},
        {text: "Gen 4", value: "gen4"}
      ],
      hms: [],
      generationSelection: null,
      hmSelection: []
    }
  },

  methods: {
    clearPokemon: function(event) {
      this.pokemon.splice(0, this.pokemon.length);
    },

    hmChanged: function(event) {
      this.updatePokemonList();
    },

    generationChanged: function(event) {
      this.updateHmList();
      this.updatePokemonList();
    },

    updateHmList: function(event) {
      this.hms.splice(0, this.hms.length);

      var k = Object.keys(json[this.generationSelection])

      k.forEach((e) => {
        this.hms.push({name: e});
      });

      this.hmSelection = [];
    },

    updatePokemonList: function(event) {
      this.clearPokemon();

      if (this.generationSelection === null || this.hmSelection == null) {
        return;
      }

      var hmPokemon = [];

      this.hmSelection.forEach((hm) => {
        if (hmPokemon.length == 0) {
          hmPokemon = json[this.generationSelection][hm];
        }
        else {
          hmPokemon = _.intersection(hmPokemon, json[this.generationSelection][hm]);
        }
      });

      hmPokemon.forEach((e) => {
        this.pokemon.push({
          name: e
        });
      });
    }
  }
};
</script>

<style>
</style>
