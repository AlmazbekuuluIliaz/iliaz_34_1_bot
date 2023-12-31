from aiogram import types, Dispatcher
from config import bot
from keyboards.inline_buttons import questionnaire_one_keyboard
# from scraping.news_scraper import NewsScraper
from database.sql_commands import Database
from handlers.reference_menu import check_balance


async def start_questionnaire(call: types.CallbackQuery):
    print(call)
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="R u hungry ?",
        reply_markup=await questionnaire_one_keyboard()
    )

async def yes_answer(call: types.CallbackQuery):
    print(call)
    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="Ok",
    )

async def no_answer(call: types.CallbackQuery):
    print(call)
    await bot.delete_message(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id
    )
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="Glad you r not hungry",
    )
# async def latest_news_call(call: types.CallbackQuery):
#     scraper = NewsScraper()
#     links = scraper.parse_data()
#     for link in links:
#         await bot.send_message(
#             chat_id=call.message.chat.id,
#             text=scraper.PLUS_URL + link,
#         )
async def check_balance_call(call: types.CallbackQuery):
    balance = await check_balance(call.from_user.id, Database())
    await bot.send_message(
        chat_id=call.from_user.id,
        text=f"Ваш баланс: {balance} баллов"
    )
def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionnaire,
                                       lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(yes_answer,
                                       lambda call: call.data == "hungry_yes")
    dp.register_callback_query_handler(no_answer,
                                       lambda call: call.data == "hungry_no")
    # dp.register_callback_query_handler(latest_news_call,
    #                                    lambda call: call.data == "latest_news")