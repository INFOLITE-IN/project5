print("[INFO]: Importing Your API_ID, API_HASH, BOT_TOKEN")
import re
from asyncio import (gather, get_event_loop, sleep)

from aiohttp import ClientSession
from pyrogram import (Client, filters, idle)
from Python_ARQ import ARQ

from config import bot, BOT_TOKEN, ARQ_API_KEY, ARQ_API_BASE_URL, LANGUAGE
bot_token= BOT_TOKEN

print("[INFO]: Checking... Your Details")

bot_id = int(bot_token.split(":")[0])
print("[INFO]: Code running by master Prince Op")
arq = None


async def AngelQuery(query: str, user_id: int):
    query = (
        query
        if LANGUAGE == "en"
        else (await arq.translate(query, "en")).result.translatedText
    )
    resp = (await arq.Angel(query, user_id)).result
    return (
        resp
        if LANGUAGE == "en"
        else (
            await arq.translate(resp, LANGUAGE)
        ).result.translatedText
    )


async def type_and_send(message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else 0
    query = message.text.strip()
    await message._client.send_chat_action(chat_id, "typing")
    response, _ = await gather(AngelQuery(query, user_id), sleep(2))
    if "Luna" in response:
        responsee = response.replace("Angel", "Social")
    else:
        responsee = response
    if "Aco" in responsee:
        responsess = responsee.replace("Aco", "Angel")
    else:
        responsess = responsee
    if "Who is Angel?" in responsess:
        responsess2 = responsess.replace("Who is Angel?", "Heroine Of Telegram")
    else:
        responsess2 = responsess
    await message.reply_text(responsess2)
    await message._client.send_chat_action(chat_id, "cancel")


@bot.on_message(
    ~filters.private
    & filters.text
    & ~filters.command("start")
    & ~filters.edited,
    group=69,
)
async def chat(_, message):
    if message.reply_to_message:
        if not message.reply_to_message.from_user:
            return
        from_user_id = message.reply_to_message.from_user.id
        if from_user_id != bot_id:
            return
    else:
        match = re.search(
            "[.|\n]{0,}iris[.|\n]{0,}",
            message.text.strip(),
            flags=re.IGNORECASE,
        )
        if not match:
            return
    await type_and_send(message)


@bot.on_message(
    filters.private
    & ~filters.command("start")
    & ~filters.edited
)
async def chatpm(_, message):
    if not message.text:
        await message.reply_text("Ufff... Ignoring .... ¯\_(ツ)_/¯")
        return
    await type_and_send(message)


@bot.on_message(filters.command("start") & ~filters.edited)
async def startt(_, message):
    await message.reply_text("
𝙸'𝚊𝚖 𝙰𝚗𝚐𝚎𝚕, 𝙼𝚊𝚌𝚑𝚒𝚗𝚎 𝙻𝚎𝚊𝚛𝚗𝚒𝚗𝚐 𝙲𝚑𝚊𝚝 𝙱𝚘𝚝
𝚝𝚑𝚊𝚝 𝚌𝚊𝚗 𝚝𝚊𝚕𝚔 𝚊𝚋𝚘𝚞𝚝 𝚊𝚗𝚢 𝚝𝚘𝚙𝚒𝚌 𝚒𝚗 𝚊𝚗𝚢 𝚀𝚞𝚎𝚜𝚝𝚒𝚘𝚗𝚜.
")


async def main():
    global arq
    session = ClientSession()
    arq = ARQ(ARQ_API_BASE_URL, ARQ_API_KEY, session)

    await bot.start()
    print(
        """
Your AngelChatBot Is Deployed Successfully.
"""
    )
    await idle()


loop = get_event_loop()
loop.run_until_complete(main())
