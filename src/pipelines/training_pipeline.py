"""
Training Pipeline for FraudShield AI.
"""

from __future__ import annotations

from app.core.logger import logger

from src.data.data_loader import DataLoader
from src.data.splitter import DatasetSplitter

from src.feature_engineering.preprocessing_pipeline import (
    PreprocessingPipeline,
)

from src.training.model_factory import ModelFactory
from src.training.trainer import ModelTrainer
from src.training.hyperparameter_tuner import HyperparameterTuner
from src.training.parameter_grid import PARAMETER_GRIDS

from src.evaluation.evaluator import ModelEvaluator

from src.models.model_saver import ModelSaver


class TrainingPipeline:
    """
    End-to-end training pipeline.
    """

    def run(self):

        logger.info("Starting Training Pipeline...")

        # ==========================
        # Load Dataset
        # ==========================

        loader = DataLoader()
        df = loader.load_dataset()
        # Development Mode
        df = df.sample(
        n=50000,
        random_state=42,
        )

        # ==========================
        # Preprocessing
        # ==========================

        preprocessing = PreprocessingPipeline()
        processed_df = preprocessing.process(df)

        # ==========================
        # Split Dataset
        # ==========================

        splitter = DatasetSplitter(processed_df)
        splits = splitter.split_dataset()

        # ==========================
        # Create Model
        # ==========================


        model_name = "random_forest"

        factory = ModelFactory()

        model = factory.get_model(
        model_name,
        n_estimators=50,
        random_state=42,
        n_jobs=-1,
        )

        # ==========================
        # Train Model
        # ==========================

        trainer = ModelTrainer(model)

        trained = trainer.train(
            splits["X_train"],
            splits["y_train"],
        )

        # ==========================
        # Baseline Evaluation
        # ==========================

        evaluator = ModelEvaluator(
            trained["model"]
        )

        baseline_results = evaluator.evaluate(
            splits["X_test"],
            splits["y_test"],
        )

        # ==========================
        # Hyperparameter Tuning
        # ==========================

        params = PARAMETER_GRIDS[model_name]

        tuner = HyperparameterTuner(
            trained["model"],
            params,
        )

        tuned = tuner.optimize(
            splits["X_train"],
            splits["y_train"],
        )

        # ==========================
        # Tuned Evaluation
        # ==========================

        tuned_evaluator = ModelEvaluator(
            tuned["best_model"]
        )

        tuned_results = tuned_evaluator.evaluate(
            splits["X_test"],
            splits["y_test"],
        )

        # ==========================
        # Save Best Model
        # ==========================

        saver = ModelSaver()

        saved_model = saver.save(
            tuned["best_model"],
            "models/artifacts/random_forest.pkl",
        )

        # ==========================
        # Results
        # ==========================

        logger.info("=" * 60)
        logger.info("Baseline Model")
        logger.info("=" * 60)

        logger.info(
            f"Accuracy : {baseline_results['accuracy']:.4f}"
        )

        logger.info(
            f"Precision: {baseline_results['precision']:.4f}"
        )

        logger.info(
            f"Recall   : {baseline_results['recall']:.4f}"
        )

        logger.info(
            f"F1 Score : {baseline_results['f1_score']:.4f}"
        )

        logger.info("=" * 60)
        logger.info("Tuned Model")
        logger.info("=" * 60)

        logger.info(
            f"Accuracy : {tuned_results['accuracy']:.4f}"
        )

        logger.info(
            f"Precision: {tuned_results['precision']:.4f}"
        )

        logger.info(
            f"Recall   : {tuned_results['recall']:.4f}"
        )

        logger.info(
            f"F1 Score : {tuned_results['f1_score']:.4f}"
        )

        logger.info("=" * 60)

        logger.info(
            f"Best Parameters : {tuned['best_parameters']}"
        )

        logger.info(
            f"Best CV Score : {tuned['best_score']:.4f}"
        )

        logger.info(
            f"Saved Model : {saved_model}"
        )

        logger.info("=" * 60)

        return {
            "model": tuned["best_model"],
            "metrics": tuned_results,
            "best_parameters": tuned["best_parameters"],
            "model_path": saved_model,
        }