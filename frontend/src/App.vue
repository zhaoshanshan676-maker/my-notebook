<template>
  <div class="layout">
    <Sidebar :notes="notes" :loading="loading" @select="onSelect" @create="onCreate" />
    <div class="content">
      <Toolbar :note="current" @save="onSave" @delete="onDelete" @summarize="onSummarize" @enhance="onEnhance" />
      <SearchBar @search="onSearch" />
      <Editor v-model:title="title" v-model:content="content" />
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue'
import Sidebar from './components/Sidebar.vue'
import Toolbar from './components/Toolbar.vue'
import SearchBar from './components/SearchBar.vue'
import Editor from './components/Editor.vue'
import { useNotesStore } from './stores/notes'
import { useEditorStore } from './stores/editor'

const notesStore = useNotesStore()
const editorStore = useEditorStore()

const notes = computed(() => notesStore.list)
const loading = computed(() => notesStore.loading)
const current = computed(() => editorStore.current)
const title = computed({
  get: () => editorStore.title,
  set: v => editorStore.setTitle(v)
})
const content = computed({
  get: () => editorStore.content,
  set: v => editorStore.setContent(v)
})

onMounted(() => {
  notesStore.fetchList()
})

function onSelect(id) {
  notesStore.fetchDetail(id).then(note => editorStore.setCurrent(note))
}

function onCreate() {
  notesStore.create({ title: '未命名', content: '' }).then(note => editorStore.setCurrent(note))
}

function onSave() {
  if (!current.value) return
  notesStore.update(current.value.id, { title: title.value, content: content.value })
}

function onDelete() {
  if (!current.value) return
  notesStore.remove(current.value.id).then(() => notesStore.fetchList())
}

function onSummarize() {
  if (!current.value) return
  editorStore.summarize(current.value.id)
}

function onEnhance() {
  editorStore.enhance(content.value).then(text => editorStore.setContent(text))
}

function onSearch(q) {
  notesStore.search(q)
}
</script>

<style>
.layout { display: grid; grid-template-columns: 280px 1fr; height: 100vh; }
.content { display: grid; grid-template-rows: auto auto 1fr; }
</style>