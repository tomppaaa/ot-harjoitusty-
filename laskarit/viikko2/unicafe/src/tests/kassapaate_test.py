import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate = Kassapaate()

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_konstruktori_edulliset_annokset_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_konstruktori_maukkaat_annokset_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    

    def test_ostaa_edullisen_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(340)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_ostaa_edullisen_kateisella_vajaa(self): 
        self.kassapaate.syo_edullisesti_kateisella(140)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_ostaa_maukkaan_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_ostaa_maukkaan_kateisella_vajaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_ostaa_edullisen_kortilla(self): 

        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.60 euroa")
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)


    def test_ostaa_maukkaan_kortilla(self): 

        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 6.00 euroa")
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_ostaa_edullisen_kortilla_vajaa(self): 
        self.edullinenvajaa = Maksukortti(100)

        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.edullinenvajaa), False)
        self.assertEqual(str(self.edullinenvajaa), "Kortilla on rahaa 1.00 euroa")
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)


    def test_ostaa_maukkaan_kortilla_vajaa(self): 
        self.maukasvajaa = Maksukortti(300)

        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maukasvajaa), False)
        self.assertEqual(str(self.maukasvajaa), "Kortilla on rahaa 3.00 euroa")
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lataa_kortille_saldoa(self): 
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 600)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 16.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100600)

    def test_lataa_kortille_saldoa_neg(self):
        
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -600)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

