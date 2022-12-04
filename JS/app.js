const express = require('express')
const sgMail = require('@sendgrid/mail')
const app = express()
const port = 3000

app.get('/apisendmail', (req, res) => {
    //sgMail.setApiKey(process.env.SENDGRID_API_KEY)
    sgMail.setApiKey("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")
    const msg = {
      to: 'dhrumildma@gmail.com', // Change to your recipient
      from: 'dhrumildma@gmail.com', // Change to your verified sender
      subject: 'Sending with SendGrid is Fun',
      text: 'and easy to do anywhere, even with Node.js',
      html: '<strong>and easy to do anywhere, even with Node.js</strong>',
    }
    sgMail
      .send(msg)
      .then(() => {
        console.log('Email sent')
      })
      .catch((error) => {
        console.error(error)
      })
  res.send('Hello World!')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})