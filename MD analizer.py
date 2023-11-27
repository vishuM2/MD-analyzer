import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def medical_data_visualizer(file_path):
    # Load the data into a Pandas DataFrame
    df = pd.read_csv(file_path)

    # Display the first few rows of the DataFrame
    print("Sample of the data:")
    print(df.head())

    # Basic statistics
    print("\nBasic statistics:")
    print(df.describe())

    # Age distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df['age'], bins=20, kde=True)
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()

    # BMI distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df['bmi'], bins=20, kde=True)
    plt.title('BMI Distribution')
    plt.xlabel('BMI')
    plt.ylabel('Frequency')
    plt.show()

    # Blood pressure distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df['blood_pressure'], bins=20, kde=True)
    plt.title('Blood Pressure Distribution')
    plt.xlabel('Blood Pressure')
    plt.ylabel('Frequency')
    plt.show()

    # Correlation matrix
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=.5)
    plt.title('Correlation Matrix')
    plt.show()

if __name__ == "__main__":
    # Provide the path to your medical data CSV file
    file_path = "path/to/your/medical_data.csv"
    medical_data_visualizer(file_path)
