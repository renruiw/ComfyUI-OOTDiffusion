from .parsing_api import load_atr_model, load_lip_model, inference


class Parsing:
    def __init__(self, atr_model_path, lip_model_path, *, device):
        self.device = device
        self.atr_model = load_atr_model(atr_model_path).to(device)
        self.lip_model = load_lip_model(lip_model_path).to(device)

    def __call__(self, input_image):
        parsed_image, face_mask = inference(
            self.atr_model, self.lip_model, input_image, device=self.device
        )
        return parsed_image, face_mask
