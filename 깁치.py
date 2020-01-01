import discord
from captcha.image import ImageCaptcha
import random

client = discord.Client()


@client.event
async def on_ready():
    print("로그인")
    print(client.user.name)
    print("ID:")
    print(client.user.id)
    print("------------------") 

@client.event
async def on_message(message):
    if message.content.startswith("꼬추"):
        await message.channel.send("음란성 발언은 자제해주세요. (경고 1회)")
    if message.content.startswith("의사양반"):
        await message.channel.send("음란성 발언은 자제해주세요. (경고 1회)")
    if message.content.startswith("안녕하세요"):
        await message.channel.send("안녕하십니까? 저는 여러분들의 도우미, VB입니다!")
    if message.content.startswith("씨발"):
        await message.channel.send("욕설은 자제해주시기 바랍니다.")
    if message.content.startswith("시발"):
        await message.channel.send("욕설은 자제해주시기 바랍니다.")
    if message.content.startswith("tlqkf"):
        await message.channel.send("욕설은 자제해주시기 바랍니다.")
    if message.content.startswith("샤발"):
        await message.channel.send("욕설은 자제해주시기 바랍니다.")
    if message.content.startswith("시1발"):
        await message.channel.send("욕설은 자제해주시기 바랍니다.")
    if message.content.startswith("시2발"):
        await message.channel.send("욕설은 자제해주시기 바랍니다.")
    if message.content.startswith("시22발"):
        await message.channel.send("욕설은 자제해주시기 바랍니다.")
    if message.content.startswith("ㅅㅂ"):
        await message.channel.send("욕설은 자제해주시기 바랍니다.")
    if message.content.startswith("sibal"):
        await message.channel.send("욕설은 자제해주시기 바랍니다.")
    if message.content.startswith("슈발"):
        await message.channel.send("욕설은 자제해주시기 바랍니다.")
    if message.content.startswith("개새끼"):
        await message.channel.send("욕설은 자제해주시기 바랍니다.")
    if message.content.startswith("새끼"):
        await message.channel.send("욕설은 자제해주시기 바랍니다.")
    if message.content.startswith("개샊"):
        await message.channel.send("욕설은 자제해주시기 바랍니다.")
    if message.content.startswith("지랄"):
        await message.channel.send("욕설은 자제해주시기 바랍니다.")
    if message.content.startswith("미친"):
        await message.channel.send("욕설은 자제해주시기 바랍니다.")
    if message.content.startswith("와 샌즈"):
        await message.channel.send("욕설은 자제해주시기 바랍니다.")
    if message.content.startswith("뒤졌다"):
        await message.channel.send("욕설은 자제해주시기 바랍니다.")
    if message.content.startswith("뒤짐"):
        await message.channel.send("욕설은 자제해주시기 바랍니다.")
    if message.content.startswith("김두한"):
        await message.channel.send("욕설은 자제해주시기 바랍니다.")
    if message.content.startswith("시바"):
        await message.channel.send("욕설은 자제해주시기 바랍니다.")
    if message.content.startswith("1972년 11월 21일"):
        await message.channel.send("에엑따♂")
    if message.content.startswith("!인증"):
        Image_captcha = ImageCaptcha()
        msg = ""
        a = ""
        for i in range(6):
            a += str(random.randint(0, 9))
        name = str(message.author.id) + ".png"
        Image_captcha.write(a, name)
        await message.channel.send(file=discord.File(name))
        def check(msg):
            return msg.author == message.author and msg.channel == message.channel
        try:
            msg = await client.wait_for("message", timeout=10, check=check)
        except:
            await message.channel.send("``인증에 실패하였습니다. (대기 시간이 초과되었습니다.)``")
            return
        if msg.content == a:
            await message.channel.send("``코드가 일치합니다.``")
            await message.channel.send("``인증 완료! -사전예약 보상- 사전예약 상자가 지급되었습니다.``")
        else:
            await message.channel.send("``인증에 실패하였습니다. (사유:코드 불일치)``")
    if message.content.startswith("!ver"):
        Image_captcha = ImageCaptcha()
        msg = ""
        a = ""
        for i in range(6):
            a += str(random.randint(0, 9))
        name = str(message.author.id) + ".png"
        Image_captcha.write(a, name)
        await message.channel.send(file=discord.File(name))
        def check(msg):
            return msg.author == message.author and msg.channel == message.channel
        try:
            msg = await client.wait_for("message", timeout=10, check=check)
        except:
            await message.channel.send("``인증에 실패하였습니다. (대기 시간이 초과되었습니다.)``")
            return
        if msg.content == a:
            await message.channel.send("``코드가 일치합니다.``")
            await message.channel.send("``인증 완료! -사전예약 보상- 사전예약 상자가 지급되었습니다.``")
        else:
            await message.channel.send("``인증에 실패하였습니다. (사유:코드 불일치)``")
client.run('NTU2NjYwMjc0MzgwNDA2ODA1.Xggq6w.c3Llr_uSVrIgPFvCJ2X5XY74CFc')
