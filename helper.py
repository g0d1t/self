from pyrogram import Client, filters, idle , errors
from pyrogram.types import *
from pyrogram.raw import functions , base , types
import os
try:
    import pyromod.listen
except ImportError:
    os.system("python3 -m pip install pyromod")    

api_id = 00000 # API ID
api_hash = '00000' # API HASH
app = Client("SelfBot", api_id, api_hash)
  
help1 = """
    ✯𝑴𝒖𝒕𝒆✯
➤ `.mute` ⤳ (𝑰𝒏𝒃𝒖𝒊𝒍𝒕 𝑴𝒖𝒕𝒆)
➤ `.unmute` ⤳ (𝑼𝒏𝒎𝒖𝒕𝒆)
➤ `.allunmute` ⤳ (𝑫𝒆𝒍𝒆𝒕𝒆 𝑨𝒍𝒍 𝑴𝒖𝒕𝒆)"""

help3 = """
    ✯𝑮𝒓𝒐𝒖𝒑✯
𝑰𝒇 𝒀𝒐𝒖 𝑨𝒅𝒎𝒊𝒏 𝒊𝒏 𝑮𝒓𝒐𝒖𝒑
➤ `.ban` ⤳ (𝑹𝒆𝒑𝒍𝒚 𝑶𝒓 𝑼𝒔𝒆𝒓𝒏𝒂𝒎𝒆)
➤ `.unban` ⤳ (𝑹𝒆𝒑𝒍𝒚 𝑶𝒓 𝑼𝒔𝒆𝒓𝒏𝒂𝒎𝒆)
➤ `.setmute` ⤳ (𝑹𝒆𝒑𝒍𝒚 𝑶𝒓 𝑼𝒔𝒆𝒓𝒏𝒂𝒎𝒆)
➤ `.delmute` ⤳ (𝑹𝒆𝒑𝒍𝒚 𝑶𝒓 𝑼𝒔𝒆𝒓𝒏𝒂𝒎𝒆)
➤ `.setchatphoto` ⤳ (𝑶𝒏𝒍𝒚 𝑹𝒆𝒑𝒍𝒚)
➤ `.setchattitle` ⤳ (𝑵𝒂𝒎𝒆)
➤ `.setchatbio` ⤳ (𝑩𝒊𝒐)
➤ `.setchatusername` ⤳ (𝑼𝒔𝒆𝒓𝒏𝒂𝒎𝒆)
➤ `.pin` ⤳ (𝑶𝒏𝒍𝒚 𝑹𝒆𝒑𝒍𝒚)
➤ `.unpin` ⤳ (𝑶𝒏𝒍𝒚 𝑹𝒆𝒑𝒍𝒚)
➤ `.unpinall` ⤳ (𝑵𝒐 𝑹𝒆𝒑𝒍𝒚)
➤ `.deletechannel` ⤳ (𝑼𝒔𝒆𝒓𝒏𝒂𝒎𝒆)
➤ `.deletegroup` ⤳ (𝑼𝒔𝒆𝒓𝒏𝒂𝒎𝒆)
➤ `.delallmsguser` ⤳ (𝑶𝒏𝒍𝒚 𝑹𝒆𝒑𝒍𝒚)
➤ `.slowmod` ⤳ (𝑵𝒖𝒎)
➤ `.delete` ⤳ (𝑵𝒖𝒎)
➤ `.tadmin` ⤳ (𝑵𝒐 𝑹𝒆𝒑𝒍𝒚)
➤ `.delethistory` ⤳ (𝑵𝒐 𝑹𝒆𝒑𝒍𝒚)"""

