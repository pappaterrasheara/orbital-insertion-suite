# Orbital Insertion Suite

A trajectory simulation and optimization toolkit for powered ascent and orbital insertion.
Built to be clear, testable, and extensible—focused on disciplined assumptions and readable results.

## Core Capabilities (planned)
- Powered-ascent propagation with mass depletion, thrust, drag, and gravity
- Parameterized guidance (pitch program / gravity-turn style) with constraints
- Optimization to meet insertion targets (apoapsis/periapsis or orbital energy) under limits (max-q, max g)
- Analysis and visualization: altitude, velocity, mass, dynamic pressure, acceleration, flight path angle

## Philosophy
This project prioritizes:
- explicit assumptions
- unit consistency
- sanity checks and regression tests
- plots that an aerospace reviewer expects

## Repository Structure
- `src/` simulation, guidance, optimization, and visualization modules
- `docs/` assumptions, equations, and roadmap
- `tests/` unit and regression tests
- `notebooks/` exploratory analysis and demos

## Status
Early development. Initial milestones:
- baseline ascent simulator
- baseline guidance
- constraint tracking (max-q, max g)
- first optimizer pass

## How to Contribute (team workflow)
- Use branches (e.g., `feature/simulator-core`, `feature/guidance-law`)
- Open pull requests for review before merging to `main`
- Use branches (e.g., `feature/simulator-core`, `feature/guidance-law`)
- Open pull requests for review before merging to `main`
