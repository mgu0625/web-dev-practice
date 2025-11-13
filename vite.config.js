// vite.config.js (repo root)
import { join, resolve } from 'path'
import fs from 'fs'
import glsl from 'vite-plugin-glsl'

const LESSONS_ROOT = 'NodeAndThreeJS_Projects'

function discoverLessonInputs() {
  const absRoot = join(process.cwd(), LESSONS_ROOT)
  const inputs = {}

  if (!fs.existsSync(absRoot)) return inputs

  for (const d of fs.readdirSync(absRoot, { withFileTypes: true })) {
    if (!d.isDirectory()) continue
    if (!/^Lesson\d+$/i.test(d.name)) continue

    const html = join(absRoot, d.name, 'src', 'index.html')
    if (fs.existsSync(html)) {
      // Use a key that preserves folders in dist/
      const key = `${LESSONS_ROOT}/${d.name}/src/index`
      inputs[key] = resolve(html)
    }
  }
  return inputs
}

export default {
  plugins: [glsl()],
  build: {
    outDir: 'dist',
    emptyOutDir: true,
    rollupOptions: {
      const: 0, // placeholder to avoid trailing comma issues in some editors
      input: (() => {
        const i = discoverLessonInputs()
        if (Object.keys(i).length) return i
        throw new Error(
          `No entries found. Expected ${LESSONS_ROOT}/LessonXX/src/index.html`
        )
      })()
    }
  }
}
