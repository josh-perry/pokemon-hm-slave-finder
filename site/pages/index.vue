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

var pokes = []

var generations = [
  {text: "Gen 1 (RBY)", value: "gen1"},
  {text: "Gen 2 (GSC)", value: "gen2"}
]

var hms = [
  "cut",
  "flash",
  "surf",
  "fly"
]

export default {
  components: {
    Pokemon
  },

  data() {
    return {
      generationSelection: "gen1",
      pokemon: pokes,
      generations: generations,
      hms: hms,
      hmSelection: "flash"
    }
  },

  methods: {
    clearPokemon: function(event) {
      pokes.splice(0, pokes.length);
    },

    generationChanged: function(event) {
      this.clearPokemon();

      json[this.generationSelection][this.hmSelection].forEach((e) => {
        pokes.push({
          name: e
        });
      });
    }
  }
};
</script>

<style>
</style>
