// vite.config.js (repo root)
import { resolve, join } from 'path'
import fs from 'fs'
import glsl from 'vite-plugin-glsl'

const LESSONS_ROOT = 'NodeAndThreeJS_Projects'

function discoverLessonHtmlInputs() {
  const abs = join(process.cwd(), LESSONS_ROOT)
  if (!fs.existsSync(abs)) return []

  return fs
    .readdirSync(abs, { withFileTypes: true })
    .filter(d => d.isDirectory() && /^Lesson\d+$/i.test(d.name))
    .map(d => {
      const html = join(abs, d.name, 'index.html')
      return fs.existsSync(html) ? resolve(html) : null
    })
    .filter(Boolean)
}

export default {
  plugins: [glsl()],
  build: {
    outDir: 'dist',
    emptyOutDir: true,
    rollupOptions: {
      input: discoverLessonHtmlInputs()
    }
  }
}
