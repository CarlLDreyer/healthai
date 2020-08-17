const express = require('express')
// const path = require('path')
// const https = require('https')
const http = require('http')
// const axios = require('axios')
// const fs = require('fs')
const bodyParser = require('body-parser')
const app = express()

// const httpsOptions = {
//   cert: fs.readFileSync('./ssl/selfsigned.crt'),
//   key: fs.readFileSync('./ssl/selfsigned.key')
// }

const port = process.env.PORT || '3000'
app.set('port', port)

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: false }))

app.get('/', (req, res) => {
  res.send('Backend running')
})

// app.post('/rasa', (req, res) => {
//   axios({
//     method: 'post',
//     url: 'https://10.241.40.8:5005/webhooks/rest/webhook',
//     data: req.body
//   })
//     .then((response) => {
//       res.send(response.data)
//       res.end()
//     })
//     .catch((error) => {
//       res.status(400).end()
//     })
// })

// const server = https.createServer(httpsOptions, app)
const server = http.createServer(app);

server.listen(port, () => console.log(`API running on ${port}`))
