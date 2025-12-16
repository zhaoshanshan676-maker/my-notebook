import { defineStore } from 'pinia'
import api from '../services/api'
import * as local from '../services/local'

export const useNotesStore = defineStore('notes', {
  state: () => ({ list: [], loading: false }),
  actions: {
    async fetchList(q) {
      this.loading = true
      try {
        const res = await api.get('/api/notes', { params: q ? { q } : {} })
        this.list = res.data
      } catch {
        this.list = local.list(q)
      } finally { this.loading = false }
    },
    async fetchDetail(id) {
      try {
        const res = await api.get(`/api/notes/${id}`)
        return res.data
      } catch {
        return local.get(id)
      }
    },
    async create(payload) {
      try {
        const res = await api.post('/api/notes', payload)
        await this.fetchList()
        return res.data
      } catch {
        const n = local.create(payload)
        await this.fetchList()
        return n
      }
    },
    async update(id, payload) {
      try {
        const res = await api.put(`/api/notes/${id}`, payload)
        await this.fetchList()
        return res.data
      } catch {
        const n = local.update(id, payload)
        await this.fetchList()
        return n
      }
    },
    async remove(id) {
      try {
        await api.delete(`/api/notes/${id}`)
        await this.fetchList()
      } catch {
        local.remove(id)
        await this.fetchList()
      }
    },
    async search(q) { await this.fetchList(q) }
  }
})