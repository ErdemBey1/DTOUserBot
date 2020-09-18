# Copyright (C) 2020 TeamDerUntergang.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# Created by @thisisulvis
#
# for DTÖ UserBot

""" İnsanlarla əylənmək üçün hazırlanmış UserBot modulu """

from asyncio import sleep
from random import choice, getrandbits, randint
from re import sub
import time
import asyncio

from collections import deque

import requests

from cowpy import cow

from userbot import CMD_HELP, ZALG_LIST
from userbot.events import register
from userbot.modules.admin import get_user_from_event

# ================= CONSTANT =================
EMOJIS = [
    "😂",
    "😂",
    "👌",
    "✌",
    "💞",
    "👍",
    "👌",
    "💯",
    "🎶",
    "👀",
    "😂",
    "👓",
    "👏",
    "👐",
    "🍕",
    "💥",
    "🍴",
    "💦",
    "💦",
    "🍑",
    "🍆",
    "😩",
    "😏",
    "👉👌",
    "👀",
    "👅",
    "😩",
    "🚰",
]

UWUS = [
    "(・`ω´・)",
    ";;w;;",
    "owo",
    "UwU",
    ">w<",
    "^w^",
    r"\(^o\) (/o^)/",
    "( ^ _ ^)∠☆",
    "(ô_ô)",
    "~:o",
    ";-;",
    "(*^*)",
    "(>_",
    "(♥_♥)",
    "*(^O^)*",
    "((+_+))",
]

FACEREACTS = [
    "ʘ‿ʘ",
    "ヾ(-_- )ゞ",
    "(っ˘ڡ˘ς)",
    "(´ж｀ς)",
    "( ಠ ʖ̯ ಠ)",
    "(° ͜ʖ͡°)╭∩╮",
    "(ᵟຶ︵ ᵟຶ)",
    "(งツ)ว",
    "ʚ(•｀",
    "(っ▀¯▀)つ",
    "(◠﹏◠)",
    "( ͡ಠ ʖ̯ ͡ಠ)",
    "( ఠ ͟ʖ ఠ)",
    "(∩｀-´)⊃━☆ﾟ.*･｡ﾟ",
    "(⊃｡•́‿•̀｡)⊃",
    "(._.)",
    "{•̃_•̃}",
    "(ᵔᴥᵔ)",
    "♨_♨",
    "⥀.⥀",
    "ح˚௰˚づ ",
    "(҂◡_◡)",
    "ƪ(ړײ)‎ƪ​​",
    "(っ•́｡•́)♪♬",
    "◖ᵔᴥᵔ◗ ♪ ♫ ",
    "(☞ﾟヮﾟ)☞",
    "[¬º-°]¬",
    "(Ծ‸ Ծ)",
    "(•̀ᴗ•́)و ̑̑",
    "ヾ(´〇`)ﾉ♪♪♪",
    "(ง'̀-'́)ง",
    "ლ(•́•́ლ)",
    "ʕ •́؈•̀ ₎",
    "♪♪ ヽ(ˇ∀ˇ )ゞ",
    "щ（ﾟДﾟщ）",
    "( ˇ෴ˇ )",
    "눈_눈",
    "(๑•́ ₃ •̀๑) ",
    "( ˘ ³˘)♥ ",
    "ԅ(≖‿≖ԅ)",
    "♥‿♥",
    "◔_◔",
    "⁽⁽ଘ( ˊᵕˋ )ଓ⁾⁾",
    "乁( ◔ ౪◔)「      ┑(￣Д ￣)┍",
    "( ఠൠఠ )ﾉ",
    "٩(๏_๏)۶",
    "┌(ㆆ㉨ㆆ)ʃ",
    "ఠ_ఠ",
    "(づ｡◕‿‿◕｡)づ",
    "(ノಠ ∩ಠ)ノ彡( \\o°o)\\",
    "“ヽ(´▽｀)ノ”",
    "༼ ༎ຶ ෴ ༎ຶ༽",
    "｡ﾟ( ﾟஇ‸இﾟ)ﾟ｡",
    "(づ￣ ³￣)づ",
    "(⊙.☉)7",
    "ᕕ( ᐛ )ᕗ",
    "t(-_-t)",
    "(ಥ⌣ಥ)",
    "ヽ༼ ಠ益ಠ ༽ﾉ",
    "༼∵༽ ༼⍨༽ ༼⍢༽ ༼⍤༽",
    "ミ●﹏☉ミ",
    "(⊙_◎)",
    "¿ⓧ_ⓧﮌ",
    "ಠ_ಠ",
    "(´･_･`)",
    "ᕦ(ò_óˇ)ᕤ",
    "⊙﹏⊙",
    "(╯°□°）╯︵ ┻━┻",
    r"¯\_(⊙︿⊙)_/¯",
    "٩◔̯◔۶",
    "°‿‿°",
    "ᕙ(⇀‸↼‶)ᕗ",
    "⊂(◉‿◉)つ",
    "V•ᴥ•V",
    "q(❂‿❂)p",
    "ಥ_ಥ",
    "ฅ^•ﻌ•^ฅ",
    "ಥ﹏ಥ",
    "（ ^_^）o自自o（^_^ ）",
    "ಠ‿ಠ",
    "ヽ(´▽`)/",
    "ᵒᴥᵒ#",
    "( ͡° ͜ʖ ͡°)",
    "┬─┬﻿ ノ( ゜-゜ノ)",
    "ヽ(´ー｀)ノ",
    "☜(⌒▽⌒)☞",
    "ε=ε=ε=┌(;*´Д`)ﾉ",
    "(╬ ಠ益ಠ)",
    "┬─┬⃰͡ (ᵔᵕᵔ͜ )",
    "┻━┻ ︵ヽ(`Д´)ﾉ︵﻿ ┻━┻",
    r"¯\_(ツ)_/¯",
    "ʕᵔᴥᵔʔ",
    "(`･ω･´)",
    "ʕ•ᴥ•ʔ",
    "ლ(｀ー´ლ)",
    "ʕʘ̅͜ʘ̅ʔ",
    "（　ﾟДﾟ）",
    r"¯\(°_o)/¯",
    "(｡◕‿◕｡)",
]

