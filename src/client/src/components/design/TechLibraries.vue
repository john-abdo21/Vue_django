<template>
  <section class="grid grid-rows-2 grid-cols-3 gap-6 brightness-125">
    <img :src="django" class="tech-icon django-img" />
    <img :src="mariadb" class="tech-icon mariadb-shadow" />
    <img :src="docker" class="tech-icon docker-img" />
    <img :src="vue" class="tech-icon vue-img" />
    <img :src="tailwind" class="tech-icon tailwind-img" />
    <img :src="vite" class="tech-icon vite-img" />
  </section>
</template>

<script setup>
import django from '@/assets/django.svg';
import docker from '@/assets/docker.webp';
import mariadb from '@/assets/mariadb.svg';
import tailwind from '@/assets/tailwind.svg';
import vite from '@/assets/vite.svg';
import vue from '@/assets/vue.svg';
</script>
