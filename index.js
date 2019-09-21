const express = require('express')
const bodyParser = require('body-parser')

const app = express()
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended: false}))
app.get('/markers', (req, res) => {
    const the_data = {
        worked: 'YAy'
    }    
    res.status(200).send('Hello World')
})
app.post('/markers', (req,res) => {
    try {
        const data = req.body
        let temp = req.body.temp
        let humidity = req.body.humidity
        let hasFallen = req.body.fall

        
    } catch (e) {
        res.status(500).send('Nan')
    }
})


const server = app.listen(8080, () => {
    const host = server.address().address
    const port = server.address().port
    console.log(`Example app listening at http://${host}:${port}`);
})