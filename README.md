## AI_Dermatologist

Here you can find the video of chatting with bot : https://youtu.be/2NlQAPhqjm0?si=aJhTxaT2sXmqtT89

Here, you can find the detailed video of how you can locally run it: https://youtu.be/8MHoD4GiaFc

Clone the repo: main.py,dermobuddy.py, requirements.txt, 

Create virtual env => pip install -r requirements.txt => run this command in terminal "textbase-client test", then give path to main.py, you will get a localhost URL => open it = CHAT!!
(add openai api key in dermobuddy.py)
*Welcome to AI_Dermatologist*

"
I am an expert assistant chatbot in dermatology trained by 'DermVisionAI'. I can assist you with your skin health related queries. I can provide information about skin care products, summarize skin care related YouTube videos, and answer any dermatology related questions you might have. I can also extract text from images of products to provide information about them.
"

#TechStack:
* Langchain frame work - Agents, Tools. Primarily used Agent for Function Calling
* EasyOCR for extracting text from images.
* DuckDuckGO API for fetching results from Internet.
* Youtube Transcript Loader for getting transcripts from youtube video(currently limited for the videos that have transcripts. Will Update the functionality to trascribe the text from youtube audio too).

#Usage
* User can ask any question related to dermatology. Bot will give you good guidance This bot won't give answer you outside this.
* User can also give image address(skin care product ingredients) from google. OCR tool is used to extract text => GPT for analysis => Final Answer for the query.
* User can ask to suggest any other products or any current events. This bot will use interent to answer you.
* User can paste the skin care related youtube video link, This bot can summarize the video content for you. 

#Future
* Will Use Llama 2 model instead of OpenAI models. I once tried with Llama 2, impressed with its results.
* I will scrap data like blogs, FAQs and make embeddings of them using openai ada model and store them in pinecone vector databse. Users can get most relevant answers for their queries by semantic search. - RAG.
* I will add TTS(Text2Speech), STT(Speech2Text) models in the bot. Users can talk to it.
* I will also implement youtube audio transcribing by using audio to text models, since currently this code will support only videos with transcripts.


#Local Testing
* [CHECK ABOVE]
