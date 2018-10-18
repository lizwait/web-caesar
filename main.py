from flask import Flask, request
from caesar import caesar
from vigenere import vigenere

app = Flask(__name__)
app.config['DEBUG'] = True
form = """
<html>
    <head><title>Golden Girls Encrypt</title>
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
                margin: 10px 0px 10px 0px;
                width: 540px;
                height: 120px;
                border: 0;
                padding: 4px 8px;
                font-family: 'Chakra Petch', sans-serif;
                font-size: 20px;
                background-color: #FF91B4;
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
            img {{
                float: right;
            }}
            .first-choice {{
                background-color: #F0F757;
            }}
            .second-choice {{
                background-color: #48BAC4;
            }}
            h1{{
                font-family: 'Chakra Petch', sans-serif;
                text-align: center;
                color: #D34BAF;
            }}
            h2 {{
                font-family: 'Chakra Petch', sans-serif;
                text-align: center;
                color: #5BD373;

            }}

        </style>
    </head>
    <body>
      <h1>Super Secret Encryption: Golden Girls Edition</h1>
      <form action= "/" method= "POST">
        <input class= "first_choice" type="radio" id="caesar" name="encryptionType" value="caesar" />
        <label for="caesar"><strong>Caesar:</strong></label>
        <label  for="rotate">Rotation Number</label>
        <input class= "first-choice" name="rot" type= "text" id=rotate /></br>
        <input class= "second-choice" type="radio" id="vigenere" name="encryptionType" value="vigenere" />
        <label for="vigenere"><strong>Vigenere:</strong></label>
        <label for="encryptKey">Encrypt Key</label>
        <input class= "second-choice" name="key" type= "text" id="encryptKey" />
      <div>
        <textarea name="text">{0}</textarea>
      </div>
      <div>  
        <input id= "button" type= "submit" />
      </div>
      <div>
      </form>
      <h2 id= "Golden">Thank you for being a friend.</h2>
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