RUNS_STR = [
    "Hey! Hara gedirsən?",
    "Ha? Nə? Qaçdılar ?",
    "ZZzzZZzz... Noldu? oh, yenə onlarimiş, boş ver.",
    "Geri gəl!",
    "Qaçın OneBot gəlir !!",
    "Divara diqqət elə !",
    "Məni onlarnan tək saxlama !!",
    "Qaçsan, ölərsən.",
    "Ay səni zarafatcııl, mən hər yerdəyəm.",
    "Bunu elədiyivə görə peşman olacağsan...",
    "/kickme butonunu da yoxlaya bilərsən, əyləncəli olduğunu söyləyirlər.",
    "Get başqa birini narahat elə, burda heçkimin vecinə deyilsən.",
    "Qaça bilərsən amma gizlənə bilməzsən.",
    "Eləyəbildiklərin elə bu qədərdi ?",
    "Arxandayam...",
    "Qonağların var!",
    "Bunu asan yoldan edə biləriy, yada çətin yoldan.",
    "Başa düşmürsən, elə mi?",
    "Haha, qaçsan yaxşı olar.!",
    "Zəhmət olmasa, xatırlat mənə nə qədər veciməsən?",
    "Sənin yerində olsam daha da sürətli qaçardım.",
    "Bu tamamiylə axtardığımız robotdu.",
    "Bəlkə bəxt sənə gülər.",
    "Tanınmış son sözlər.",
    "Və sonsuza qədər itkin düşdülər, heç görunmədilər.",
    "\"Hey, mənə baxın ! Bottan qaça bilirəm çox əlayam!\" - bu adam",
    "Bəli bəli, /kickme butonuna indidən bas.",
    "Baxın, bu üzüyü alın və Mordor'a gedin.",
    "Əfsanəyə görə onlar hələ də işləyir...",
    "Harry Potter'ın əksinə, valideyinlərin səni məndən qoruya bilməz.",
    "Qorxu əsəbə, əsəb nifrətə, nifrət acıya yol açar. Qorxu içində qaçmaya davam eləsən,"
    "bir sonraki Vader sən olabilərsən.",
    "Birdən çox hesablama edildikdən sonra, dalaverelerine olan marağımın tam olarağ 0’a bərabər olduğuna qərar verdim.",
    "Əfsanəyə görə onlar hələ də işləyir.",
    "Davam elə, səni burda istədiyimizə əmin deyiləm.",
    "Sən bir sihirb- Oh. Gözlə. Sen Harry deyilsən, davam elə.",
    "KARİDORDA QAÇMAYIN!",
    "Görüşəriy bəbəyim.",
    "Kim itləri buraxdı ?",
    "Gülməlidi çünkü heçkimin vecinə deyil.",
    "Ah, nə böyük itki. Bu səfərkini sevmişdim.",
    "Açığı canım, vecimə deyil.",
    "Südüm bütün oğlanları avluya çəkir... Biraz da bərk qaç!",
    "Doğruları qaldıra BİLMƏZSƏN!",
    "Keçmiş zamanlarda, çox çox uzağ bir qalaksidə kimsə vecinə ala bilərdi. Amma artığ ele deyil.",
    "Hey, onlara bax! Qaçınılmaz banhammer'dən qaçırlar... Nə qədər də şirin.",
    "Han əvvəl vuruldu. Mən də elə edəcəm",
    "Ağ dovşanın, arxasında nə edirsən ?",
    "Həkimin də söylədiyi kimi... QAÇ!",
]