help4 = """
    ✯𝑻𝒊𝒎𝒆✯
➤ `.timename` ⤳ (𝑶𝒏 𝑶𝒓 𝑶𝒇𝒇)
➤ `.2timename` ⤳ (𝑶𝒏 𝑶𝒓 𝑶𝒇𝒇)
➤ `.timebio` ⤳ (𝑶𝒏 𝑶𝒓 𝑶𝒇𝒇)
➤ `.2timebio` ⤳ (𝑶𝒏 𝑶𝒓 𝑶𝒇𝒇)
➤ `.3timebio` ⤳ (𝑶𝒏 𝑶𝒓 𝑶𝒇𝒇)
➤ `.fontname` ⤳ (𝑶𝒏 𝑶𝒓 𝑶𝒇𝒇)
    ✯𝑷𝒓𝒐𝒇𝒊𝒍𝒆 𝑷𝒉𝒐𝒕𝒐✯
➤ `.setprofile` ⤳ (𝑹𝒆𝒑𝒍𝒚)
➤ `.delprofile` ⤳ (𝑫𝒆𝒍𝒆𝒕𝒆 𝑷𝒓𝒐𝒇𝒊𝒍𝒆)"""

help5 = """
    ✯𝑯𝒆𝒍𝒑 𝑭𝒖𝒍𝒍✯
➤ `.setname` ⤳ (𝑵𝒂𝒎𝒆)
➤ `.setlastname` ⤳ (𝑳𝒂𝒔𝒕 𝑵𝒂𝒎𝒆)
➤ `.setbio` ⤳ (𝑩𝒊𝒐)
➤ `.fontfa` ⤳ (𝑷𝒆𝒓𝒔𝒊𝒂𝒏 𝑭𝒐𝒏𝒕)
➤ `.fonten` ⤳ (𝑬𝒏𝒈𝒍𝒊𝒔𝒉 𝑭𝒐𝒏𝒕)
➤ `.clone` ⤳ (𝑪𝒍𝒐𝒏𝒆 𝑼𝒔𝒆𝒓)
➤ `.block` ⤳ (𝑹𝒆𝒑𝒍𝒚 𝑶𝒓 𝑼𝒔𝒆𝒓𝒏𝒂𝒎𝒆)
➤ `.unblock` ⤳ (𝑹𝒆𝒑𝒍𝒚 𝑶𝒓 𝑼𝒔𝒆𝒓𝒏𝒂𝒎𝒆)
➤ `.join` ⤳ (𝑪𝒉𝒂𝒕 𝑼𝒔𝒆𝒓𝒏𝒂𝒎𝒆)
➤ `.creatchannel` ⤳ (𝑵𝒂𝒎𝒆)
➤ `.creatsupergroup` ⤳ (𝑵𝒂𝒎𝒆)
➤ `.creatgroup` ⤳ (𝑵𝒂𝒎𝒆)
➤ `.searchwiki` ⤳ (𝑳𝒊𝒏𝒌 𝑵𝒂𝒎𝒆)
➤ `.mention` ⤳ (𝑹𝒆𝒑𝒍𝒚 𝑶𝒓 𝑼𝒔𝒆𝒓𝒏𝒂𝒎𝒆)
➤ `.get_message` ⤳ (𝑹𝒆𝒑𝒍𝒚)
➤ `.voice` ⤳ (𝑻𝒆𝒙𝒕)
➤ `.searchapp` ⤳ (𝑨𝒑𝒑 𝑵𝒂𝒎𝒆)
➤ `.sms` ⤳ (𝑷𝒉𝒐𝒏𝒆 𝑵𝒖𝒎𝒃𝒆𝒓)"""

help6 = """
    ✯𝑺𝒆𝒓𝒗𝒆𝒓 𝑰𝒏𝒇𝒐✯
➤ `.ping` ⤳ (𝑺𝒕𝒂𝒕𝒖𝒔)
➤ `.on_off_status` ⤳ (𝑺𝒕𝒂𝒕𝒖𝒔)
➤ `.cpu` ⤳ (𝑪𝑷𝑼 𝑰𝒏𝒇𝒐)
➤ `.memory` ⤳ (𝑴𝒆𝒎𝒐𝒓𝒚 𝑰𝒏𝒇𝒐)
➤ `.system-inf` ⤳ (𝑺𝒚𝒔𝒕𝒆𝒎 𝑰𝒏𝒇𝒐)
    ✯𝑰𝒏𝒇𝒐𝒓𝒎𝒂𝒕𝒊𝒐𝒏✯
➤ `.file_info` ⤳ (𝑹𝒆𝒑𝒍𝒚 𝑶𝒓 𝑼𝒔𝒆𝒓𝒏𝒂𝒎𝒆) 𝑭𝒊𝒍𝒆 𝑰𝒏𝒇𝒐
➤ `.inf` ⤳ (𝑹𝒆𝒑𝒍𝒚 𝑶𝒓 𝑼𝒔𝒆𝒓𝒏𝒂𝒎𝒆) 𝑪𝒉𝒂𝒕 𝑰𝒏𝒇𝒐
➤ `.id` ⤳ (𝑹𝒆𝒑𝒍𝒚 𝑶𝒓 𝑼𝒔𝒆𝒓𝒏𝒂𝒎𝒆) 𝑼𝒔𝒆𝒓 𝑰𝒏𝒇𝒐"""

