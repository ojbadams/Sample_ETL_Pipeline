FROM bitnami/python:latest

RUN install_packages libmariadb-dev vim cron

COPY ./CustomScripts /app/app.ini
COPY ./CustomScripts/app /app/app
COPY ./CustomScripts/config.py /app/config.py
COPY ./CustomScripts/run.py /app/run.py

COPY ./CustomScripts/requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

# COPY CustomScripts/cron_settings.txt /etc/cron.d/cron
# RUN chmod 0644 /etc/cron.d/cron
# RUN crontab /etc/cron.d/cron
# RUN touch /var/log/cron.log

USER 1001
WORKDIR /app
CMD [ "python" ]
