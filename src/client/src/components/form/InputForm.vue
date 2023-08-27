<template>
  <input
    :type="type"
    :name="name"
    class="base-elm form-value"
    v-model="modelValue"
  />
</template>

<script setup>
import { computed } from 'vue';
import { stringProps, multiTypeProps } from '@/driver/vh';

const props = defineProps({
  type: stringProps(),
  name: stringProps(),
  value: multiTypeProps([Number, String]),
});
const emits = defineEmits(['change']);
const modelValue = computed({
  get: () => props.value,
  set: (value) => {
    emits('change', value);
  },
});
</script>
