from imports_and_defs import *

kupon = "sfsdddddddddd22df"
with open('date.json', 'r') as file:
	date_json = json.load(file)
	kol_sms = date_json['kol_sms'][0]
	kol_redisok = date_json['kol_redisok'][0]
	deter_ppls = date_json['deter_ppls'][0]
	obyavleniya = date_json['obyavleniya'][0]
	zaprosi = date_json['zaprosi'][0]
	premium_persons = date_json['premium_persons'][0]
	
while True:
	for event in longpoll.listen():
		if event.type == VkBotEventType.MESSAGE_NEW:
			if event.from_chat:

				id = event.chat_id
				msg = event.object.message['text'].lower()
				user_id = event.object.message['from_id']
				try:
					data_user = vk_session.method("users.get", {"user_ids": user_id})[0] #data_user["first_name"] data_user["last_name"]
				except:
					pass


				all_sms += 1
				if all_sms == 40:
					senderUR("СУП")
				if all_sms == 150:
					senderUR("Вы такие крутые!")
				if all_sms == 360:
					senderUR("Понятно")
					senderUR("пахпх")
				if all_sms % 400 == 0:
					part_kpn1 = ''.join(random.choice(string.ascii_lowercase) for x in range(4))
					part_kpn2 = ''.join(random.choice(string.ascii_lowercase) for x in range(4))
					part_kpn3 = ''.join(random.choice(string.ascii_lowercase) for x in range(4))
					part_kpn4 = ''.join(random.choice(string.ascii_lowercase) for x in range(4))
					kupon = f'{part_kpn1}-{part_kpn2}-{part_kpn3}-{part_kpn4}'
					senderUR(f"💳Купон на 25 редисок: {kupon}")
				if all_sms == 800:
					senderUR("еще 200 сообщений	и конфа самоуничтожится")
				if all_sms == 1250:
					senderUR("Я ВАС ОБОЖАЮ!")
				if all_sms == 1310:
					senderUR("аххааххааххааха")
				# if all_sms == 1500:
				# 	senderUR("Не забывайте, что сейчас проходит зимний калейдоскоп! (не проходит)")
				# 	senderUR("Информация тут -> 15 декабря!")
				if all_sms == 1800:
					senderUR("СУП")
				if all_sms == 1000:
					senderUR("Казино открыто")
					
				try:
					kol_sms[str(user_id)] += 1
				except KeyError:
					kol_redisok[str(user_id)] = 0
					kol_sms[str(user_id)] = 1
					deter_ppls[str(user_id)] = 1

				try:
					all_determ = int(deter_ppls['all_detem'])
					determinator = int(deter_ppls[str(user_id)])
					if (kol_sms[str(user_id)] % 10 == 0) and (kol_sms[str(user_id)] > 10):
						kol_redisok[str(user_id)] += determinator * all_determ
				except:
					print("Ошибка в получении редисок!")

				try:
					dey = event.message.action["type"]
					invite_id = event.message.action['member_id']
				except:
					dey = ""
					invite_id = -100

				if dey=="chat_invite_user":
					sender(id, f'Не забываем кидать @id{invite_id}(сиськи)!')
				if dey=='chat_invite_user_by_invitelink':
					sender(id, f'Не забываем кидать @id{invite_id}(сиськи!)')

				if msg in text.bot_dont_work and str(user_id) !="-162946406":
					sender(id, text.hello_bot())
				if msg in text.howareu_user and str(user_id) !="-162946406":
					sender(id, text.howareu_bot())
				if msg in text.howareu_user1 and str(user_id) !="-162946406":
					sender(id, "Нормально, а у тебя как?")
				if msg in text.whatareudoing_user and str(user_id) !="-162946406":
					sender(id, text.whatareudoing_bot())
				if msg in text.bye_user and str(user_id) !="-162946406":
					sender(id, text.bye_bot())
				if msg in text.help_user and str(user_id) !="-162946406":
					sender(id, text.help_bot)
				if (text.card_user[0] in msg) or (text.card_user[1] in msg) and (str(user_id) !="-162946406"):
					sender(id, text.card_bot())
				if msg in text.vel_user:
					vel()
				if msg in text.merch_user and str(user_id) !="-162946406":
					sender(id, text.merch_bot)
				if msg.startswith(text.stavka_user_blue) or msg.startswith(text.stavka_user_red):
					sender(id, check_user_stk(user_id, msg))


				if msg.startswith("!в банк редиски ") or msg.startswith("! в банк редиски "):
					try:
						give_redisk = int(msg.split(" ")[-1])
						if give_redisk <= kol_redisok[str(user_id)] and give_redisk > 0:	
							kol_redisok["full_bank"] += give_redisk
							kol_redisok[str(user_id)] -= give_redisk
							senderUR("Обмен прошёл успешно!")
							senderUR(f"В банке: {kol_redisok['full_bank']} редисок!")
							if kol_redisok["full_bank"] >= 5000:
								senderUR(f"Было куплено улучшение. Общее колчиство получаемых редисок увеличивается на 15%!\n \
Всего 15% 🌟🌟🌟")
								kol_redisok["full_bank"] -= 5000
								deter_ppls["all_detem"] = 1.15
								senderUR(f"В банке: {kol_redisok['full_bank']} редисок!")
						else:
							senderUR("Обмен невозможен!")
					except:
						senderUR("Произошла ошибка!")

				if msg.startswith("!отдать редиски ") or msg.startswith("! отдать редиски "):
					try:
						peer_id = str(event.object.message["reply_message"]['from_id'])
						give_redisk = int(msg.split(" ")[-1])
						if give_redisk < kol_redisok[str(user_id)] and give_redisk > 0:	
							kol_redisok[peer_id] += give_redisk
							kol_redisok[str(user_id)] -= give_redisk
							senderUR("Обмен прошёл успешно!")
							senderUR(f"Осталось {round(kol_redisok[str(user_id)], 1)} редисок!")
						else:
							senderUR("Обмен невозможен!")
					except:
						senderUR("Произошла ошибка!")

