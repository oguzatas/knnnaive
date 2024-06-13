# correlation.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# dataset.py dosyasından veri yükleme fonksiyonunu içe aktarın
from dataset import load_data

def plot_correlation_matrix():
    # Veriyi yükleme
    df = load_data()

    # Korelasyon matrisini hesaplama
    correlation_matrix = df.corr()

    # Korelasyon matrisini görselleştirme
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')
    plt.show()

if __name__ == "__main__":
    plot_correlation_matrix()
