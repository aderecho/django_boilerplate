# Laravel-Style Django API Boilerplate

Production-ready Django REST API boilerplate with:

- Django + DRF
- PostgreSQL
- JWT auth
- Pagination and filtering
- Swagger / OpenAPI docs
- Celery + Redis
- Gunicorn
- Nginx reverse proxy
- Environment-based settings
- Laravel-like folder layout:
  - controllers
  - services
  - models
  - routes
  - transformers
  - helpers
  - middlewares

---

## 📁 Project Structure

```bash
my_django_api/
├── docker-compose.yml
├── docker-compose.dev.yml
├── docker-compose.prod.yml
├── Dockerfile
├── .dockerignore
├── .env.dev
├── .env.prod.example
├── requirements/
│   ├── base.txt
│   └── dev.txt
├── nginx/
│   └── default.conf
├── src/
│   ├── manage.py
│   ├── config/
│   │   ├── asgi.py
│   │   ├── wsgi.py
│   │   ├── urls.py
│   │   └── settings/
│   │       ├── base.py
│   │       ├── development.py
│   │       └── production.py
│   └── app/
│       ├── controllers/
│       ├── services/
│       ├── models/
│       ├── routes/
│       ├── transformers/
│       ├── helpers/
│       ├── middlewares/
│       └── modules/
│           └── users/
```

---

## ⚙️ Requirements

- Docker & Docker Compose
- Python 3.12+

---

### Development

```bash
cp .env.dev .env
docker compose -f docker-compose.dev.yml up --build
```

Open:

- API: http://localhost:8000/api/v1/
- Swagger: http://localhost:8000/api/docs/
- Redoc: http://localhost:8000/api/redoc/

---

### Production

```bash
cp .env.prod.example .env.prod
docker compose -f docker-compose.prod.yml up --build -d
```

---

## First commands

```bash
docker compose -f docker-compose.dev.yml up --build
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```
---

## Auth endpoints

- `POST /api/v1/auth/register/`
- `POST /api/v1/auth/login/`
- `POST /api/v1/auth/refresh/`
- `POST /api/v1/auth/logout/`
- `GET /api/v1/auth/me/`

## Sample CRUD endpoints

- `GET /api/v1/posts/`
- `POST /api/v1/posts/`
- `GET /api/v1/posts/{id}/`
- `PUT /api/v1/posts/{id}/`
- `DELETE /api/v1/posts/{id}/`

## Health endpoint

- `GET /health/`

## Filtering and pagination

Examples:

```bash
GET /api/v1/posts/?search=django
GET /api/v1/posts/?status=published
GET /api/v1/posts/?ordering=-created_at
GET /api/v1/posts/?page=2&page_size=5
```


## 👨‍💻 Author

AOD