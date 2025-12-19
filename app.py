import gradio as gr
from state import LearningState
from pdf_utils import load_pdf
from agents import *

state = LearningState()

def upload_pdf(file):
    global state
    state.sections = load_pdf(file.name)
    state.paper_title = file.name
    return f"Loaded {len(state.sections)} sections."

def chat(user_input, history):
    global state

    if history is None:
        history = []

    action = teaching_orchestrator(state, user_input)

    if action == "overview":
        response = overview_agent(state)
    elif action == "explain":
        response = explain_agent(state, user_input)
    elif action == "quiz":
        response = quiz_agent(state)
    else:
        response = "Can you clarify what you want to learn?"

    history.append({"role": "user", "content": user_input})
    history.append({"role": "assistant", "content": response})

    return history

with gr.Blocks() as demo:
    gr.Markdown("# 📄 Paper Tutor Agent")

    pdf = gr.File(file_types=[".pdf"])
    status = gr.Textbox(interactive=False)
    pdf.upload(upload_pdf, pdf, status)

    chatbot = gr.Chatbot()
    msg = gr.Textbox(placeholder="Ask for overview, explanation, or quiz")
    send = gr.Button("Send")

    send.click(chat, [msg, chatbot], chatbot)

demo.launch()