HELLOSTR = [
    "Salamm!",
    "‘Nə var nə yox Müdür!",
    "Necəsən’?",
    "‘Hey Nə baş verir?",
    "Salam, salam, salam!",
    "Salamm, kim var orda?, Mən danışıram.",
    "Bunun kim olduğunu bilirsən",
    "Hey Yo!",
    "Nə var nə yox.",
    "Salamlar və salamlar !",
    "Salam, günişığı!",
    "Hey, nə var nə yox, salam!",
    "Necə gedir’, balaca civciv?",
    "Ce-e!",
    "Necəsən-doody!",
    "Salam, birinci sinif küçüyü!",
    "Barışağ!",
    "Salam, dostum!",
    "S-salam!",
]

SHGS = [
    "┐(´д｀)┌",
    "┐(´～｀)┌",
    "┐(´ー｀)┌",
    "┐(￣ヘ￣)┌",
    "╮(╯∀╰)╭",
    "╮(╯_╰)╭",
    "┐(´д`)┌",
    "┐(´∀｀)┌",
    "ʅ(́◡◝)ʃ",
    "┐(ﾟ～ﾟ)┌",
    "┐('д')┌",
    "┐(‘～`;)┌",
    "ヘ(´－｀;)ヘ",
    "┐( -“-)┌",
    "ʅ（´◔౪◔）ʃ",
    "ヽ(゜～゜o)ノ",
    "ヽ(~～~ )ノ",
    "┐(~ー~;)┌",
    "┐(-。ー;)┌",
    r"¯\_(ツ)_/¯",
    r"¯\_(⊙_ʖ⊙)_/¯",
    r"¯\_༼ ಥ ‿ ಥ ༽_/¯",
    "乁( ⁰͡  Ĺ̯ ⁰͡ ) ㄏ",
]

CRI = [
    "أ‿أ",
    "╥﹏╥",
    "(;﹏;)",
    "(ToT)",
    "(┳Д┳)",
    "(ಥ﹏ಥ)",
    "（；へ：）",
    "(T＿T)",
    "（πーπ）",
    "(Ｔ▽Ｔ)",
    "(⋟﹏⋞)",
    "（ｉДｉ）",
    "(´Д⊂ヽ",
    "(;Д;)",
    "（>﹏<）",
    "(TдT)",
    "(つ﹏⊂)",
    "༼☯﹏☯༽",
    "(ノ﹏ヽ)",
    "(ノAヽ)",
    "(╥_╥)",
    "(T⌓T)",
    "(༎ຶ⌑༎ຶ)",
    "(☍﹏⁰)｡",
    "(ಥ_ʖಥ)",
    "(つд⊂)",
    "(≖͞_≖̥)",
    "(இ﹏இ`｡)",
    "༼ಢ_ಢ༽",
    "༼ ༎ຶ ෴ ༎ຶ༽",
]

