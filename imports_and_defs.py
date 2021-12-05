import vk_api, time, random, datetime, schedule, string
from datetime import date
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from vk_api.upload import VkUpload
import text
import json

main_token = "0ddc4d363df96068ea2f478a9e306640f75bed339c85d3e28ae83464df04b2f7dd193f8523bca12600139"

vk_session = vk_api.VkApi(token = main_token)
session_api = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, 204376695)



all_sms = 0


def sender(id, text):
	vk_session.method("messages.send", {"chat_id" : id, "message" : text, "random_id" : 0})

def senderUR(text):
	vk_session.method("messages.send", {"chat_id" : 5, "message" : text, "random_id" : 0})

def vel():
	user_1 = random.choice(users)["first_name"] + " " + random.choice(users)["last_name"]
	senderUR(f'Этому миру просто необходим герой - {user_1}!')

def check_user_stk(user_id, msg):
	msg = msg
	if kol_redisok[str(user_id)] < 10:
		return "У вас мало редисок!"
	else:
		return stavk(user_id, msg)

def stavk(user_id, msg):
	try:
		if int(msg[10:]) > kol_redisok[str(user_id)]:
			return "У вас нет такого кол-ва редисок!"
		else:
			kol_redisok[str(user_id)] -= int(msg[10:])
			if str(msg[8]) == "c":
				team = "синей"
			else:
				team = "красной"
			return f'Ставка принята! Вы в {team} команде.'
	except:
		return "Произошла ошибка, попробуйте еще раз!"

members = session_api.messages.getConversationMembers(peer_id=2000000000+5,)['items']
users = session_api.messages.getConversationMembers(peer_id=2000000000+5)["profiles"]
random_member = random.choice(members)["member_id"]




def send_photo(upload, photo1):
	response1 = upload.photo_messages(photo1)
	owner_id1 = response1['owner_id']
	photo_id1 = response1['id']
	access_key1 = response1['access_key']
	attachment1 = f'photo{owner_id1}_{photo_id1}_{access_key1}'
	vk_session.method("messages.send", {"chat_id" : 5, "message" : "", "random_id" : 0, 'attachment' : attachment1})
