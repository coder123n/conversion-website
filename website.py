from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    firstname = request.args['firstname'] #get user's input for color input
    lastname = request.args['lastname'] #get user's input for color input
    favoritecolor = request.args['favoritecolor'] #get user's input for color input
    response = "Hello my name is 'firstname' 'lastname' and my favorite color is 'favoritecolor'."
    return render_template('response.html', responseFromServer = response)
    
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
