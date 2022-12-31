import request from "./request";

const userRegister = (username, password) => {
  return request.post(
    'user/register',
    {username, password},
  );
}

const userLogin = (formData, isKeep) => {
  return request.post(
    `user/token`,
    formData,
    {
      params: {is_keep: isKeep}
    }  
  )
}

const userAutoLogin = token => {
  return request.get(
    'user/login',
    {
      headers: {'Authorization': token}
    }
  )
}

export {userRegister, userLogin, userAutoLogin}