# 				if msg = "!я":
# 					senderUR(f'👤{data_user["first_name"]} {data_user["last_name"]}\n\n \
# 🌰{round(kol_redisok[str(user_id)], 1)}\n \
# 💎нет премиума! (!купить премиум 1000)\n ')


				# if msg.startswith("!добавить объявление") or msg.startswith("! добавить объявление"):
				# 	try:
				# 		stikerpak_sell = str(msg.split(" ")[-2]).lower()
				# 		pay_sell = int(msg.split(" ")[-1])
				# 		if pay_sell < 30:
				# 			senderUR("⚠Маленькая цена! (от 30)")
				# 		elif str(user_id) in obyavleniya:
				# 			senderUR("⚠У вас уже есть активное объявление!")
				# 		elif stikerpak_sell not in text.stikers:
				# 			senderUR("⚠Нет такого стикерпака!")
				# 		else:
				# 			obyavleniya[str(user_id)] = f'{data_user["first_name"]} {data_user["last_name"]} : {stikerpak_sell} {pay_sell}'
				# 			senderUR("Объявление зарегистрировано!")
				# 	except:
				# 		senderUR("⚠Произошла ошибка!")

				# if msg == "!удалить объявление":
				# 	try:
				# 		del obyavleniya[str(user_id)]
				# 		senderUR("Объявление успешно удалено!")
				# 	except:
				# 		senderUR("⚠Произошла ошибка!")



				# if msg == "!объявления":
				# 	try:
				# 		main_paypers = ""
				# 		for i in obyavleniya:
				# 			main_paypers += f'👤{obyavleniya[i]} редисок \n\n'
				# 		senderUR(main_paypers)
				# 	except:
				# 		senderUR("⚠Произошла ошибка или объявлений нет!")

				# if msg.startswith("!запрос ") or msg.startswith("! запрос "):
				# 	try:
				# 		stikerpak_need = str(msg.split(" ")[-1]).lower()
				# 		if stikerpak_need not in text.stikers:
				# 			senderUR("⚠Нет такого стикерпака!")
				# 		elif str(user_id) in zaprosi:
				# 			senderUR("⚠У вас уже есть активный запрос!")
				# 		else:
				# 			zaprosi[str(user_id)] = f'{data_user["first_name"]} {data_user["last_name"]} : {stikerpak_need}'
				# 			senderUR("Запрос зарегистрирован!")
				# 	except:
				# 		senderUR("⚠Произошла ошибка!")

				# if msg == "!запросы":
				# 	try:
				# 		zaprosi_all = ""
				# 		for i in zaprosi:
				# 			zaprosi_all += f'👤{zaprosi[i]}\n\n'
				# 		senderUR(zaprosi_all)
				# 	except:
				# 		senderUR("⚠Произошла ошибка или запросов нет!")

				# if msg == "!удалить запрос":
				# 	try:
				# 		del zaprosi[str(user_id)]
				# 		senderUR("Запрос успешно удален!")
				# 	except:
				# 		senderUR("⚠Произошла ошибка!")


				if msg == '!к-премиум 500':
					if kol_redisok[str(user_id)] > 500 and str(user_id) not in premium_persons:
						kol_redisok[str(user_id)] -= 500
						premium_persons[str(user_id)] = 1
						senderUR("✅ Теперь вы можете пользоваться казино без ограничений!")
					else:
						senderUR("❌ У вас мало редисок или уже куплен премиум статус!")


				if msg == "!питомец":
					senderUR("Скоро вы сможете покупать пушистых полькинов! Собирайте редиски!")




				if msg == "!все редиски":
					senderUR(f"Общий капитал: {round(sum([kol_redisok[key] for key in kol_redisok]),1)}")
				if msg == '!редиски казино':
					senderUR(f"В банке казино: {round(kol_redisok['kasino_bank'], 1)} редисок!")

				if (msg.startswith('! казино') or msg.startswith('!казино')) and ((all_sms >= 500) or (str(user_id) in premium_persons)):
					try:
						if str(user_id) in premium_persons:
							gamer_name = f'✨Игрок: {data_user["first_name"]} {data_user["last_name"]}💎\n\n'
							kof_win1 = 3.1
							kof_win2 = 2.1
							predel_stavki = 35
						else:
							gamer_name = f'✨Игрок: {data_user["first_name"]} {data_user["last_name"]}\n\n'
							kof_win1 = 2.9
							kof_win2 = 1.9
							predel_stavki = 20

						r = random.randint(0,36)
						game = msg.split(" ")[-1]
						game_stavka = int(msg.split(" ")[-2])
						game_info = f"🚩Ставка {game_stavka}\n \
🎰Ожиданиие: {game} \n \
🎲На рулетке: {r}\n\n"
						lose_info = "❌Вы проиграли!\n\n"

						if kol_redisok[str(user_id)] > 400 and str(user_id) not in premium_persons:
							senderUR("У вас слишком много денег! Вы крутые!")
							game = 0

						if r == 0:
							kol_redisok[str(user_id)] -= game_stavka
							kol_redisok["kasino_bank"] += game_stavka
							balance_info = f"🌰Ваш баланс: {round(kol_redisok[str(user_id)], 1)}"
							senderUR(gamer_name+game_info+lose_info+balance_info)
						elif game == "1-12" and kol_redisok[str(user_id)] >= game_stavka and game_stavka >= 5 and game_stavka <= predel_stavki and r != 0:
							if r <= 12:	
								kol_redisok[str(user_id)] -= game_stavka
								kol_redisok["kasino_bank"] += game_stavka
								kol_redisok[str(user_id)] += (game_stavka * kof_win1)
								kol_redisok["kasino_bank"] -= (game_stavka * kof_win1)
								win_info = f'✅Вы выиграли {(game_stavka * kof_win1)-game_stavka}\n\n'
								balance_info = f"🌰Ваш баланс: {round(kol_redisok[str(user_id)], 1)}"
								senderUR(gamer_name+game_info+win_info+balance_info)
							else:
								kol_redisok[str(user_id)] -= game_stavka
								kol_redisok["kasino_bank"] += game_stavka
								balance_info = f"🌰Ваш баланс: {round(kol_redisok[str(user_id)], 1)}"
								senderUR(gamer_name+game_info+lose_info+balance_info)
						elif game == "13-24" and kol_redisok[str(user_id)] >= game_stavka and game_stavka >= 5 and game_stavka <= predel_stavki and r != 0:
							if (r >= 13) and (r <= 24):
								kol_redisok[str(user_id)] -= game_stavka
								kol_redisok["kasino_bank"] += game_stavka
								kol_redisok[str(user_id)] += (game_stavka * kof_win1)
								kol_redisok["kasino_bank"] -= (game_stavka * kof_win1)
								win_info = f'✅Вы выиграли {(game_stavka * kof_win1)-game_stavka}\n\n'
								balance_info = f"🌰Ваш баланс: {round(kol_redisok[str(user_id)], 1)}"
								senderUR(gamer_name+game_info+win_info+balance_info)
							else:
								kol_redisok[str(user_id)] -= game_stavka
								kol_redisok["kasino_bank"] += game_stavka
								balance_info = f"🌰Ваш баланс: {round(kol_redisok[str(user_id)], 1)}"
								senderUR(gamer_name+game_info+lose_info+balance_info)
						elif game == "25-36" and kol_redisok[str(user_id)] >= game_stavka and game_stavka >= 5 and game_stavka <= predel_stavki and r != 0:
							if (r >= 25) and (r <= 36):
								kol_redisok[str(user_id)] -= game_stavka
								kol_redisok["kasino_bank"] += game_stavka
								kol_redisok[str(user_id)] += (game_stavka * kof_win1)
								kol_redisok["kasino_bank"] -= (game_stavka * kof_win1)
								win_info = f'✅Вы выиграли {(game_stavka * kof_win1)-game_stavka}\n\n'
								balance_info = f"🌰Ваш баланс: {round(kol_redisok[str(user_id)], 1)}"
								senderUR(gamer_name+game_info+win_info+balance_info)
							else:
								kol_redisok[str(user_id)] -= game_stavka
								kol_redisok["kasino_bank"] += game_stavka
								balance_info = f"🌰Ваш баланс: {round(kol_redisok[str(user_id)], 1)}"
								senderUR(gamer_name+game_info+lose_info+balance_info)
						elif game == "четное" and kol_redisok[str(user_id)] >= game_stavka and game_stavka >= 5 and game_stavka <= predel_stavki and r != 0:
							if (r%2 == 0) and r != 0:
								kol_redisok[str(user_id)] -= game_stavka
								kol_redisok["kasino_bank"] += game_stavka
								kol_redisok[str(user_id)] += (game_stavka * kof_win2)
								kol_redisok["kasino_bank"] -= (game_stavka * kof_win2)
								win_info = f'✅Вы выиграли {(game_stavka * kof_win2)-game_stavka}\n\n'
								balance_info = f"🌰Ваш баланс: {round(kol_redisok[str(user_id)], 1)}"
								senderUR(gamer_name+game_info+win_info+balance_info)
							else:
								kol_redisok[str(user_id)] -= game_stavka
								kol_redisok["kasino_bank"] += game_stavka
								balance_info = f"🌰Ваш баланс: {round(kol_redisok[str(user_id)], 1)}"
								senderUR(gamer_name+game_info+lose_info+balance_info)
						elif game == "нечетное" and kol_redisok[str(user_id)] >= game_stavka and game_stavka >= 5 and game_stavka <= predel_stavki and r != 0:
							if (r%2 == 1) and r != 0:
								kol_redisok[str(user_id)] -= game_stavka
								kol_redisok["kasino_bank"] += game_stavka
								kol_redisok[str(user_id)] += (game_stavka * kof_win2)
								kol_redisok["kasino_bank"] -= (game_stavka * kof_win2)
								win_info = f'✅Вы выиграли {(game_stavka * kof_win2)-game_stavka}\n\n'
								balance_info = f"🌰Ваш баланс: {round(kol_redisok[str(user_id)], 1)}"
								senderUR(gamer_name+game_info+win_info+balance_info)
							else:
								kol_redisok[str(user_id)] -= game_stavka
								kol_redisok["kasino_bank"] += game_stavka
								balance_info = f"🌰Ваш баланс: {round(kol_redisok[str(user_id)], 1)}"
								senderUR(gamer_name+game_info+lose_info+balance_info)
						else:
							senderUR("❗Игра невозможна❗\n \
Убедитесь что ваша ставка от 5 до 20 редисок\n \
Выбранный лот доллжен быть (1-12/13-24/25-36/четное/нечетное)")
					except:
						senderUR("⚠Произошла ошибка!")
				if msg.startswith('! казино') or msg.startswith('!казино') and all_sms <= 500 and str(user_id) not in premium_persons:
					senderUR(f"⚠До откытия казино осталось : {500-all_sms} сообщений")


				if msg.startswith("!купон ") or msg.startswith("! купон "):
					kpn = msg.split(" ")[-1]
					if kpn == kupon:
						kol_redisok[str(user_id)] += 25
						senderUR("💳Купон принят!\n🌰Вы получили 25 редисок!")
						kupon = "0x00x0000s0000d00fdsf0sdgadasdgwaefdKSDJFAWEIOFJ98wef9q342amwfe9"
					else:
						senderUR("Купон не найден!")

				if msg == "!карта премиума":
					for i in premium_persons:
						if user_id == i:
							sender(id, f'Вы уже имеете премиум статус!')



				if "+" in msg and str(user_id) !="-162946406":
					kol_redisok[str(user_id)] -= 4
					kol_redisok["265618599"] += 2
					kol_redisok["241895651"] += 2
					senderUR("МИНУС РЕДИСКА!")
					sender(id, f"Плюс поставил - 50 руб отдал!@id{user_id}(Читай правила!)")


				if msg == "!магазин":
					senderUR("🏪МАГАЗИН УЧАСТНИКА🏪\n\n \
📈1) Плюс 20% к получаемым редискам!⚡ (Цена 300)\n \
Команда - !купить ул1\n \
📈2) Плюс 40% к получаемым редискам!⚡⚡ (Цена 500)\n \
Команда - !купить ул2\n \
📈3) Плюс 65% к получаемым редискам!⚡⚡⚡ (Цена 1000)\n \
Команда - !купить ул3\n \
📈4) Плюс 100% к получаемым редискам!⚡⚡⚡⚡ (Цена 2000)\n \
Команда - !купить ул4\n \
📈5) Плюс 200% к получаемым редискам!⚡⚡⚡⚡⚡ (Цена 5000)\n \
Команда - !купить ул5\n \
📈6) Плюс 300% к получаемым редискам!⚡⚡⚡⚡⚡⚡ (Цена 10000)\n \
Команда - !купить ул6\n\n\n \
🏪ОБЩИЙ МАГАЗИН🏪\n\n \
Плюс 15% к получаемым редискам!🌟🌟🌟 (Цена 5000)\n \
Команда - !в банк редиски (число)")

				if (msg == "!купить ул1") and (str(user_id) !="-162946406"):
					if deter_ppls[str(user_id)] >= 1.2:
						senderUR("❗Вы уже купили это улучшение!")
					if kol_redisok[str(user_id)] >= 300 and deter_ppls[str(user_id)] < 1.2:
						deter_ppls[str(user_id)] = 1.2
						kol_redisok[str(user_id)] -= 300
						senderUR("✅Покупка прошла успешно!")
					else:
						senderUR(f"⚠Не хватает редисок! Необходимо 300. У вас {round(kol_redisok[str(user_id)], 1)}")

				if (msg == "!купить ул2") and (str(user_id) !="-162946406"):
					if deter_ppls[str(user_id)] >= 1.4:
						senderUR("❗Вы уже купили это улучшение!")
					if kol_redisok[str(user_id)] >= 500 and deter_ppls[str(user_id)] < 1.4:
						deter_ppls[str(user_id)] = 1.4
						kol_redisok[str(user_id)] -= 500
						senderUR("✅Покупка прошла успешно!")
					else:
						senderUR(f"⚠Не хватает редисок! Необходимо 500. У вас {round(kol_redisok[str(user_id)], 1)}")

				if (msg == "!купить ул3") and (str(user_id) !="-162946406"):
					if deter_ppls[str(user_id)] >= 1.65:
						senderUR("❗Вы уже купили это улучшение!")
					if kol_redisok[str(user_id)] >= 1000 and deter_ppls[str(user_id)] < 1.65:
						deter_ppls[str(user_id)] = 1.65
						kol_redisok[str(user_id)] -= 1000
						senderUR("✅Покупка прошла успешно!")
					else:
						senderUR(f"⚠Не хватает редисок! Необходимо 1000. У вас {round(kol_redisok[str(user_id)], 1)}")

				if (msg == "!купить ул4") and (str(user_id) !="-162946406"):
					if deter_ppls[str(user_id)] >= 2:
						senderUR("❗Вы уже купили это улучшение!")
					if kol_redisok[str(user_id)] >= 2000 and deter_ppls[str(user_id)] < 2:
						deter_ppls[str(user_id)] = 2
						kol_redisok[str(user_id)] -= 2000
						senderUR("✅Покупка прошла успешно!")
					else:
						senderUR(f"⚠Не хватает редисок! Необходимо 2000. У вас {round(kol_redisok[str(user_id)], 1)}")

				if (msg == "!купить ул5") and (str(user_id) !="-162946406"):
					if deter_ppls[str(user_id)] >= 3:
						senderUR("❗Вы уже купили это улучшение!")
					if kol_redisok[str(user_id)] >= 5000 and deter_ppls[str(user_id)] < 3:
						deter_ppls[str(user_id)] = 3
						kol_redisok[str(user_id)] -= 5000
						senderUR("✅Покупка прошла успешно!")
					else:
						senderUR(f"⚠Не хватает редисок! Необходимо 5000. У вас {round(kol_redisok[str(user_id)], 1)}")

				if (msg == "!купить ул6") and (str(user_id) !="-162946406"):
					if deter_ppls[str(user_id)] >= 4:
						senderUR("❗Вы уже купили это улучшение!")
					if kol_redisok[str(user_id)] >= 10000 and deter_ppls[str(user_id)] < 4:
						deter_ppls[str(user_id)] = 4
						kol_redisok[str(user_id)] -= 10000
						senderUR("✅Покупка прошла успешно!")
					else:
						senderUR(f"⚠Не хватает редисок! Необходимо 10000. У вас {round(kol_redisok[str(user_id)], 1)}")

				# if msg == "!пополнить редиски":
				# 	senderUR("💰Поплнение возможно от 100 редисок (20 руб)")
				# 	senderUR("<- пишите в личные сообщения бота для пополнения")

				# if msg == '!вывести редиски':
				# 	senderUR("💰Вывод возможен от 500 редисок (50 руб)")
				# 	senderUR("<- пишите в личные сообщения бота для вывода")

				# if msg == "!курс редиски":
				# 	senderUR("Покупка: 0,2 руб")
				# 	senderUR("Продажа: 0,1 руб")

				if msg in text.redis_user and str(user_id) !="-162946406":
					try:
						sender(id, f'🌰У @id{user_id}(тебя) {round(kol_redisok[str(user_id)], 1)} редисок!')
						if deter_ppls[str(user_id)] == 1.2:
							senderUR("Дополнительный доход 20% \n⚡")
						if deter_ppls[str(user_id)] == 1.4:
							senderUR("Дополнительный доход 40% \n⚡⚡")
						if deter_ppls[str(user_id)] == 1.65:
							senderUR("Дополнительный доход 65% \n⚡⚡⚡")
						if deter_ppls[str(user_id)] == 2:
							senderUR("Дополнительный доход 100% \n⚡⚡⚡⚡")
						if deter_ppls[str(user_id)] == 3:
							senderUR("Дополнительный доход 200% \n⚡⚡⚡⚡⚡")
						if deter_ppls[str(user_id)] == 4:
							senderUR("Дополнительный доход 300% \n⚡⚡⚡⚡⚡⚡")
					except KeyError:
						kol_redisok[str(user_id)] = 0
						sender(id, f'🌰У @id{user_id}(тебя) {round(kol_redisok[str(user_id)], 1)} редисок!')

				if msg in text.bank_user:
					senderUR(f"💰В банке: {kol_redisok['full_bank']} редисок!💰\n \
Дополнительный общий доход: 10% 🌟🌟")

				# if all_sms == 2:
				# 	for kei in kol_redisok:
				# 		try:
				# 			if kol_sms[kei] > 10:
				# 				kol_redisok[kei] += 35
				# 		except:
				# 			continue
				# 	senderUR("Технические работы завершились! Все получили по 35 редисок\nСегодня казино открыто весь день!\n Так же сегодня за сообщения дают бонусных 30%!")

				# if kol_sms[str(user_id)] == 300:
				# 	sender(id, f"Поздравляем, @id{user_id}(ВЫ) заработали написали 300 сообщений!")
				# 	sender(6, f"@id{user_id}(Гадость) +1 шт.")
				# if kol_sms[str(user_id)] == 110:
				# 	sender(id, f'Поздравляем, @id{user_id}(У ТЕБЯ) 10 редисок и ты можешь делать ставки!')

				saves = {"kol_sms":[kol_sms],'kol_redisok':[kol_redisok], 'deter_ppls':[deter_ppls], \
				"obyavleniya":[obyavleniya], 'zaprosi':[zaprosi], 'premium_persons':[premium_persons]}
				with open('date.json', 'w') as file:
					json.dump(saves, file, indent=2, ensure_ascii=False)


		if event.type == VkBotEventType.WALL_POST_NEW:
			senderUR("Новый пост в группе! https://vk.com/uselessrednecks")