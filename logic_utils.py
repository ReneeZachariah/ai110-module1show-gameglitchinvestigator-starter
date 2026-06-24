def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    # FIX: Refactored from app.py in collaboration with AI; validates and
    # coalesces input into an int.
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # FIX: Moved from app.py and corrected numeric vs string comparison bugs.
 
    try:
        g = int(guess)
        s = int(secret)
    except (ValueError, TypeError):
        # Fallback: compare as strings for equality only.
        if str(guess) == str(secret):
            return "Win", "🎉 Correct!"
        # Ordering is ambiguous for non-numeric secrets; return a deterministic hint.
        return "Too Low", "📉 Go LOWER!"

    # Numeric comparison with correct hint messages.
    if g == s:
        return "Win", "🎉 Correct!"
    if g > s:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
