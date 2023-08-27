<template>
  <div class="form-control" :class="direction === 'row' || 'flex-col'">
    <FormLabel :label="label" />
    <div>
      <InputForm :type="type" :name="name" :value="value" @change="setValue" />
    </div>
  </div>
</template>
<script setup>
import InputForm from '@/components/form/InputForm.vue';
import FormLabel from '@/components/form/FormLabel.vue';
import { stringProps, multiTypeProps, unionProps } from '@/driver/vh';

const props = defineProps({
  type: stringProps(),
  name: stringProps(),
  label: stringProps(),
  value: multiTypeProps([Number, String]),
  direction: unionProps(String, ['row', 'col'], 'row'),
});
const emits = defineEmits(['change']);
const setValue = (value) => {
  emits('change', value);
};
</script>
