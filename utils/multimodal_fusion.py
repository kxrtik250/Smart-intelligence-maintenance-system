def fuse_features(data: dict):
    fused = {}
    img = data.get('image_pred',{})
    fused['image_score'] = img.get('defect_score', 0.0)
    sensor = data.get('sensor_pred',{})
    fused['sensor_anomaly'] = sensor.get('anomaly', False)
    fused['sensor_score'] = sensor.get('score', 0.0)
    fused['log_length'] = len(data.get('log_text','')) if data.get('log_text') else 0
    return fused
