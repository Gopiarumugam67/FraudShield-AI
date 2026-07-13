from setuptools import find_packages, setup

setup(
    name="fraudshield_ai",
    version="1.0.0",
    description="Enterprise Credit Card Fraud Detection Platform",
    author="Gopinath A",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "fastapi",
        "uvicorn",
        "streamlit",
        "plotly",
        "shap",
        "joblib",
        "python-dotenv",
    ],
    python_requires=">=3.10",
)