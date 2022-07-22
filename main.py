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

#check if the bot is working
@client.slash_command(name="ping", description="checks if the bot is available")
async def ping(ctx):
    await ctx.send("pong", ephemeral=False)

input_processing_message = "Processing input... <:magago:1000115411372752966>"

#what the dog doing
@client.slash_command(name="dogdoing", description="WHAT the dog doing (attach an image please)")
async def dogdoing(ctx, image_url):
    await ctx.send(input_processing_message)
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img = img.resize((180,204))
    dogimg = Image.open("./res/dog.png")
    dogimg.paste(img, (327, 304))
    with BytesIO() as image_binary:
        dogimg.save(image_binary, 'PNG')
        image_binary.seek(0)
        await ctx.send(file=disnake.File(fp=image_binary, filename='image.png'))

#kanye west
@client.slash_command(name="kanyewest", description="kanye west doing funny stuff")
async def kanyewest(ctx, image_url):
    await ctx.send(input_processing_message)
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img = img.resize((174,164))
    kanyeimg = Image.open("res/kanyewest.png")
    kanyeimg.paste(img, (240,395))
    with BytesIO() as image_binary:
        kanyeimg.save(image_binary, 'PNG')
        image_binary.seek(0)
        await ctx.send(file=disnake.File(fp=image_binary, filename='image.png'))

#mp4 to gif
@client.slash_command(name="mp4togif", description="converts mp4 to gif")
async def mp4togif(ctx, video_url):
    try:
        await ctx.send(input_processing_message)
        response = requests.get(video_url).content
        with open('output/togif.mp4', 'wb') as handler:
            handler.write(response)
            clip = VideoFileClip("output/togif.mp4").resize(0.35)
            clip.write_gif("output/togif.gif", fps=clip.fps/1.5, program="ffmpeg", )
            with open("output/togif.gif", "rb") as g:
                await ctx.send("content", file=disnake.File("output/togif.gif"))
    except:
        await ctx.send("Error while processing file input or sending output")



#runs the bot
client.run(os.getenv("TOKEN"))