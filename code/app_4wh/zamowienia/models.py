from django.db import models


class detale(models.Model):
    index = models.CharField(max_length=30)
    ilosc_w_opakowaniu = models.IntegerField(default=0,help_text="imość w pełnym opakowaniu.")

    def __str__(self):
        return f"index: {self.index} ilość w opakowaniu: {self.ilosc_w_opakowaniu}"

class zamowienia(models.Model):
    index_detalu = models.CharField(max_length=30)
    ilosc_opakowan = models.IntegerField()
    osoba_zamawiajaca = models.CharField(max_length=30)
    termin_zamowienia = models.DateField("data",default='0-0-0')

    def __str__(self):

        formatted_date = self.termin_zamowienia.strftime('%Y-%m-%d')

        return f"osoba zamawiająca: {self.osoba_zamawiajaca} index: {self.index_detalu} ilość opakowań: {self.ilosc_opakowan} data zamówienia: {formatted_date}"

