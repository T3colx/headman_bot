#!/usr/bin/python
# -*- coding: utf-8 -*-

import telebot
import config
import dbworker
from telebot import types

##############################

bot = telebot.TeleBot(config.token)

##############################

back = "← Back"
top = "↑ Top"

start_panel = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
start_panel.add("↓ Преподы", "↓ Полезные ссылки", "Calendar", "Drive")

professor_panel = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
professor_panel.add("↓ Физика", "↓ Прога / Информатика", "Английский", "Деканат")
professor_panel.add(back)

professor_physics_panel = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
professor_physics_panel.add("Лекции", "Лабораторные", "Практика")
professor_physics_panel.add(back, top)

professor_programming_panel = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
professor_programming_panel.add("Лекции", "Практика", "Основы информатики")
professor_programming_panel.add(back, top)

useful_links_panel = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
useful_links_panel.add("ЛК Студента", "Карта кампуса", "↓ Курсы", "↓ Актуал04ка",  "Закрытие метро")
useful_links_panel.add(back)

useful_links_choosing_course_panel = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
useful_links_choosing_course_panel.add("ИКНТ'шные", "Не ИКНТ'шные", "Гуманитарные", "Open Edu")
useful_links_choosing_course_panel.add(back, top)

useful_links_fresh_news_panel = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
useful_links_fresh_news_panel.add("Медком", "Студкарта", "Скидки", "СтудПодписки")
useful_links_fresh_news_panel.add(back, top)


######################################################
######################################################


######################################################
#                                                    #
#             Start menu and top button              #
#                                                    #
######################################################

def top_action(message_0):
    bot.send_message(message_0.chat.id,
                     "Я вас категорически приветствую!\n"
                     "Чем могу помочь?",
                     reply_markup=start_panel)
    dbworker.set_state(message_0.chat.id, config.States.S_START.value)


def choosing_subject_action(message_0):
    dbworker.set_state(message_0.chat.id, config.States.S_PROFESSORS.value)
    bot.send_message(message_0.chat.id, "Выберите предмет.", reply_markup=professor_panel)


def choosing_link_action(message_0):
    dbworker.set_state(message_0.chat.id, config.States.S_USEFUL_LINKS.value)
    bot.send_message(message_0.chat.id, "Выберите категорию.", reply_markup=useful_links_panel)


######################################################


@bot.message_handler(commands=["start"])
def cmd_start(message):
    top_action(message)


@bot.message_handler(content_types=["text"],
                     func=lambda message:
                     dbworker.get_current_state(message.chat.id) == config.States.S_START.value)
def welcome_message(message):
    if message.text == "↓ Преподы":
        choosing_subject_action(message)
    elif message.text == "↓ Полезные ссылки":
        choosing_link_action(message)
    elif message.text == "Calendar":
        bot.send_message(message.chat.id, config.g_calendar)
    elif message.text == "Drive":
        bot.send_message(message.chat.id, config.g_drive)


@bot.message_handler(commands=["reset"])
def cmd_reset(message):
    bot.send_message(message.chat.id, "Начнём по-новой.")
    dbworker.set_state(message.chat.id, config.States.S_START.value)


######################################################
######################################################


######################################################
#                                                    #
#                  Professors page                   #
#                                                    #
######################################################


@bot.message_handler(content_types=["text"],
                     func=lambda message:
                     dbworker.get_current_state(message.chat.id) == config.States.S_PROFESSORS.value)
def professor_page(message):
    if message.text == "↓ Физика":
        dbworker.set_state(message.chat.id, config.States.S_PROFESSORS_PHYSICS.value)
        bot.send_message(message.chat.id, "Выберите препода.", reply_markup=professor_physics_panel)
    elif message.text == "↓ Прога / Информатика":
        dbworker.set_state(message.chat.id, config.States.S_PROFESSORS_PROGRAMMING.value)
        bot.send_message(message.chat.id, "Выберите препода.", reply_markup=professor_programming_panel)
    elif message.text == "Английский":
        bot.send_message(message.chat.id, "Пятницкий Алексей Николаевич\n"
                                          "E-mail: pyatnitskij_an@spbstu.ru")
    elif message.text == "Деканат":
        bot.send_message(message.chat.id, "*переезжает*")
    #######################################################################
    elif message.text == back:
        top_action(message)


@bot.message_handler(content_types=["text"],
                     func=lambda message:
                     dbworker.get_current_state(message.chat.id) == config.States.S_PROFESSORS_PHYSICS.value)
def professors_physics_page(message):
    if message.text == "Лекции":
        bot.send_message(message.chat.id, "Андреева Татьяна Николаевна\n"
                                          "E-mail: andreeva_ta@spbstu.ru")
    elif message.text == "Лабораторные":
        bot.send_message(message.chat.id, "Крупина Марина Алексеевна\n"
                                          "E-mail: krupina_ma@spbstu.ru")
    elif message.text == "Практика":
        bot.send_message(message.chat.id, "Герчиков Леонид Григорьевич\n"
                                          "E-mail: gerchikov_lg@spbstu.ru")
    #######################################################################
    elif message.text == back:
        choosing_subject_action(message)
    elif message.text == top:
        top_action(message)


@bot.message_handler(content_types=["text"],
                     func=lambda message:
                     dbworker.get_current_state(message.chat.id) == config.States.S_PROFESSORS_PROGRAMMING.value)
