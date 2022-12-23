FROM bitnami/mariadb:10.10

COPY CustomScripts/init.sql /docker-entrypoint-initdb.d
COPY CustomScripts/proc_transform.sql /docker-entrypoint-initdb.d

USER 1001
ENTRYPOINT [ "/opt/bitnami/scripts/mariadb/entrypoint.sh" ]
CMD [ "/opt/bitnami/scripts/mariadb/run.sh" ]
