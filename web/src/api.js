import axios from 'axios'
import { server } from './sets'

function serverRequest(method, json={}) {
	console.log(server.link + method, json)
	return axios.post(server.link + method, json)
}

function handlerResult(res, handlerSuccess, handlerError) {
	if (res['error']) {
		console.log(res)
		handlerError(res)
	} else {
		console.log(res)
		handlerSuccess(res)
	}
}

export default function api(method, json={}, handlerSuccess=()=>{}, handlerError=()=>{}) {
	json['token'] = localStorage.getItem('token')
	serverRequest(method, json).then((res) => handlerResult(res.data, handlerSuccess, handlerError))
}