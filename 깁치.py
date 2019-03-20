import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print("로그인")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    await client.change_presence(game=discord.Game(name='닭작가 먹는중', type=1))
     

@client.event
async def on_message(message):
    if message.content.startswith("깁치야 안녕"):
        await client.send_message(message.channel, "안녕! 난 깁치봇이야! 심심할땐 나랑 놀면돼!")
    if message.content.startswith("깁치야 뭐해"):
        await client.send_message(message.channel, "그냥 놀아")
    if message.content.startswith("깁치야 넌 누구야"):
        await client.send_message(message.channel, "나도 몰라")
    if message.content.startswith("깁치야 오랜만"):
        await client.send_message(message.channel, "미안한데 난 너 몰라")
    if message.content.startswith("깁치야 아야나는?"):
        await client.send_message(message.channel, "겁나 못생긴 노래봇!!")
    if message.content.startswith("깁치야 미육이는?"):
        await client.send_message(message.channel, "디코최강 천재")
    if message.content.startswith("깁치야 그루비는?"):
        await client.send_message(message.channel, "세계최강 음질!!")
    if message.content.startswith("깁치야 닭작가는?"):
        await client.send_message(message.channel, "(?)")
    if message.content.startswith("깁치야 너는"):
        await client.send_message(message.channel, "에뿌리 뽜리 쒜마뉌!!")
    if message.content.startswith("깁치야 닥쳐"):
        await client.send_message(message.channel, "죄송합니다")
    if message.content.startswith("시발련아"):
        await client.send_message(message.channel, "왜그러세요 ㅠㅠ")
    if message.content.startswith("깁치야 도움"):
        await client.send_message(message.channel, "깁치야 (안녕,뭐해,넌 누구야,오랜만,아야나는?,미육이는?,그루비는?,닭작가는?,너는,닥쳐,시발련아")
    if message.content.startswith("깁치야 주사위"):
        roll = message.content.split(" ")
        rolld = roll[1].split("d")
        dice = 0
        for i in range(1, int(rolld[0])+1):
            dice = dice + random.randint(1, int(rolld[1]))
        await client.send_message(message.channel, str(dice))



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
