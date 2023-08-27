<template>
  <button class="base-button" :type="type" @click="onClick">
    <slot></slot>
  </button>
</template>

<script setup>
import { unionProps, funcProps } from '@/driver/vh';

const props = defineProps({
  type: unionProps(String, ['button', 'submit']),
  onClick: funcProps(),
});
</script>
