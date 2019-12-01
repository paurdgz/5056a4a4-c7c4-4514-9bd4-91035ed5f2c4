import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Amortization(object):

    def _init_(self, amount, interest, n):
        self.amount = amount
        self.interest = interest
        self.n = n

    def anualidad(self):
        anualidad = -(self.amount / ((1-(1+self.interest)**(self.n))/self.interest))
        return anualidad

    def get_table(self):
        anualidad = self.anualidad()
        saldo = [0]
        tasa = [0]
        anualidadt = [anualidad]
        capital = [self.amount]

        for j in range(self.n):
            anualidadt.append(anualidadt[-1])
            tasa.append(capital[-1] * (self.interest))
            saldo.append(anualidadt[-1] - tasa[-1])
            capital.append(capital[-1] - saldo[-1])

        tabla = pd.DataFrame([saldo, tasa, anualidadt, capital]).transpose()
        tabla = tabla.rename(columns={0: 'saldo', 1: 'interes', 2: 'anualidad', 3: 'capitañ'})
        return tabla


    def get_plot(self):
        tabla = self.get_table()
        figura = plt.figure(1)
        plt.subplot(2, 2, 1)
        plt.plot(list(np.arange(self.n) + 1), list(tabla.iloc[1:, 0]))
        plt.title('Principal')
        plt.xlabel('Periods')
        plt.ylabel('Amount $')
        plt.subplot(2, 2, 2)