pycharm:
  file.managed:
   - name: {{ pillar.get('pycharm_installer_target') }}
   - source: {{ pillar.get('pycharm_installer_source') }}

{{ pillar.get('mysql_server_package', 'mysql-server') }}:
  pkg.installed


{% if grains['os'] != 'Windows'%}
python-pkgs:
  pkg.installed:
    - names:
      - python-django
{% else %}
Python 2.7.8:
  pkg.installed
{% endif %}