"""Placeholder CNN model file for image defect detection."""
def load_image_model():
    return {'model': 'dummy_cnn', 'version': '0.1'}

def predict_defect(model, image_path):
    import os
    fname = os.path.basename(image_path or '')
    score = 0.9 if 'bad' in fname.lower() else 0.1
    return {'defect_score': score, 'label': 'defect' if score>0.5 else 'ok'}
