from fastapi import FastAPI, Query  # Import FastAPI and Query parameter
from openai import OpenAI

app = FastAPI()

openai_config = {  # Assuming you have your OpenAI API key stored securely
    "api_key": "YOUR_OPENAI_API_KEY"
}




@app.get("/")
async def generate_image(q: str = Query(..., description="Search query for the image")):
    """
    Generates an image using DALL-E 3 based on the provided query parameter.

    Parameters:
        q (str): The search query for the desired image.

    Returns:
        dict: A dictionary containing the generated image URL or an error message.
    """

    try:
        client = OpenAI(api_key=openai_config["api_key"])
        response = client.images.generate(
            model="dall-e-3",
            prompt=q,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        return {"image_url": response.data[0].url}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while generating the image."}
