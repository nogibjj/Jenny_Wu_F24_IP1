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
    stat_md = desc_stats.to_markdown()
    with open("cong_age_summary.md", "w", encoding="utf-8") as file:
        file.write("Describe:\n")
        file.write(stat_md)
        file.write("\n\n")
        file.write("![congressional_age](python_files/outputs/congressional_age.png)\n")
    return stat_md
    print(
        f'The average age of a Congress member from during a  {round(desc_stats["mean"], 3)}'
    )
    print(
        f'The median age of a Congress member from during a {round(desc_stats["50%"], 3)}'
    )
    print(
        f'Standard Deviation between the ages of Congress members is {round(desc_stats["std"], 3)}'
    )

    return desc_stats


"""Building Visualization"""


def hist_cong_age(general_df, col):
    """builds a histogram for the ages of all Congressmembers"""

    plt.hist(general_df[col], bins=20, edgecolor="black")
    plt.title("Distribution of Ages in Congress", fontsize=16)
    plt.xlabel("Age", fontsize=14)
    plt.ylabel("Frequency", fontsize=14)
    plt.savefig("output/congressional_age.png")
    plt.show()


def age_dist_50(general_df):
    """builds a bar graph that demonstrates distribution of age cross chambers"""
    # Convert 'start_date' column to datetime format
    general_df["start_date"] = pd.to_datetime(general_df["start_date"])

    # Bin the ages into 5-year intervals
    general_df["age_group"] = pd.cut(
        general_df["age_years"], bins=range(20, 101, 5), right=False
    )

    # Group by chamber and age group to get frequency counts
    chamber_age_group_counts = (
        general_df.groupby(["chamber", "age_group"]).size().unstack(fill_value=0)
    )

    # Plot a bar graph for each chamber's age distribution (with binned ages)
    chamber_age_group_counts.T.plot(kind="bar", figsize=(12, 8), stacked=False)
    plt.title("Age Distribution by Chamber in Congress (Binned)")
    plt.xlabel("Age Group (Years)")
    plt.ylabel("Frequency")
    plt.legend(title="Chamber", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()

    if is_jupyter is True:
        plt.savefig("./outputs/chamber_age.png")
    if is_jupyter is False:
        plt.savefig("python_files/outputs/output.png")
        plt.show()
