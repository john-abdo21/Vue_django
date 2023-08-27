import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import jsconfigPaths from 'vite-jsconfig-paths';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue(), jsconfigPaths()],
  server: {
    watch: {
      usePolling: true,
    },
  },
});
