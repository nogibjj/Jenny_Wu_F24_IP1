"""Takes a csv file, reads it, and creates graphs"""

import pandas as pd
import sys

sys.path.append("python_files/main_files")
from desc_stats_main import main


def test_main():
    result = main()
    assert result is None


if __name__ == "__main__":
    test_main()
