# src/prep.py — shared data loading & prep, imported by every deep-dive notebook
import pandas as pd
import numpy as np


def time_to_seconds(t):
    if pd.isna(t) or not isinstance(t, str):
        return np.nan
    parts = [int(p) for p in t.strip().split(":")]
    if len(parts) == 3:
        return parts[0] * 3600 + parts[1] * 60 + parts[2]
    elif len(parts) == 2:
        return parts[0] * 60 + parts[1]
    return np.nan


def load_results():
    """Race results with all time columns converted to seconds.
    Includes a corrected run/finish for Charif (official run time was inflated
    by re-entering the tracked course; true finish 7:06:54, photo-corroborated)."""
    df = pd.read_csv("../data/Raw/ironman703agadir2025-results.csv")

    for col in ['Swim Time', 'Bike Time', 'Run Time',
                'Transition 1 Time', 'Transition 2 Time', 'Overall Time']:
        df[col + ' (s)'] = df[col].apply(time_to_seconds)

    # ---- DATA CORRECTION: Charif's run split ----
    mask = df['Name'].str.contains('GHILANI', case=False, na=False)
    corrected_finish = 7 * 3600 + 6 * 60 + 54          # 7:06:54 = 25614s
    df['Run Time (s) corrected'] = df['Run Time (s)']
    df['Overall Time (s) corrected'] = df['Overall Time (s)']
    df.loc[mask, 'Run Time (s) corrected'] = corrected_finish - (2763 + 434 + 13291 + 170)
    df.loc[mask, 'Overall Time (s) corrected'] = corrected_finish

    return df


def load_activities():
    """Strava activities with parsed dates."""
    df = pd.read_csv("../data/Raw/activities.csv")
    df['date'] = pd.to_datetime(df['Activity Date'],
                                format='%b %d, %Y, %I:%M:%S %p', errors='coerce')
    return df