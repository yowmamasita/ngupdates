Ferris Angular App Bootstrap
============================

Aw yiss, time to angularize your Ferris application with some attitude.

Here's what you do, gangster:

1. Copy everything here into your Ferris project:

        cp -r angular-app-bootstrap/* name-of-your-project/

2. Include the plugin's yaml in app.yaml:

        includes:
        - ferris/include.yaml
        # If plugins require inculdes, put them here.
        - plugins/angular/include.yaml

3. Optionally (if you want to test/use templates in angular-app directly) enable the plugin in routes.py:

        # Plugins
        plugins.enable('angular')

3. Commit yo' stuff, sucka.

Referencing Items in angular-app
--------------------------------

Everything in ``/angular-app`` is mapped to the static file handler ``/ng``. So to include ``angular-app/controllers/test.js`` you'd use the url ``/ng/controllers/test.js``. 

Additionally, all templates under ``/angular-app/templates`` are available in the prefix ``/angular``, so in your Ferris templates you can include ``/angular-app/templates/meow.html`` with the path ``/angular/meow.html``. 

Installing JavaScript Libraries (Components)
--------------------------------------------

Use Bower like a real G! Just add to the depedencies in bower.json then run ``bower install`` from within 'angular-app' and it'll handle the rest. Also, yes, you *should* commit these to the repository.

Rendering Templates Directly
----------------------------

If you enabled the plugin you can render any template in ``angular-app/templates`` directly from the browser using jinja2 by loading up ``/ng-view/path/to/template.html`` (don't forget your ``{%raw%}`` tag).
