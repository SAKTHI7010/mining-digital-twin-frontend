COLOR_NORMAL = '#2ECC71'
COLOR_CAUTION = '#F39C12'
COLOR_ALARM = '#E74C3C'
COLOR_OPTIMIZED = '#3498DB'
COLOR_SIMULATED = '#9B59B6'

KPI_TARGETS = {
    "throughput": 1200,
    "recovery": 88.0,
    "concentrate_grade": 28.0,
    "tail_grade": 0.08,
    "energy_intensity": 18.0,
    "water_intensity": 0.80,
    "availability": 95.0
}

UNIT_LABELS = {
    "SAG": "SAG Mill",
    "BM": "Ball Mill",
    "CYC": "Hydrocyclone",
    "FL_RO": "Flotation Rougher",
    "FL_CL": "Flotation Cleaner",
    "FL_SC": "Flotation Scavenger",
    "THK": "Thickener",
    "FIL": "Belt Filter"
}

TIME_WINDOWS = {
    '15min': 15,
    '1h': 60,
    '8h': 480,
    '24h': 1440,
    '7d': 10080
}

MINING_TERMINOLOGY = {
    "throughput": "t/h of ore processed",
    "recovery": "% of valuable mineral recovered into concentrate",
    "concentrate_grade": "% of valuable mineral in the final product",
    "tail_grade": "% of valuable mineral lost to tailings",
    "P80": "80% passing size of the grind product (microns)",
    "kWh/t": "Kilowatt-hours per tonne of ore (Energy Intensity)"
}
