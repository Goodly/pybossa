# -*- coding: utf8 -*-
# This file is part of PyBossa.
#
# Copyright (C) 2015 SciFabric LTD.
#
# PyBossa is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBossa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBossa.  If not, see <http://www.gnu.org/licenses/>.

import datetime
import uuid

from sqlalchemy.orm import class_mapper

import logging


log = logging.getLogger(__name__)


class DomainObject(object):

    def dictize(self):
        out = {}
        for col in self.__table__.c:
            out[col.name] = getattr(self, col.name)
        return out

    def info_public_keys(self, data=None):
        """Return a dictionary of info field with public keys."""
        out = dict()
        if data is None:
            data = self.dictize()
        for key in self.public_info_keys():
            out[key] = data.get('info').get(key)
        return out

    def to_public_json(self, data=None):
        """Return a dict that can be exported to JSON
        with only public attributes."""

        out = dict()
        if data is None:
            data = self.dictize()
        for col in self.public_attributes():
            if col == 'info':
                out[col] = self.info_public_keys(data=data)
            else:
                out[col] = data.get(col)
        return out

    def public_attributes(self):
        """To be override by other class."""
        pass

    def public_info_keys(self):
        """To be override by other class."""
        pass

    @classmethod
    def undictize(cls, dict_):
        raise NotImplementedError()

    def __str__(self):  # pragma: no cover
        return self.__unicode__().encode('utf8')

    def __unicode__(self): # pragma: no cover
        repr = u'<%s' % self.__class__.__name__
        table = class_mapper(self.__class__).mapped_table
        for col in table.c:
            try:
                repr += u' %s=%s' % (col.name, getattr(self, col.name))
            except Exception, inst:
                repr += u' %s=%s' % (col.name, inst)

        repr += '>'
        return repr

def make_timestamp():
    now = datetime.datetime.utcnow()
    return now.isoformat()


def make_uuid():
    return str(uuid.uuid4())


def update_project_timestamp(mapper, conn, target):
    """Update method to be used by the relationship objects."""
    sql_query = ("update project set updated='%s' where id=%s" %
                 (make_timestamp(), target.project_id))
    conn.execute(sql_query)

def update_target_timestamp(mapper, conn, target):
    """Update target update column."""
    sql_query = ("update %s set updated='%s' where id=%s" %
                 (target.__tablename__, make_timestamp(), target.id))
    conn.execute(sql_query)

