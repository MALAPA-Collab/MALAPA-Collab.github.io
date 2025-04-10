import { defineConfig } from 'astro/config';

export default defineConfig({
  output: 'static',
  base: '/',  // correct for your case
  site: 'https://malapa-collab.github.io/',  // <-- this is key
});