help7 = """
    ✯𝑬𝒏𝒆𝒎𝒚✯
➤ `.setenemy` ⤳ (𝑹𝒆𝒑𝒍𝒚 𝑶𝒓 𝑼𝒔𝒆𝒓𝒏𝒂𝒎𝒆)
➤ `.friend` ⤳ (𝑹𝒆𝒑𝒍𝒚 𝑶𝒓 𝑼𝒔𝒆𝒓𝒏𝒂𝒎𝒆)
➤ `.allf` ⤳ (𝑫𝒆𝒍𝒆𝒕𝒆 𝑨𝒍𝒍 𝑬𝒏𝒆𝒎𝒚)"""

help8 = """
    ✯𝑰𝒏𝒔𝒕𝒂𝒈𝒓𝒂𝒎✯
➤ `.instalogin` ⤳ (𝑳𝒐𝒈𝒊𝒏)
➤ `.imloged` ⤳ (𝑪𝒉𝒆𝒄𝒌 𝒀𝒐𝒖𝒓 𝑳𝒐𝒈𝒊𝒏)
    ✯𝑰𝒇 𝒀𝒐𝒖 𝑳𝒐𝒈𝒆𝒅 𝑰𝒏 𝑻𝒐 𝑰𝒏𝒔𝒕𝒂𝒈𝒓𝒂𝒎✯
➤ `.mypageinfo` ⤳ (𝒀𝒐𝒖𝒓 𝑰𝒏𝒇𝒐)
➤ `.follow` ⤳ (𝑼𝒔𝒆𝒓𝒏𝒂𝒎𝒆)
➤ `.unfollow` ⤳ (𝑼𝒔𝒆𝒓𝒏𝒂𝒎𝒆)
➤ `.instagetuser` ⤳ (𝑼𝒔𝒆𝒓 𝑰𝒏𝒇𝒐)
➤ `.edit_firstname` ⤳ (𝑵𝒂𝒎𝒆)
➤ `.edit_biography` ⤳ (𝑩𝒊𝒐)
➤ `.instadl` ⤳ (𝑷𝒐𝒔𝒕 𝑼𝒓𝒍) 𝑫𝒐𝒘𝒏𝒍𝒐𝒂𝒅 𝑷𝒐𝒔𝒕
➤ `.story` ⤳ (𝑺𝒕𝒐𝒓𝒚 𝑼𝒓𝒍) 𝑫𝒐𝒘𝒏𝒍𝒐𝒂𝒅 𝑺𝒕𝒐𝒓𝒚"""

help9 = """
    ✯𝑷𝒓𝒂𝒄𝒕𝒊𝒄𝒂𝒍✯
➤ `.tp` ⤳ (𝑺𝒕𝒊𝒄𝒌𝒆𝒓 𝑻𝒐 𝑷𝒊𝒄)
➤ `.ts` ⤳ (𝑷𝒊𝒄 𝑻𝒐 𝑺𝒕𝒊𝒄𝒌𝒆𝒓)
➤ `.tg` ⤳ (𝑺𝒕𝒊𝒄𝒌𝒆𝒓 𝑻𝒐 𝑮𝒊𝒇)
    ✯𝑻𝒊𝒎𝒆𝒓 𝑷𝒊𝒄✯
➤ `.dl` ⤳ (𝑺𝒆𝒏𝒅 𝒕𝒐 𝑴.𝑪𝒉𝒂𝒕)
➤ `waitt` ⤳ (??𝒆𝒏𝒅 𝑻𝒐 𝑺𝒂𝒗𝒆𝒅 𝑴𝒆𝒔𝒔𝒂𝒈𝒆)
    ✯𝑺𝒑𝒂𝒎✯
➤ `.spam` ⤳ (𝑵𝒖𝒎 𝑶𝒇 𝑺𝒑𝒂𝒎 + 𝑻𝒆𝒙𝒕 𝑶𝒓 𝑹𝒆𝒑𝒍𝒚)
➤ `.spm` ⤳ (𝑵𝒖𝒎 𝑶𝒇 𝑺𝒑𝒂𝒎 + 𝑻𝒆𝒙𝒕)
    ✯𝑻𝒊𝒎𝒆✯
➤ `.time` ⤳ (𝑻𝒊𝒎𝒆)
➤ `.timepic` ⤳ (𝑻𝒊𝒎𝒆 𝑷𝒉𝒐𝒕𝒐)"""

