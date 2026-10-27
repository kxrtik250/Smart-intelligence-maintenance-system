"""Placeholder for sensor time-series anomaly detection model."""

def load_sensor_model():
    return {'model': 'dummy_lstm', 'version': '0.1'}

def detect_anomaly(model, sensor_df):
    # Select only numeric columns (exclude timestamp)
    numeric_df = sensor_df.select_dtypes(include=['number'])
    
    if numeric_df.empty:
        return {'anomaly': False, 'score': 0.0, 'max_val': 0.0, 'threshold': 0.0}
    
    thr = numeric_df.mean().mean() + 3 * numeric_df.std().mean()
    max_val = numeric_df.max().max()
    is_anom = bool(max_val > thr) if thr > 0 else False
    score = float(max_val / (thr + 1e-6)) if thr > 0 else 0.0
    
    return {
        'anomaly': is_anom, 
        'score': score, 
        'max_val': float(max_val), 
        'threshold': float(thr)
    }
