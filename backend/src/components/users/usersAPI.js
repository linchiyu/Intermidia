const connection = require('../../database/connection');
const bcrypt = require('bcryptjs');
const { generateDateString } = require('../utils/utils');
const jwt = require('jsonwebtoken')

module.exports = {
	async index(request, response) {
		const { email, password } = request.body;

		const user = await connection('user').where({ email: email }).first();

		if (!user){
			return response.status(400).send({ error: "User not found."});
		}

		if (!bcrypt.compareSync(password, user.password)) {
			return response.status(404).send({ error: "Incorrect password."});
		}

		await connection('user').where({ id: user.id }).first().update({last_login: generateDateString() });

		user.password = undefined;

		const token = await jwt.sign({ id: user.id }, "153158614secret", { expiresIn: 86400 });

		return response.status(200).json({user, token});
	},

	async create(request, response) {
		const { first_name, last_name, email, password } = request.body;

		const user = await connection('user').where({ email: email }).first();

		if (user){
			return response.status(400).send({ error: "User already exists."})
		}

		const salt = await bcrypt.genSaltSync(10);
		const hash = await bcrypt.hashSync(password, salt);

		await connection('user').insert({
			first_name,
			last_name,
			email,
			password: hash,
		});

		return response.json({ email });
	}
}