# Gerekli kütüphaneleri yükleyin
import pandas as pd
import matplotlib.pyplot as plt

# dataset.py dosyasından veri yükleme fonksiyonunu içe aktarın
from dataset import load_data

# Veriyi yükleme
df = load_data()

# Temel istatistikler
summary = df.describe(include='all')

# Depresyon durumuna göre veriyi gruplayarak ortalama değerler
grouped = df.groupby('Depression State').mean()

# Sonuçları görüntüleme
print(summary)
print(grouped)

# Ortalama değerleri bar grafiği olarak görselleştirme
grouped.plot(kind='bar', figsize=(14, 8))
plt.title('Average Scores for Each Symptom Across Different Depression States')
plt.ylabel('Average Score')
plt.xlabel('Depression State')
plt.legend(loc='upper right')
plt.show()

# Scatter plot: Fatigue ve Hopelessness arasındaki ilişki
plt.figure(figsize=(10, 6))
plt.scatter(df['Fatigue'], df['Hopelessness'], c='blue', alpha=0.5)
plt.title('Scatter Plot of Fatigue vs Hopelessness')
plt.xlabel('Fatigue')
plt.ylabel('Hopelessness')
plt.show()

# Box plot: Depresyon durumlarına göre Fatigue dağılımı
plt.figure(figsize=(12, 6))
df.boxplot(column='Fatigue', by='Depression State', grid=False)
plt.title('Box Plot of Fatigue by Depression State')
plt.suptitle('')
plt.xlabel('Depression State')
plt.ylabel('Fatigue')
plt.show()
