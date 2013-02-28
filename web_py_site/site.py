import web
import models

web.config.debug = True

render = web.template.render('/Users/shankar.narayan/Dropbox/fourthmain/projects/website/web_py_site/templates/',base='newbase')

urls = (
		'/','index',
		'/contact','contact',
		'/blog','blog',
		'/blog/(\d+)','blogView',
		'/gallery','gallery',
		'/gallery/(\d+)','galleryView',
		'/admin','admin' #A create update and delete mechanism with passwords for two people.
		)
		
class index:
	def GET(self):
		galleryItem = models.get('items')
		return render.index(galleryItem)
		
		
class blog:
	def GET(self):
		blogItem = models.get('posts')
		return render.blog(blogItem)
		
class blogView:
	def GET(self,id):
		post = models.gets('posts',int(id))
		return render.blogview(post)
		

class gallery:
	def GET(self):
		galleryItems = models.get('items')
		return render.gallery(galleryItems)
		
class galleryView:
	def GET(self,id):
		galleryItem = models.gets('items',int(id))
		return render.galleryview(galleryItem)
		
class contact:
	def GET(self):
		return render.contact()
		
class admin:
	def GET(self):
		#send form with password. confirm password by checking it against the database. create a session where the user can create,update or delete 
		#content, which either writes to db
		return render.admin()
		
		
	def POST(self):	
		id = web.input()
		authenticate = models.authenticate(id)
		if authenticate == True:
			web.seeother('/admin/editable')
		else:
			web.seeother('/admin')
			
	
		
		
app = web.application(urls,globals())

if __name__=='__main__':app.run()
