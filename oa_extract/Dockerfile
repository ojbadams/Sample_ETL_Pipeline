FROM bitnami/python:latest

RUN install_packages libmariadb-dev vim cron

RUN echo Copying Custom Python Packages 
COPY CustomPackages/datatransformer /app/datatransformer
COPY CustomPackages/simplemysql /app/simplemysql
COPY CustomPackages/setup.py /app/setup.py

RUN echo Installing Custom Python Packages
RUN python3 /app/setup.py install

RUN echo Removing Custom Python Packages
RUN rm -r /app/datatransformer
RUN rm -r /app/simplemysql
RUN rm -r /app/build
RUN rm -r /app/dist
RUN rm -r /app/*.egg-info
RUN rm /app/setup.py

RUN echo Installing Normal Python Packagess
COPY requirements.txt /app/requirements.txt
COPY CustomScripts/run.py /app/run.py

RUN pip3 install -r requirements.txt


# COPY CustomScripts/cron_settings.txt /etc/cron.d/cron
# RUN chmod 0644 /etc/cron.d/cron
# RUN crontab /etc/cron.d/cron
# RUN touch /var/log/cron.log

USER 1001
WORKDIR /app
CMD [ "python" ]
