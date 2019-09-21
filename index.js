const admin = require('firebase-admin')
let serviceAccount = require('./shellhacks2019-e4acf182aaa4.json')
admin.initializeApp(
    {
        credential: admin.credential.cert(serviceAccount)
    }
)
let db = admin.firestore();


const express = require('express')
const bodyParser = require('body-parser')

const app = express()
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended: false}))
app.get('/markers',async (req, res) => {
    let alldata = []
    await db.collection('users').get()
        .then((snapshot) => {
            snapshot.forEach((doc) => {
            console.log(doc.id, '=>', JSON.stringify(doc.data()));
            alldata.push(JSON.stringify(doc.data()))
            });
        })
        .catch((err) => {
            console.log('Error getting documents', err);
            res.status(500).send('Error')
    });
    res.status(200).send(alldata)
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