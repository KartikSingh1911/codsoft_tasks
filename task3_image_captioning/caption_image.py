"""
TASK 3: IMAGE CAPTIONING WITH A PRETRAINED BLIP MODEL

Uses Salesforce BLIP to describe the contents of an image.
The first run downloads model files from Hugging Face.
"""

import argparse
import sys
from pathlib import Path

try:
    import torch
    from PIL import Image, UnidentifiedImageError
    from transformers import BlipProcessor, BlipForConditionalGeneration
except ImportError as error:
    print("A required package is missing.")
    print("Install dependencies with:")
    print("python -m pip install -r task3_image_captioning/requirements.txt")
    print(f"Details: {error}")
    sys.exit(1)


MODEL_NAME = "Salesforce/blip-image-captioning-base"


def generate_caption(image_path: Path, max_length: int = 50) -> str:
    """Load the image-captioning model and generate one caption."""
    if not image_path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")

    try:
        image = Image.open(image_path).convert("RGB")
    except UnidentifiedImageError as error:
        raise ValueError("The selected file is not a supported image.") from error

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")
    print("Loading the pretrained BLIP model (first run may take a while)...")

    processor = BlipProcessor.from_pretrained(MODEL_NAME)
    model = BlipForConditionalGeneration.from_pretrained(MODEL_NAME)
    model.to(device)
    model.eval()

    inputs = processor(images=image, return_tensors="pt").to(device)

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_length=max_length,
            num_beams=5
        )

    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption.strip()


def main():
    parser = argparse.ArgumentParser(
        description="Generate a text caption for an image using BLIP."
    )
    parser.add_argument("image", help="Path to an image file, e.g. photo.jpg")
    parser.add_argument(
        "--max-length",
        type=int,
        default=50,
        help="Maximum generated caption length (default: 50)"
    )
    args = parser.parse_args()

    if args.max_length < 5:
        parser.error("--max-length must be at least 5")

    try:
        caption = generate_caption(Path(args.image), args.max_length)
        print("\n" + "=" * 54)
        print("GENERATED IMAGE CAPTION")
        print("=" * 54)
        print(caption)
        print("=" * 54)
    except (FileNotFoundError, ValueError, OSError) as error:
        print(f"Error: {error}")
        sys.exit(1)
    except Exception as error:
        print(f"Could not generate caption: {error}")
        print("Check your internet connection and try again.")
        sys.exit(1)


if __name__ == "__main__":
    main()
