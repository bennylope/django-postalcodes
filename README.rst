Django Postal Codes
===================

A simple data model for storing postal codes with placenames and location.

Installing
----------

You can clone the repository and install from source::

    python setup.py install

or use `pip` to install from PyPI::

    pip install django-postalcodes

Getting data
------------

Postal code data is available from a number of sources, typically on a country
by country basis. The United States Census Bureau maintains the `Gazetteer
database <http://www.census.gov/geo/www/gazetteer/gazette.html>`_, including
detailed zip code data. The `GeoNames geographical database
<http://www.geonames.org/export/>`_ also provides postal code data for
international postal codes (and other places).

Rather than include data files which may be of little to no use for many
users, you can import data from the aformentioned sources, or use one of two
SQL files I've made available based on the GeoNames data. Each file contains a
multi-value insert and has been tested in PostgreSQL. The same queries should
work in MySQL, although they will require modification to be of use with
Sqlite.

* `International postal codes <http://dl.dropbox.com/u/6515401/postalcodes/postalcodes_international.sql.zip>`_ (9 MB)
* `US zip codes using state abbreviations <http://dl.dropbox.com/u/6515401/postalcodes/postalcodes_us.sql.zip>`_ (623 KB)

The data is licensed under the `Database Contents License <http://opendatacommons.org/licenses/dbcl/1.0/>`_.
