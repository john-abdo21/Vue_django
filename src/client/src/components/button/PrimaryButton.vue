<template>
  <BaseButton class="base-button bg-main-primary" :type="type" @click="onClick">
    <slot></slot>
  </BaseButton>
</template>

<script setup>
import { unionProps, funcProps } from '@/driver/vh';
import BaseButton from './BaseButton.vue';

const props = defineProps({
  type: unionProps(String, ['button', 'submit']),
  onClick: funcProps(),
});
</script>
