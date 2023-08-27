import { get, post } from '@/driver/api';

export default {
  namespaced: true,
  state: {
    isAuthenticated: false,
    loginId: '',
    firstName: '',
    lastName: '',
    enFirstName: '',
    enLastName: '',
  },
  getters: {
    greetingMessage(state) {
      return `ようこそ${state.lastName}${state.firstName}さん`;
    },
  },
  mutations: {
    setUserState(
      state,
      {
        isAuthenticated,
        loginId = '',
        firstName = '',
        lastName = '',
        enFirstName = '',
        enLastName = '',
      },
    ) {
      state.isAuthenticated = isAuthenticated;
      state.loginId = loginId;
      state.firstName = firstName;
      state.lastName = lastName;
      state.enFirstName = enFirstName;
      state.enLastName = enLastName;
    },
    resetUserState(state) {
      state.isAuthenticated = false;
      state.loginId = '';
      state.firstName = '';
      state.lastName = '';
      state.enFirstName = '';
      state.enLastName = '';
    },
  },
  actions: {
    async sessionCheck({ commit }) {
      return get('/api/session_check').then((res) => {
        commit('setUserState', res.data);
        return res.data;
      });
    },
    async login({ commit }, payload) {
      return post('/api/login', payload).then((res) => {
        commit('setUserState', res.data);
        return res.data;
      });
    },
    async logout({ commit }) {
      return post('/api/logout').then((res) => {
        commit('resetUserState');
        return res.data;
      });
    },
  },
};
