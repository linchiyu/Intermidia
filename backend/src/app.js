const express = require('express');
/*importação do validador*/
const { errors } = require('celebrate'); 
/*importação do modulo de segurança de acesso*/
const cors = require('cors');
/*importação das rotas*/
const routes = require('./routes');

const app = express();

/*informar a url da requisição que é autorizada
se deixar vazio, todas as apps podem acessar
*/
app.use(cors());
/*app.use(cors({
	origin: 'http://meuapp.com'
}));*/

/*informar ao app que as requisições deverão ser tratadas como json
express irá converter as requisições de json para objeto*/
app.use(express.json());
app.use(routes);
app.use(errors());

//app.listen(3333);

module.exports = app;