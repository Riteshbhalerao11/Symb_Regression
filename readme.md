# ML4SCI GSOC 2024 Evaluation Tasks

## Project Title: Transformer Models for Symbolic Calculations of Squared Amplitudes in HEP

This repository contains code and resources related to evaluation tasks for [symbolic calculation projects](https://docs.google.com/document/d/19ybdCLbxJs2mFsxni4yN9FP4ADlK4mxltF9OVSmbRXE/edit). More specifically, it contains solutions for Common tasks and Specific task 3.1.

## Trained Models

Models have been hosted as Kaggle datasets. They can be used in any one of the mentioned three ways, which are:

1. Direct Download link
2. Via Kaggle API
   ```
   kaggle datasets download username/model
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
   kaggle datasets download riteshbhalerao/bert-sym-regression
   ```
## General Information

This repository consists of the training scripts in the form of notebooks for the evaluation tasks.

- **Task_1&2_Transformers.ipynb** corresponds to Common task 1 as well as Common task 2. It consists of training scripts for Vanilla Transformer Encoder Decoder model.

- **Task_3.1_Bert2Bert.ipynb** corresponds to evaluation task 3.1 and consists of training code for the Bert2Bert model.
  
- The **Inference/** contains the notebooks for evaluating the trained models.

- **Viz/** contains some interesting attention visualization of trained bert2bert model.

## Evaluation results & findings

In both the tasks, sequence accuracies have been calculated on 10 % of the training data size with random samples which were unseen during training. 

### Common tasks 1 & 2

A variety of Transformer architectures along with parameters were experimented with. They were also trained on a variety of data sizes up to the maximum possible as per time & hardware. Following is the summarization of some of the experiments. Below accuracies are subject to slight deviations given the randomness of data.

| Data Size | Seq Acc (%) | Num Layers | Hidden Dims | Emb Size | Nhead |
|-----------|-------------|------------|-------------|----------|-------|
| 100k      | 65          | 3          | 512         | 512      | 8     |
| 200k      | 73          | 3          | 1024        | 512      | 8     |
| 400k      | 80          | 4          | 3072        | 512      | 8     |
| 600k      | 80          | 4          | 3072        | 512      | 8     |

The model with 400k data samples after running for 30 epochs performed decently & has been provided above. The trend is simple, larger data & architecture expansion will lead to better accuracies & thereby, a well-generalized model for this task.

### Specific task 3.1

## NOTE : Two lines of code were accidentally deleted (specifically related to tokenization) in Bert2Bert training scripts leading to drastic reduce in accuracy. Apologies for the same. New trained model will be updated by 11th April.

Extensive experimentation with a lot of models, parameters & configurations was done in a very short time span. During experimentation, it became evident that these models tended to overfit quickly and exhibited slow learning tendencies, indicating insufficient data for effective learning. Attempts to mitigate these issues by reducing model complexity led to pronounced underfitting and encountered saddle points during training. Regrettably, training these models on larger datasets was not feasible due to resource constraints and time limitations. The following table summarizes some of the experiments to provide an overview.

| Data Size | Seq Acc (%) | Num Layers | Model       |
|-----------|-------------|------------|-------------|
| 300k      | 13          | 6          | LED         | 
| 200k      | 8           | 6          | LongT5      | 
| 200k      | 28          | 3          | BART        | 
| 400k      | 72          | 3          | BERT2BERT   |

Out of all the models, Bert2Bert seems the most promising. All the long-context models turned out to be the worst performers. Also, maximum token length being 256 use of these models does not seem to add value. Bert2Bert, which utilizes BERT configurations for the encoder as well as decoder, achieved better performance than the rest of the LLMs.

