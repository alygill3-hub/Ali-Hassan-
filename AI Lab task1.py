"""
Lab 1: Task 1 - Historical AI Milestones Timeline
File: lab1_timeline.py
"""

timeline = [
    ("1950", "Turing's Imitation Game", "Foundational framework for testing machine intelligence.", "Turing (1950)"),
    ("1956", "Dartmouth Conference", "Formally established AI as an independent discipline.", "McCarthy et al. (1955)"),
    ("1974-80", "First AI Winter", "Severe funding drops due to limited hardware & hype.", "Crevier (1993)"),
    ("1997", "IBM Deep Blue Victory", "Proved specialized search beats world chess champions.", "Campbell et al. (2002)"),
    ("2020", "OpenAI GPT-3 Release", "Proved massive compute/data scaling enables general NLP.", "Brown et al. (2020)")
]

print("=" * 90)
print(f"{'YEAR':<10} | {'EVENT':<25} | {'SIGNIFICANCE':<35} | {'SOURCE':<15}")
print("=" * 90)

for year, event, sig, source in timeline:
    print(f"{year:<10} | {event:<25} | {sig:<35} | {source:<15}")

print("=" * 90)