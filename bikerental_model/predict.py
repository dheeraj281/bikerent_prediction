# load the pipeline, get a dataframe, validate, run the prediction.
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Union
from bikerental_model.config.core import config
from bikerental_model.processing.data_manager import load_pipeline
from bikerental_model.processing.validation import validate_inputs
from bikerental_model import __version__ as _version

pipeline_file_name = f"{config.app_config_.pipeline_save_file}{_version}.pkl"
bikerental_pipe = load_pipeline(file_name = pipeline_file_name)

def make_prediction(*, input_data: Union[pd.DataFrame, dict]) -> dict:
    """Make a prediction using a saved model """
    validated_data, errors = validate_inputs(input_df = pd.DataFrame(input_data))   
    # validated_data = validated_data[config.model_config_.features]
    validated_data = validated_data.reindex(columns = config.model_config_.features)  
    results = {"predictions": None, "version": _version, "errors": errors}    
    if not errors:
        predictions = bikerental_pipe.predict(validated_data)
        results = {"predictions": np.floor(predictions), "version": _version, "errors": errors}
    return results

if __name__ == "__main__":

    data_in = {'dteday': ['2012-11-6'], 'season': ['winter'], 'hr': ['6pm'], 'holiday': ['No'], 'weekday': ['Tue'],
               'workingday': ['Yes'], 'weathersit': ['Clear'], 'temp': [16], 'atemp': [17.5], 'hum': [30], 'windspeed': [10]}

    print(make_prediction(input_data = data_in))