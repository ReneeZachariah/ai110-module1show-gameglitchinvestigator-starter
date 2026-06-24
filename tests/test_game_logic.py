import os
import sys

# Ensure project root is on sys.path so tests can import top-level modules.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import os
import sys

# Ensure project root is on sys.path so tests can import top-level modules.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logic_utils import check_guess

# FIX: Added regression tests for mixed-type comparisons during pair-programming with AI.


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, msg = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, msg = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, msg = check_guess(40, 50)
    assert outcome == "Too Low"


def test_mixed_type_numeric_comparison_low():
    # Bug case: numeric guess vs string secret must compare numerically (9 < "10")
    outcome, msg = check_guess(9, "10")
    assert outcome == "Too Low"
    assert msg == "📈 Go HIGHER!"


def test_mixed_type_numeric_comparison_high():
    # Another mixed-type case: numeric guess > string secret
    outcome, msg = check_guess(11, "10")
    assert outcome == "Too High"
    assert msg == "📉 Go LOWER!"
