=====
farmacia
=====

farmacia is a Django app to conduct Web-based farmacia. For each question,
visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "farmacia" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'farmacia',
    ]

2. Include the farmacia URLconf in your project urls.py like this::

    path('farmacia/', include('farmacia.urls')),

3. Run ``python manage.py migrate`` to create the farmacia models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a farmacia (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/farmacia/ to participate in the farmacia.