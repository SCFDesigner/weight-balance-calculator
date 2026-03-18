# Student Pilot One-Stop Shop — Tecnam P2006T / G1000

A web-based training tool for student pilots flying the **Tecnam P2006T** with a **Garmin G1000** glass cockpit. All information is sourced directly from the **POH/AFM** and **school-specific maneuvers guides and checklists** to ensure accuracy.

---

## What's Inside

### Weight & Balance Calculator (`index.html`)
An interactive weight and balance tool for the P2006T. Enter passenger weights, baggage, and fuel to instantly calculate:
- Total weight and CG location
- Whether the loading is within the aircraft's approved envelope
- Visual envelope plot

### Airspeed / V-Speed Study (`airspeeds quiz.html`)
A flashcard-style study tool for memorizing P2006T V-speeds. All values are taken directly from the POH/AFM.

### Chairfly Trainer (`p2006t_chairfly.html`)
A simulated G1000 cockpit environment for chair-flying maneuvers. Walk through procedures step-by-step with:
- Animated PFD and MFD representations
- Checklist and emergency procedure overlays
- Step-by-step callouts for each maneuver

---

## Data Sources

All data — airspeeds, weight limits, CG envelopes, checklists, and procedures — comes from:
- **Tecnam P2006T POH / AFM**
- **School-specific maneuvers guide**
- **School-specific normal and emergency checklists**

Nothing is estimated or approximated. If a value is in this tool, it has a source document.

---

## Purpose

Built for personal use during primary flight training. The goal is a single tab that covers everything needed for ground study and pre-flight preparation — numbers, procedures, and chair-flying — without switching between multiple documents.

---

## Python Quiz (Legacy)

`airspeeds_quiz.py` is an earlier terminal-based V-speed quiz. Requires Python 3.6+.

```bash
python3 airspeeds_quiz.py
```
