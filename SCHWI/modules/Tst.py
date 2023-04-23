import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SCHWI import app


async def search_find_anime_list(anime_name: str):
    
    query = '''
        query ($search: String) {
            Page {
                media(search: $search, type: ANIME) {
                    id
                    title {
                        romaji
                        english
                        native
                    }
                    episodes
                    duration
                    status
                    bannerImage
                }
            }
        }
    '''
    variables = {"search": anime_name}
    url = "https://graphql.anilist.co"
    response = requests.post(url, json={"query": query, "variables": variables})

   
    if response.status_code != 200:
        print("Api Error")
        return 
    
    data = response.json()["data"]
    anime_list = data["Page"]["media"]
    if not anime_list:
        print("Not Found")
        return

    banner_image = None
    if len(anime_list) == 1:
        banner_image = anime_list[0]["bannerImage"]
    else:
        banner_images = [anime["bannerImage"] for anime in anime_list if anime["bannerImage"]]
        if banner_images:
            banner_image = random.choice(banner_images)

    message_text = "TOP 4 SEARCH RESULTS:"
    buttons = []
    for i, anime in enumerate(anime_list[:4]):
        title = anime["title"]["english"] or anime["title"]["romaji"]
        anime_id = anime["id"]
        buttons.append([InlineKeyboardButton(f"🖥️{title}", callback_data=f"Anime_{anime_id}")])
        F_B = InlineKeyboardMarkup(buttons)
        return message_text, banner_image, F_B




@app.on_message(filters.command("len"))
async def kkk(client, message):
    H = message.chat.id
    args = message.text.split()
    if len(args) < 2:
        await message.reply_text("Please provide an anime name or ID after the command")
        return

    arg = args[1]
    if arg.isdigit():
        anime_id = int(arg)
        await message.reply_text(f"Id: {anime_id}")
    else:
        anime_name = arg
        message_text, banner_image, F_B = search_find_anime_list(anime_name, message)
        await app.send_photo(H, photo=banner_image, caption=message_text, reply_markup=F_B)



















@app.on_message(filters.command("anime"))
async def anime_search(client, message):

    args = message.text.split()
    if len(args) < 2:
        await message.reply_text("<b>Please provide an anime name or ID after the command.</b>")
        return

    arg = args[1]
    if arg.isdigit():
        try:
            anime_id = int(arg)
        except Exception as e:
            await message.reply_text(e)
        await message.reply_text(anime_id)
    else:
        try:
            anime_name = arg
        except Exception as e:
            await message.reply_text(e)
        await message.reply_text(anime_name)


















