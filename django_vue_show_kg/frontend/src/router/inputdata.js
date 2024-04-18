/**
 * 请求接口js
 */

import { request2 } from "./axios3"

/**
 * Search data interface
 * @param {dict} params {"field": "value"}
 * @returns 
 */
export const inputData = (params) => {
    return request2({
        url: "/api/peoplesubmit/",
        method: "POST",
        headers: {"Content-Type": "application/x-www-form-urlencoded"},
        data: params
    })
}  