SLAP_TEMPLATES = [
    "{victim} istifadəçisini {item} ilə {hits} .",
    "{victim} istifadəçisini {item} ilə üzünə {hits} .",
    "{victim} istifadəçisini {item} ilə biraz {hits} .",
    "{victim} istifadəçisinə {item} {throws} .",
    "{victim} istifadəçisini {item} ilə üzünə {throws} .",
    "{victim} istifadəçisinə tərəf {item} atır.",
    "{victim} axmaqına {item} ilə şillə vurur.",
    "{victim} istifadəçisini yere sabitləyib ard-arda {item} ilə {hits} .",
    "{item} alarağ {victim} {hits}.",
    "{victim} istifadəçisini stola bağlayıb {item} {throws} .",
    "{victim} istifadəçisini dostca itələyərək lavada üzməyi öyrədir."
]

ITEMS = [
    "dəmir tava",
    "böyük alabalığ",
    "beyzbol çubuğu",
    "kriket çubuğu",
    "taxta baston",
    "mismar",
    "yazıcı",
    "lapatka",
    "boru monitoru",
    "fizika dəftəri",
    "krem aparatı",
    "Richard Stallman'ın portreti",
    "televizor",
    "beş ton kamaz",
    "koli bandajı",
    "kitab",
    "dizüstü komputer",
    "köhnə televizor",
    "daşlı kisə",
    "göyqurşağı alabalığı",
    "plastik cücə",
    "mismarlı çubuğ",
    "yanğın söndürücü",
    "ağır daş",
    "kir yığını",
    "arı yuvası",
    "çürüy ət parçası",
    "ayı",
    "tonlarca kərpic",
]

THROW = [
    "atır",
    "fırladır",
    "tullayır",
    "yağdırır",
]

HIT = [
    "vurur",
    "bərk vurur",
    "şillələyir",
    "yumruğlayır",
    "keçirdir",
]

# ===========================================


@register(outgoing=True, pattern=r"^.(\w+)say (.*)")
async def univsaye(cowmsg):
    """ .cowsay əmri bir şeylər söyləyən iney düzəldir """
    arg = cowmsg.pattern_match.group(1).lower()
    text = cowmsg.pattern_match.group(2)

    if arg == "cow":
        arg = "default"
    if arg not in cow.COWACTERS:
        return
    cheese = cow.get_cow(arg)
    cheese = cheese()

    await cowmsg.edit(f"`{cheese.milk(text).replace('`', '´')}`")


@register(outgoing=True, pattern="^:/$", ignore_unsafe=True)
async def kek(keks):
    """ Özünüzü yoxlayın ;)"""
    uio = ["/", "\\"]
    for i in range(1, 15):
        time.sleep(0.3)
        await keks.edit(":" + uio[i % 2])


@register(pattern="^.slap(?: |$)(.*)", outgoing=True)
async def who(event):
    """ Hədəflənən istifadəçiyə şillə atar. """
    replied_user = await get_user_from_event(event)
    if replied_user:
        replied_user = replied_user[0]
    else:
        return
    caption = await slap(replied_user, event)

    try:
        await event.edit(caption)

    except BaseException:
        await event.edit(
            "`Bu adamı şillələyə bilmərəm, yanıma cubuğ və daş götürməliyəm !!`"
        )


async def slap(replied_user, event):
    """ Şillə vuranda gülməli cümlə qur !! """
    user_id = replied_user.id
    first_name = replied_user.first_name
    username = replied_user.username

    if username:
        slapped = "@{}".format(username)
    else:
        slapped = f"[{first_name}](tg://user?id={user_id})"

    temp = choice(SLAP_TEMPLATES)
    item = choice(ITEMS)
    hit = choice(HIT)
    throw = choice(THROW)

    caption = "DTÖUserBot " + temp.format(
        victim=slapped, item=item, hits=hit, throws=throw)

    return caption


@register(outgoing=True, pattern="^-_-$", ignore_unsafe=True)
async def lol(lel):
    """ Tamam... """
    okay = "-_-"
    for i in range(10):
        okay = okay[:-1] + "_-"
        await lel.edit(okay)


@register(outgoing=True, pattern="^;_;$", ignore_unsafe=True)
async def fun(e):
    t = ";_;"
    for j in range(10):
        t = t[:-1] + "_;"
        await e.edit(t)


