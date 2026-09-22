from datetime import datetime

def format_value(value, unit, decimals=2) -> str:
    if value is None:
        return "N/A"
    return f"{value:.{decimals}f} {unit}"

def format_delta(current, target) -> tuple:
    if current is None or target is None:
        return ("0", "normal")
    diff = current - target
    color = "normal"
    if diff > 0:
        color = "good"
    elif diff < 0:
        color = "alarm"
    return (f"{diff:+.2f}", color)

def format_timestamp(ts) -> str:
    if not ts:
        return ""
    if isinstance(ts, str):
        try:
            ts = datetime.fromisoformat(ts.replace("Z", "+00:00"))
        except:
            return ts
    return ts.strftime("%Y-%m-%d %H:%M:%S")

def format_kpi_status(value, target, tolerance_pct) -> str:
    if value is None or target is None:
        return "normal"
    lower_bound = target * (1 - tolerance_pct / 100)
    upper_bound = target * (1 + tolerance_pct / 100)
    if value >= target:
        return "good"
    elif value >= lower_bound:
        return "caution"
    return "alarm"

def format_confidence(pct) -> str:
    if pct is None:
        return "N/A"
    color = "green" if pct >= 80 else "orange" if pct >= 50 else "red"
    return f"<span style='color:{color}'>{pct:.1f}%</span>"
