from dotenv import load_dotenv
from agent import AIAgent
import os

load_dotenv()

def save_to_knowledge_base(query, text):
    os.makedirs("knowledge_base", exist_ok=True)
    filename = os.path.join("knowledge_base", f"{query}.txt")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    agent = AIAgent()
    query = input("Enter video topic/title: ").strip()

    title, transcript = agent.run(query)

    print("\n==============================")
    print("VIDEO TITLE:")
    print(title)
    print("\nTRANSCRIPT / SUMMARY:")
    print(transcript)
    print("==============================\n")

    save_to_knowledge_base(query, transcript)
    print("Transcript saved successfully.")
