"""Takes a csv file, reads it, and creates graphs"""

import pandas as pd
import matplotlib.pyplot as plt


def load_and_preprocess(csv):
    """loads the data"""
    general_df = pd.read_csv(csv)
    return general_df


"""Summary Statistics"""


def get_summary_stats(general_df, col):
    """function that calls for the summary statistics for the variable age_years"""
    desc_stats = general_df[col].describe()
    return desc_stats


"""Building Visualization"""


def hist_cong_age(general_df, col):
    """builds a histogram for the ages of all Congressmembers"""

    plt.hist(general_df[col], bins=20, edgecolor="black")
    plt.title("Distribution of Ages in Congress", fontsize=16)
    plt.xlabel("Age", fontsize=14)
    plt.ylabel("Frequency", fontsize=14)
    plt.savefig("output/congressional_age.png")
    # plt.show()

def age_dist_50(general_df, desc_stats):
    """builds a bar graph that demonstrates distribution of age cross chambers"""
    # Convert 'start_date' column to datetime format
    general_df["start_date"] = pd.to_datetime(general_df["start_date"])

    # Bin the ages into 5-year intervals
    general_df["age_group"] = pd.cut(
        general_df["age_years"], bins=range(20, 101, 5), right=False
    )

    # Group by chamber and age group to get frequency counts
    chamber_age_group_counts = (
        general_df.groupby(["chamber", "age_group"], observed=False).size().unstack(fill_value=0)
    )
# .size().unstack(fill_value=0)
    # Plot a bar graph for each chamber's age distribution (with binned ages)
    chamber_age_group_counts.T.plot(kind="bar", figsize=(12, 8), stacked=False)
    plt.title("Age Distribution by Chamber in Congress (Binned)")
    plt.xlabel("Age Group (Years)")
    plt.ylabel("Frequency")
    plt.legend(title="Chamber", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.savefig("output/chamber_age.png")
    # plt.show()

    stat_md = desc_stats.to_markdown()
    with open("cong_age_summary.md", "w", encoding="utf-8") as file:
        file.write("Describe:\n")
        file.write(stat_md)
        file.write("\n\n")
        file.write("![congressional_age](/output/congressional_age.png)\n")
        file.write("\n\n")
        file.write("![chamber_age](output/chamber_age.png)\n")
