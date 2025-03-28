import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score

from bikerental_model.config.core import config
from bikerental_model.pipeline import bikerental_pipe
from bikerental_model.processing.data_manager import load_dataset, save_pipeline

def run_training() -> None:
    
    """
    Train the model.
    """

    # read training data
    data = load_dataset(file_name=config.app_config_.training_data_file)

    features = config.model_config_.features

    print("data length",len(data))
    # divide train and test
    X_train, X_test, y_train, y_test = train_test_split(
        data[features],  # predictors
        data[config.model_config_.target],
        test_size=config.model_config_.test_size,
        
        random_state=config.model_config_.random_state,
    )
    print("X_train shape",X_train.shape)
    print("X_test shape",X_test.shape)      
    print("y_train shape",y_train.shape)
    print("y_test shape",y_test.shape)
    # Pipeline fitting
    bikerental_pipe.fit(X_train,y_train)
    print("Pipeline fitting done")
    print("---------------`-------`--------------------prediction starts---------------`-------`--------------------")
    save_pipeline(pipeline_to_persist= bikerental_pipe)


    y_pred = bikerental_pipe.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Mean Squared Error: {mse}")
    print(f"R-squared: {r2}")
    
if __name__ == "__main__":
    run_training()
