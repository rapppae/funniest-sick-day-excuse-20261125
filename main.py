"""Entry for make.fun bounty: The Funniest Sick-Day Excuse
Slug: u-zeroxfive-the-funniest-sick-day-excuse-37423a36
Entry text (118 characters, gate max 200). Written to /output/entry.txt with no trailing newline.
"""
import os

ENTRY = """Sorry, I can't come in today — my bed has filed a formal complaint and I'm legally required to stay and negotiate."""

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