@register(outgoing=True, pattern="^.fp$")
async def facepalm(e):
    """ Utanmağ  🤦‍♂ """
    await e.edit("🤦‍♂")


@register(outgoing=True, pattern="^.cry$")
async def cry(e):
    """ bunu eləsən, həmişə ağlayaram !! """
    await e.edit(choice(CRI))


@register(outgoing=True, pattern="^.cp(?: |$)(.*)")
async def copypasta(cp_e):
    """ copypasta """
    textx = await cp_e.get_reply_message()
    message = cp_e.pattern_match.group(1)

    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await cp_e.edit("`😂Mənə💯BİR✌️mE🅱️In👐Ver👏`")
        return

    reply_text = choice(EMOJIS)
    b_char = choice(message).lower()
    for owo in message:
        if owo == " ":
            reply_text += choice(EMOJIS)
        elif owo in EMOJIS:
            reply_text += owo
            reply_text += choice(EMOJIS)
        elif owo.lower() == b_char:
            reply_text += "🅱️"
        else:
            if bool(getrandbits(1)):
                reply_text += owo.upper()
            else:
                reply_text += owo.lower()
    reply_text += choice(EMOJIS)
    await cp_e.edit(reply_text)


@register(outgoing=True, pattern="^.vapor(?: |$)(.*)")
async def vapor(vpr):
    """ Hər şeyi vaporlaşdırın! """
    reply_text = list()
    textx = await vpr.get_reply_message()
    message = vpr.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await vpr.edit("`M ə n ə b i r m ə t n v e r !`")
        return

    for charac in message:
        if 0x21 <= ord(charac) <= 0x7F:
            reply_text.append(chr(ord(charac) + 0xFEE0))
        elif ord(charac) == 0x20:
            reply_text.append(chr(0x3000))
        else:
            reply_text.append(charac)

    await vpr.edit("".join(reply_text))


@register(outgoing=True, pattern="^.str(?: |$)(.*)")
async def stretch(stret):
    """ Mesajı gözəlcə uzadın."""
    textx = await stret.get_reply_message()
    message = stret.text
    message = stret.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await stret.edit("`Məəəənəəə biiiiir məəətnnnn veeeeer!`")
        return

    count = randint(3, 10)
    reply_text = sub(r"([aeiouAEIOUａｅｉｏｕＡＥＩＯＵаеиоуюяыэё])", (r"\1" * count),
                     message)
    await stret.edit(reply_text)


@register(outgoing=True, pattern="^.zal(?: |$)(.*)")
async def zal(zgfy):
    """ Kaos hissini çağırın. """
    reply_text = list()
    textx = await zgfy.get_reply_message()
    message = zgfy.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await zgfy.edit(
            "`M ə n ə b i r m ə t n v e r ! `"
        )
        return

    for charac in message:
        if not charac.isalpha():
            reply_text.append(charac)
            continue

        for _ in range(0, 3):
            charac += choice(ZALG_LIST[randint(0,2)]).strip()

        reply_text.append(charac)

    await zgfy.edit("".join(reply_text))
    

@register(outgoing=True, pattern="^.hi$")
async def hoi(hello):
    """ Herkesi selamlayın """
    await hello.edit(choice(HELLOSTR))


@register(outgoing=True, pattern="^.owo(?: |$)(.*)")
async def faces(owo):
    """ UwU """
    textx = await owo.get_reply_message()
    message = owo.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await owo.edit("` UwU mənə bir mətn ver ! `")
        return

    reply_text = sub(r"(r|l)", "w", message)
    reply_text = sub(r"(R|L)", "W", reply_text)
    reply_text = sub(r"n([aeiou])", r"ny\1", reply_text)
    reply_text = sub(r"N([aeiouAEIOU])", r"Ny\1", reply_text)
    reply_text = sub(r"\!+", " " + choice(UWUS), reply_text)
    reply_text = reply_text.replace("ove", "uv")
    reply_text += " " + choice(UWUS)
    await owo.edit(reply_text)


@register(outgoing=True, pattern="^.react$")
async def react_meme(react):
    """ UserBot'un hər şeyə raksiya verməsini alındırın. """
    await react.edit(choice(FACEREACTS))


@register(outgoing=True, pattern="^.shg$")
async def shrugger(shg):
    r""" ¯\_(ツ)_/¯ """
    await shg.edit(choice(SHGS))


