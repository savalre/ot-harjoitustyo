import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.paate = Kassapaate()
        self.kortti = Maksukortti(1000)
    
    def test_kassassa_rahasumma_1000(self):
        rahamaara = self.paate.kassassa_rahaa
        self.assertEqual(rahamaara, 100000)
    
    def test_alussa_ei_lounaita_myyty(self):
        myydyt = self.paate.edulliset + self.paate.maukkaat
        self.assertEqual(myydyt,0)
    
    def test_kateisosto_edullinen_onnistuu(self):
        self.paate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.paate.kassassa_rahaa, 100240)
        self.assertEqual(self.paate.edulliset, 1)
    
    def test_kateisosto_maukas_onnistuu(self):
        self.paate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.paate.kassassa_rahaa, 100400)       
        self.assertEqual(self.paate.maukkaat, 1)
    
    def test_kateisosto_edullinen_ei_onnistu(self):
        self.assertEqual(self.paate.syo_edullisesti_kateisella(230), 230)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
        self.assertEqual(self.paate.edulliset, 0)

    def test_kateisosto_maukas_ei_onnistu(self):
        self.assertEqual(self.paate.syo_maukkaasti_kateisella(230), 230)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
        self.assertEqual(self.paate.maukkaat, 0)

    def test_kortti_edullinen_onnistuu(self):
        self.assertTrue(self.paate.syo_edullisesti_kortilla(self.kortti), True)
    
    def test_kortti_maukas_onnistuu(self):
        self.assertTrue(self.paate.syo_maukkaasti_kortilla(self.kortti), True)

    def test_korttiostolla_saldo_kasvaa(self):
        self.paate.syo_edullisesti_kortilla(self.kortti)
        self.assertTrue(self.paate.edulliset, 1)

    def test_kortti_maukas_ei_onnistu(self):
        self.kortti.ota_rahaa(1000)
        viesti = self.paate.syo_maukkaasti_kortilla(self.kortti)
        self.assertFalse(viesti, False)
        self.assertEqual(str(self.kortti), "saldo: 0.0")


    def test_kortti_edullinen_ei_onnistu(self):
        self.kortti.ota_rahaa(1000)
        viesti = self.paate.syo_edullisesti_kortilla(self.kortti)
        self.assertFalse(viesti, False)
        self.assertEqual(str(self.kortti), "saldo: 0.0")

    def test_korttimaksu_ei_muuta_kassasaldoa(self):
        self.paate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)       

    def test_kortin_lataus_muuttaa_saldoa(self):
        self.paate.lataa_rahaa_kortille(self.kortti, 100)
        self.assertEqual(self.paate.kassassa_rahaa, 100100)
        self.assertEqual(str(self.kortti), "saldo: 11.0")

    def test_kortin_lataus_väärin_ei_muuta_saldoa(self):
        self.paate.lataa_rahaa_kortille(self.kortti, -100)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
        self.assertEqual(str(self.kortti), "saldo: 10.0")
