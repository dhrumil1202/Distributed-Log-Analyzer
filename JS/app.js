const express = require('express')
const sgMail = require('@sendgrid/mail')
const app = express()
var bodyParser = require('body-parser')

var jsonParser = bodyParser.json()
const port = 3000

app.use(bodyParser.urlencoded({extended:false}))
app.use(bodyParser.json())

app.post('/apisendmail', (req, res) => {
    //sgMail.setApiKey(process.env.SENDGRID_API_KEY)
    sgMail.setApiKey("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")
    console.log(req.body)
    email = req.body.email
    console.log(email)
    data = req.body.logs
    console.log(data)
    const msg = {
      to: email, // Change to your recipient
      from: 'dhrumildma@gmail.com', // Change to your verified sender
      subject: 'Error Notification',
      text: 'and easy to do anywhere, even with Node.js',
      html: 'This is a test mail to check sendgrid api service!!!',
    }
    
    sgMail
      .send(msg)
      .then(() => {
        console.log('Email sent')
        response = "Email Sent"
      })
      .catch((error) => {
        console.error(error)
        response = "Error Occured"
      })
  res.send("Email Sent")
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})