@register(outgoing=True, pattern="^.run$")
async def runner_lol(run):
    await run.edit(choice(RUNS_STR))


@register(outgoing=True, pattern="^oof$")
async def oof(e):
    t = "oof"
    for j in range(16):
        t = t[:-1] + "of"
        await e.edit(t)

                      
@register(outgoing=True, pattern="^Oof$")
async def Oof(e):
    t = "Oof"
    for j in range(16):
        t = t[:-1] + "of"
        await e.edit(t)


@register(outgoing=True, pattern="^skrrt$")
async def oof(e):
    t = "skrrt"
    for j in range(16):
        t = t[:-1] + "rt"
        await e.edit(t)
        

@register(outgoing=True, pattern="^Skrrt$")
async def oof(e):
    t = "Skrrt"
    for j in range(16):
        t = t[:-1] + "rt"
        await e.edit(t)


@register(outgoing=True, pattern="^\.(.*)")
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 101)
    input_str = event.pattern_match.group(1)
    if input_str == "fuk":
        await event.edit(input_str)
        animation_chars = [
            "🍆       🍑️",
            "🍆     🍑️",
            "🍆  🍑️",
            "🍆🍑️💦"
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 4])


@register(outgoing=True, pattern="^.kalp (.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    deq = deque(list("️❤️🧡💛💚💙💜🖤"))
    for _ in range(32):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)
    await event.edit("❤️🧡💛" + input_str + "💚💙💜🖤")


@register(outgoing=True, pattern="^.10iq$")
async def iqless(e):
    await e.edit(
    "DÜÜÜT DÜÜÜTT AÇ YOLU AÇÇ HAYDİ ASLAN PARÇASI YOLU AÇ \n"
    "HAYDİ BAX ƏNGƏLLİ GÖZLƏYİR BURDA HAYDİ DÜÜÜTTT ♿️ BAX \n"
    "ƏSƏBLƏŞDİ DOSTUM HAYDİ YOLU AÇ HAYDİ DÜÜÜT DÜÜTT BİİİPP \n"
    "HAYDİ DƏ SÜRƏTLİ OLL DÜÜÜTT BİİİPPP ♿️♿️ BAX SÜRƏTLƏNDİ ƏNGƏLLİ \n"
    "QARDAŞIMIZ TEZ KÖZ GƏTİR TEZ DÜÜÜTT DÜÜÜT DÜÜÜÜTTTTT \n"
    "BİİİİPPP BİİİİİPPP DÜÜÜTTT ♿️♿️♿️♿️ BAX SAYILARI ARTIR \n"
    "AÇDIN MI YOLU AÇMADIN PÜÜÜÜ REZİİİLL DÜÜÜÜTTT ♿️♿️♿️ \n"
    "♿️♿️♿️ BAX ÇOXALDILAR BAX DƏLI GELIR DƏLİLƏŞDİ DƏLI \n"
    "AÇ YOLU DUTDUTDURURURUDUTTT♿️♿️♿️♿️♿️♿️♿️♿️♿️ \n"
    "♿️♿️♿️♿️♿️KAFAYI YEDI BUNLAR AÇ ALAAAA YOLU"
    )
    
    
