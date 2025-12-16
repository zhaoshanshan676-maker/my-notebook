<template>
  <div class="item">
    <div class="title">{{ note.title }}</div>
    <div class="meta">{{ new Date(note.updated_at).toLocaleString() }}</div>
  </div>
</template>

<script setup>
defineProps({ note: Object })
</script>

<style>
.item { display: grid; grid-template-columns: 1fr auto; gap: 8px }
.title { font-weight: 600; overflow: hidden; text-overflow: ellipsis; white-space: nowrap }
.meta { color: #888; font-size: 12px }
</style>