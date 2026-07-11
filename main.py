from src.data.data_loader import DataLoader
from src.data.statistics import DatasetStatistics
from src.data.splitter import DatasetSplitter
from src.data.versioning import DatasetVersioning


def main():

    # Load Dataset
    loader = DataLoader()
    df = loader.load_dataset()

    # Dataset Statistics
    stats = DatasetStatistics(df)
    report = stats.generate_report()

    print("\n========== DATASET REPORT ==========")
    print(report)

    # Dataset Split
    splitter = DatasetSplitter(df)
    splits = splitter.split_dataset()

    print("\n========== DATASET SPLIT ==========")
    print("Train:", splits["X_train"].shape)
    print("Validation:", splits["X_validation"].shape)
    print("Test:", splits["X_test"].shape)

    # Dataset Version
    version = DatasetVersioning(df)
    metadata = version.generate_version()

    print("\n========== DATASET VERSION ==========")
    print(metadata)


if __name__ == "__main__":
    main()