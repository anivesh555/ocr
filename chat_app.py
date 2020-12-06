
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
  return render_template('index.html')

from flask_dropzone import Dropzone
...
dropzone = Dropzone(app)
...
# Dropzone settings
app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*'
app.config['DROPZONE_REDIRECT_VIEW'] = 'results'


from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import os

...
# Uploads settings
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/uploads'
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB

from flask import Flask, render_template
from flask_dropzone import Dropzone
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import os
app = Flask(__name__)
dropzone = Dropzone(app)
# Dropzone settings
app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*'
app.config['DROPZONE_REDIRECT_VIEW'] = 'results'
# Uploads settings
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/uploads'
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB
@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/results')
def results():
    return render_template('results.html')
from flask import Flask, render_template, request
...
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file_obj = request.files
        for f in file_obj:
            file = request.files.get(f)
            print (file.filename)
        return "uploading..."
    return render_template('index.html')



















































# from flask import Flask ,jsonify ,request
# from flask_socketio import SocketIO 
# import os
# from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename



# app=Flask(__name__)
# app.config['SECRET_KEY'] ='bhadawar'

# socketio =SocketIO(app)


# @app.route('/')

# def index():
# 	return app.send_static_file('index.html')

# @socketio.on('msg')
# def handle_msg(data):
# 	socketio.emit('push',data,broadcast=True ,include_self=False)


# UPLOAD_FOLDER = '/home/same/Python/app/uploads'
# ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# @app.route('/')

# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         # if user does not select file, browser also
#         # submit a empty part without filename
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
# 	# print(data)



# if __name__ =="__main__":
# 	app.run()


# from flask import Flask , jsonify ,request


# app =Flask(__name__)






# # @app.route('/neon')

# # def hello():
# # 	return 'jay mata di'

# # def neon():
# # 	return 'new one function jusrt ti ensure the requriesnt or home page whtrarfver'


# # if __name__ == "__main__":
# # 	app.run()



# #Creat our own api

# # app=(__name__)

# # app.route('//')

# users=[
# {'id':3,'name':"anives",'age':23},
# {'id':33,'name':"aniveshsds",'age':22},
# {'id':23,'name':"a34nives",'age':24}
# ]
# @app.route('/')

# def index():
# 	return app.send_static_file('index.html')




# @app.route('/getusers')
# def getusers():
# 	return jsonify(users)


# @app.route('/user/<id>')   #we get str as a input 

# def user(id):
# 	#list comprehension 
# 	#result= [u for u in users if u['id']==id]
# 	#return jsonify(result)
# 	#lembda
# 	result=list(filter(lambda u:str(u['id'])==id,users))
# 	return jsonify(result)

# if __name__ == "__main__":
# 	app.run()