@register(outgoing=True, pattern="^.mizah$")
async def mizahshow(e):
    await e.edit(
    "⚠️⚠️⚠️MmMmMmMizahh Şoww😨😨😨😨😱😱😱😱😱 \n"
    "😱😱⚠️⚠️ 😂😂😂😂😂😂😂😂😂😂😂😂😂😂😱😵 \n"
    "😂😂👍👍👍👍👍👍👍👍👍👍👍👍👍 MiZah \n"
    "ŞəLaLəsNdEn b1r qurTluM aLdım✔️✔️✔️✔️ \n"
    "AHAHAHAHAHAHHAHAHAHAHAHAHAHAHAHAHAHHAHAHAHAHA \n"
    "HAHAHAHAHAHAHHAHAHAHAHAHAHA😂😂😂😂😂😂😂😂 \n"
    "😂 GÜLMƏLİDİ ALA GÜLMƏLİ \n"
    "haLaL aLa ✔️✔️✔️✔️✔️✔️✔️✔️👏👏👏👏👏👏👏👏 \n"
    "👏 ƏfSaNə mMmMiZah şooooovv 👏👏👏👏👏😂😂😂😂 \n"
    "😂😂😂😂😂😂⚠️ \n"
    "💯💯💯💯💯💯💯💯💯 \n"
    "BRAT EYNİ BİİİZ 😂😂😂👏👏 \n"
    "💯💯⚠️⚠️♿️AÇ YOLU POST SAHİBİ VƏ ONU ♿️QORUYANLAR \n"
    "GELİR ♿️♿️ DÜÜTT♿️ \n"
    "DÜÜÜÜT♿️DÜÜT♿️💯💯⚠️ \n"
    "♿️GÜLMƏLİİİ ♿️ \n"
    "CJWJCJWJXJJWDJJQUXJAJXJAJXJWJFJWJXJAJXJWJXJWJFIWIXJQJJQJASJAXJ \n"
    "AJXJAJXJJAJXJWJFWJJFWIIFIWICIWIFIWICJAXJWJFJEICIIEICIEIFIWICJSXJJS \n"
    "CJEIVIAJXBWJCJIQICIWJX💯💯💯💯💯💯😂😂😂😂😂😂😂 \n"
    "😂⚠️😂😂😂😂😂😂⚠️⚠️⚠️😂😂😂😂♿️♿️♿️😅😅 \n"
    "😅😂👏💯⚠️👏♿️🚨"
    )    


@register(outgoing=True, pattern="^.moon$")
async def moon(event):
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^.clock$")
async def clock(event):
    deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^.mock(?: |$)(.*)")
async def spongemocktext(mock):
    """ Elə və həqiqi əyləncəni tap. """
    reply_text = list()
    textx = await mock.get_reply_message()
    message = mock.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await mock.edit("`mƏnƏ bIr mETn vEr!`")
        return

    for charac in message:
        if charac.isalpha() and randint(0, 1):
            to_app = charac.upper() if charac.islower() else charac.lower()
            reply_text.append(to_app)
        else:
            reply_text.append(charac)

    await mock.edit("".join(reply_text))


@register(outgoing=True, pattern="^.clap(?: |$)(.*)")
async def claptext(memereview):
    """ İnsanları tərifləyin! """
    textx = await memereview.get_reply_message()
    message = memereview.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await memereview.edit("`Hah, mənası olmadan alqışlamıram!`")
        return
    reply_text = "👏 "
    reply_text += message.replace(" ", " 👏 ")
    reply_text += " 👏"
    await memereview.edit(reply_text)


@register(outgoing=True, pattern=r"^.f (.*)")
async def payf(event):
    paytext = event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        paytext * 8, paytext * 8, paytext * 2, paytext * 2, paytext * 2,
        paytext * 6, paytext * 6, paytext * 2, paytext * 2, paytext * 2,
        paytext * 2, paytext * 2)
    await event.edit(pay)


@register(outgoing=True, pattern="^.lfy (.*)")
async def let_me_google_that_for_you(lmgtfy_q):
    textx = await lmgtfy_q.get_reply_message()
    qry = lmgtfy_q.pattern_match.group(1)
    if qry:
        query = str(qry)
    elif textx:
        query = textx
        query = query.message
    query_encoded = query.replace(" ", "+")
    lfy_url = f"http://lmgtfy.com/?s=g&iie=1&q={query_encoded}"
    payload = {'format': 'json', 'url': lfy_url}
    r = requests.get('http://is.gd/create.php', params=payload)
    await lmgtfy_q.edit(f"Aha, kefivə bax.\
    \n[{query}]({r.json()['shorturl']})")


@register(pattern=r".scam(?: |$)(.*)", outgoing=True)
async def scam(event):
    """ Saxta söhbət əməliyyatları üçün kiçik bir əmr !! """
    options = [
        'typing', 'contact', 'game', 'location', 'voice', 'round', 'video',
        'photo', 'document', 'cancel'
    ]
    input_str = event.pattern_match.group(1)
    args = input_str.split()
    if len(args) is 0:
        scam_action = choice(options)
        scam_time = randint(30, 60)
    elif len(args) is 1:
        try:
            scam_action = str(args[0]).lower()
            scam_time = randint(30, 60)
        except ValueError:
            scam_action = choice(options)
            scam_time = int(args[0])
    elif len(args) is 2:
        scam_action = str(args[0]).lower()
        scam_time = int(args[1])
    else:
        await event.edit("`Invalid Syntax !!`")
        return
    try:
        if (scam_time > 0):
            await event.delete()
            async with event.client.action(event.chat_id, scam_action):
                await sleep(scam_time)
    except BaseException:
        return