help10 = """
    ✯𝑭𝒊𝒓𝒔𝒕 𝑪𝒐𝒎𝒎𝒆𝒏𝒕✯
➤ `.firstcom` ⤳ (𝑶𝒏 𝑶𝒓 𝑶𝒇𝒇) 
➤ `.first_message` ⤳ (𝑹𝒆𝒑𝒍𝒚)
    ✯𝑺𝒆𝒏𝒅 𝑨𝒕 𝑨 𝑻𝒊𝒎𝒆✯
➤ `.text_time` ⤳ (𝑯𝑯 : 𝒎𝒎) 
➤ `.text_send_time` ⤳ (𝑻𝒆𝒙𝒕 𝑶𝒓 𝑹𝒆𝒑𝒍𝒚)
➤ `.photo_time` ⤳ (𝑯𝑯 : 𝒎𝒎)
➤ `.photo_send_time` ⤳ (𝑹𝒆𝒑𝒍𝒚 𝑻𝒐 𝑷𝒊𝒄)"""

help11 = """
    ✯𝑭𝒖𝒏✯
➤ `Reload` ⤳ (𝑹𝒆𝒍𝒐𝒂𝒅)
➤ `.khaymallist` ⤳ (𝑳𝒊𝒔𝒕)
    ✯𝑪𝒉𝒆𝒂𝒕𝒊𝒏𝒈✯
➤ `.tas` ⤳ (𝟏 - 𝟔)
➤ `.dart` ⤳ (𝑫𝒂𝒓𝒕)
➤ `.bowling` ⤳ (𝒃𝒐𝒘𝒍𝒊𝒏𝒈)
➤ `.basketball` ⤳ (𝒃𝒂𝒔𝒌𝒆𝒕𝒃𝒂𝒍𝒍)
➤ `.football` ⤳ (𝟏 𝑶𝒓 𝟒) ⤳ 1 = 𝑭𝒂𝒊𝒍 | 4 = 𝑮𝒐𝒂𝒍"""

help12 = """
    ✯𝑻𝒐𝒐𝒍𝒔✯
➤ `.ip` ⤳ (𝑮𝒆𝒕 𝑺𝒊𝒕𝒆 𝑰𝒑)
➤ `.whoisip` ⤳ (𝑰𝒑 𝑰𝒏𝒇𝒐)
➤ `.nimurl` ⤳ (𝑼𝒓𝒍 𝒉𝒂𝒍𝒇 𝒑𝒓𝒊𝒄𝒆)
➤ `.qrcode` ⤳ (𝑴𝒂𝒌𝒆 𝑸𝑹 𝑪𝒐𝒅𝒆)
➤ `.screenurl` ⤳ (𝑺𝒄𝒓𝒆𝒆𝒏 𝑼𝒓𝒍)
➤ `.pindl` ⤳ (𝑷𝒊𝒏𝑻𝒆𝒓𝒆𝒔𝒕 𝑫𝒍)
➤ `.dllink` ⤳ (𝑼𝒓𝒍)
    ✯𝑴𝒐𝒗𝒊𝒆✯
➤ `.imdb` ⤳ (𝑴𝒐𝒗𝒊𝒆 𝑵𝒂𝒎𝒆)
    ✯𝒀𝒐𝒖𝒕𝒖𝒃𝒆✯
➤ `.music` ⤳ (𝑵𝒐𝒕 𝑾𝒐𝒓𝒌𝒊𝒏𝒈)
➤ `.ytdl` ⤳ (𝑵𝒐𝒕 𝑾𝒐𝒓𝒌𝒊𝒏𝒈)
    ✯𝑷𝒐𝒓𝒏✯
➤ `.xnxx` ⤳ (𝑵𝒖𝒍𝒍)
    ✯𝑶𝒄𝒓✯
➤ `.ocr` ⤳ (𝑶𝒄𝒓)"""

