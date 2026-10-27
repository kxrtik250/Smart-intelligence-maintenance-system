import pandas as pd
from models.image_defect_cnn import load_image_model, predict_defect
from models.sensor_lstm import load_sensor_model, detect_anomaly
from utils.speech_to_text import transcribe_audio

class PerceptionAgent:
    def __init__(self):
        self.image_model = load_image_model()
        self.sensor_model = load_sensor_model()

    def collect_data(self, image_path=None, sensor_path=None, log_path=None, audio_path=None):
        data = {}
        if image_path:
            data['image_path'] = image_path
            data['image_pred'] = predict_defect(self.image_model, image_path)
        if sensor_path:
            try:
                df = pd.read_csv(sensor_path)
            except Exception:
                df = pd.DataFrame()
            data['sensor_df'] = df
            data['sensor_pred'] = detect_anomaly(self.sensor_model, df) if not df.empty else {}
        if log_path:
            try:
                with open(log_path, 'r', encoding='utf-8') as f:
                    data['log_text'] = f.read()
            except Exception:
                data['log_text'] = ''
        if audio_path:
            data['transcript'] = transcribe_audio(audio_path)
        return data
