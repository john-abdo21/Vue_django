<template>
  <div class="dark size-full">
    <RouterView />
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import useAppInit from '@/composables/useAppInit';

const { isRequireLogin, dispatchResolveInitialPage } = useAppInit();

onMounted(() => {
  if (isRequireLogin) dispatchResolveInitialPage();
});
</script>
