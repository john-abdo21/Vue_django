<template>
  <Menu v-if="isAuthenticated">
    <MenuButton :class="'ml-auto'">
      <AnonymousUserIcon size="2xl" />
    </MenuButton>
    <MenuItems
      :as="'ul'"
      :class="'base-secondary-elm drop-shadow-lg absolute right-0 mt-10 mr-2 p-2 rounded-md'"
    >
      <MenuItem :as="'li'">
        <button
          type="button"
          class="w-full flex gap-2 items-center py-1 px-2 rounded-md text-left hover:bg-main-primary"
        >
          <ProfileEditIcon size="sm" />プロフィール
        </button>
      </MenuItem>
      <MenuItem :as="'li'">
        <button
          type="button"
          class="w-full flex gap-2 items-center py-1 px-2 rounded-md text-left hover:bg-main-primary"
          @click="dispatchLogout"
        >
          <LogoutIcon size="sm" />ログアウト
        </button>
      </MenuItem>
    </MenuItems>
  </Menu>
</template>
<script setup>
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue';
import AnonymousUserIcon from '@/components/icon/AnonymousUserIcon.vue';
import LogoutIcon from '@/components/icon/LogoutIcon.vue';
import ProfileEditIcon from '@/components/icon/ProfileEditIcon.vue';
import useAuth from '@/composables/useAuth';
import useUserState from '@/composables/useUserState';

const { dispatchLogout } = useAuth();
const { isAuthenticated } = useUserState();
</script>
