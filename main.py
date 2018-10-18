from flask import Flask, request
from caesar import caesar
from vigenere import vigenere

app = Flask(__name__)
app.config['DEBUG'] = True
form = """
<html>
    <head>
    <link href="https://fonts.googleapis.com/css?family=Chakra+Petch:400,700" rel="stylesheet">
        <style>
            form {{
                background-color: #9799CA;
                padding: 20ps;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 0;
                width: 540px;
                height: 120px;
                border: 0;
                padding: 4px 8px;
                font-family: 'Chakra Petch', sans-serif;
                font-size: 20px;
            }}
            body {{
                background-color: #9799CA;
            }}
            #button {{
                background-color: #7BCDBA;
                padding: 10px;
                border: 0;
                font-family: 'Chakra Petch', sans-serif;
                font-size: 15px;
            }}
            input, label, textarea{{
                font-family: 'Chakra Petch', sans-serif;
            }}
        </style>
    </head>
    <body>
      <form action= "/" method= "POST">
        <input type="radio" id="caesar" name="encryptionType" value="caesar" />
        <label for="caesar">Caesar</label>
        <label for="rotate">Rotate by:</label>
        <input name="rot" type= "text" id=rotate /></br>
        <input type="radio" id="vigenere" name="encryptionType" value="vigenere" />
        <label for="vigenere">Vigenere</label>
        <label for="encryptKey">Encrypt key:</label>
        <input name="key" type= "text" id="encryptKey" />
      <div>
        <textarea name="text">{0}</textarea>
      </div>
      <div>  
        <input id= "button" type= "submit" />
      </div>
      </form>
    </body>
</html>        
"""

@app.route("/", methods=["POST"])
def caesar_or_vigenere():

    if request.form['encryptionType'] == "caesar":
        rot= int(request.form['rot'])
        text= request.form['text']
    
        return form.format(caesar(text, rot))
    else: 
        text= request.form['text']
        key= request.form['key']

        return form.format(vigenere(text, key))

@app.route("/")
def index():
    return form.format('')

app.run()