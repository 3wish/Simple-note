const request = axios.create({
  baseURL: 'http://localhost:3000/api',
  // use the following baseURL when you depoly this app.
  //baseURL: 'http://your_server_ip/your_server_port'
  timeout: 5000,
});

request.interceptors.request.use(
  config => config,
  error => Promise.reject(error)
);

request.interceptors.response.use(
  response => {
    if (response.status >= 200 && response.status < 400) {
      return response.data;
    }
  },

  error => Promise.reject(error)
);

export default request;

