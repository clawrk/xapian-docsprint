=========
Databases
=========

.. contents:: Table of contents

Pretty much all Xapian operations revolve around a Xapian database.  Before
searches can be performed, details of the documents to be searched need to
be put into a database; the search process then refers to the database to
efficiently determine the best matches for a given query.  The process of
putting documents into the database is usually referred to as *indexing*.

The main information stored in a database is a mapping from each term to a
list of all the documents it occurs in, together with various statistics
about these occurrences.  It may also store the full text, or extracts,
from the documents, so that result summaries can be displayed.  Databases
can also contain additional data for spelling correction and synonym
expansion, and developers can even store arbitrary key-value pairs in part
of the database.

Backends
========

Xapian databases store data in custom formats which allow searches to be
performed extremely quickly; Xapian does not use a relational database as
its datastore.  There are several database backends; the main backend in
the 1.4 release series of Xapian is called the *Glass* backend.  This
stores information in the filesystem (under a given path).

It is possible to perform searches across multiple databases at once, and
Xapian will handle merging the results together appropriately.  This
feature can be combined with remote databases to handle datasets which are
too large for a single machine, by performing searches across multiple
remote databases.

.. todo:: Document using add_database() to achieve this

.. todo:: trunk supports writable multi databases

.. todo:: mapping of docids

On-disk databases
-----------------

As mentioned, Xapian 1.4 has a default database type called *Glass*;
:ref:`earlier formats can be upgraded using Xapian's copydatabase utility
<upgrading-databases>`. When opening an existing database, Xapian will
automatically figure out the backend to use.

If you're
familiar with data storage structures, you might be interested to know that
both Chert and Glass use a copy-on-write B+-tree structure - but don't worry
if that doesn't mean anything to you!

Stub database files
-------------------

Xapian supports a simple text file format for listing the locations of
a set of databases (either on the local file system, or remote databases).
Such files are called *stub-databases*, and can be used to point to a
database when the physical database location may vary; for example, because
a new database is being built nightly, and is named according to the date
on which it was built.

These files are recognised by the autodetection in the Database
constructor or you can open them explicitly using
``Xapian::DB_BACKEND_STUB``.

If the path provided to the Database constructor is a directory
containing a file called ``XAPIANDB``, such ``XAPIANDB`` file is
considered to be the stub database file.

The stub database format specifies one database per line, prefixed by
the type. For example::

  remote localhost:23876
  auto /var/spool/xapian/webindex

This way you can have a pre-canned sets of databases to search.

Using such stub files you can swap databases atomically (with a file
renaming) in a production environment without having to worry about
race conditions. For example, if you want to rebuild the database from
scratch and replace it, you can build the database using a new
directory, prepare a stub file with the new path, and finally move the
stub file over the one which the running code is using.

This technique is better than just replacing the database directory,
which is affected by race conditions.

Database types
^^^^^^^^^^^^^^

The current types understood by Xapian are:

``auto``
    This isn't an actual database format, but rather auto-detection of
    one of the disk based backends (e.g. "chert" or "glass"). It takes a
    single specified path (which can be to a file or directory) as argument::

      auto /var/spool/xapian/webindex

``glass``
    Glass is the default backend in Xapian 1.4.x. It supports
    incremental modifications, concurrent single-writer and
    multiple-reader access to a database. It's very efficient and
    highly scalable, and more compact than chert. It takes a path as
    argument like ``auto``.

``chert``
    Chert was the default backend in Xapian 1.2.x. It supports
    incremental modifications, concurrent single-writer and
    multiple-reader access to a database. It's very efficient and
    highly scalable. It takes a path as argument like ``auto``.

``inmemory``
    This type is a database held entirely in memory. It was originally
    written for testing purposes only, but may prove useful for
    building up temporary small databases.

``remote``
    This can specify either a "program" or TCP remote backend, for example::

      remote :ssh xapian-prog.example.com xapian-progsrv /srv/xapian/db1

    or::

      remote xapian-tcp.example.com:12345

    If the first character of the second word is a colon (:), then
    this is skipped and the remainder of the line is used as the
    command to run xapian-progsrv and the "program" variant of the
    remote backend is used. Otherwise the TCP variant of the remote
    backend is used, and the rest of the line specifies the host and
    port to connect to.

.. todo:: uses e.g. keeping latest changes in a small DB you merge periodically

In-memory databases
-------------------

Xapian has an *inmemory* database type, which may be useful for testing and
perhaps some short-term usage. However it is inefficient, and does not support
all of Xapian's features (such as spelling correction, synonyms or replication),
so for production systems it is often better to use an on-disk database such
as *Glass*, with the files stored in a RAM disk.

Remote databases and replication
--------------------------------

Xapian's *remote* database backend allows the database to be
located on a different machine and accessed via a custom protocol.

There is also special support for :ref:`replicating databases <replication>`
to multiple machines, such that only the parts of the database which have been
modified are copied; this can be useful for redundancy and load-balancing purposes.

Concurrent access
=================

Most backend formats (and certainly the main backend format for each release)
will allow updates to be grouped into transactions, and will allow at least some
old versions of the database to be searched while new ones are being written.
Currently, all the backends only support a single writer existing at a given
time; attempting to open another writer on the same database will throw
:xapian-class:`DatabaseLockError` to indicate that it wasn't possible to acquire a
lock.  Multiple concurrent readers are supported (in addition to the writer).

When a database is opened for reading, a fixed snapshot of the database is
referenced by the reader, (essentially `Multi-Version Concurrency Control`_).
Updates which are made to the database will not be visible to the reader unless
it calls :xapian-method:`Database::reopen()`.  If the reader is already reading
the latest committed version of the database then
:xapian-just-method:`reopen()` has no effect and is a cheap operation, so if
you are reusing the same :xapian-class:`Database` object for multiple searches
then it is a reasonable strategy to call :xapian-just-method:`reopen()` prior
to each search.

.. _Multi-Version Concurrency Control: https://en.wikipedia.org/wiki/Multiversion_concurrency_control

Currently Xapian's disk based backends have a limitation to their *multi-version
concurrency* implementation - specifically, at most two versions can exist
concurrently.  Therefore a reader will be able to access its snapshot of the
database without limitations when only one change has been made and committed by
the writer, but after the writer has made two changes, readers will receive a
:xapian-class:`DatabaseModifiedError` if they attempt to access a part of the database
which has changed.  In this situation, the reader can be updated to the latest
version using the :xapian-method:`Database::reopen()` method.

Locking
-------

With the disk-based Xapian backends, when a database is opened for writing,
a lock is obtained on the database to ensure that no further writers are
opened concurrently.  This lock will be released when the database writer
is closed (or automatically if the writer process dies).

One unusual feature of Xapian's locking mechanism (at least on POSIX
operating systems other than Linux) is that Xapian forks a subprocess to hold
the lock, rather than holding it in the main process.  This is to avoid the
lock being accidentally released due to the slightly unhelpful semantics of
fcntl locks.  Linux kernel 3.15 added new OFD fcntl locks which have more
helpful semantics which Xapian uses in preference, avoiding the need to fork
a subprocess to hold the lock.
