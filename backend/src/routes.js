const express = require('express');
//const crypto = require('crypto');
const { celebrate, Segments, Joi } = require('celebrate');

const UsersAPI = require('./components/users/usersAPI');



const routes = express.Router();



routes.get('/', (request, response) => {
	return response.send('Bem vindo à API da parceria Intermídia x Articfox!');
});

routes.post('/api/register', UsersAPI.create);
routes.post('/api/login', UsersAPI.index);


/*exportando as rotas para que outros arquivos possam 'enxergar' routes.js*/
module.exports = routes;