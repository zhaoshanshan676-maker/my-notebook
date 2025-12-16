<template>
  <div class="search">
    <input :value="q" @input="onInput" placeholder="搜索" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
const q = ref('')
const emit = defineEmits(['search'])
function onInput(e) { q.value = e.target.value; emit('search', q.value) }
</script>

<style>
.search { padding: 8px; border-bottom: 1px solid #eee }
.search input { width: 100%; padding: 6px 8px }
</style>