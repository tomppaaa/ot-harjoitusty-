import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_on_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_lataus_toimii(self):
    	self.maksukortti.lataa_rahaa(250)

    	self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 12.50 euroa")

    def test_ota_rahaa(self):
    	self.maksukortti.ota_rahaa(250)

    	self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.50 euroa")

    def test_saldo_ei_muutu_negatiiviseksi(self):
    	self.maksukortti.ota_rahaa(1250)

    	self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_ota_rahaa_True(self):
    	self.assertEqual(self.maksukortti.ota_rahaa(250), True)

    def test_ota_rahaa_False(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1250), False)