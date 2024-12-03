import pandas as pd
import asyncio
import aiohttp
from PIL import Image
from io import BytesIO

data = pd.read_json("data/products.jsonl", lines=True)
data.drop_duplicates(subset=["id"], inplace=True)
data.dropna(inplace=True)
data.reset_index(inplace=True)

async def download_image(url: str):
    # Asynchronously download the image
    async with aiohttp.ClientSession() as session:
        for attempt in range(3): 
            try:
                async with session.get(url) as response:
                    if response.status == 200:
                        # Read image content
                        img_data = await response.read()
                        return img_data
                    else:
                        print(f"Attempt {attempt + 1}: Received status code {response.status}")
            except aiohttp.ClientError as e:
                print(f"Attempt {attempt + 1}: Request failed with exception: {e}")
        
            # await asyncio.sleep(3)  # Wait before retrying

async def save_image(image_data: bytes, filename: str):
    # Open image from bytes and save it
    img = Image.open(BytesIO(image_data))
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    img.save(filename)
    print(f"Image saved as {filename}")

async def download_and_save_images(image_urls: list):
    # Iterate over the list of image URLs
    for i, url in enumerate(image_urls):
        print(url[1])
        print(f"Downloading image {i+1} from {url[1]}")
        image_data = await download_image(url[1])
        if image_data:
            filename = f"data/images/{url[0]}.jpg"  # You can customize the filename here
            await save_image(image_data, filename)

async def main():
    # List of image URLs to download and save
    image_urls = zip(data["id"], data["thumbnail_url"])
    
    # Download and save images asynchronously
    await download_and_save_images(image_urls)

# Run the async main function
asyncio.run(main())
