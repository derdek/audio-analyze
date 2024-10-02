from transformers import pipeline

from ml_models.get_device import get_device


def analyse_emotional_tone(text: str):
    classifier = pipeline(
        "sentiment-analysis",
        model="ml_models/text-classificator",
        device=get_device()
    )
    return classifier(text)[0]["label"]