help13 = """
    ✯𝑻𝒆𝒙𝒕 𝑴𝒐𝒅𝒆✯
➤ `.bold` ⤳ (𝑶𝒏 𝑶𝒓 𝑶𝒇𝒇)
➤ `.spoiler` ⤳ (𝑶𝒏 𝑶𝒓 𝑶𝒇𝒇)
➤ `.italic` ⤳ (𝑶𝒏 𝑶𝒓 𝑶𝒇𝒇)
➤ `.finglish` ⤳ (𝑶𝒏 𝑶𝒓 𝑶𝒇𝒇)
➤ `.code` ⤳ (𝑶𝒏 𝑶𝒓 𝑶𝒇𝒇)
➤ `.underline` ⤳ (𝑶𝒏 𝑶𝒓 𝑶𝒇𝒇)
➤ `.strike` ⤳ (𝑶𝒏 𝑶𝒓 𝑶𝒇𝒇)
➤ `.emoji` ⤳ (𝑶𝒏 𝑶𝒓 𝑶𝒇𝒇)"""

help14 = """
    ✯𝑨𝒖𝒕𝒐 𝑨𝒏𝒔𝒘𝒆𝒓✯
➤ `.answer` ⤳ (𝑶𝒏 𝑶𝒓 𝑶𝒇𝒇)
➤ `.addan` ⤳ (𝑸𝒖𝒆𝒔𝒕𝒊𝒐𝒏: 𝑨𝒏𝒔𝒘𝒆𝒓)
➤ `.delan` ⤳ (𝑸𝒖𝒆𝒔𝒕𝒊𝒐𝒏)
➤ `.anlist` ⤳ (𝑨𝒏𝒔𝒘𝒆𝒓 𝑳𝒊𝒔𝒕)
➤ `.anclear` ⤳ (𝑨𝒏𝒔𝒘𝒆𝒓 𝑪𝒍𝒆𝒂𝒏)"""

help15 = """
    ✯𝑨𝒏𝒕𝒊 𝑫𝒆𝒍𝒆𝒕𝒆 𝑴𝒆𝒎𝒃𝒆𝒓✯
➤ `.anti_fuck` ⤳ (𝑶𝒏 𝑶𝒓 𝑶𝒇𝒇)
➤ `.antich` ⤳ (-𝟏𝟎𝟎 + 𝑪𝒉𝒂𝒕 𝑰𝒅)
➤ `.limit_del` ⤳ (𝑳𝒊𝒎𝒊𝒕 𝑶𝒇 𝑫𝒆𝒍𝒆𝒕𝒆 𝑴𝒆𝒎𝒃𝒆𝒓)"""

help16 = """
    ✯𝑪𝒐𝒅𝒆 𝑹𝒖𝒏𝒏𝒆𝒓✯
➤ `.py` ⤳ (𝑪𝒐𝒅𝒆)
➤ `.js` ⤳ (𝑪𝒐𝒅𝒆)
➤ `.php` ⤳ (𝑪𝒐𝒅𝒆)
➤ `.kotlin` ⤳ (𝑪𝒐𝒅𝒆)
➤ `.go` ⤳ (𝑪𝒐𝒅𝒆)
➤ `.java` ⤳ (𝑪𝒐𝒅𝒆)
➤ `.lua` ⤳ (𝑪𝒐𝒅𝒆)
    ✯𝑪𝒐𝒅𝒆 𝑺𝒄𝒓𝒆𝒆𝒏𝑺𝒉𝒐𝒕✯
➤ `.carbon` ⤳ (𝑪𝒂𝒓𝒃𝒐𝒏) 𝑹𝒆𝒑𝒍𝒚
➤ `.exec` ⤳ (𝑬𝒙𝒆𝒄𝒖𝒕𝒆 𝑪𝒐𝒅𝒆) 𝑹𝒆𝒑𝒍𝒚"""

