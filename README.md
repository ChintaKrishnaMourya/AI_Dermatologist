## AI_Dermatologist

Welcome to AI_Dermatologist.

"
I am an expert assistant chatbot in dermatology trained by 'DermVisionAI'. I can assist you with your skin health related queries. I can provide information about skin care products, summarize skin care related YouTube videos, and answer any dermatology related questions you might have. I can also extract text from images of products to provide information about them.
"

#TechStack:
* Langchain frame work - Agents, Tools. Primarily used Agent for Function Calling
* EasyOCR for extracting text from images.
* DuckDuckGO API for fetching results from Internet.
* Youtube Transcript Loader for getting transcripts from youtube video(currently limited for the videos that have transcripts. Will Update the functionality to trascribe the text from youtube audio too).

#Usage
* User can ask any question related to dermatology. This bot won't give answer you outside this.
* User can also give image address(skin care product ingredients) from google. OCR tool is used to extract text => GPT for analysis => Final Answer for the query.
* User can ask to suggest any other products or any current events. This bot will use interent to answer you.
* User can paste the skin care related youtube video link, This bot can summarize the video content for you. 

#Future
* Will Use Llama 2 model instead of OpenAI models. I once tried with Llama 2, impressed with its results.

#Local Testing
* Clone the Repo, install requirements, run textbase-client test, give path to main.py
