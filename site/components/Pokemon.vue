<template>
  <div class="pokemon">
    <img :src="`img/${generation}/${pokemon.id}.png`">

    <span>
      {{pokemon.name}}
    </span>
  </div>
</template>

<script>
export default {
  props: ["pokemon", "generation"]
}
</script>

<style>
.pokemon {
  border: 1px #373737 solid;
  flex: 0 0 50%;
}

.pokemon > img {
  width: 20%;
  height: auto;
  vertical-align: middle;
}
</style>
