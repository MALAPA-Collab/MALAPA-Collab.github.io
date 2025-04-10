import { defineConfig } from 'astro/config';

export default defineConfig({
  output: 'static',
  base: '/',  // root — because it's an org/user GitHub Pages site
});