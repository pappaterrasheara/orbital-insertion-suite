# Roadmap — Orbital Insertion Suite

## Milestone 0 — Project Tidiness
- [ ] Repo structure + docs scaffolding
- [ ] Formatting + linting (ruff + black) and basic test runner (pytest)
- [ ] Consistent units strategy (SI everywhere) + unit conventions documented in `docs/assumptions.md`
- [ ] Add a `runs/` directory convention (timestamped outputs: JSON + plots)

## Milestone 1 — Baseline Ascent Simulator (MVP)
- [ ] 1D/2D ascent propagation (time integration)
- [ ] Mass depletion + thrust model (constant thrust / Isp to start)
- [ ] Atmosphere + drag model (simple, documented)
- [ ] Output time history (state + derived quantities)
- [ ] Save outputs as:
      - `runs/<timestamp>/results.json`
      - `runs/<timestamp>/summary.json`
      - `runs/<timestamp>/plots.png` (or multiple plots)

**Owner split**
- Physics core: Sheara Isabella Pappaterra T.
- Packaging/tests: Luis Camilo Alvarez C.

## Milestone 2 — Guidance + Constraints
- [ ] Parameterized pitch program (piecewise or smooth polynomial)
- [ ] Track max dynamic pressure (q), max acceleration (g-load proxy), and burnout conditions
- [ ] “Scenario presets” for repeatable runs
- [ ] Clear failure states (e.g., negative mass, diverged integration, invalid guidance parameters)

## Milestone 2.5 — Results Schema Contract (UI-ready)
- [ ] Define a stable results JSON schema (inputs, time series, summary, constraints, success/fail reasons)
- [ ] Serializer + version tag (e.g., `"schema_version": "0.1"`)
- [ ] Create one “golden run” dataset for demos and UI development (no backend required)

Rationale: the UI must consume a contract, not simulator internals.

## Milestone 3 — Orbital Insertion Targets
- [ ] Define target metrics (apoapsis/periapsis OR orbital energy proxy)
- [ ] Evaluate insertion quality from final state
- [ ] Basic validation checks (sanity bounds)

## Milestone 4 — Optimization
- [ ] Optimize pitch parameters to hit targets under constraints
- [ ] Compare baseline vs optimized performance (objective value + constraint margins)
- [ ] Add failure detection (non-physical solutions, optimizer divergence, constraint infeasibility)

## Milestone 5 — Visualization + Demo
- [ ] Standard plots (altitude, velocity, mass, q, accel, flight path angle)
- [ ] One “golden demo” scenario for a 2–3 minute video
- [ ] Short technical write-up in `docs/` (assumptions, equations, results, limitations)

## Milestone 6 — Mission Console (Webpage UI)
We build a webpage interface after the simulator MVP and results schema are stable.

### Phase 6A — Fast Win UI (optional)
- [ ] Streamlit mission console (Python-only) for rapid UX validation
- [ ] Controls: guidance parameters, vehicle/stage parameters, constraints
- [ ] Outputs: plots + mission summary tiles + pass/fail reasons

### Phase 6B — Production UI (Python + TypeScript)
Backend (Python)
- [ ] FastAPI service with endpoints:
      - POST `/simulate`
      - POST `/optimize` (later)
      - GET  `/scenarios`
      - GET  `/health`
- [ ] Input validation (pydantic) + helpful error messages

Frontend (TypeScript)
- [ ] React + TypeScript mission console
- [ ] UI layout:
      - Inputs panel (vehicle + guidance + constraints)
      - Results panel (summary cards + plots)
- [ ] Run history (compare two runs side-by-side)

Goal: a professional mission-analysis experience without bloating physics scope.

## Milestone 7 — Packaging + Quality Gates
- [ ] GitHub Actions CI: lint + tests on every pull request
- [ ] `pyproject.toml` for dependencies and tooling
- [ ] Minimal CLI entry point (`python -m orbital_insertion_suite ...`)
- [ ] Release v0.1 tag + stable “golden demo” command
