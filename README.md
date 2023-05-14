# NLP_Sentiment_UC3M - Sentiment Analysis Task - Rest-MEX

https://sites.google.com/cicese.edu.mx/rest-mex-2022/tracks/sentiment-analysis-task

The subtask is a classification task where the participating system can predict the polarity of an opinion issued by a tourist who traveled to the most representative places, restaurants and hotels in Mexico. This collection was obtained from the tourists who shared their opinion on TripAdvisor between 2002 and 2021. Each opinion's class is an integer between [1, 5], where 1 represents the most negative polarity and 5 the most positive. Also, each opinion has the type label.

## Authors
- Mario Pérez Enriquéz
- Javier Alonso Mencía
- Isabel Segura-Bedmar

## Paper
https://ceur-ws.org/Vol-3202/restmex-paper11.pdf

## To install
1. Python version 3.9.*
2. pip install -r requirements.txt

## Project structure
1. DATA -> data from the competition
2. PREPROCESS_DATA -> analyze and process data
3. Data_Augmentation_Summarization -> applying Data Augmentation to create new data instances
4. SVM -> aproach using SVM to solve the task  
5. RobertaEsp -> aproach using transformers based on RobertaESP model to solve the task  
6. GPT2 -> aproach using transformers based on GPT2 model to solve the task  
7. Final_Inference -> Apply best models to Test Dataset and submit competition results

## Hardware
- RTX 3060 12GB
- 32GB RAM
- i7 6700K

## Metrics
- precision
- recall
- f1
