import web,datetime,hashlib

db = web.database(dbn='sqlite',db='main.db')
authdb = web.database(dbn='sqlite',db='users.db')

def get(tableName):
	try:
		return db.select(tableName,order='id DESC')
	except IndexError:
		return none

def gets(tableName,id):
	try:
		return db.select(tableName,where='id=$id',vars=locals())[0]
	except IndexError:
		return none

def newBlog(tableName,title,content):
	db.insert(tableName,title=title,content=content)
	
def newGallery(tableName,content):
	db.insert(tableName,content=content)
	
def delete(tableName,id):
	db.delete(tableName,where='id=$id',vars=locals())



def authenticate(id): #whatever comes from the post request
	pwdhash = hashlib.md5(id.password).hexdigest()
	check = authdb.execute('select * from users where password=?',(pwdhash))
	if check:
		session.loggedin = True
		return True
	else:
		return False
		
