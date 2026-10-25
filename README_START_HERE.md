# Quantum City Lab — 30-Program Integrated Platform

A standalone Streamlit research application for 10 quantum-computing modules, 5 carbon-nanomaterials modules and 5 carbon-emissions modules 5 sensor modules and 5 quantum-photonics modules.

## Windows setup

1. Extract this ZIP to a **new folder** such as `C:\Users\YOURNAME\QuantumCityLab20`. Do not overwrite your existing QuantumCityLab folder or its `.env` credentials.
2. Open PowerShell in the extracted folder (File Explorer address bar: type `powershell` and press Enter).
3. Install packages: `py -m pip install -r requirements.txt`
4. Start: `py -m streamlit run app.py`
5. Open the local URL shown (usually `http://localhost:8501`). To stop, press Ctrl+C in PowerShell.
6. Run automated tests: `py -m pytest -q`

## Publish a separate website (Streamlit Community Cloud)

1. Create a **private GitHub repository** and upload `app.py`, `models.py`, `requirements.txt`, `README_START_HERE.md`, and `tests/` (do not upload `.env`, keys, raw private datasets or personal files).
2. Sign in to https://share.streamlit.io/ and create an app from that repository, selecting `app.py` as the entrypoint.
3. Choose an available app name and deploy. The actual public URL is assigned by the host; **this ZIP does not create or reserve a live URL**.
4. Community Cloud apps can be publicly accessible even if their source repository is private. For private research data and IBM credentials, choose a hosting service with authentication and secret management before uploading.
5. This dashboard **does not submit IBM jobs**. A production IBM integration requires a secure server-side API and user authentication; never embed an IBM API key in a public client or repository.

## Program guide

| IDs | Section | Focus |
|---|---|---|
| 01–10 | Quantum Computing | Bell states, recorded IBM results, statistics, qubit screening, circuit depth, shots, runtime, benchmarking and pilot ROI |
| 11–15 | Carbon Nanomaterials | CNT CVD output, graphene yield, interconnect scaling, quality control and factory economics |
| 16–20 | Carbon Emissions | GHG footprint, energy emissions, reduction pathways, capture economics and smart city forecasts |
| 21–25 | Sensors & Diamond Sensors | Signal-to-noise, NV diamond magnetometry, NV thermometry, photon statistics and sensor networks |
| 26–30 | Quantum Photonics | Fiber photon loss, single-photon detection, interferometry, QKD link budget and photonic chip losses |

All modules support editable inputs, a sensitivity graph, CSV export and JSON evidence export. Equations are in `models.py` for reproducibility. Defaults are **illustrative**, not measured industrial parameters. All output is for research/education, not engineering certification, compliance or investment decisions.

## Historical experiments

Experiments 01–05 are summarized in the app as screenshot-transcribed observations. Experiment 02: 265/1000 unexpected parity (26.5%). Experiment 05: 8/1000 (0.8%). This is an observed difference, not a causal demonstration of optimizer effectiveness. The historical records do not include original IBM job metadata, calibration snapshots or independently verified raw hardware data.

## Recommended next improvements

- Import original IBM CSV/JSON and job IDs from the user's existing laptop project.
- Add repeated randomized A/B hardware runs with the same shots, comparable backend conditions, calibration snapshots, uncertainty and cost tracking.
- Replace illustrative CNT/graphene yields with literature-supported or pilot-plant measurements.
- Replace placeholder grid factors with documented jurisdiction/year-specific factors; define GHG Protocol scopes and boundaries.
- Add access control, persistent database, audit trails, CI and secure backend IBM job submission before production use.

## Photonics interpretation

The five added photonics tools are transparent analytical teaching models, not photonic circuit simulators or secure quantum communication demonstrations. No IBM photonic hardware is connected.


## Alignment with the author's Quantum City book
Every module includes an expandable city-use-case panel with relevant chapters, a conventional benchmark, measurable KPIs, and evidence status. The dashboard adds the ten-stage Q-CITY pathway, a 30-program mapping table, downloadable alignment CSV, and a pilot decision record export. See `BOOK_ALIGNMENT_30_PROGRAMS.csv`.

**Important distinction:** Carbon nanomaterials and emissions programs are enabling urban technologies, not quantum technologies by definition. They belong in the Quantum City ecosystem only where an actual urban outcome, integration case, or testable quantum-hybrid hypothesis exists. Diamond NV sensing and quantum photonics have more direct quantum-technology relevance, but still require conventional benchmarks. Chapter mappings are editorial interpretations, not quotations from the book.