def professor_programming_page(message):
    if message.text == "Лекции":
        bot.send_message(message.chat.id, "Глухих Михаил Игоревич\n"
                                          "E-mail: glukhikh@mail.ru\n"
                                          "VK: vk.com/mike_gl\n"
                                          "Telegram: t.me/kotlinasfirst2020")
    elif message.text == "Практика":
        bot.send_message(message.chat.id, "Валерий ... <Отчество>... Соболь\n"
                                          "Telegram: @conyashka")
    elif message.text == "Основы информатики":
        bot.send_message(message.chat.id, "Новопашенный Андрей Гелиевич\n"
                                          "E-mail: nov-andr@yandex.ru\n"
                                          "E-mail: anovo@spbstu.ru")
    #######################################################################
    elif message.text == top:
        top_action(message)
    elif message.text == back:
        choosing_subject_action(message)


######################################################
######################################################


######################################################
#                                                    #
#                 Useful links page                  #
#                                                    #
######################################################

@bot.message_handler(content_types=["text"],
                     func=lambda message:
                     dbworker.get_current_state(message.chat.id) == config.States.S_USEFUL_LINKS.value)
def choosing_link_page(message):
    if message.text == "ЛК Студента":
        bot.send_message(message.chat.id, "https://lk.spbstu.ru/")
    elif message.text == "↓ Курсы":
        dbworker.set_state(message.chat.id, config.States.S_USEFUL_LINKS_COURSES.value)
        bot.send_message(message.chat.id, "В наличии есть:", reply_markup=useful_links_choosing_course_panel)
    elif message.text == "Карта кампуса":
        bot.send_message(message.chat.id, "https://www.spbstu.ru/campus-map/")
    elif message.text == "Закрытие метро":
        bot.send_message(message.chat.id, "http://www.metro.spb.ru/rejimrabotystancii.html")
    elif message.text == "↓ Актуал04ка":
        dbworker.set_state(message.chat.id, config.States.S_USEFUL_LINKS_FRESH_NEWS.value)
        bot.send_message(message.chat.id, "Выберите ", reply_markup=useful_links_fresh_news_panel)

    #######################################################################
    elif message.text == back:
        top_action(message)


@bot.message_handler(content_types=["text"],
                     func=lambda message:
                     dbworker.get_current_state(message.chat.id) == config.States.S_USEFUL_LINKS_COURSES.value)
def choosing_course_page(message):
    if message.text == "Гуманитарные":
        bot.send_message(message.chat.id, "https://dl-hum.spbstu.ru/")
    elif message.text == "Не ИКНТ'шные":
        bot.send_message(message.chat.id, "https://lms.spbstu.ru/")
    elif message.text == "ИКНТ'шные":
        bot.send_message(message.chat.id, "https://dl.spbstu.ru/")
    elif message.text == "Open Edu":
        bot.send_message(message.chat.id, "https://sso.openedu.ru/")
    #######################################################################
    elif message.text == top:
        top_action(message)
    elif message.text == back:
        choosing_link_action(message)


@bot.message_handler(content_types=["text"],
                     func=lambda message:
                     dbworker.get_current_state(message.chat.id) == config.States.S_USEFUL_LINKS_FRESH_NEWS.value)
def choosing_fresh_news_page(message):
    if message.text == "Медком":
        bot.send_message(message.chat.id, "https://www.spbstu.ru/freshman/medical/medical.html")
    elif message.text == "Студкарта":
        bot.send_message(message.chat.id, "https://www.spbstu.ru/freshman/card/card.html")
    elif message.text == "Скидки":
        bot.send_message(message.chat.id, "--  РЖД - Бонус \n"
                                          "Вам будет предоставлена скидка в размере 25% на проезд в купейных вагонах "
                                          "и вагонах с местами для сидения.\n"
                                          "Что нужно сделать?\n"
                                          "- Получить справку в автомате в главном здании или в 1 корпусе.\n"
                                          "- На сайте rzd-bonus.ru через обратную связь прикрепить фотографию "
                                          "справки.\n\n"
                                          "Скидка будет действовать до 1 сентября следующего учебного года.\n\n"
                                          "-- Эрмитаж \n"
                                          "Бесплатные посещения. \n\n"
                                          "-- Этнографический музей \n"
                                          "-- Суворовский музей \n"
                                          "-- Кунсткамера \n"
                                          "Билеты за 100 рублей.\n\n"
                                          "-- Формула кино/Синема парк \n"
                                          "Скидка 20% на билеты.\n\n"
                                          "-- Михайловский театр \n"
                                          "Скидка 50% на билеты.\n\n"
                                          "-- Батутный клуб «720». \n\n"
                                          "-- Каток на Новой Голландии. \n"
                                          "-- Каток на Гагарин парке. \n\n"
                                          "Главное, всегда иметь при себе студенческий билет.")

    elif message.text == "СтудПодписки":
        bot.send_message(message.chat.id, "-- Apple Music\n"
                                          "-- Vk music/Boom\n"
                                          "-- Spotify\n"
                                          "-- Microsoft Office 365 и OneDrive\n"
                                          "-- Matlab\n"
                                          "-- Autodesk\n"
                                          "-- Adobe\n\n"
                                          "Для оформления необходимо входить под корпоративной почтой Политеха")
    #######################################################################
    elif message.text == top:
        top_action(message)
    elif message.text == back:
        choosing_link_action(message)


######################################################
######################################################


######################################################
#                                                    #
#                    Running bot                     #
#                                                    #
######################################################


if __name__ == "__main__":
    bot.infinity_polling()
