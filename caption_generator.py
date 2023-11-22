from transformers import pipeline

pipe = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

def generate_caption(image):
    """
    Creates a caption for the given image.
    """
    results = pipe(image)
    # If the result is a list of dictionaries, access the first item
    if isinstance(results, list) and len(results) > 0:
        return results[0]['generated_text']
    else:
        raise ValueError("The model didn't return a proper result.")
