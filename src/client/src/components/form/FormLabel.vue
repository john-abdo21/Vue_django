<template>
  <label class="form-label">{{ label }}</label>
</template>

<script setup>
import { stringProps } from '@/driver/vh';

const props = defineProps({
  label: stringProps(),
});
</script>
