'''
ARCHES - a program developed to inventory and manage immovable cultural heritage.
Copyright (C) 2013 J. Paul Getty Trust and World Monuments Fund

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
'''

import os
from operator import itemgetter
from tests import test_settings
from tests.base_test import ArchesTestCase
from django.core import management
from arches.app.models.models import TileModel, ResourceInstance
from arches.app.utils.betterJSONSerializer import JSONSerializer, JSONDeserializer
from arches.app.utils.v3_migration.graph_migrator import Resource


# these tests can be run from the command line via
# python manage.py test arches/app/utils/v3_migration/tests/resource_tests.py --pattern="*.py" --settings="tests.test_settings"


class resourceTests(ArchesTestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        ResourceInstance.objects.all().delete()
        with open(os.path.join('arches/app/utils/v3_migration/tests/fixtures/v3_json/hk_fullexport.json'), 'rU') as f:
            archesfile = JSONDeserializer().deserialize(f)
        self._aResource = Resource(archesfile['resources'][1])


    @classmethod
    def tearDownClass(cls):
        pass


    def test_parent(self):
        node = self._aResource.nodes.get('27ef3bc4-a326-4b9d-bc97-3265a51fa812')
        self.assertEqual(node['parent'], '379cb79f-3fbb-488b-8703-074110788ef1')

    def test_cardinality_n(self):
        pass
