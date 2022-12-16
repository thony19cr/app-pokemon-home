## APP Pokemon

App Pokemon - Gestor de Owners

### Requerimientos
* Python 3.6+
* Django <4
* Pipenv

#### Configuracion
```
Nota: Cambiar <django_project> por 'app_pokemon' en cada paso de este documento
```

#### Crera un entorno virtual e enstalar requerimientos del proyecto
```
pip install -r requirements.txt

```

#### Crear las tablas en nuestra BD de nuestras apps
```
python manage.py makemigrations --settings=<django_project>.settings.local
python manage.py migrate --settings=<django_project>.settings.local
```

#### Iniciar proyecto

* Ejecutar servidor de prueba
```
python manage.py runserver --settings=<django_project>.settings.local
```

### Test
* Cumplimiento de la guía de estilo de python
```
flake8 .
```