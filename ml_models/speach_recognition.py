import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline

from ml_models.get_device import get_device


def speach_recognition(audio_path: str) -> str:
    device = get_device()
    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
    model_id = "ml_models/speach-recognition"
    model = AutoModelForSpeechSeq2Seq.from_pretrained(
        model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=False
    )
    model.to(device)
    processor = AutoProcessor.from_pretrained(model_id)
    pipe = pipeline(
        "automatic-speech-recognition",
        model=model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        max_new_tokens=128,
        chunk_length_s=15,
        batch_size=16,
        torch_dtype=torch_dtype,
        device=device,
    )
    result = pipe(audio_path)
    return result["text"]
