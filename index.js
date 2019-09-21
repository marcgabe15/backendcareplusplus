const Firestore = require('@google-cloud/firestore')
const firestore = new Firestore({
    projectId: 'shellhacks2019-1f061',
    keyFileName: '../shellhacks2019-1f061-0e7bb7b00044.json'
})


let documentRef = firestore.doc('users/6DpUCcj3yX8Zfj9goBQ1')
documentRef.get().then(documentSnapshot => {
    if (documentSnapshot.exists) {
        console.log(createTime.toDate())
    }
}).catch((err) => {
    console.log(err)
    console.log("Promise rejected")
})
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
        let hasFlooded = req.body.flooded
        let body_text = req.body.text

        
    } catch (e) {
        res.status(500).send('Nan')
    }
})


const server = app.listen(8080, () => {
    const host = server.address().address
    const port = server.address().port
    console.log(`Example app listening at http://${host}:${port}`);
})