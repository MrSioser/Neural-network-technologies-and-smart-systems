import os
import argparse
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown
from openai import OpenAI

def main():
    load_dotenv()
    console = Console()

    parser = argparse.ArgumentParser(description="CLI для локального LM Studio (OpenAI-compatible).")
    parser.add_argument("--system", "-s", type=str, default="Ти AI-асистент, відповідай українською.",
                        help="System prompt для моделі.")
    parser.add_argument("--temperature", "-t", type=float, default=0.4, help="Креативність відповіді (0.0-1.0).")
    parser.add_argument("--max-tokens", "-m", type=int, default=512, help="Максимум токенів у відповіді.")
    parser.add_argument("--model", "-mod", type=str, default="local-model", help="Назва моделі.")
    args = parser.parse_args()

    load_dotenv()
    base_url = os.environ["OPENAI_BASE_URL"]
    api_key = os.environ["OPENAI_API_KEY"]

    client = OpenAI(base_url=base_url, api_key=api_key)
    console.print("[bold cyan]🔹 Підключення до LM Studio...[/bold cyan]")
    console.print(f"URL: {base_url}\nМодель: {args.model}\n")

    messages = [{"role": "system", "content": args.system}]
    console.print("[bold green]💬 Введи свій запит (напиши 'exit' щоб вийти)[/bold green]")

    while True:
        user_input = input("\n🧠 Ти: ").strip()
        if user_input.lower() in ["exit", "quit", "вихід"]:
            console.print("\n👋 Завершую діалог.")
            break

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model=args.model,
            messages=messages,
            temperature=args.temperature,
            max_tokens=args.max_tokens
        )

        answer = response.choices[0].message.content
        messages.append({"role": "assistant", "content": answer})

        console.rule("[bold yellow]Відповідь моделі")
        console.print(Markdown(answer))
        console.rule()

        logs_path = Path("logs")
        logs_path.mkdir(exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = logs_path / f"dialog_{ts}.md"

        with open(log_file, "w", encoding="utf-8") as f:
            f.write(f"# Діалог {ts}\n\n")
            for msg in messages:
                role = "👤 Користувач" if msg["role"] == "user" else "🤖 Модель" if msg["role"] == "assistant" else "⚙️ Система"
                f.write(f"**{role}:**\n{msg['content']}\n\n")

        console.print(f"[dim] Діалог збережено: {log_file}[/dim]")

if __name__ == "__main__":
    main()