help17 = """
    ✯𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝑴𝒆𝒏𝒖✯
➤ `.welcome` ⤳ (𝑶𝒏 𝑶𝒓 𝑶𝒇𝒇)
➤ `.welcome_add` ⤳ (𝑻𝒆𝒙𝒕)
➤ `.welcome_show` ⤳ (𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝑺𝒉𝒐𝒘)
➤ `.welcome_reset` ⤳ (𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝑹𝒆𝒔𝒆𝒕)"""

mark = InlineKeyboardMarkup(
     [
         [
             InlineKeyboardButton('𝑬𝒏𝒆𝒎𝒚 👤',callback_data='eny'),
             InlineKeyboardButton('𝑴𝒖𝒕𝒆 🔕',callback_data='mute') 

         ],
         [
             InlineKeyboardButton('𝑮𝒓𝒐𝒖𝒑 👥',callback_data='group'), 
             InlineKeyboardButton('𝑷𝒓𝒂𝒄𝒕𝒊𝒄𝒂𝒍 🌐',callback_data='prc')
         ],
         [
             InlineKeyboardButton('𝑨𝒏𝒕𝒊 𝑫𝒆𝒍𝒆𝒕𝒆 🔰',callback_data='anti_delete_member')
         ],
         [
             InlineKeyboardButton('𝑻𝒐𝒐𝒍𝒔 ⚙️',callback_data='tool'),
             InlineKeyboardButton('𝑷𝒓𝒐𝒇𝒊𝒍𝒆 🏞',callback_data='profile')
         ],
         [
              InlineKeyboardButton('𝑭𝒖𝒏 🎭',callback_data='fun'),
             InlineKeyboardButton('𝑻𝒆𝒙𝒕 𝑴𝒐𝒅𝒆 🧩',callback_data='textmode')
         ],
         [
             InlineKeyboardButton('𝑯𝒆𝒍𝒑 𝑭𝒖𝒍𝒍 📕',callback_data='helpful'), 
             InlineKeyboardButton('𝑰𝒏𝒇𝒐 ℹ️',callback_data='info')
         ],
         [
             InlineKeyboardButton('𝑭𝒊𝒓𝒔𝒕 𝑪𝒐𝒎𝒎𝒆𝒏𝒕 1️⃣',callback_data='first'),
         ],
         [
             InlineKeyboardButton('𝑪𝒐𝒅𝒆 𝑶𝒑𝒕𝒊𝒐𝒏 </>',callback_data='eval'),
             InlineKeyboardButton('𝑨𝒖𝒕𝒐 𝑨𝒏𝒔𝒘𝒆𝒓 ⚙️',callback_data='autoan')
         ],
         [
             InlineKeyboardButton('𝑾𝒆𝒍𝒄𝒐𝒎𝒆 ✨️',callback_data='welcome'),
             InlineKeyboardButton('𝑰𝒏𝒔𝒕𝒂𝒈𝒓𝒂𝒎 💎',callback_data='insta')
         ],
         [
             InlineKeyboardButton('𝑪𝒍𝒐𝒔𝒆 𝑷𝒂𝒏𝒆𝒍',callback_data='close')
         ],
     ]
)

dast = InlineKeyboardMarkup(
     [
         [
             InlineKeyboardButton("𝑩𝒂𝒄𝒌", callback_data='back')
         ]
     ]
)

openpanelbot = InlineKeyboardMarkup(
     [
         [
             InlineKeyboardButton("Panel", switch_inline_query_current_chat='panel')
         ]
     ]
)

keyboard_idk = ReplyKeyboardMarkup(
     [
         [
             ("Add User"),
             ("Delete User"),
             ("User List")
         ],
         [
             ("Add Owner"),
             ("Delete Owner"),
             ("Owner List")
         ]
     ],
one_time_keyboard=True,resize_keyboard=True)

my_users = [00000] # ID Owner
users = filters.user(my_users) 

my_owners = [00000] # ID Owner
owners = filters.user(my_owners) 

