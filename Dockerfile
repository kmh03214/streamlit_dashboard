# app/Dockerfile

FROM streamlit

WORKDIR /app

RUN apt-get update && apt-get install -y

# RUN git clone https://github.com/streamlit/streamlit-example.git .

# RUN pip3 install -r requirements.txt
COPY . .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "main_page.py", "--server.port=8501", "--server.address=0.0.0.0"]