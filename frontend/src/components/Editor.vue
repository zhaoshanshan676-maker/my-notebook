<template>
  <div class="editor">
    <input class="title" :value="title" @input="$emit('update:title', $event.target.value)" placeholder="请输入标题" />
    <textarea class="content" :value="content" @input="$emit('update:content', $event.target.value)" placeholder="请输入内容"></textarea>
  </div>
</template>

<script setup>
defineProps({ title: String, content: String })
defineEmits(['update:title', 'update:content'])
</script>

<style>
.editor { display: grid; grid-template-rows: auto 1fr }
.title { font-size: 20px; padding: 8px; border: none; border-bottom: 1px solid #eee; outline: none }
.content { padding: 12px; outline: none; border: none; resize: none; width: 100%; height: 100% }
</style>