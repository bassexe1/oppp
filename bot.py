import discord
from discord.ext import commands
import os

# Configuración del bot
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} está listo y conectado.")

# Comando simple
@bot.command()
async def hola(ctx):
    await ctx.send("¡Hola! Soy tu bot.")

# Comando para probar el ping
@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! Latencia: {round(bot.latency * 1000)}ms")

# Manejo de errores (opcional)
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"Ocurrió un error: {str(error)}")

# Iniciar el bot
if __name__ == "__main__":
    TOKEN = os.getenv("MTMzMzYzNjE4NDM2MjE5MjkyNg.Giq0dO.FykU7_MWILaZI4N9qgd34UCxcptJp7TzMTUyj8")  # Define la variable de entorno en GitHub
    if TOKEN:
        bot.run(TOKEN)
    else:
        print("Error: No se encontró el token en las variables de entorno.")
