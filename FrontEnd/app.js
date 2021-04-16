const express = require('express');
const router = express.Router();
const app = express();
const mongoose = require('mongoose');
const expressEjsLayout = require('express-ejs-layouts')
//mongoose
mongoose.connect('mongodb://localhost/test',{useNewUrlParser: true, useUnifiedTopology : true})
.then(() => console.log('connected,,'))
.catch((err)=> console.log(err));
//EJS
app.set('view engine', 'ejs');
app.use(expressEjsLayout);
//bodyparser
app.use(express.urlencoded({extended : false}));

//routes
app.use('/', require('../../../../Desktop/frontend/routes'));
app.use('/users',require('../../../../Desktop/frontend/routes/users'));

app.listen(3000);
