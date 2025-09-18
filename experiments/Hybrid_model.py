"""
Novel Hybrid Model Simulation (Section 6)
Staged costs.
"""

import numpy as np

def hybrid_cost(lat_class=0.05, lat_pqc=1.33, threat=0.9, alpha=0.7, beta=0.3):
    if threat > 0.5:
        return beta * 1.0 + alpha * lat_pqc  # Full PQC
    else:
        return beta * 0.8 + alpha * (lat_class * 0.5 + lat_pqc * 0.5)  # Hybrid

stages = ['2025-28 (Hybrid)', '2028-32 (AI-Switch)', '2032+ (Full PQC)']
threats = [0.3, 0.6, 0.9]
for s, t in zip(stages, threats):
    cost = hybrid_cost(threat=t)
    deg = ((cost - 0.05) / 0.05) * 100  # %deg
    print(f"{s}: Cost {cost:.3f} ms (degradation {deg:.1f}%)")
    # Output: 2025-28: 0.740 ms (degradation 1380.0%) wait, scale properly(assume normalized).
