from workers import WorkerEntrypoint, Response
from js import fetch
import json


class Default(WorkerEntrypoint):
    async def fetch(self, request):

        # Browser থেকে খুললে
        if request.method == "GET":
            return Response("TAIEF Market Bot is running!")

        # Telegram webhook শুধু POST পাঠাবে
        if request.method != "POST":
            return Response("Method Not Allowed", status=405)

        try:
            update = await request.json()

            message = update.get("message", {})
            chat = message.get("chat", {})
            text = message.get("text", "")

            # /start command
            if text == "/start":
                chat_id = chat.get("id")

                if chat_id:
                    data = {
                        "chat_id": chat_id,
                        "text": "👋 স্বাগতম!\n\n🛒 TAIEF Market Bot চালু হয়েছে।"
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
            return Response(
                "Error: " + str(e),
                status=500
            )
