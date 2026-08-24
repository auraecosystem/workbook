confidence_values = detector.compute_language_confidence_values("languages are awesome")

for result in confidence_values:
    print(f"{result.language.name}: {result.value:.2f}")

# Output:
# ENGLISH: 1.00
# SPANISH: 0.00
# FRENCH: 0.00
# GERMAN: 0.00