from fileinput import filename
import os
import disnake
from disnake.ext import commands
from PIL import Image
import requests
from io import BytesIO
from moviepy.editor import VideoFileClip
from dotenv import load_dotenv

load_dotenv()


client = commands.Bot()

@client.slash_command(name="ping", description="checks if the bot is available")
async def ping(ctx):
    await ctx.send("pong", ephemeral=False)

@client.slash_command(name="dogdoing", description="WHAT the dog doing (attach an image please)")
async def dogdoing(ctx, image_url):
    await ctx.send("Processing input... (I'm not esmbot, but this kinda may take a while) <:magago:1000115411372752966>")
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img = img.resize((180,204))
    dogimg = Image.open("./res/dog.png")
    dogimg.paste(img, (327, 304))
    with BytesIO() as image_binary:
        dogimg.save(image_binary, 'PNG')
        image_binary.seek(0)
        await ctx.send(file=disnake.File(fp=image_binary, filename='image.png'))

@client.slash_command(name="mp4togif", description="converts mp4 to gif")
async def mp4togif(ctx, video_url):
    await ctx.send("Processing input... (I'm not esmbot, but this kinda may take a while) <:magago:1000115411372752966>")
    response = requests.get(video_url).content
    with open('output/togif.mp4', 'wb') as handler:
        handler.write(response)
        clip = VideoFileClip("output/togif.mp4").resize(0.5)
        clip.write_gif("output/togif.gif", fps=clip.fps/1.5, program="ffmpeg", )
        with open("output/togif.gif", "rb") as g:
            await ctx.send("content", file=disnake.File("output/togif.gif"))


client.run(os.getenv("TOKEN"))