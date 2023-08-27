import { useStore } from 'vuex';
import { useRouter } from 'vue-router';

export const appInitPath = `${location.pathname}${location.search}${location.hash}`;

export const noLoginPathList = ['/login'];

export const isRequireLogin = !noLoginPathList.includes(appInitPath);

export const resolveInitialPage = (data, router) => {
  if (data.isAuthenticated) {
    if (isRequireLogin) {
      router.push(appInitPath);
    } else {
      router.push('/home');
    }
  } else {
    router.push('/login');
  }
};

export default () => {
  const { dispatch } = useStore();
  const router = useRouter();

  const dispatchResolveInitialPage = async () => {
    dispatch('user/sessionCheck').then((data) => {
      resolveInitialPage(data, router);
    });
  };

  return {
    isRequireLogin,
    dispatchResolveInitialPage,
  };
};
