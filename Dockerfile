FROM python:3.13-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE = 1

ENV PYTHONUNBUFFERED = 1

WORKDIR /app

RUN apt-get update && apt-get upgrade

RUN apt-get install -y curl

# use uv to manage python dependencies
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/ 

COPY ./requirements.txt .

RUN uv pip install -r requirements.txt --system 

COPY . .

EXPOSE 8080

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8080" ]