from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/")
def render_response():
    firstname = request.args['first name'] #get user's input for color input
    lastname = request.args['last name'] #get user's input for color input
    favoritecolor = request.args['color'] #get user's input for color input
    return render_template('response.html', responseFromServer = response)
    
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
