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
