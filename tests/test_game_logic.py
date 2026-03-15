from logic_utils import check_guess, get_range_for_difficulty


def test_difficulty_ranges_scale_with_difficulty():
    # Hard should have a larger range than Normal, which should be larger than Easy
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert easy_high < normal_high < hard_high


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Regression tests for the swapped-hint / string-comparison bug ---


def test_too_high_message_says_lower():
    # Bug: when guess > secret, message incorrectly said "Go HIGHER!"
    # It should say "Go LOWER!" so the player knows to decrease their guess
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_too_low_message_says_higher():
    # Bug counterpart: when guess < secret, message should say "Go HIGHER!"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_numeric_comparison_not_lexicographic():
    # Bug: secret was cast to str on even attempts, causing "5" > "20" (lexicographic)
    # to return "Too High" even though 5 < 20 numerically.
    # guess=5, secret=20 must always be "Too Low".
    outcome, _ = check_guess(5, 20)
    assert outcome == "Too Low"


def test_numeric_comparison_two_digit_boundary():
    # Another lexicographic edge case: "9" > "10" alphabetically but 9 < 10 numerically
    outcome, _ = check_guess(9, 10)
    assert outcome == "Too Low"
