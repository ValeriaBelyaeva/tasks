from bot_text import anikdoti
import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(
    token='a371464ee45c256f1d2fd5d2425e0b23b6cf431845b6c5f8af24c8b3f30a8a29cc007ab6ede4323cfcc23')

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
name = 0
is_time = False
do = True
list_go = False
list_go2 = False
name_go = False
plan_test = []

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        # Слушаем longpoll, если пришло сообщение то:
        if list_go:
            if not list_go2:

                list_go = True
                point = ''
                sign = 1
                for char in event.text.lower():
                    if char in '0123456789':
                        point += char
                if point != '':
                    point = int(point)
                    tmp_point = point
                    list_go2 = True
            if point != "":
                if tmp_point - point < tmp_point + 1:

                    if tmp_point - point == -1:
                        if tmp_point - point == 0:
                            vk.messages.send(  # Отправляем собщение
                                user_id=event.user_id,
                                random_id="",
                                message='введи ' + str(tmp_point - point + 1) + ' пункт: ')

                    elif tmp_point - point == tmp_point:
                        plan.append(event.text.lower())
                        if len(event.text.lower()) > 1:
                            plan_test.append(event.text.lower()[:-1])
                        else:
                            plan_test.append(event.text.lower())

                    else:
                        plan.append(event.text.lower())
                        if len(event.text.lower()) > 1:
                            plan_test.append(event.text.lower()[:-1])
                        else:
                            plan_test.append(event.text.lower())

                        vk.messages.send(  # Отправляем собщение
                            user_id=event.user_id,
                            random_id="",
                            message='введи ' + ' пункт: ' + str(tmp_point - point + 1))

                    point -= 1

                    if tmp_point - point == tmp_point + 1:
                        vk.messages.send(  # Отправляем собщение, составь список
                            user_id=event.user_id,
                            random_id="",
                            message='Ваш план создан!')
                        list_go = False
                        list_go2 = False
            else:
                list_go = False
                list_go2 = False

        elif 'прив' in event.text.lower():
            vk.messages.send(  # Отправляем собщение
                user_id=event.user_id,
                random_id="",
                message='Привет! Я чат бот. Хочешь узнать, что я умею?')

        elif ('анекдот' in event.text.lower() or 'ещё' in event.text.lower()) and not (
                'не хочу анекдот' in event.text.lower()):
            nom = random.randint(0, 17)
            vk.messages.send(  # Отправляем собщение
                user_id=event.user_id,
                random_id="",
                message=str(anikdoti[nom]))

        elif ':(' in event.text.lower():
            nom = random.randint(0, 3)
            vk.messages.send(  # Отправляем собщение
                user_id=event.user_id,
                random_id="",
                message=':)')

        elif ('имя' in event.text.lower() or 'зовут' in event.text.lower()) and 'запомни' in event.text.lower():
            vk.messages.send(  # Отправляем собщение
                user_id=event.user_id,
                random_id="",
                message='Напиши своё имя: ')
            name_go = True

        elif name_go:
            name = event.text
            vk.messages.send(  # Отправляем собщение
                user_id=event.user_id,
                random_id="",
                message='Я запомнил.')
            name_go = False

        elif 'как ' in event.text.lower() and 'меня' in event.text.lower() and not ('запомни ' in event.text.lower()):
            if name:
                vk.messages.send(  # Отправляем собщение
                    user_id=event.user_id,
                    random_id="",
                    message='Тебя зовут ' + name)
            else:
                vk.messages.send(  # Отправляем собщение
                    user_id=event.user_id,
                    random_id="",
                    message='Ты не говорил как тебя зовут.')

        elif 'составь' in event.text.lower() and ('план' in event.text.lower() or 'список' in event.text.lower()):
            plan = []
            plan_test = []
            vk.messages.send(  # Отправляем собщение
                user_id=event.user_id,
                random_id="",
                message='Сколько в нём будет пунктов?')
            list_go = True

        elif ('какой' in event.text.lower() or 'покажи' in event.text.lower()) and (
                'план' in event.text.lower() or 'список' in event.text.lower()):
            if len(plan):
                string = ''
                for i in range(len(plan)):
                    if i != 0:
                        string += str(plan[i]) + ', '

                vk.messages.send(  # Отправляем собщение
                    user_id=event.user_id,
                    random_id="",
                    message='Вот ваш план: ' + string)
            else:
                vk.messages.send(  # Отправляем собщение
                    user_id=event.user_id,
                    random_id="",
                    message='Ты ещё не составлял план.')

        elif 'умеешь' in event.text.lower() or 'да' in event.text.lower():
            vk.messages.send(  # Отправляем собщение
                user_id=event.user_id,
                random_id="",
                message='''Я умею составлять списки, могу запомнить твоё имя, расскажу тебе анекдот.''')

        elif 'пок' in event.text.lower() and not "покажи" in event.text.lower():
            vk.messages.send(  # Отправляем собщение
                user_id=event.user_id,
                random_id="",
                message="Пока")
            do = False

        else:
            vk.messages.send(  # Отправляем собщение
                user_id=event.user_id,
                random_id="",
                message='Я тебя не понял.')
