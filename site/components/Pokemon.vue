<template>
  <div>
    <img :src="`img/${generation}/${pokemon.id}.png`">
    {{pokemon.name}}
  </div>
</template>

<script>
export default {
  props: ["pokemon", "generation"]
}
</script>
