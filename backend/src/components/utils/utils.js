module.exports = {
	generateDateString(){
		return new Date().toISOString().substr(0, 19).replace('T', ' ');
	}
}
