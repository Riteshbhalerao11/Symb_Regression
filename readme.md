# ML4SCI GSOC 2024 Evaluation Tasks

## Project Title: Transformer Models for Symbolic Calculations of Squared Amplitudes in HEP

This repository contains code and resources related to evaluation tasks for [symbolic calculation projects](https://docs.google.com/document/d/19ybdCLbxJs2mFsxni4yN9FP4ADlK4mxltF9OVSmbRXE/edit). More specifically, it contains solutions for Common tasks and Specific task 3.1.

## Trained Models

Models have been hosted as Kaggle datasets. They can be used in any one of the mentioned three ways, which are:

1. Direct Download link
2. Via Kaggle API
   ```
   kaggle datasets download -p /path/to/model
   ```
3. Using the `opendatasets` Python library
   ```python
   import opendatasets as od
   od.download('Dataset.link')
   ```

Following are the links for the trained models:

### 1. Transformer EncoderDecoder
- [Link](https://www.kaggle.com/datasets/riteshbhalerao/transformer-sym-regression/data)
- [Direct download link](https://www.kaggle.com/datasets/riteshbhalerao/transformer-sym-regression/download?datasetVersionNumber=1)
- ```
  kaggle datasets download riteshbhalerao/transformer-sym-regression
  ```

### 2. Bert2Bert (BertGeneration)
- [Link](https://www.kaggle.com/datasets/riteshbhalerao/bert-sym-regression)
- [Direct Download link](https://www.kaggle.com/datasets/riteshbhalerao/bert-sym-regression/download?datasetVersionNumber=1)
- ```
   kaggle datasets download -p /path/to/model
   ```
