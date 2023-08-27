<template>
  <header class="flex h-14 p-3 base-elm border-b-2 border-b-main-primary">
    <div class="text-2xl">Dashboard</div>
    <UserMenu />
  </header>
</template>

<script setup>
import UserMenu from '@/features/userMenu/UserMenu.vue';
</script>
