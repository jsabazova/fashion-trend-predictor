# For flask backend:
FROM python:3.9-slim
WORKDIR /app
COPY ./backend /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]

# for frontend
FROM node:16
WORKDIR /app
COPY ./frontend /app
RUN npm install
RUN npm run build

