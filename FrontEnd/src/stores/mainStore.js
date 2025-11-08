import { defineStore } from "pinia";
import api from "@/services/api";

export const useMainStore = defineStore("main", {
  state: () => ({
    // Estado global
    theme: "light",
    loading: false,
    error: null,

    // Contenido del backend
    content: [],
    bibliography: [],
  }),

  actions: {
    async fetchContent(sectionSlug) {
      this.loading = true;
      this.error = null;
      try {
        const res = await api.get(`content/?section=${sectionSlug}`);
        this.content = res.data;
      } catch (err) {
        this.error = err;
      } finally {
        this.loading = false;
      }
    },

    async fetchBibliography() {
      this.loading = true;
      this.error = null;
      try {
        const res = await api.get("bibliography/");
        this.bibliography = res.data;
      } catch (err) {
        this.error = err;
      } finally {
        this.loading = false;
      }
    },
  },
});
