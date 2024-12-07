# -*- coding: utf-8 -*-
"""Gorev10_Emre Ozgen.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15Wte041BWKYbSfjMER_UqI77LYGGOhwb

#Görev-10:
iris veri seti ile;

lojistik regresyon algoritması ile sınıflandırma modeli geliştiriniz ve modelin başarısını değerlendiriniz.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.preprocessing import StandardScaler




iris = load_iris() # scikit-learn kütüphanesinden direkt alıyoruz
df = pd.DataFrame(iris.data)
df.columns = iris.feature_names # Veri setindeki bilgileri kullanarak sütun isimlendirme
# sepal (çanak yaprak) ve petal (taç yaprak) ve çiçeklerin uzunluk ve genişlikleri
df.columns=['Çanak Yaprak Uzunluğu (cm)', 'Çanak Yaprak Genişliği (cm)','Taç Yaprak Uzunluğu (cm)','Taç Yaprak Genişliği (cm)']

df.info()

# Hedef değişkeninin yüklenmesi
df['Tür'] = iris.target

# Tür kolunundaki numaralara, tür isimlerini verme
df['Tür'] = df['Tür'].replace({0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'})
df.head(80)

# Veri incelemesi
print(df.info())  # Veri türlerini kontrol et
print(df.describe().T)  # Temel istatistikler
print(df['Tür'].value_counts())  # Türlerin dağılımını kontrol et

# Veri kümesini görselleştirme (her bir özelliğe göre dağılımı ve sınıflar arasındaki ilişkileri gösterme)

sns.pairplot(df,hue='Tür', diag_kind='kde')
plt.show()

# Türlere göre taç yaprak uzunluk ve genişliğin görselleştirilmesi
sns.scatterplot(x=df['Taç Yaprak Uzunluğu (cm)'], y=df['Taç Yaprak Genişliği (cm)'], hue=df['Tür'], palette='Set1')
plt.title('Taç Yaprak Özellikleri ile Türler Arasındaki İlişki')
plt.show()

# Yukarının çanak yaprak hali (Pek anlamlı görünmüyor burası)
sns.scatterplot(x=df['Çanak Yaprak Uzunluğu (cm)'], y=df['Çanak Yaprak Genişliği (cm)'], hue=df['Tür'], palette='Set1')
plt.title('Taç Yaprak Özellikleri ile Türler Arasındaki İlişki')
plt.show()

# Veri Setini Eğitim ve Test Olarak (Bağımsız ve bağımlı değişkenleri) ayırma

# Bağımsız değişkenler (X)
X = df.drop('Tür', axis=1)

# Bağımlı değişken (y)
y = df['Tür']

# Eğitim ve test setlerine ayırma (%70 eğitim, %30 test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standartlaştırma
scaler = StandardScaler()
scaled_X_train = scaler.fit_transform(X_train)
scaled_X_test = scaler.transform(X_test)

# Lojistik Regresyon Modelini Eğitme
# Modeli oluştur ve eğit
log_model = LogisticRegression()  # Maksimum iterasyon artırılarak modelin daha iyi öğrenmesi sağlanır
log_model.fit(scaled_X_train, y_train)  # Modeli eğit

# Test seti üzerinde tahmin yap
y_pred = log_model.predict(scaled_X_test)

accuracy_score(y_test, y_pred)

confusion_matrix(y_test, y_pred)

# Model Performansını Değerlendirme
# Başarı metrikleri
print("Doğruluk Oranı (Accuracy):", accuracy_score(y_test, y_pred))  # Doğruluk oranını hesapla
print("\nSınıflandırma Raporu:\n", classification_report(y_test, y_pred))  # Precision, Recall, F1-Score

# Karmaşıklık Matrisi ile Değerlendirme
# Karmaşıklık matrisi
cm = confusion_matrix(y_test, y_pred)  # Karmaşıklık matrisini oluştur
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=iris.target_names)  # Matrisi görselleştir
disp.plot()
plt.show()

print(classification_report(y_test, y_pred))

single_sample = X_test.iloc[5]
single_sample

# Modelin Tahminleri ile Görselleştirme
# Gerçek değerler ve tahminlerin karşılaştırılması
plt.figure(figsize=(8, 6))
sns.scatterplot(x=X_test['Taç Yaprak Uzunluğu (cm)'],
                y=X_test['Taç Yaprak Genişliği (cm)'],
                hue=y_pred,
                style=y_test,
                palette='deep')
plt.title("Lojistik Regresyon Tahminleri ve Gerçek Değerler")
plt.xlabel("Taç Yaprak Uzunluğu (cm)")
plt.ylabel("Taç Yaprak Genişliği (cm)")
plt.legend(title="Tahminler")
plt.show()