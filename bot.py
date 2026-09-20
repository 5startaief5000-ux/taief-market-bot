from workers import WorkerEntrypoint, Response
from js import fetch
import json


class Default(WorkerEntrypoint):
    async def fetch(self, request):
        if request.method == "GET":
            return Response("TAIEF Market Bot is running!")

        if request.method != "POST":
            return Response("Method not allowed", status=405)

        try:
            update = await request.json()

            message = update.get("message", {})
            chat = message.get("chat", {})
            text = message.get("text", "")

            if text == "/start":
                chat_id = chat.get("id")

                data = {
                    "chat_id": chat_id,
                    ld
                    if __name__ == "__main__":
    main()
                    ext": "👋 স্বাগতম!\n\nTAIEF Market Bot চালু হয়েছে।"
                }

                token = self.env.BOT_TOKEN

                await fetch(
                    f"https://api.telegram.org/bot{token}/sendMessage",
                    {
                        "method": "POST",
                        "headers": {
                            "Content-Type": "application/json"
                        },
                        "body": json.dumps(data)
                    }
                )

            return Response("OK")

        except Exception as e:
            return Response("Error: " + str(e), status=500)ld
