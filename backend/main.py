from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chatbot import chat, client_searchtest, MODEL_ID, types

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    prompt: str

@app.post("/chat")
async def chat_endpoint(data: PromptRequest):
    prompt = data.prompt

    system_instruction_searchtest = """
    Analyze the input prompt and determine whether it requires a Google search...
    Respond with only one of the following two words:
    "SEARCH" or "GK"
    """

    response_search = client_searchtest.models.generate_content(
        model=MODEL_ID,
        config=types.GenerateContentConfig(system_instruction=system_instruction_searchtest),
        contents=prompt
    )

    if response_search.text.strip() == "SEARCH":
        prompt = "SEARCH : " + prompt

    response = chat.send_message(prompt)

    if response.candidates and response.candidates[0].content.parts:
        text = ''.join(part.text for part in response.candidates[0].content.parts)
    else:
        text = "No valid response"

    return {"reply": text}
