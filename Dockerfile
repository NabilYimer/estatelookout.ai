FROM python:3.11


WORKDIR usr/app/src   

copy . .
RUN pip install -r ./requirements.txt && \
    python -m spacy download en_core_web_sm


CMD ["streamlit", "run", "app/app.py"]

