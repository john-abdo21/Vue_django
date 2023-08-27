import { reactive } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
import { resolveInitialPage } from '@/composables/useAppInit';

export default () => {
  const { dispatch } = useStore();
  const router = useRouter();

  const formState = reactive({
    loginId: '',
    password: '',
  });

  const setLoginId = (value) => {
    formState.loginId = value;
  };

  const setPassword = (value) => {
    formState.password = value;
  };

  const dispatchLogin = () => {
    dispatch('user/login', {
      params: {
        loginId: formState.loginId,
        password: formState.password,
      },
    }).then((data) => {
      resolveInitialPage(data, router);
    });
  };

  const dispatchLogout = () => {
    dispatch('user/logout').then(() => {
      router.push('/login');
    });
  };

  return {
    formState,
    setLoginId,
    setPassword,
    dispatchLogin,
    dispatchLogout,
  };
};
