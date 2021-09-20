FROM python:3.9

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV API_KEY None

COPY . .

EXPOSE 8080

RUN sh setup.sh

CMD ["streamlit", "run", "app.py"]