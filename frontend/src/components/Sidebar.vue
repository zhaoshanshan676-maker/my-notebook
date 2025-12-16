<template>
  <div class="sidebar">
    <div class="header">
      <button @click="$emit('create')">新建笔记</button>
    </div>
    <div v-if="loading" class="loading">加载中</div>
    <ul v-else class="list">
      <li v-for="n in notes" :key="n.id" @click="$emit('select', n.id)">
        <NoteListItem :note="n" />
      </li>
    </ul>
  </div>
  </template>

<script setup>
import NoteListItem from './NoteListItem.vue'
defineProps({ notes: Array, loading: Boolean })
</script>

<style>
.sidebar { border-right: 1px solid #eee; padding: 8px; overflow: auto }
.header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px }
.list { list-style: none; padding: 0; margin: 0 }
.list li { padding: 8px; cursor: pointer }
.list li:hover { background: #f7f7f7 }
</style>