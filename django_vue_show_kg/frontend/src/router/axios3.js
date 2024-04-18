/**
 * django 基础请求网络发送包定义
 */

import axios from 'axios'

const request2 = axios.create({
  baseURL: 'http://127.0.0.1:8000',
  timeout: 15000,
})


//切割字符串
let getCookie = function (name, token) {
  console.log("name=", name)
  console.log("token=", token)
  var value = '; ' + token
  var parts = value.split('; ' + name + '=')
  if (parts.length === 2) return parts.pop().split(';').shift()
}

request2.interceptors.request.use(
  function(config) {
    // 在post请求前统一添加X-CSRFToken的header信息
    let token = document.cookie;
    if(token && config.method == 'post'){
      config.headers['X-CSRFToken'] = getCookie('csrftoken',token);
    }
    return config;
  },
  function(error) {
    // Do something with request error
    return Promise.reject(error);
  }
)

request2.interceptors.response.use(
	response => {
    console.log("====response.data:", response.data)
    return response.data
  }
)

 export {
  request2
 } 
