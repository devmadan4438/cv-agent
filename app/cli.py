from app.core.logger import setup_logger
from app.services.chat_service.chat_service import ChatService


def start_cli():
    setup_logger()

    session_id = input("[Agent] > Please enter session id: ").strip()

    chat = ChatService()

    print("\nType 'exit' or 'quit' to leave.\n")

    while True:
        try:
            message = input("[You] > ").strip()

            if message.lower() in {"exit", "quit"}:
                print("[Agent] > Goodbye!")
                break

            if not message:
                continue

            print("[Agent] >", end=" ", flush=True)

            for chunk in chat.start_chat(
                session_id=session_id,
                message=message,
                mode="CLI",
            ):
                print(chunk, end="", flush=True)

            print("\n")

        except KeyboardInterrupt:
            print("\n[Agent] > Goodbye!")
            break

        except Exception as e:
            print(f"\n[Error] {e}\n")


if __name__ == "__main__":
    start_cli()