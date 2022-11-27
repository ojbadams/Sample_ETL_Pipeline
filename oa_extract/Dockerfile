FROM bitnami/python:latest

RUN install_packages libmariadb-dev vim

COPY CustomPackages/datatransformer /app/datatransformer
COPY CustomPackages/simplemysql /app/simplemysql
COPY CustomPackages/setup.py /app/setup.py

#RUN pip3 install setup.py

#RUN rm -r /app/datatransformer
#RUN rm -r /app/simplemysql
#RUN rm /app/setup.py

COPY requirements.txt /app/requirements.txt
COPY CustomScripts/run.py /app/run.py

RUN pip3 install -r requirements.txt

WORKDIR /app
CMD [ "python" ]
