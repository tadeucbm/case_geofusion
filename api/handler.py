import pickle
import pandas as pd
from flask import Flask, request, Response
from geo.Geo import Geofusion

# loading model
model = pickle.load(open('/home/tcbm/projs/case_geofusion/model/model_faturamento.pkl', 'rb'))

app = Flask(__name__)

@app.route('/geo/predict', methods=['POST'])
def geo_predict():
    test_json = request.get_json()
    
    if test_json: # tem dados
        if isinstance(test_json, dict): # unico exemplo
            test_raw = pd.DataFrame(test_json, index=[0])
        else: # multiplos exemplos
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())
            
        # instanciando a calsse Geofusion
        pipeline = Geofusion()
        
        # feature engineering
        df1 = pipeline.feature_engineering(test_raw)
        
        # get_prediction
        df2 = pipeline.get_prediction(model, df1)
        
        return df2
        
    else:
        return Response('{}', status=200, mimetype='application/json')
    
if __name__ == '__main__':
    app.run('0.0.0.0')
