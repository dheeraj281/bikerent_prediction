import numpy as np
import pandas as pd
from pydantic import BaseModel, ValidationError
from typing import List, Optional, Tuple
from bikerental_model.config.core import config
from bikerental_model.processing.data_manager import pre_pipeline_preparation


def validate_inputs(*, input_df: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[dict]]:
    """Check model inputs for unprocessable values."""

    pre_processed = pre_pipeline_preparation(data_frame=input_df)
    validated_data = pre_processed[config.model_config_.features].copy()
    errors = None

    try:
        # replace numpy nans so that pydantic can validate
        MultipleDataInputs(
            inputs=validated_data.replace({np.nan: None}).to_dict(orient="records")
        )
    except ValidationError as error:
        errors = error.json()

    return validated_data, errors


class DataInputSchema(BaseModel):
    month: Optional[int]
    year: Optional[int]
    season: Optional[int]
    hr: Optional[int]
    holiday: Optional[int]
    weekday: Optional[int]
    workingday: Optional[int]
    weathersit: Optional[int]
    temp: Optional[float]
    atemp: Optional[float]
    hum: Optional[float]
    windspeed: Optional[float]
    casual: Optional[int]
    registered: Optional[int]
    cnt: Optional[int]


class MultipleDataInputs(BaseModel):
    inputs: List[DataInputSchema]

# dteday,season,hr,holiday,weekday,workingday,weathersit,temp,atemp,hum,windspeed,casual,registered,cnt
