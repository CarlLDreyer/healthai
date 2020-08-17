import axios from 'axios'

export default () => {
  return axios.create({
    baseUrl: 'http://localhost:5005',
  })
}
