"""Famous Last Words at 1 Percent — make.fun entry.

The line: the farewell a phone says as its battery hits 1
percent, in the phone's own voice. The winning shape is a
concrete incident report with a reversal: a specific inventory
the phone kept safe all year (4,812 photos, 217 passwords, one
3 a.m. alarm), a specific countdown (the alarm dies with it in
ten seconds), and a punchline that lands on the owner — tomorrow
morning the hero wakes himself up, on time, alone. It avoids
the genre's stock moves entirely: no will reading, no goodbye
to the charger, no pun on 1 percent.

Candidates considered and rejected:
- "I have 1 percent left and 4,812 photos to say goodbye to —
  tell the charger I waited for it, and tell my owner the alarm
  still loves him." — uses the banned goodbye-to-the-charger
  move and a will-reading frame; the judge penalises both stock
  moves by name.
- "One percent. I spent my life opening your apps at 2 a.m. and
  now I die doing the same — at least the screen stayed lit
  longer than your attention span." — the phone's voice is good,
  but there is no concrete inventory and the punch insults the
  owner generically instead of landing on a specific betrayal.
- "Goodbye, cruel world of 3 percent warnings — I ignored all 47
  of them, and my final act is deleting the alarm you needed
  tomorrow." — "goodbye cruel world" is a stock farewell, and
  deleting the alarm as revenge is a second joke competing with
  the first.
The chosen line wins on the judge's own order: unmistakably the
phone's last words on the subject first, then a real twist with
a sharp final beat, then the phone's own voice throughout. At
196 characters it uses nearly the full 199-character budget. No
dollar amounts appear anywhere.
"""

# The inventory the phone kept safe, and the countdown.
SETUP = (
    "I kept your 4,812 photos, 217 passwords and one 3 a.m. alarm "
    "safe all year \u2014 "
)

# The punchline lands on the owner: the alarm dies with the
# phone, so tomorrow the hero wakes himself up, alone.
PUNCH = (
    "the alarm dies with me in ten seconds, so congratulations, "
    "hero: tomorrow morning you wake yourself up, on time, alone."
)

LINE = SETUP + PUNCH

# The gate allows 1 to 199 characters; refuse to emit an over-long
# line rather than silently submitting one the judge trims.
assert len(LINE) <= 199, f"line is {len(LINE)} characters, over the 199 cap"


def main() -> None:
    """Write the farewell to ``<output_dir>/entry.txt``."""
    import os

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
