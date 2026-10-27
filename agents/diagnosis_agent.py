from utils.multimodal_fusion import fuse_features
from models.text_transformer import summarize_text

class DiagnosisAgent:
    def __init__(self):
        pass

    def analyze(self, multimodal_data: dict):
        fused = fuse_features(multimodal_data)
        reasons = []
        severity = 'low'
        if fused.get('image_score',0) > 0.6:
            reasons.append('Visual defect detected')
            severity = 'high'
        if fused.get('sensor_anomaly', False):
            reasons.append('Sensor anomaly detected')
            severity = 'critical' if fused.get('sensor_score',0)>2.0 else 'medium'
        if multimodal_data.get('log_text'):
            short = summarize_text(multimodal_data['log_text'])
        else:
            short = ''
        summary = {
            'short_summary': short,
            'reasons': reasons,
            'severity': severity,
            'details': fused
        }
        return summary