@register(pattern=r".type(?: |$)(.*)", outgoing=True)
async def typewriter(typew):
    """ Klaviaturanızı bir daktiloya çevirmək üçün kiçik bir əmr ! """
    textx = await typew.get_reply_message()
    message = typew.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await typew.edit("`Mənə bir mətn ver !`")
        return
    sleep_time = 0.03
    typing_symbol = "|"
    old_text = ""
    await typew.edit(typing_symbol)
    await sleep(sleep_time)
    for character in message:
        old_text = old_text + "" + character
        typing_text = old_text + "" + typing_symbol
        await typew.edit(typing_text)
        await sleep(sleep_time)
        await typew.edit(old_text)
        await sleep(sleep_time)


CMD_HELP.update({
    "memes":
    ".cowsay\
\nİşlədilişi: bir şeylər söyləyən inək.\\n\n:/\
\nİşlədilişi: Özünüzə nəzarət edin ;)\
\n\n-_-\
\nİşlədilişi: Tamam...\
\n\n;_;\
\nİşlədilişi: `-_-` kimi ama ağlıyır.\
\n\n.cp\
\nİşlədilişi: Məhşur copypasta modulu\
\n\n.vapor\
\nİşlədilişi: Hər şeyi vaporlaştırın!\
\n\n.str\
\nİşlədilişi: Mesajı yaxşıca uzadın.\
\n\n.10iq\
\nİşlədilişi: Axmaqlıq səviyyənizi ölçün !!\
\n\n.mizah\
\nİşlədilişi: Axmaqlıq səviyyənizi ölçün !!\
\n\n.zal\
\nİşlədilişi: Kaos hissini çağırın.\
\n\noof\
\nİşlədilişi: ooooof\
\n\nskrrt\
\nİşlədilişi: skrrrrt\
\n\n.fuk\
\nİşlədilişi: ¯\_(ツ)_/¯\
\n\n.kalp\
\nİşlədilişi: Sevginizi göstərin.\
\n\n.fp\
\nİşlədilişi: Utanmağ  🤦‍♂\
\n\n.moon\
\nİşlədilişi: Ay animasiyası.\
\n\n.clock\
\nİşlədilişi: Saat animasiyası.\
\n\n.hi\
\nİşlədilişi: Hərkəsi salamlayın!\
\n\n.owo\
\nİşlədilişi: UwU\
\n\n.react\
\nİşlədilişi: UserBot'un hər şeyə reaksiya verməsini alındırın.\
\n\n.slap\
\nİşlədilişi: təsadüfi obyektlərlə sürüşdürmək üçün mesajı cavablandırın !!\
\n\n.cry\
\nİşlədilişi: bunu eləsən, həmişə ağlayaram.\
\n\n.shg\
\nİşlədilişi: ¯\_(ツ)_/¯\
\n\n.run\
\nİşlədilişi: UserBot'u qaçızdırar!\
\n\n.mock\
\nİşlədilişi: Elə və həqiqi əyləncəni tap.\
\n\n.clap\
\nİşlədilişi: İnsanları tərifləyin!\
\n\n.f <emoji/karakter>\
\nİşlədilişi: Hörmətlər..\
\n\n.type\
\nİşlədilişi: Klaviaturanızı bir daktiloya çevirmək üçün kiçik bir əmr !\
\n\n.lfy <sorğu>\
\nİşlədilişi: Google-un sizin üçün bunu axtarmasına icazə verin.\
\n\n.scam <hadisə> <vaxt>\
\n[Mövcud hadisələr: (typing, contact, game, location, voice, round, video, photo, document, cancel)]\
\nİşlədilişi: Əylənmək üçün saxta söhbət əməliyyatları yaradın. (Varsayılan əməliyyat: yazmaq)\
\n\nDüzənləmələr üçün təşəkkür edirik @thisisulvis @umudmmmdov1"
})
