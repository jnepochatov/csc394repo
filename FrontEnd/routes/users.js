const express = require('express');
const router = express.Router();

//GET
router.get('/login', (req,res)=>{
	res.render('login');
})
router.get('/register',(req,res)=>{
	res.render('register')
	})
router.get('/home', (req, res)=>{
	res.render('home')
})
router.get('/termsOfAgreement',(req, res)=>{
	res.render('termsOfAgreement')
})
router.get('/aboutUs',(req, res)=>{
	res.render('aboutUs')
})
router.get('/help',(req, res)=>{
	res.render('help')
})
router.get('/faq',(req, res)=>{
	res.render('faq')
})
router.get('/contactUs',(req, res)=>{
	res.render('contactUs')
})
router.get('/baseProfile',(req, res)=>{
	res.render('baseProfile')
})
router.get('/jobSearch',(req, res)=>{
	res.render('jobSearch')
})
router.get('/applications',(req, res)=>{
	res.render('applications')
})
router.get('/settings',(req, res)=>{
	res.render('settings')
})
router.get('/testing',(req, res)=>{
	res.render('testing')
})




//POST
router.post('/register',(req,res)=>{
})
router.post('/login',(req,res,next)=>{
	})
router.post('/home',(req,res)=>{
})
router.post('/termsOfAgreement', (req,res)=>{
})
router.post('/aboutUs', (req,res)=>{
})
router.post('/help', (req,res)=>{
})
router.post('/faq', (req,res)=>{
})

router.post('/baseProfile', (req,res)=>{
})
router.post('/testing', (req,res)=>{
})




//logout
router.get('/logout',(req,res)=>{
})






//home
router.get('/home', (req, res)=>{
})
router.get('/termsOfAgreement', (req,res)=>{
})
router.get('/aboutUs', (req,res)=>{
})
router.get('/help', (req,res)=>{
})
router.get('/baseProfile', (req,res)=>{
})
router.get('/testing', (req,res)=>{
})

module.exports = router;
