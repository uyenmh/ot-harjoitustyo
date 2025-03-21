import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luodun_kassapaatteen_rahamaara_ja_lounaiden_maara_on_oikein(self):
        saatu_tulos = (self.kassapaate.kassassa_rahaa_euroina(), self.kassapaate.edulliset, self.kassapaate.maukkaat)
        odotettu_tulos = (1000.0,0,0)

        self.assertEqual(saatu_tulos, odotettu_tulos)

    def test_kateinen_ei_riita_syomaan_edullisesti(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        saatu_tulos = (self.kassapaate.kassassa_rahaa_euroina(),vaihtoraha,self.kassapaate.edulliset)
        odotettu_tulos = (1000.0,200,0)

        self.assertEqual(saatu_tulos,odotettu_tulos)

    def test_kateisosto_toimii_kun_syodaan_edullisesti(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)
        saatu_tulos = (self.kassapaate.kassassa_rahaa_euroina(),vaihtoraha,self.kassapaate.edulliset)
        odotettu_tulos = (1002.4,60,1)

        self.assertEqual(saatu_tulos,odotettu_tulos)

    def test_kateinen_ei_riita_syomaan_maukkaasti(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(300)
        saatu_tulos = (self.kassapaate.kassassa_rahaa_euroina(),vaihtoraha,self.kassapaate.maukkaat)
        odotettu_tulos = (1000.0,300,0)

        self.assertEqual(saatu_tulos,odotettu_tulos)

    def test_kateisosto_toimii_kun_syodaan_maukkaasti(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        saatu_tulos = (self.kassapaate.kassassa_rahaa_euroina(),vaihtoraha,self.kassapaate.maukkaat)
        odotettu_tulos = (1004.0,100,1)

        self.assertEqual(saatu_tulos,odotettu_tulos)

    def test_kortilla_ei_ole_tarpeeksi_rahaa_syomaan_edullisesti(self):
        kortti = Maksukortti(200)
        boolean = self.kassapaate.syo_edullisesti_kortilla(kortti)
        saatu_tulos = (kortti.saldo_euroina(),self.kassapaate.edulliset,boolean)
        odotettu_tulos = (2.0,0,False)

        self.assertEqual(saatu_tulos,odotettu_tulos)

    def test_korttiosto_toimii_kun_syodaan_edullisesti(self):
        boolean = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        saatu_tulos = (self.maksukortti.saldo_euroina(),self.kassapaate.edulliset,boolean)
        odotettu_tulos = (7.6,1,True)

        self.assertEqual(saatu_tulos,odotettu_tulos)

    def test_kortilla_ei_ole_tarpeeksi_rahaa_syomaan_maukkaasti(self):
        kortti = Maksukortti(200)
        boolean = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        saatu_tulos = (kortti.saldo_euroina(),self.kassapaate.maukkaat,boolean)
        odotettu_tulos = (2.0,0,False)

        self.assertEqual(saatu_tulos,odotettu_tulos)

    def test_korttiosto_toimii_kun_syodaan_maukkaasti(self):
        boolean = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        saatu_tulos = (self.maksukortti.saldo_euroina(),self.kassapaate.maukkaat,boolean)
        odotettu_tulos = (6.0,1,True)

        self.assertEqual(saatu_tulos,odotettu_tulos)

    def test_rahan_lataaminen_kortille_onnistuu_positiivisella_summalla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,1000)
        saatu_tulos = (self.kassapaate.kassassa_rahaa_euroina(),self.maksukortti.saldo_euroina())
        odotettu_tulos = (1010.0,20.0)

        self.assertEqual(saatu_tulos,odotettu_tulos)

    def test_rahan_lataaminen_kortille_ei_onnistu_negatiivisella_summalla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,-1000)
        saatu_tulos = (self.kassapaate.kassassa_rahaa_euroina(),self.maksukortti.saldo_euroina())
        odotettu_tulos = (1000.0,10.0)

        self.assertEqual(saatu_tulos,odotettu_tulos)