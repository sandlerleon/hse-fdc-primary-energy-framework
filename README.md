# Beyond PUE: A Boundary-Aware Primary-Energy Framework

Leon Sandler, The Conscious Machine, Independent Researcher — sandler.leon@gmail.com

Code and manuscript for "Beyond PUE: A Boundary-Aware Primary-Energy Framework
for Evaluating Self-Powered Computing Infrastructure, with Application to a
Hybrid Offshore Floating Data Center," prepared for submission to *Discover
Sustainability* (Springer Nature).

## Summary

Power usage effectiveness (PUE) is the dominant data-center sustainability
metric, but it is defined only over the facility boundary: cooling and
auxiliary overhead relative to IT load. For self-powered infrastructure that
generates its own electricity on site, this boundary excludes exactly the
losses — fuel-to-electricity conversion, and any carbon-capture parasitic
load — that determine whether total energy use is actually efficient. This
study develops a boundary-aware primary-energy accounting framework,

```
η_primary = η_cycle × (1 − CCS_penalty) / PUE
```

and applies it as a case study to a proposal-stage architecture, the Hybrid
Seabed-Energy Floating Data Center (HSE-FDC), which combines offshore
associated-gas turbines, a wave-energy-converter array, carbon capture, and
passive marine cooling, and which had claimed a PUE of approximately 1.04
with negligible grid dependency.

Using literature-grounded parameters, the case study finds a plausible
facility PUE of 1.08–1.09 (comparable to, not better than, real marine-cooled
benchmarks), while the wave array contributes under 1.2% of average power —
far short of a genuine hybrid baseload. Critically, this favorable facility
PUE corresponds to a primary energy efficiency of only 25.5–38.7%, below a
conventional grid-tied facility (43.0%) and dramatically below a
renewable-grid-tied facility (93.5%). A favorable facility PUE does not, by
itself, indicate favorable total energy efficiency once on-site generation is
included.

## Contents

- `manuscript/` — manuscript and cover letter (Word), CC BY 4.0.
- `code/` — Python (NumPy-free, standard library + Matplotlib), MIT license:
  - `hsefdc_model.py` — the complete, self-contained accounting model: wave
    power flux (Falnes 2007 deep-water formulation), gas-turbine baseload,
    facility PUE, the boundary-aware primary-energy-efficiency metric, and
    CCS-penalty-adjusted carbon intensity. Running it reproduces every
    quantitative result in the manuscript exactly (`hsefdc_results.json`).
  - `generate_figures.py` — regenerates Figures 1–4 from the model output,
    formatted per Discover Sustainability's figure requirements (no in-image
    titles, sans-serif 8–12 pt lettering).
  - `hsefdc_results.json` — machine-readable output of the model run.
  - `fig1_gas_vs_wave_supply.png`, `fig2_pue_benchmarks.png`,
    `fig3_primary_energy_efficiency.png`, `fig4_carbon_intensity.png` —
    regenerated figures from the above script.

Run with `python hsefdc_model.py` then `python generate_figures.py`
(requires `matplotlib`; no other dependencies). All results are derived from
the cited literature parameters (Section 3 of the manuscript) — nothing is
fitted to any measured dataset, since this is a proposal-stage feasibility
case study, not an operating facility.

**Note on carbon-intensity accounting:** the manuscript's carbon-intensity
figures (Section 4.4) are computed per kWh *delivered to the IT load* (i.e.
including the facility PUE overhead), matching the basis of the US-grid-average
comparator. This is implemented consistently in `hsefdc_model.py` and
documented in code comments.

## License

Code: MIT (see `LICENSE` at repo root — the top-level `LICENSE` file
applies to `code/`). Manuscript: CC BY 4.0 (see `manuscript/LICENSE`).
