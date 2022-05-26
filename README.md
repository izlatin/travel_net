# travel_net
Социальная сеть для любителей путешествований и нестандартного отдыха

## функционал
1. Посты, лайки, комменты, лайки на комментах
2. Бесконечный скорлл на ленте
3. Личный профиль - аватарка + имя фамилия
4. В каждом посте есть вложенная геолокация + вложения картинок (опционально)
5. Карта с отображением самых популярных постов на местности

## как запустить 
1. git clone
2. создать `.env` и положить в папку travelnet/, можно использовать `example.env` за основу
3. `cd travelnet && python manage.py runserver`
4. profit 😎

### переменные .env 
- `MAPBOX_TOKEN` - Токен для mapbox, без него на фронте не будет грузиться карта (как и запускаться проект)
- `DEBUG` - дебаг, true/false
- `SECRET_KEY` - secret key, рандомный набор знаков для криптографии в джанго

