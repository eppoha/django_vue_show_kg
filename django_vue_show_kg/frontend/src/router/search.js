/**
 * 请求接口js
 */

import { request2 } from "./axios2"

/**
 * Search data interface
 * @param {dict} params {"field": "value"}
 * @returns 
 */
export const searchData = (params) => {
    return request2({
        url: "/api/peoplesearch/",
        method: "POST",
        headers: {"Content-Type": "application/x-www-form-urlencoded"},
        data: params
    })
}  


