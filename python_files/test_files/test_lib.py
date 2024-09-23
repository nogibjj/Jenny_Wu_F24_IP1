"""
Test goes here

"""

import pandas as pd
import pytest
import sys

sys.path.append("python_files/main_files")
import lib

example_csv = "https://raw.githubusercontent.com/fivethirtyeight/data/master/congress-demographics/data_aging_congress.csv"


def test_load_and_preprocess():
    """test that loading the csv will work"""
    general_df = lib.load_and_preprocess(example_csv)
    assert general_df is not None
    assert general_df.shape == (29120, 13)


def test_get_summary_stats():
    """test that the summary function will work"""
    test_desc_stats = lib.get_summary_stats(pd.read_csv(example_csv), "age_years")
    # assert test_desc_stats["min"] == pytest.approx(23.665982, 0.1)
    # assert test_desc_stats["std"] == pytest.approx(10.763105, 0.1)
    assert test_desc_stats is not None


def test_hist_cong_age():
    general_df = lib.load_and_preprocess(example_csv)
    test_hist = lib.hist_cong_age(general_df, "age_years")
    assert test_hist is None


def test_age_dist_50():
    general_df = lib.load_and_preprocess(example_csv)
    desc_stats = lib.get_summary_stats(pd.read_csv(example_csv), "age_years")
    test_hist_50 = lib.age_dist_50(general_df, desc_stats)
    assert test_hist_50 is None


test_get_summary_stats()
test_load_and_preprocess()
test_hist_cong_age()
test_age_dist_50()
