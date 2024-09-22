"""
Test goes here

"""

import pandas as pd
import pytest
from main import load_and_preprocess, get_summary_stats


example_csv = "https://raw.githubusercontent.com/fivethirtyeight/data/master/congress-demographics/data_aging_congress.csv"


def test_load_and_preprocess():
    """test that loading the csv will work"""
    general_df = load_and_preprocess(example_csv)
    assert general_df is not None
    assert general_df.shape == (29120, 13)


def test_get_summary_stats():
    """test that the summary function will work"""
    test_desc_stats = get_summary_stats(pd.read_csv(example_csv), "age_years")
    assert test_desc_stats["mean"] == pytest.approx(
        53.73247531045273, 0.1
    )  # assert approximate
    assert test_desc_stats["min"] == pytest.approx(23.6659822039699, 0.1)
    assert test_desc_stats["std"] == pytest.approx(10.763104939987494, 0.1)


test_get_summary_stats()
test_load_and_preprocess()