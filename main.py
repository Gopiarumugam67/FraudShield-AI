from src.data.data_loader import DataLoader
from src.data.splitter import DatasetSplitter

loader = DataLoader()

df = loader.load_dataset()

splitter = DatasetSplitter(df)

splits = splitter.split_dataset()

print(splits["X_train"].shape)

print(splits["X_validation"].shape)

print(splits["X_test"].shape)