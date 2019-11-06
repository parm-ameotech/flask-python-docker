
@app.route("/")
def index():
	# user = User(password='password@123')
	# db.session.add(user)
	# db.session.commit
	user = User.query.filter_by(password='password@123')
	data ={
		'name':'Customer Site', 'user':user.count()
	}
	return render_template("index.html", data=data)
