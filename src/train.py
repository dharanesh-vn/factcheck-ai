import pandas as pd
import numpy as np
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from preprocessing import clean_text

def load_and_prep_data():
    base_path = os.path.join(os.path.dirname(__file__), '../data')
    
    print("Loading True.csv...")
    true_df = pd.read_csv(os.path.join(base_path, 'True.csv'))
    print("Loading Fake.csv...")
    fake_df = pd.read_csv(os.path.join(base_path, 'Fake.csv'))
    
    # Add labels
    true_df['label'] = 1
    fake_df['label'] = 0
    
    # Combine
    df = pd.concat([true_df, fake_df]).reset_index(drop=True)
    
    # Shuffle
    df = df.sample(frac=1).reset_index(drop=True)
    
    print(f"Total samples: {len(df)}")
    return df

def train():
    df = load_and_prep_data()
    
    # Combine title and text for better context
    print("Pre-processing text...")
    df['total_text'] = df['title'] + " " + df['text']
    
    # For large datasets, we might take a subset if resources are limited, 
    # but let's try the full dataset first.
    # df = df.head(10000) 
    
    X = df['total_text']
    y = df['label']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Vectorizing...")
    tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
    tfidf_train = tfidf_vectorizer.fit_transform(X_train)
    tfidf_test = tfidf_vectorizer.transform(X_test)
    
    print("Training PassiveAggressiveClassifier...")
    pac = PassiveAggressiveClassifier(max_iter=50)
    pac.fit(tfidf_train, y_train)
    
    y_pred = pac.predict(tfidf_test)
    score = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {round(score*100,2)}%')
    
    # Save model and vectorizer
    model_dir = os.path.join(os.path.dirname(__file__), '../model')
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
        
    print("Saving models...")
    joblib.dump(pac, os.path.join(model_dir, 'model.pkl'))
    joblib.dump(tfidf_vectorizer, os.path.join(model_dir, 'vectorizer.pkl'))
    print("Done!")

if __name__ == "__main__":
    train()
