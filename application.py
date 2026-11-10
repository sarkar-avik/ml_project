from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import sys
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
from src.exception import CustomException

application = Flask(__name__)
app = application

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    try:
        if request.method == 'GET':
            return render_template('home.html')
        else:
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('race_ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                writing_score=float(request.form.get('writing_score')),
                reading_score=float(request.form.get('reading_score'))
            )

            pred_df = data.get_data_as_dataframe()
            print(pred_df)
            
            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)
            
            # Limit prediction to 100 and format to 2 decimal places
            results = f"{min(float(results[0]), 100):.2f}"

            return render_template('home.html', results=results)
    
    except Exception as e:
        raise CustomException(e, sys)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
        