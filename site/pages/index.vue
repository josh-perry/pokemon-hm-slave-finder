<template>
  <section class="container">
    <select v-model="generationSelection" @change="generationChanged($event)">
      <option v-for="g in generations" v-bind:value="g.value">
        {{g.text}}
      </option>
    </select>

    <select v-model="hmSelection" @change="generationChanged($event)">
      <option v-for="hm in hms" v-bind:value="hm">
        {{hm}}
      </option>
    </select>

    <ul>
      <li v-for="p in pokemon">
        <pokemon :name="p.name"/>
      </li>
    </ul>
  </section>
</template>

<script>
import Pokemon from '~/components/Pokemon.vue'
import json from '~/hm_data.json'

var generations = [
  {text: "Gen 1 (RBY)", value: "gen1"},
  {text: "Gen 2 (GSC)", value: "gen2"}
]

export default {
  components: {
    Pokemon
  },

  data() {
    return {
      pokemon: [],
      generations: [
        {text: "Gen 1 (RBY)", value: "gen1"},
        {text: "Gen 2 (GSC)", value: "gen2"}
      ],
      hms: [],
      generationSelection: null,
      hmSelection: null
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
        this.hms.push(e);
      });

      // If the selected field move isn't in the new generation then reset it
      if (!this.hms.includes(this.hmSelection)) {
        this.hmSelection = null;
      }
    },

    updatePokemonList: function(event) {
      this.clearPokemon();

      if (this.generationSelection === null || this.hmSelection == null) {
        return;
      }

      json[this.generationSelection][this.hmSelection].forEach((e) => {
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
