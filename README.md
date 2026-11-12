# EARTH ON TRIAL — AURELIUS-9

An open-world-inspired sci-fi strategy game featuring a Pakistani planetary scientist, a truck-art-inspired expedition vessel, planetary investigation missions and an intergalactic tribunal.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy
On Streamlit Community Cloud, choose this repository, branch `main`, main file `app.py`.

## Controls
WASD / Arrow keys to move around the 3D hangar. Press E near a gold mission beacon. Touch arrows and the interaction control work on touch devices.

## Architecture
Three.js renders the interactive hangar inside a Streamlit HTML component. Streamlit Python manages missions, evidence, scientist profile, ship naming, resources and tribunal outcome. Mission evidence values are game mechanics, not live scientific measurements.

Pakistani design inspirations include truck art, Ajrak-inspired geometry, emerald enamel, brass and marigold.
