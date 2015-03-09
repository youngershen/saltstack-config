{% if grains['os'] == 'Windows' %}
pycharm_installer_target: d:/dev/pycharm.rar
pycharm_installer_source: salt://pycharm.rar
{% else %}
pycharm_installer_target: /usr/local/tools/pycharm.tar.gz
pycharm_installer_source: salt://pycharm.tar.gz
{% endif %}
{% if grains['os'] == 'Ubuntu' or grains['os'] == 'Debian' %}
mysql_server_package: mysql-server
{% elif grains['os'] == 'Windows' %}
mysql_server_package: MySQL Installer - Community
{% endif %}