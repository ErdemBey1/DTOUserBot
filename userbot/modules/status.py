# Copyright (C) 2020 @umudmmmdov1.
#
# Licensed under the @umudmmmdov1 Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# DTÖUserBot - @umudmmmdov1

from userbot import CMD_HELP, ASYNC_POOL, tgbot, SPOTIFY_DC, G_DRIVE_CLIENT_ID, lastfm, LYDIA_API_KEY, YOUTUBE_API_KEY, OPEN_WEATHER_MAP_APPID, AUTO_PP, REM_BG_API_KEY, OCR_SPACE_API_KEY, PM_AUTO_BAN, BOTLOG_CHATID
from userbot.events import register
from telethon import version
from platform import python_version

def durum(s):
    if s == None:
        return "❌"
    else:
        if s == False:
            return "❌"
        else:
            return "✅"

@register(outgoing=True, pattern="^.status")
async def statuss(event):

    await event.edit(f"""
**Python Versiya:** `{python_version()}`
**TeleThon Vərsiya:** `{version.__version__}` 
**DTÖUserBot Versiya:** `1.1`

**Plugin Sayı:** `{len(CMD_HELP)}`

**Inline Bot:** `{status(tgbot)}`
**Spotify:** `{status(SPOTIFY_DC)}`
**GDrive:** `{status(G_DRIVE_CLIENT_ID)}`
**LastFm:** `{status(lastfm)}`
**YouTube ApiKey:** `{status(YOUTUBE_API_KEY)}`
**Lydia:** `{status(LYDIA_API_KEY)}`
**OpenWeather:** `{status(OPEN_WEATHER_MAP_APPID)}`
**AutoPP:** `{status(AUTO_PP)}`
**RemoveBG:** `{status(REM_BG_API_KEY)}`
**OcrSpace:** `{status(OCR_SPACE_API_KEY)}`
**Pm AutoBan:** `{status(PM_AUTO_BAN)}`
**BotLog:** `{status(BOTLOG_CHATID)}`
**Pluginlər:** `Qalıcı`

**Her şey normaldı ✅**
    """)

CMD_HELP["status"] = "✏️ **Əmr:** .status\n🔰 **İşlədilişi:** Əlavə olunan Apilər və versiyaları göstərər."
