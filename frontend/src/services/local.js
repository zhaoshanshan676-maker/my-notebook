const KEY = 'notebook_notes'

function load() {
  const raw = localStorage.getItem(KEY)
  return raw ? JSON.parse(raw) : []
}

function save(list) {
  localStorage.setItem(KEY, JSON.stringify(list))
}

export function list(q) {
  const items = load().sort((a,b)=>new Date(b.updated_at)-new Date(a.updated_at))
  if (!q) return items.map(n=>({ id:n.id, title:n.title, updated_at:n.updated_at }))
  const like = q.toLowerCase()
  return items.filter(n => (n.title||'').toLowerCase().includes(like) || (n.content||'').toLowerCase().includes(like)).map(n=>({ id:n.id, title:n.title, updated_at:n.updated_at }))
}

export function get(id) {
  const n = load().find(x=>x.id===id)
  return n || null
}

export function create({ title, content }) {
  const items = load()
  const id = items.length ? Math.max(...items.map(i=>i.id))+1 : 1
  const now = new Date().toISOString()
  const n = { id, title, content, summary:'', keywords:[], updated_at: now }
  items.push(n)
  save(items)
  return n
}

export function update(id, { title, content }) {
  const items = load()
  const idx = items.findIndex(i=>i.id===id)
  if (idx<0) return null
  const now = new Date().toISOString()
  items[idx] = { ...items[idx], title, content, updated_at: now }
  save(items)
  return items[idx]
}

export function remove(id) {
  const items = load().filter(i=>i.id!==id)
  save(items)
  return true
}