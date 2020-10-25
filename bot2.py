import vk_api, vk
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id

vk_session = vk_api.VkApi(token='5681f33fa1a9e833372e21cae5c62cdddff34bbb0b18aca0f7ea069e9fc27a0ee08b94fe96d09305a8dcd')

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
longpoll = VkBotLongPoll(vk_session, club199739242)
vk = vk_session.get_api()
from vk_api.longpoll import VkLongPoll, VkEventType

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
    	if 'Ку' in str(event) or 'Привет' in str(event) or 'Хай' in str(event) or 'Хелло' in str(event) or 'Хеллоу' in str(event):
    		if event.from_chat:
    vk.messages.send(
    key = (''),
    server = (''),
    ts=(''),
    random_id = get_random_id(),
    message='Привет!',
    chat_id = event.chat_id
    )