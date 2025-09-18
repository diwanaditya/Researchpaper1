**Key Insights:**
- Lattice-based (Kyber/Saber/Dilithium) dominate for 5G/6G: Low latency, suitable for URLLC/SUCI.
- SPHINCS+ lags in signing (2.61 ms), risking bandwidth in handovers.
- Hybrid model (from hybrid_model.py): <2% degradation (e.g., 0.68 ms at low threat).

## Benchmark Table

| Algorithm    | Operation | Mean Time (ms) | Std Dev (ms) | Notes |
|--------------|-----------|----------------|--------------|-------|
| Kyber-512   | Keygen    | 1.30          | 0.17        | Excellent for SUCI; NTT-optimized. |
| Dilithium-2 | Signing   | 0.04          | 0.03        | Competitive for auth/handovers; rejection sampling. |
| RSA-2048    | Keygen    | 5.89          | 2.52        | Baseline; quantum-vulnerable, slow. |
| ECC-256     | Keygen    | 0.00          | 0.00        | Fast classical; but Shor-broken. |
| Saber       | Keygen    | 1.24          | 0.16        | SCA-resistant edge over Kyber; LWR-based. |
| SPHINCS+    | Signing   | 2.61          | 0.35        | Conservative hash-based; large sigs limit URLLC. |

## Raw Outputs
- Kyber-512 Keygen: 1.30 ± 0.17 ms  
- Dilithium-2 Signing: 0.04 ± 0.03 ms  
- RSA-2048 Keygen: 5.89 ± 2.52 ms  
- ECC-256 Keygen: 0.00 ± 0.00 ms  
- Saber Keygen: 1.24 ± 0.16 ms  
- SPHINCS+ Signing: 2.61 ± 0.35 ms  

For questions: diwanaditya964@gmail.com
