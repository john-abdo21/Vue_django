<template>
  <div class="non-navigation-page">
    <div>{{ greetingMessage }}</div>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useStore } from 'vuex';

const store = useStore();
const greetingMessage = computed(() => {
  return store.getters['user/greetingMessage'];
});
</script>
