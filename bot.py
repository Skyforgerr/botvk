<<<<<<< Updated upstream
import vk_api
from vk_api.bot_longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token='5681f33fa1a9e833372e21cae5c62cdddff34bbb0b18aca0f7ea069e9fc27a0ee08b94fe96d09305a8dcd')
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def sender(id, text): 
	vk_session.method('messages.send', {'user_id': id, 'message' : text, 'random_id' : 0, 'chat_id': 1})


for event in longpoll.listen():
	if event.type == VkEventType.MESSAGE_NEW:
		if event.to_me:
			msg = event.text.lower()
			id = event.user_id
			if msg == 'ты кто?':
				sender(id, 'Бот Евлампий')
			elif msg == 'привет':
				sender(id, 'Ну дарова')
=======
import vk_api, vk
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id

vk_session = vk_api.VkApi(token='5681f33fa1a9e833372e21cae5c62cdddff34bbb0b18aca0f7ea069e9fc27a0ee08b94fe96d09305a8dcd')

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
longpoll = VkBotLongPoll(vk_session, '199739242')
vk = vk_session.get_api()
from vk_api.longpoll import VkLongPoll, VkEventType

Lslongpoll = VkLongPoll(vk_session)
Lsvk = vk_session.get_api()

keyboard = VkKeyboard(one_time=True)
keyboard.add_button('Привет', color=VkKeyboardColor.NEGATIVE)
keyboard.add_button('Клавиатура', color=VkKeyboardColor.POSITIVE)
keyboard.add_line()
keyboard.add_location_button()
keyboard.add_line()
keyboard.add_vkpay_button(hash="action=transfer-to-group&group_id=183415444")

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

    if event.from_chat:
    vk.messages.send(
        keyboard = keyboard.get_keyboard(),
        key = ('21b7e67abf6b938c8223242c37b4ff873efe1453'),
        server = ('https://lp.vk.com/wh183415444'),
        ts=('3539'),
        random_id = get_random_id(),
        message='Держи',
        chat_id = event.chat_id
        )
>>>>>>> Stashed changes
