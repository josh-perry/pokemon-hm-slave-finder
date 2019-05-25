<template>
  <section class="container">
    <h1>Pokemon HM Slave Finder Thing</h1>

    <div class="block">
      <h2>Which generation are you playing?</h2>
      <select v-model="generationSelection" @change="generationChanged($event)">
        <option v-for="g in generations" v-bind:value="g.value">
          {{g.text}}
        </option>
      </select>
    </div>

    <div v-if="generationSelection" class="block">
      <h2>Which HMs do you need the Pokemon to know?</h2>
      <ul>
        <li v-for="hm in hms">
          <input type="checkbox" :id="hm.name" :value="hm.name" v-model="hmSelection" @change="hmChanged">
          <label :for="hm">{{hm.name}}</label>
        </li>
      </ul>
    </div>

    <div v-if="hmSelection.length > 0" class="block">
      <h2>These Pokemon can learn those HMs</h2>
      <div class="flex-container">
        <pokemon v-for="p in pokemon" :pokemon="p" :generation="generationSelection"/>
      </div>
    </div>
  </section>
</template>

<script>
import intersectionBy from 'lodash'

import Pokemon from '~/components/Pokemon.vue'
import json from '~/static/hm_data.json'

export default {
  components: {
    Pokemon
  },

  data() {
    return {
      checkedNames: [],
      pokemon: [],
      generations: [
        {text: "Red/Blue/Yellow", value: "gen1"},
        {text: "Gold/Silver/Crystal", value: "gen2"},
        {text: "Ruby/Sapphire/Emerald/FireRed/LeafGreen", value: "gen3"},
        {text: "Diamond/Pearl/Platinum/SoulSilver/HeartGold", value: "gen4"}
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
          hmPokemon = _.intersectionBy(hmPokemon, json[this.generationSelection][hm], 'id');
        }
      });

      hmPokemon.forEach((e) => {
        this.pokemon.push(e);
      });
    }
  }
};
</script>

<style>
.block {
  margin-top: 5%;
  padding: 5%;
  border: 1px solid #5c5c5c;
}

select {
  width: 100%;
}

ul {
  list-style: none;
}

.flex-container {
  display: flex;
  flex-wrap: wrap;
}

h2 {
  margin-bottom: 5%;
}
</style>
