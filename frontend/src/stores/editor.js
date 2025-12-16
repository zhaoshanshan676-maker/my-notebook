import { defineStore } from 'pinia'
import api from '../services/api'

export const useEditorStore = defineStore('editor', {
  state: () => ({ current: null, title: '', content: '', summary: '', keywords: [] }),
  actions: {
    setCurrent(note) { this.current = note; this.title = note.title || ''; this.content = note.content || ''; this.summary = note.summary || ''; this.keywords = note.keywords || [] },
    setTitle(v) { this.title = v },
    setContent(v) { this.content = v },
    async summarize(id) {
      try {
        const res = await api.post('/api/ai/summarize', { note_id: id })
        this.summary = res.data.summary; this.keywords = res.data.keywords
      } catch {}
    },
    async enhance(text) {
      try {
        const res = await api.post('/api/ai/enhance', { text })
        return res.data.enhanced_text
      } catch {
        return text
      }
    }
  }
})