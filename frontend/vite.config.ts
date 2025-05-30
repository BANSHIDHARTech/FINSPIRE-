import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";
import path from "path";


const noopPlugin = () => ({
  name: "noop-plugin",
});

export default defineConfig(({ mode }) => ({
  server: {
    host: "::",
    port: 8080,
  },
  plugins: [
    react(),
    mode === "development" && noopPlugin(),
  ].filter(Boolean),
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
}));