@app.on_inline_query()
def answer(client, inline_query):
    if inline_query.from_user.id in my_users:
      inline_query.answer(
          results=[
              InlineQueryResultArticle(
                  title="Helper",
                  input_message_content=InputTextMessageContent(
                      f"𝙃𝙚𝙡𝙡𝙤 {inline_query.from_user.first_name}\n 𝙒𝙚𝙡𝙘𝙤𝙢𝙚 𝙏𝙤 𝙃𝙚𝙡𝙥𝙚𝙧 𝘽𝙤𝙩 "
                  ),
                  description="Helper Panel",
                  reply_markup=mark
              )
          ],
          cache_time=1
      )

@app.on_callback_query(users)
async def test(app, call): 
    if call.data == "back":
         await app.edit_inline_text(inline_message_id=call.inline_message_id, text=f"User: `{call.from_user.first_name}`\n**Main Menu**", reply_markup=mark)
                  
    elif call.data == "eny":
         await app.edit_inline_text(inline_message_id=call.inline_message_id, text=help7 , reply_markup=dast)
         
    elif call.data == "mute":
         await app.edit_inline_text(inline_message_id=call.inline_message_id, text=help1 , reply_markup=dast)
         
    elif call.data == "group":
         await app.edit_inline_text(inline_message_id=call.inline_message_id, text=help3 , reply_markup=dast)
       
    elif call.data == "prc":
         await app.edit_inline_text(inline_message_id=call.inline_message_id, text=help9 , reply_markup=dast)
         
    elif call.data == "anti_delete_member":
         await app.edit_inline_text(inline_message_id=call.inline_message_id, text=help15 , reply_markup=dast)
         
    elif call.data == "fun":
         await app.edit_inline_text(inline_message_id=call.inline_message_id, text=help11 , reply_markup=dast)
         
    elif call.data == "tool":
         await app.edit_inline_text(inline_message_id=call.inline_message_id, text=help12 , reply_markup=dast)
         
    elif call.data == "profile":
         await app.edit_inline_text(inline_message_id=call.inline_message_id, text=help4 , reply_markup=dast)
         
    elif call.data == "textmode":
         await app.edit_inline_text(inline_message_id=call.inline_message_id, text=help13 , reply_markup=dast)
       
    elif call.data == "helpful":
         await app.edit_inline_text(inline_message_id=call.inline_message_id, text=help5 , reply_markup=dast)
         
    elif call.data == "info":
         await app.edit_inline_text(inline_message_id=call.inline_message_id, text=help6 , reply_markup=dast)
         
    elif call.data == "first":
         await app.edit_inline_text(inline_message_id=call.inline_message_id, text=help10 , reply_markup=dast)
         
    elif call.data == "insta":
         await app.edit_inline_text(inline_message_id=call.inline_message_id, text=help8 , reply_markup=dast)
         
    elif call.data == "eval":
         await app.edit_inline_text(inline_message_id=call.inline_message_id, text=help16 , reply_markup=dast)
         
    elif call.data == "autoan":
         await app.edit_inline_text(inline_message_id=call.inline_message_id, text=help14 , reply_markup=dast)
         
    elif call.data == "welcome":
         await app.edit_inline_text(inline_message_id=call.inline_message_id, text=help17 , reply_markup=dast)

    elif call.data == "close":
         await app.edit_inline_text(inline_message_id=call.inline_message_id, text="❋ 𝑯𝒆𝒍𝒑𝒆𝒓 𝑷𝒂𝒏𝒆𝒍 𝑪𝒍𝒐𝒔𝒆𝒅")
   
@app.on_callback_query(~users)
def test(app, call): 
  call.answer("دست نزن بچه 🗿", show_alert=True)
    
@app.on_message(filters.private&owners&filters.command("panel"), group=-1)
async def updates(app, m:Message):
     await app.send_message(m.chat.id, "**QuiteCreateCliBot Panel Owner**", reply_markup=keyboard_idk)
    
