from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Assalamu'alaikum Permisi Boleh lewat")


@register(outgoing=True, pattern='^p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Assalamu'alaikum Permisi Boleh lewat")


@register(outgoing=True, pattern='^L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Wa'alaikumussalam Semoga bermanfaat salamnya")


@register(outgoing=True, pattern='^l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Wa'alaikumussalam Semoga bermanfaat salamnya")


CMD_HELP.update({
    "salam":
    "`P atau p`\
\nUsage: Untuk Memberi salam.\
\n\n`L atau l`\
\nUsage: Untuk Menjawab Salam."
})
