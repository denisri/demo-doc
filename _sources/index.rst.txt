Documentation Sphinx
====================

Généralités
-----------

http://www.sphinx-doc.org/en/master/

Il faut:

* un fichier de config :doc:`conf.py <auto_examples/conf>`
* un fichier de doc d'entrée ``index.rst`` (format: `RestructuredText <http://docutils.sourceforge.net/rst.html>`_)

On peut générer ``conf.py`` en utilisant la commande: ``sphinx-quickstart``. Il faut ensuite l'éditer.

Sphinx / RestructuredText permet comme pas mal de langages de Markup, de faire des documents assez facilement, avec des titres à plusieurs niveaux, des liens http externes, des liens et références internes etc.

On peut utiliser des styles, qu'on choisit dans le fichier de conf, et qu'on peut customiser par des CSS.

Sphinx ajoute le parsing de code source python et permet de faire la doc de modules, classes, fonctions python. Il a aussi des extensions.

``autodoc``, peut-être la plus importante, permet le parsing automatique des modules / classes python.

Il y a d'autres extensions pour les liens (références croisées) entre docs sphinx et les classes documentées (``intersphinx``), des galleries d'images et de sniplets de code (``sphinx-gallery``), pour documenter facilement et lisiblement les paramètres des fonctions (``napoleon`` ou ``numpydoc``), etc etc.

Ex de lien sur un autre document: :doc:`moduledoc`

Générer le HTML
---------------

Si on a généré un ``Makefile`` avec ``sphinx-quickstart``, il suffit de faire:

.. code-block:: bash

    make html

dans le bon directory (``doc/`` ici).

Sinon on peut le faire à la main:

.. code-block:: bash

    sphinx-build . _build/html


Code python
-----------

Ex de bloc de code python::

    from capsul.api import capsul_engine

    ce = capsul_engine()
    process = ce.get_process_instance(
        'capsul.pipeline.test.test_activation.MyPipeline'

On peut évidemment faire des liens sur des :class:`sample_module.mod1.Class1` du projet (nom "long"), ou avec un nom "court": :class:`~sample_module.mod1.Class1`, ou :class:`sous un autre nom <sample_module.mod1.Class1>`.

Avec *intersphinx* on peut aussi faire des liens sur les classes / foonctions / modules d'autres projets: :class:`argparse.ArgumentParser`, :class:`capsul.pipeline.pipeline.Pipeline`.

Ou des :capsul:`liens sur des pages de projets externes <index.html>` avec *extlinks*.

Notebooks
---------

*nbsphinx* peut convertir des `notebooks jupyter <https://jupyter.org/>`_ en docs sphinx, consultables dans la doc. Ça nécessite un peu de config et préprocessing pour vraiment bien s'intégrer.

* Consulter le notebook converti en sphinx: :doc:`tutorial/sample_notebook`
* Le télécharger: `Sample Notebook <_static/tutorial/sample_notebook.ipynb>`_

Le préprocessing a été ajouté à :doc:`conf.py <auto_examples/conf>` qui est exécuté automatiquement à chaque build de doc. Il sert à:

* convertir le notebook avec le bon noyau python (python2 / python3)
* copier le notebook "brut" dans la doc construite de manière à être téléchargeable aussi, pas seulement en version convertie en sphinx.
* copier les images qui vont avec le notebook dans la doc construite.

Ça nécessite d'avoir aussi installé `pandoc <https://pandoc.org/>`_.


Sphinx-Gallery
--------------

`sphinx_gallery <https://sphinx-gallery.github.io/stable/index.html>`_ inclut des "code snippets" avec des images dans les docs. Il faut un directory de codes (``.py``) avec un fichier ``README.txt`` dedans (en sphinx) qui fait l'en-tête.
Tous les fichiers de code doivent avoir une docstring au début.

Si le code génère une figure `matplotlib <http://matplotlib.org>`_, cette figure sera récupérée et utilisée comme imagette pour le snippet en question. Notons que :func:`~matplotlib.pyplot.imshow` permet d'intéger n'importe quelle image.

.. ifconfig:: 'sphinx_gallery.gen_gallery' in extensions

    :doc:`auto_examples/index`

Il faut configurer sphinx-gallery dans :doc:`conf.py <auto_examples/conf>`.


Traitements et pipelines Capsul
-------------------------------

On peut générer de la doc Sphinx pour les process et pipelines Capsul, en utilisant :mod:`capsul.sphinxext.capsul_pipeline_rst <capsul.sphinxext>`.

:doc:`process_docs/example_module/capsul/index`

La commande adéquate peut être ajoutée dans :doc:`conf.py <auto_examples/conf>`. Ça revient à lancer la commande:

.. code-block:: bash

    python -m capsul.sphinxext.capsul_pipeline_rst -i sample_module.capsul -o _build/html/process_docs/example_module --schema


Intégration à github gh-pages via Travis-ci
-------------------------------------------

La doc peut être construite par `Travis-CI <https://travis-ci.org/>`_ et injectée dans la branche ``gh-pages`` du projet `GitHub <https://github.com>`_.

Pour cela il faut:

* donner les droits à travis-ci de pousser la doc dans le projet github (la branche ``gh-pages`` est sous git). Pour cela il faut générer un "github personal access token", et le mettre en variable d'environnement dans le build travis-ci (ici c'est ``GITHUB_ACCESS_TOKEN``). `La doc est ici <https://docs.travis-ci.com/user/deployment/pages/>`_.
* avoir créé sur GitHub la branche ``gh-pages`` (vide, possiblement détachée).
* configurer ``.travis.yaml``, en ajoutant un truc de ce genre (la condition ici est liée à des variables définies plus tôt dans ``.travis.yaml``, il faut l'adapter):

.. code-block:: yaml

    deploy:
      provider: pages
      skip_cleanup: true
      github_token: $GITHUB_ACCESS_TOKEN
      target-branch: gh-pages
      local-dir: doc/_build/html
      on:
        branch: master
        condition: $PUSH_DOC_TO_GH_PAGES == yes && $TRAVIS_OS_NAME == linux && $TRAVIS_PYTHON_VERSION == 3.5



Pages de doc
------------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   moduledoc
   tutorial/sample_notebook
   auto_examples/index
   process_docs/example_module/capsul/index

