from aiogram.dispatcher.filters.state import StatesGroup, State


class AdminStatesGroup(StatesGroup):
    """Состояния в которых может находиться admin"""
    # скрытое поле для главного админа чтобы управлять другими админами
    control_admins = State()

    # когда главный админ выбрал 1 из админов
    choose_admin = State()

    # выдача новых прав для админа
    get_rights = State()

    # скрытое поле для всех админов
    hide_field = State()

    # ввод нового пароля
    enter_new_password = State()

    # подтверждение пароля 1 админа
    enter_pass_conf = State()

    # ввод пароля при входе
    enter_password = State()

    # состояние панель админа
    adm_control_panel = State()

    # бот находиться в состоянии получения названия мероприятия
    e_name = State()

    # дата
    e_date = State()

    # ожидаем описание мероприятия
    e_descript = State()

    # получаем фото
    get_photo = State()

    # получаем ссылку
    get_link = State()

    # подтверждение созданного события
    ads_confirmation = State()

    # редактирование событий
    edit_advs = State()

    # выбор нужного события
    choose_edit_advs = State()

    # меню бургеров
    burgers_menu = State()

    # ввод названия нового товара
    name_new_product = State()

    # фотка еды
    get_photo_dish = State()

    # описание товара
    dish_descript = State()

    # цена товара
    dish_price = State()

    # подтверждение правильно собранной карточки
    dish_confirmation = State()

    # выбор товара для редактирования
    choose_edit_dish = State()

    # редактирование блюда (Удаление/Изменение)
    edit_dish = State()
