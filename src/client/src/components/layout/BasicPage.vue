<template>
  <div class="base-elm size-full">
    <PageHeader />
    <RouterView />
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import PageHeader from '@/components/layout/PageHeader.vue';

export default defineComponent({
  name: 'BasicPage',
  components: {
    PageHeader,
  },
});
</script>
