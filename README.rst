Django Postal Codes
===================

A simple data model for storing postal codes with placenames and location.

Installing
----------

You can clone the repository and install from source::

    python setup.py install

or use `pip` to install from PyPI::

    pip install django-postalcodes

.. note::
    Version 0.2 requires a GIS backend (e.g. PostGIS) and is breaks backwards
    compatability with 0.1. For non-GIS based postalcodes use 0.1.

Getting data
------------

Postal code data is available from a number of sources, typically on a country
by country basis. The United States Census Bureau maintains the `Gazetteer
database <http://www.census.gov/geo/www/gazetteer/gazette.html>`_, including
detailed zip code data. The `GeoNames geographical database
<http://www.geonames.org/export/>`_ also provides postal code data for
international postal codes (and other places).

The following data file can be used to prepopulate a PostGIS database with US
postalcodes complete with location.

* `US zip codes using state abbreviations <https://dl.dropbox.com/u/6515401/postalcodes/postalcodes_gis_us.sql.zip>`_ (879 KB)

These files pertain to the 0.1 release but may still be useful. They are based
on location via decimal fields, rather than a GIS point field.

* `International postal codes <http://dl.dropbox.com/u/6515401/postalcodes/postalcodes_international.sql.zip>`_ (9 MB)
* `US zip codes using state abbreviations <http://dl.dropbox.com/u/6515401/postalcodes/postalcodes_us.sql.zip>`_ (623 KB)

The data is licensed under the `Database Contents License <http://opendatacommons.org/licenses/dbcl/1.0/>`_.
