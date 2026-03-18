# CLAUDE.md — Student Pilot One-Stop Shop (P2006T / G1000)

## Project Overview
A web-based student pilot training tool for the Tecnam P2006T with Garmin G1000. Single-page app covering:
- **Weight & Balance Calculator** (`index.html`) — interactive CG envelope calculator
- **V-Speed Study** (`airspeeds quiz.html`) — flashcard-style airspeed quiz
- **Chairfly Trainer** (`p2006t_chairfly.html`) — simulated G1000 cockpit for chair-flying procedures

## Data Accuracy Rule (non-negotiable)
All values — airspeeds, weight limits, CG envelopes, checklists, procedures — must come from:
- Tecnam P2006T POH / AFM
- School-specific maneuvers guide
- School-specific normal and emergency checklists

Never estimate, approximate, or invent values. If a number is in this tool, it has a source document.

## Stack
- Plain HTML / CSS / JavaScript — no frameworks, no build step
- Each page is a self-contained `.html` file

## Git
- Remote: `git@github.com:SCFDesigner/weight-balance-calculator.git`
- Branch: `main`
- Push after every implementation using `/usr/bin/git`

## File Map
| File | Purpose |
|------|---------|
| `index.html` | Weight & balance calculator (main page) |
| `airspeeds quiz.html` | V-speed study / quiz |
| `p2006t_chairfly.html` | Chairfly trainer with G1000 simulation |
| `p2006t-weight-balance.html` | Legacy W&B page |
| `p2006t-wb-new.html` | W&B iteration |
| `debug.html` | Debug/scratch page |
| `airspeeds_quiz.py` | Legacy Python terminal quiz |
