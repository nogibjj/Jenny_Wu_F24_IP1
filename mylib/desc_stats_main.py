"Runs function as defined in lib.py"
import lib

def main():
    """Loads a dataset
    generates summary stats and visualizations"""
    csv = "./data/us_driving_fatalities.csv"
    driving_df = lib.load_dataset(csv)

    if driving_df is not None:
        print(lib.full_describe(driving_df))
        lib.build_bar_chart(driving_df, False)


if __name__ == "__main__":
    main()