@app.on_message(filters.private&users&filters.command("start"), group=-1)
async def updates(app, m:Message):
     kos = f"@{m.from_user.username}" if m.from_user.username else m.from_user.id
     await app.send_message(m.chat.id, f"𝙃𝙚𝙡𝙡𝙤 {m.from_user.first_name}\n𝙒𝙚𝙡𝙘𝙤𝙢𝙚 𝙏𝙤 𝙃𝙚𝙡𝙥𝙚𝙧 𝘽𝙤𝙩\n𝙁𝙤𝙧 𝙜𝙚𝙩 𝙋𝙖𝙣𝙚𝙡 𝙩𝙮𝙥𝙚 ( `!help` )\n     ", reply_markup=openpanelbot)
     await app.send_message(my_owners[0], f"✅ User {kos} Started The Bot ✅")

@app.on_message(filters.private&~users&filters.command("start"), group=-1)
async def updates(app, m:Message):
     await m.delete()
     
   #______________________________Owner Panel________________________
@app.on_message(filters.private&owners)
async def updates(app, m:Message):
 text = m.text
 if text == "Add User":
   try:
     answer = await app.ask(m.chat.id, '**Send Me User ID**:')
     my_users.append(int(answer.text))
     users.add(int(answer.text))
     await app.send_message(m.chat.id, f"Successfull\nUser [ `{answer.text}` ] Added to User List")
   except Exception as er:
     await app.send_message(m.chat.id , f"❋ `ERROR` ⤳\n(`{er}`)")

 elif text == "Delete User":
   answer = await app.ask(m.chat.id, '**Send Me User ID**:')
   if int(answer.text) in users:
     try:
       num = my_users.index(int(answer.text))
       my_users.remove(my_users[num])
       users.remove(int(answer.text))
       await app.send_message(m.chat.id, f"Successfull\nUser [ `{answer.text}` ] Deleted From User List")
     except Exception as er:
       await app.send_message(m.chat.id , f"❋ `ERROR` ⤳\n(`{er}`)")
   else:
     await app.send_message(m.chat.id, f"This is Not in Users List")
             
 elif text == "User List":
   try:
     s = ""
     op = 1
     if len(my_users) >= 1:
       for i in range(0,int(len(my_users))):
         s += f"֍ {op} -> `{my_users[i]}`\n"
         op += 1
       await app.send_message(m.chat.id, f"**User List:**\n{s}")
     else:
       await app.send_message(m.chat.id, f"**User List is Empty**")
   except Exception as er:
     await app.send_message(m.chat.id , f"❋ `ERROR` ⤳\n(`{er}`)")
   
 elif text == "Add Owner":
   answer = await app.ask(m.chat.id, '**Send Me User ID**:')
   try:
     if int(answer.text) in my_users:
       my_owners.append(int(answer.text))
       owners.add(int(answer.text))
       await app.send_message(m.chat.id, f"Successfull\nUser [ `{answer.text}` ] Added to Owner List")
     else:
       await app.send_message(m.chat.id, f"این یتیم حتی یوزر هم نیست داش 😐\nاول به یوزرا اضافش کن بعد بیا مالکش کن")
   except Exception as er:
     await app.send_message(m.chat.id , f"❋ `ERROR` ⤳\n(`{er}`)")
       
 elif text == "Delete Owner":
   answer = await app.ask(m.chat.id, '**Send Me User ID**:')
   if int(answer.text) in my_users:
     try:
       num = my_owners.index(int(answer.text))
       my_owners.remove(my_owners[num])
       owners.remove(int(answer.text))
       await app.send_message(m.chat.id, f"Successfull\nUser [ `{answer.text}` ] Deleted From Owner List")
     except Exception as er:
       await app.send_message(m.chat.id , f"❋ `ERROR` ⤳\n(`{er}`)")
   else:
     await app.send_message(m.chat.id, f"This is Not in Owners List")

 elif text == "Owner List":
   try:
     s = ""
     op = 1
     if len(my_owners) >= 1:
       for i in range(0,int(len(my_owners))):
         s += f"֍ {op} -> `{my_owners[i]}`\n"
         op += 1
       await app.send_message(m.chat.id, f"**Owner List:**\n{s}")
     else:
       await app.send_message(m.chat.id, f"**Owner List is Empty**")
   except Exception as er:
     await app.send_message(m.chat.id , f"❋ `ERROR` ⤳\n(`{er}`)")


app.start(), print("started..."), idle(), app.stop()