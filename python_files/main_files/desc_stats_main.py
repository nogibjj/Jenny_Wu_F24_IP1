"""MAIN FILE"""

import lib


def main():
    """Calling the functions as defined with the specific dataset"""
    csv = "https://raw.githubusercontent.com/fivethirtyeight/data/master/congress-demographics/data_aging_congress.csv"

    general_df = lib.load_and_preprocess(csv)
    desc_stats = lib.get_summary_stats(general_df, "age_years")
    lib.hist_cong_age(general_df, "age_years")
    lib.age_dist_50(general_df, desc_stats)
    # print(general_df.head())
    print(desc_stats)


if __name__ == "__main__":
    main()
