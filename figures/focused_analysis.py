import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parent

train_df = pd.read_csv(BASE_DIR / "train.csv")
test_df = pd.read_csv(BASE_DIR / "test.csv")

all_df = pd.concat([train_df, test_df], axis=0)
all_df["set"] = "train"
all_df.loc[all_df.Survived.isna(), "set"] = "test"

# Set style for consistent look
sns.set_style("whitegrid")

# Plot 1: Sex vs Survived
plt.figure(figsize=(8, 6))
sns.countplot(data=train_df, x="Sex", hue="Survived")
plt.title("Number of passengers / Sex")
plt.xlabel("Sex")
plt.ylabel("Count")
plt.legend(title="Survived")
plt.tight_layout()
plt.savefig(BASE_DIR / "sex_survived.png", dpi=300, bbox_inches="tight")
plt.close()

# Plot 2: Parch vs Survived
plt.figure(figsize=(8, 6))
sns.countplot(data=train_df, x="Parch", hue="Survived")
plt.title("Number of passengers / Parents or Children aboard")
plt.xlabel("Parch")
plt.ylabel("Count")
plt.legend(title="Survived")
plt.tight_layout()
plt.savefig(BASE_DIR / "parch_survived.png", dpi=300, bbox_inches="tight")
plt.close()

# Plot 3: Pclass vs Survived
plt.figure(figsize=(8, 6))
sns.countplot(data=train_df, x="Pclass", hue="Survived")
plt.title("Number of passengers / Passenger Class")
plt.xlabel("Pclass")
plt.ylabel("Count")
plt.legend(title="Survived")
plt.tight_layout()
plt.savefig(BASE_DIR / "pclass_survived.png", dpi=300, bbox_inches="tight")
plt.close()

# Plot 4: Embarked vs Survived
plt.figure(figsize=(8, 6))
sns.countplot(data=train_df, x="Embarked", hue="Survived")
plt.title("Number of passengers / Embarking port")
plt.xlabel("Embarked")
plt.ylabel("Count")
plt.legend(title="Survived")
plt.tight_layout()
plt.savefig(BASE_DIR / "embarked_survived.png", dpi=300, bbox_inches="tight")
plt.close()

# Plot 5: SibSp vs Survived
plt.figure(figsize=(8, 6))
sns.countplot(data=train_df, x="SibSp", hue="Survived")
plt.title("Number of passengers / Siblings or Spouse")
plt.xlabel("SibSp")
plt.ylabel("Count")
plt.legend(title="Survived")
plt.tight_layout()
plt.savefig(BASE_DIR / "sibsp_survived.png", dpi=300, bbox_inches="tight")
plt.close()

# Plot 6: Age distribution grouped by Survived
plt.figure(figsize=(10, 6))
sns.histplot(data=train_df, x="Age", hue="Survived", bins=30, kde=False)
plt.title("Number of passengers / Age (grouped by survival)")
plt.xlabel("Age")
plt.ylabel("Count")
plt.legend(title="Survived")
plt.tight_layout()
plt.savefig(BASE_DIR / "age_survived.png", dpi=300, bbox_inches="tight")
plt.close()

print("All plots saved as PNG files in the figures/ directory!")
