import axios from 'axios';
import { API_URL } from '@/env';

const axiosClient = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
    Accept: 'application/json',
  },
  responseType: 'json',
  withCredentials: true,
});

const getCSRFToken = () => axiosClient.get('/api/csrf_token');

const validateRequestCallOptions = ({ params, onSuccess, onError }) => {
  if (typeof params !== 'object') {
    throw new Error('"params" is not a object');
  }
  if (typeof onSuccess !== 'function') {
    throw new Error('"onSuccess" is not a function');
  }
  if (typeof onError !== 'function') {
    throw new Error('"onError" is not a function');
  }
};

const defaultRequestOptions = {
  params: {},
  onSuccess: (res) => res,
  onError: (e) => {
    throw e;
  },
};

export const get = (url, options = {}) => {
  const { params, onSuccess, onError } = {
    ...defaultRequestOptions,
    ...options,
  };
  validateRequestCallOptions({ params, onSuccess, onError });
  return axiosClient.get(url, { params }).then(onSuccess).catch(onError);
};

export const post = (url, options = {}) => {
  return getCSRFToken().then((res) => {
    const config = {
      headers: { 'X-CSRF-TOKEN': res.data.token },
    };
    const { params, onSuccess, onError } = {
      ...defaultRequestOptions,
      ...options,
    };
    validateRequestCallOptions({ params, onSuccess, onError });
    return axiosClient.post(url, params, config).then(onSuccess).catch(onError);
  });
};
