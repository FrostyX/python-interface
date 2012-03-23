#!/usr/bin/env python

import os
import sys
import unittest

dirname = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(dirname, ".."))

from oshift import *

class TestUser(unittest.TestCase):
    """
    Test domain get REST API
    """
    valid_domain_name = "autotest"

    def test_invalid_domain(self):
        self.assertTrue(os.environ.has_key('OPENSHIFT_USER'),
            'Missing Openshift username!')
        self.assertTrue(os.environ.has_key('OPENSHIFT_PASSWD'),
            'Missing Openshift password!')
        self.assertTrue(os.environ.has_key("OPENSHIFT_IP"),
            'Missing instance ip variable!')

        li = Openshift(host=os.getenv('OPENSHIFT_IP'), user=os.getenv('OPENSHIFT_USER'),
                passwd="notvalid")

        status, res = li.create_domain('invalid domain name')
        expected = 'Invalid namespace: invalid domain name. Namespace must only contain alphanumeric characters.'
        error_msg = res.json['messages'][0]['text']
        self.assertEqual(error_msg, expected)

    def test_create_domain(self):
        self.assertTrue(os.environ.has_key('OPENSHIFT_USER'),
            'Missing Openshift username!')
        self.assertTrue(os.environ.has_key('OPENSHIFT_PASSWD'),
            'Missing Openshift password!')
        self.assertTrue(os.environ.has_key("OPENSHIFT_IP"),
            'Missing instance ip variable!')
        li = Openshift(host=os.getenv('OPENSHIFT_IP'), user=os.getenv('OPENSHIFT_USER'),
            passwd=os.getenv('OPENSHIFT_PASSWD'))
        status, res = li.create_domain(self.valid_domain_name)
        expected_status = 201
        self.assertEqual(status, expected_status)

    def test_delete_domain(self):
        self.assertTrue(os.environ.has_key('OPENSHIFT_USER'),
            'Missing Openshift username!')
        self.assertTrue(os.environ.has_key('OPENSHIFT_PASSWD'),
            'Missing Openshift password!')
        self.assertTrue(os.environ.has_key("OPENSHIFT_IP"),
            'Missing instance ip variable!')
        li = Openshift(host=os.getenv('OPENSHIFT_IP'), user=os.getenv('OPENSHIFT_USER'),
            passwd=os.getenv('OPENSHIFT_PASSWD'))
        status, res = li.delete_domain(force=True)

        self.assertEqual(status, 'No Content')

if __name__ == '__main__':
    unittest.main()