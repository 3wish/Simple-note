import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

import AutoImport from 'unplugin-auto-import/vite'

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    host: 'localhost',
    port: 3000,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '')
      }
    }
  },
  plugins: [
    vue(),
    AutoImport({
      // targets to transform
      include: [
        /\.[tj]sx?$/,
        /\.vue$/,
        /\.vue\?vue/,
        /\.md$/,
      ],

      // global imports to register
      imports: [
        'vue',
        'vue-router',
        'pinia',
        {
          'axios': [
            ['default', 'axios']
          ]
        }
      ],

      eslintrc: {
        enable: false,
        filepath: './.eslintrc-atuo-import.json'
      }
    }),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
