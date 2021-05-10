const express = require('express');
const router = express.Router();
var multer = require('multer');

//login page

router.get('/', (req, res)=>{
	res.render('welcome');
})
//register page
router.get('/register', (req, res)=>{
	res.render('register');
})
router.get('/home', (req, res)=>{
	res.render('home');
})

router.get('/termsOfAgreement',(req,res)=>{
	res.render('termsOfAgreement')
})

router.get('/aboutUs',(req,res)=>{
	res.render('AboutUs')
})
router.get('/help',(req,res)=>{
	res.render('help')
})
router.get('/faq',(req,res)=>{
	res.render('faq')
})
router.get('/contactUs',(req,res)=>{
	res.render('contactUs')
})
router.get('/baseProfile',(req,res)=>{
	res.render('baseProfile')
})
router.get('/jobSearch',(req,res)=>{
	res.render('jobSearch')
})
router.get('/applications',(req,res)=>{
	res.render('applications')
})
router.get('/settings',(req,res)=>{
	res.render('settings')
})
router.get('/testing',(req,res)=>{
	res.render('testing')
})
//to use router instance in other files
module.exports = router


