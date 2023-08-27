import { computed } from 'vue';
import { useStore } from 'vuex';

export default () => {
  const store = useStore();
  const isAuthenticated = computed(() => store.state.user.isAuthenticated);

  return {
    isAuthenticated,
  };
};
