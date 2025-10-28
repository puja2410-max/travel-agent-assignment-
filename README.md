# Agentic AI — Travel Itinerary Take-Home Assignment

**Problem Statement:** Design an Agentic AI system that autonomously plans optimized travel itineraries.

**Goal:** Consider weather, month/time, local holidays, road conditions, transport type, and budget constraints.

**Generated:** 2025-10-28

## Contents
- `architecture/` : system diagrams and data/control flow
- `docs/` : use cases, PEAS, agent collaboration, ethics
- `src/` : agents, message bus, service connectors, planners, models, utils, and a demo CLI
- `tests/` : unit and integration test stubs
- `infra/` : Dockerfile and k8s manifest stub
- `ci/` : GitHub Actions CI stub
- `requirements.txt` and `LICENSE`

## Quick start
1. Unzip the archive.
2. Create a virtualenv: `python -m venv .venv && source .venv/bin/activate` (Unix) or use your preferred method.
3. `pip install -r requirements.txt`
4. Run demo: `python -m src.main`
5. Run tests: `pytest -q`
