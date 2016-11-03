import unittest
from salesforce import *

class TestSalesforce(unittest.TestCase):
    """
    Test Salesforce short to long iD algorithms.
    Examples from: \
    http://salesforce.stackexchange.com/questions/27686/how-can-i-convert-a-15-char-id-value-into-an-18-char-id-value
    """

    def test_valid_tolongid(self):
        id1 = '001A0000006Vm9r'
        suffix1 = 'IAC'
        id2 = '003A0000005QB3A'
        suffix2 = 'IAW'
        id3 = '003A0000008qb1s'
        suffix3 = 'IAA'
        self.assertEquals(15, len(id1), 'A short ID is 15 characters')
        self.assertEquals(18, len(tolongid(id1)), 'A long ID is 18 characters')
        self.assertEquals(id1 + suffix1, tolongid(id1), 'The translation was incorrect')
        self.assertEquals(id2 + suffix2, tolongid(id2), 'The translation was incorrect')
        self.assertEquals(id3 + suffix3, tolongid(id3), 'The translation was incorrect')

    def test_none_tolongid(self):
        self.assertIsNone(tolongid(None), 'Give none get none!')

    def test_toolong_tolongid(self):
        id = '001A0000006Vm9rX'
        self.assertNotEquals(15, len(id), 'A short ID is 15 characters')
        self.assertIsNone(tolongid(id), 'Giving long gets the same')

    def test_long_tolongid(self):
        id = '001A0000006Vm9rIAC'
        self.assertEquals(18, len(tolongid(id)), 'A long ID is 18 characters')
        self.assertEquals(id, tolongid(id), 'Giving long gets the same')
