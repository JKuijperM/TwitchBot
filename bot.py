import os
from twitchio.ext import commands


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=os.environ['TMI_TOKEN'],
                         # client_id=os.environ['CLIENT_ID'],
                         nick=os.environ['BOT_NICK'],
                         prefix=os.environ['BOT_PREFIX'],
                         initial_channels=[os.environ['CHANNEL']])

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
        await bot.connected_channels[0].send('/me El brujero ha llegado!')

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return

        # Print the contents of our message to console...
        print(message.content)

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Send a hello back!
        await ctx.send('Hello world')


if __name__ == "__main__":
    bot = Bot()
    bot.run()

