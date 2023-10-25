from pytube import YouTube
from flask import render_template
from flask import request,redirect
from flask import session
from flask import Flask

app = Flask(__name__)
app.secret_key = 'youtube'




# URL - descargar Video Youtube
@app.route('/downloadVideo',methods=['GET','POST'])
def downloadVideo():   
    print("ente")
    if request.method == 'GET':
        return render_template("descargarYoutube.html")
    

# URL - test camara Celular
@app.route('/nuevoDriver',methods=['GET','POST'])
def nuevoDriver():   
    if request.method == 'GET':
        return render_template("nuevoEmpleado.html")
    


def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


#link = input("Enter the YouTube video URL: ")
#Download(link)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")