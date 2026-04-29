def detect_drift(reference_counts, production_counts, threshold):
    """
    Compare reference and production distributions to detect data drift.
    """
    total_ref = sum(reference_counts)
    total_prod = sum(production_counts)

    ref_probs = [ref / total_ref for ref in reference_counts]
    prod_probs = [prod / total_prod for prod in production_counts]

    tvd_sum = 0
    for rp, pp in zip(ref_probs, prod_probs):
        tvd_sum += abs(rp - pp)
    TVD = 0.5 * tvd_sum

    return {
        "score": TVD,
        "drift_detected": TVD > threshold
    }


reference_counts = [50, 50]
production_counts = [55, 45]
threshold = 0.1

print(detect_drift(reference_counts, production_counts, threshold))
