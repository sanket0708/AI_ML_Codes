from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

model = ChatMistralAI(
    model="mistral-small-2603",
    temperature=0.8
)

MODES = {
    "😡 Angry": "You are an angry AI agent.",
    "😂 Funny": "You are a funny AI agent.",
    "😢 Sad": "You are a sad AI agent."
}


def initialize_messages(mode):
    return [
        SystemMessage(content=MODES[mode])
    ]


def get_response(messages, prompt):
    messages.append(HumanMessage(content=prompt))

    response = model.invoke(messages)

    messages.append(AIMessage(content=response.content))

    return response.content