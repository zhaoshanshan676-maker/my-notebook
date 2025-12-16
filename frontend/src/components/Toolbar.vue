<template>
  <div class="toolbar">
    <button @click="$emit('save')">保存</button>
    <button @click="$emit('delete')">删除</button>
    <button @click="$emit('summarize')">AI 总结</button>
    <button @click="$emit('enhance')">AI 润色</button>
  </div>
</template>

<script setup>
defineProps({ note: Object })
defineEmits(['save','delete','summarize','enhance'])
</script>

<style>
.toolbar { display: flex; gap: 8px; padding: 8px; border-bottom: 1px solid #eee }
.toolbar button { padding: 6px 10px }
</style>