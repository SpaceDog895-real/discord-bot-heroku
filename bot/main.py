import discord
import os
from discord.ext import commands, tasks

dateList = [
    ["Doge-o-Ween", 10, 1, 0, "All of October", "Event"],
    ["Dogemas", 12, 1, 0, "All of December", "Event"],
    ["Nicky's Luck Event", 3, 1, 0, "All of March", "Event"],
    ["DJ's Easter Event", 4, 1, 0, "All of April", "Event"],
    ["Cinco De Mayo Doge", 5, 5, 0, "24 Hours", "Doge"],
    ["Soldier Doge", 5, 26, 0, "24 Hours", "Doge"],
    ["Pride Doge", 6, 1, 0, "All of June", "Doge"],
    ["Firework Doge", 7, 4, 0, "24 Hours", "Doge"],
    ["Dog Doge", 8, 26, 0, "24 Hours", "Doge"],
    ["Christmas Doge", 12, 25, 0, "24 Hours", "Doge"],
    ["Halloween Doge", 11, 31, 0, "24 Hours", "Doge"],
    ["St. Patrick's Doge", 3, 17, 0, "24 Hours", "Doge"],
    ["Easter Doge", 4, 20, 0, "24 Hours", "Doge"],
    ["Walter Doge", 4, 1, 0, "24 Hours", "Doge"],
    ["Thanksgiving Doge", 11, 27, 0, "24 Hours", "Doge"], 
]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)


class Looper(commands.Cog):
    def __init__(self, bot):
        self.printer.start()

    @tasks.loop(seconds=10.0)
    async def printer(self):
        channel = bot.get_channel(972907643595284590)

        now = discord.utils.utcnow()
        currentYear = int(now.strftime("%Y"))
        currentMonth = int(now.strftime("%m"))
        currentDay = int(now.strftime("%d"))

        for data in dateList:
            thisMonth = data[1]
            thisDay = data[2]

            if thisMonth == currentMonth and thisDay == currentDay and currentYear != data[3]:
                data[3] = currentYear

                embed = discord.Embed(
                    title = "New Limited-Time " + data[5] + "!",
                    color = 0xFFFF00,
                )

                embed.add_field(name = data[5], value = data[0], inline = True)
                embed.add_field(name = "Duration", value = data[4], inline = True)

                await channel.send(embed=embed)


@bot.event
async def on_ready():
    print("bot is a go")
    
    embed = discord.Embed(
        title = "Event Notifier is now online!",
        description = "Notifications will be sent when limited-time Events and Doges are available.",
        color = 0xFFFF00,
    )

    channel = bot.get_channel(972907643595284590)
    await channel.send(embed=embed)
    await bot.add_cog(Looper(bot))

if __name__ == '__main__':
    bot.run(os.getenv('DISCORD_TOKEN'))
