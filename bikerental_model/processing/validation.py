import numpy as np
import pandas as pd
from typing import List, Optional, Tuple
from pydantic import BaseModel, ValidationError
from bikerental_model.config.core import config
from bikerental_model.processing.data_manager import pre_pipeline_preparation


def validate_inputs(*, input_df: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[dict]]:
    """Check model inputs for unprocessable values."""
    pre_processed = pre_pipeline_preparation(data_frame=input_df)
    validated_data = pre_processed[config.model_config_.features].copy()
    errors = None
    validated_data["dteday"] = validated_data["dteday"].astype(str)
    try:
        # replace numpy nans so that pydantic can validate
        MultipleDataInputs(
            inputs=validated_data.replace({np.nan: None}).to_dict(orient="records")
        )
    except ValidationError as error:
        errors = error.json()
    return validated_data, errors


class DataInputSchema(BaseModel):
    dteday: Optional[str]
    season: Optional[str]
    hr: Optional[str]
    holiday: Optional[str]
    weekday: Optional[str]
    workingday: Optional[str]
    weathersit: Optional[str]
    temp: Optional[float]
    atemp: Optional[float]
    hum: Optional[float]
    windspeed: Optional[float]
    year: Optional[int]
    month: Optional[int]

input_data = [{
    "season": "winter",
    "dteday":"2012-11-05",
    "hr": "6am",
    "holiday": "No",
    "weekday": "Sun",
    "workingday": "Yes",
    "weathersit": "Mist",
    "temp": 6.10,
    "atemp": 3.0014,
    "hum": 49.0,
    "windspeed": 19.0012,
    "casual": 4,
    "registered": 135,
    "year": 2012,
    "month": 11
}]
class MultipleDataInputs(BaseModel):
    inputs: List[DataInputSchema]


# dteday,season,hr,holiday,weekday,workingday,weathersit,temp,atemp,hum,windspeed,casual,registered,cnt
