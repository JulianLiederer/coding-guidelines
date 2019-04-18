ZEIT ONLINE Python Coding Guidelines
====================================

Please read and adhere to [PEP 8](http://legacy.python.org/dev/peps/pep-0008/).

The following additional guidelines are structured according to the original
PEP 8 document.

Indentation
-----------

Use hanging indents whenever possible::

    foo = long_function_name(
        var_one, var_two,
        var_three, var_four)


Maximum Line Length
-------------------

Avoid breaking long lines using backslashes. Instead, use brackets.
Note, that Python implicitly joins strings that are contained in brackets::

    assert (
        '<html><body><div><h1>{{ title }}</h1>'
        '<div class="container">{{ content }}</div>'
        '</div></body></html>') in foo.contents


Imports
-------

In addition to the suggested PEP 8 import order, use a fourth section to group
import statements.

* standard library imports
* third party imports
* zeit namespace imports
* project specific imports

You should put a blank line between each group of imports. You should also
import full paths rather than importing explicitly using the `from` statement::

    import base64
    import sys

    import pyramid
    import jinja2.runtime

    import zeit.some.project
    import zeit.other.project

    import zeit.scope.project.module


    app = zeit.scope.project.module.app_factory()
