<template>
  <SectionContainer>
    <form method="post" class="login-form" @submit.prevent="dispatchLogin">
      <InputFormControl
        :type="'text'"
        :name="'username'"
        :label="'ログインID'"
        :value="formState.loginId"
        :direction="'col'"
        @change="setLoginId"
      />
      <InputFormControl
        :type="'password'"
        :name="'password'"
        :label="'パスワード'"
        :value="formState.password"
        :direction="'col'"
        @change="setPassword"
      />
      <PrimaryButton :type="'button'" :onClick="dispatchLogin"
        >ログイン</PrimaryButton
      >
    </form>
  </SectionContainer>
</template>

<script setup>
import SectionContainer from '@/components/layout/SectionContainer.vue';
import InputFormControl from '@/components/form/InputFormControl.vue';
import PrimaryButton from '@/components/button/PrimaryButton.vue';
import useAuth from '@/composables/useAuth';

const { formState, setLoginId, setPassword, dispatchLogin } = useAuth();
</script>
