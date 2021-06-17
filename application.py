
import os
import io
from flask import Flask,request,jsonify,render_template
from seeme import Client
# from fastai.vision import 

UPLOAD_FOLDER = './image'
app = Flask(__name__, static_url_path='/static')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def render_page():
    return render_template('cat-breed-detector.html')

 

@app.route('/sign',methods=['POST'])
def upload_apple():
    """
    retrieve the image uploaded and make sure it is an image file
    """
    file = request.files['file']
    image_extensions=['jpg', 'jpeg', 'png', 'JPG']
    
    if file.filename.split('.')[1] not in image_extensions:
        return jsonify('Please upload an appropriate image file')




    path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(path)
 
    client = Client()
    my_password =  "qwer1234"
    my_username =  "itsmesaira"

    client.login(my_username, my_password);



    result = client.inference("eccce51a-06d1-46d8-81f3-670008c2a997", path)
    pred = result["prediction"]
    res = result["confidence"]

  
    return jsonify({'sign': pred, 'score': res})  

if __name__ == '__main__':
    app.run(debug=False,port=os.getenv('PORT',5000))










    
    



