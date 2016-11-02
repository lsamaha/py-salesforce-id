import unittest
from salesforce import *

class TestSalesforce(unittest.TestCase):
    """
    Test Salesforce short to long iD algorithms.
    Examples from: \
    http://salesforce.stackexchange.com/questions/27686/how-can-i-convert-a-15-char-id-value-into-an-18-char-id-value
    """

    def test_tolongid(self):
        id1 = '001A0000006Vm9r'
        suffix1 = 'IAC'
        id2 = '003A0000005QB3A'
        suffix2 = 'IAW'
        id3 = '003A0000008qb1s'
        suffix3 = 'IAA'
        self.assertEquals(id1 + suffix1, tolongid(id1), 'The translation was incorrect')
        self.assertEquals(id2 + suffix2, tolongid(id2), 'The translation was incorrect')
        self.assertEquals(id3 + suffix3, tolongid(id3), 'The translation was incorrect')
