const admin = require('firebase-admin')
const uuidv4 = require('uuid/v4')
let serviceAccount = require('./shellhacks2019-e4acf182aaa4.json')
admin.initializeApp(
    {
        credential: admin.credential.cert(serviceAccount)
    }
)
let db = admin.firestore();


const app = require('express')()
const server = require('http').Server(app)
const io = require('socket.io')(server)

const bodyParser = require('body-parser')
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
app.post('/addMarker', async (req,res) => {
    let input = req.body
    let humid = req.body.humidity
    let hf = req.body.hasFlooded
    let bodyt = req.body.bodytext
    let hfall = req.body.fall
    let temp = req.body.temp
    const theid = uuidv4()
    console.log(theid)
    try {
        db.collection('users').doc(theid).set(
            {
                "humidity": humid,
                "hasFlooded": hf,
                "bodytext": bodyt,
                "temp": temp
            }
        ).then(function() {
            console.log(`document ${id} created`);
        })
        res.status(200).send(input)
    } catch(error) {
        res.status(502).send(error)
    }
})


server.listen(8080, () => {
    const host = server.address().address
    const port = server.address().port
    console.log(`Example app listening at http://${host}:${port}`);
})