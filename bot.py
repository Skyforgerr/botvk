import vk_api, vk
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
vk_session = vk_api.VkApi(token='5681f33fa1a9e833372e21cae5c62cdddff34bbb0b18aca0f7ea069e9fc27a0ee08b94fe96d09305a8dcd')
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
longpoll = VkBotLongPoll(vk_session, 'club199739242')
vk = vk_session.get_api()
from vk_api.longpoll import VkLongPoll, VkEventType

def sender(id, text): 
	vk_session.method('messages.send', {'user_id': id, 'message' : text, 'random_id' : 0, 'chat_id': 1})

	longpoll = VkLongPoll(vk_session, 'https://vk.me/join/A3EGVQmOfQ_QGwkqiNdagn0cky70reO1Q5A=')

for event in longpoll.listen():
	if event.type == VkEventType.MESSAGE_NEW:
		if event.to_me:
			msg = event.text.lower()
			id = event.user_id
			if msg == 'ты кто?':
				sender(id, 'Бот Евлампий')
			elif msg == 'привет':
				sender(id, 'Ну дарова')
