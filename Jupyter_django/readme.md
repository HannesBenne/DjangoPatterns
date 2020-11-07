Use django models in jupyter notebooks. Further reading:
https://medium.com/ayuth/how-to-use-django-in-jupyter-notebook-561ea2401852

- install requirements
- create django project
- add 'django_extensions' to installed apps
- start jupyter: python manage.py shell_plus --notebook
- create notebook with 'Django Shell-Plus' kernel
- run ***import os; os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"*** before you try to access django models
- minimalist example how to query django models in jupyter can be found in ./notebooks/Query_Users.ipynb
- read the documentation: https://docs.djangoproject.com/en/3.1/topics/db/queries/
