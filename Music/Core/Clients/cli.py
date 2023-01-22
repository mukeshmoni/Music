from pyrogram import Client

from config import (API_HASH, API_ID, BOT_TOKEN, LOG_SESSION, STRING2,
                    STRING3, STRING4, STRING5)

STRING1 = "BQBxE3LINO0xkjcku7bRgrIKuhflRvzM7vM4Jy0SQlp4S2CS4XOA80pn9dbkUdO1EQ-VfOwghXu2jB4J7UuOI_k7wHtzOyjkSnD2u95r1p-Jhysj54Dm3Xzmpy6EJXWkcmBFS781yYAtYma748teY96Q5VcQ4aSpKgClK7PbY9F7Vk9KstPDkwDdAhEIYA5pGV6d08L2xtKaPvTT_DKH7s9jVOb64B7Qef3t0mPMbBf_9wLUQvaYqjkb9r3R6IhIBefPYBB5IsOfIuQXP-O9uVtKps19n3-woHCbI3tS5yZo_LMa7sjpVnG8m2N9NLQZc2XqbOrGJWtVGkM1SRF3C6WhAAAAAUk_nSsA"

app = Client(
    "MusicBot",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
)


if not STRING1:
    ASS_CLI_1 = None
else:
    ASS_CLI_1 = Client(
        api_id=API_ID,
        api_hash=API_HASH,
        session_name=STRING1,
        plugins=dict(root="Music.Plugins.Multi-Assistant"),
    )


if not STRING2:
    ASS_CLI_2 = None
else:
    ASS_CLI_2 = Client(
        api_id=API_ID,
        api_hash=API_HASH,
        session_name=STRING2,
        plugins=dict(root="Music.Plugins.Multi-Assistant"),
    )


if not STRING3:
    ASS_CLI_3 = None
else:
    ASS_CLI_3 = Client(
        api_id=API_ID,
        api_hash=API_HASH,
        session_name=STRING3,
        plugins=dict(root="Music.Plugins.Multi-Assistant"),
    )


if not STRING4:
    ASS_CLI_4 = None
else:
    ASS_CLI_4 = Client(
        api_id=API_ID,
        api_hash=API_HASH,
        session_name=STRING4,
        plugins=dict(root="Music.Plugins.Multi-Assistant"),
    )


if not STRING5:
    ASS_CLI_5 = None
else:
    ASS_CLI_5 = Client(
        api_id=API_ID,
        api_hash=API_HASH,
        session_name=STRING5,
        plugins=dict(root="Music.Plugins.Multi-Assistant"),
    )


if not LOG_SESSION:
    LOG_CLIENT = None
else:
    LOG_CLIENT = Client(LOG_SESSION, API_ID, API_HASH)
