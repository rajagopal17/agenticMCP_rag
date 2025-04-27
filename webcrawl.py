import asyncio
from crawl4ai import *
import os
from dotenv import load_dotenv
import asyncio
from google import genai



async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://economictimes.indiatimes.com/markets",
        )
        
        cresult = result.markdown

        # Load environment variables from .env file
        load_dotenv()

        # Access your API key and initialize Gemini client correctly
        api_key = os.getenv("GEMINI_API_KEY")
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents= f'''as a intelligent assistant summarize the following content in a concise and informative manner.
            on the context provided in the below text. 
             "\n\n" + "Context: " + str{cresult} + "\n\n" + "Answer:"
            
            '''
        )

        print(f"\nGemini Response: {response.text}")
        














if __name__ == "__main__":
    asyncio.run(main())