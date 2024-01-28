# Mailing_service

Сервис для создания рассылок для ваших клиентов.

## Требования

python = "^3.11"

django = "^4.2.4"

python-dotenv = "^1.0.0"

psycopg2-binary = "^2.9.7"

pillow = "^10.0.0"


## Установка

1. Клонируйте репозиторий
2. Создайте виртуальное окружение: `poetry init`
3. Активируйте виртуальное окружение:
    - `poetry shell`
4. Установите зависимости: `poetry install`
5. Примените миграции: `python manage.py migrate`

## Использование

Зарегистрируйтесь на проекте и подтвердите регистрацию по ссылке в почте.
Далее вы можете создать рассылки для своих клиентов. После создание рассылки apschduler автоматически отправит письмо в нужное время и изменит расписание следующей отправки.


### Примеры


    def process_pending_mailings():
    
    now = timezone.now() + timedelta(hours=3)
    logger.info("Processing")
    pending_mailings = Mailing.objects.all()

    for mailing in pending_mailings:
        next_send_time = calculate_next_send_time(mailing.frequency, mailing.mailing_time)

        match mailing.status:

            case Mailing.Status.CREATED:
                if mailing.mailing_time <= now:
                    clients = mailing.clients.all()
                    for client in clients:
                        send_email(mailing, client)
                    mailing.status = Mailing.Status.STARTED
                    mailing.mailing_time = next_send_time
                    mailing.save()

            case Mailing.Status.STARTED:
                if mailing.mailing_time <= now:
                    clients = mailing.clients.all()
                    for client in clients:
                        send_email(mailing, client)
                    mailing.mailing_time = next_send_time
                    mailing.save()

