import pickle
import pandas as pd
import numpy as np

class Geofusion(object):
    def feature_engineering(self, df_1):
        # create percent_pop_ate9
        df_1['percent_pop_ate9'] = df_1['pop_ate9'] / df_1['populacao']
        
        # create percent_pop_de10a14
        df_1['percent_pop_de10a14'] = df_1['pop_de10a14'] / df_1['populacao']
        
        # create percent_pop_maisde60
        df_1['percent_pop_mais_de60'] = df_1['pop_mais_de60'] / df_1['populacao']
        
        # create percent_ab
        df_1['percent_ab'] = (df_1['domicilios_a1'] + df_1['domicilios_a2'] +
                              df_1['domicilios_b1'] + df_1['domicilios_b2']) / df_1['total_domicilios']
        
        # create densidade_bairro
        df_1['densidade_bairro'] = df_1['populacao'] / df_1['area']
        
        df_1 = df_1.drop(['pop_ate9', 'pop_de10a14', 'domicilios_a1', 'domicilios_a2',
                         'domicilios_b1', 'domicilios_b2', 'pop_mais_de60', 'area'], axis=1)
        return df_1
        
    
    def get_prediction(self, model, df_2):
        # prediction
        pred = model.predict(df_2)
        
        # aclopando as predicoes
        df_2['prediction'] = np.expm1(pred)
    
        return df_2.to_json(date_format='iso')
