# Definici�n de la clase para representar un juego de loter�a
class LotteryGame:
    def __init__(self, prize, probability):
        self.prize = prize  # Premio de la loter�a
        self.probability = probability  # Probabilidad de ganar el premio

# Funci�n de utilidad esperada para evaluar una loter�a
def expected_utility(lottery):
    return lottery.prize * lottery.probability

# Ejemplo de juego de loter�a
lottery_A = LotteryGame(prize=1000, probability=0.5)  # Una loter�a con premio de $1000 y probabilidad de ganar del 50%
lottery_B = LotteryGame(prize=2000, probability=0.3)  # Otra loter�a con premio de $2000 y probabilidad de ganar del 30%

# Calcular la utilidad esperada de cada loter�a
utility_A = expected_utility(lottery_A)
utility_B = expected_utility(lottery_B)

# Imprimir los resultados
print("Utilidad esperada de la loter�a A:", utility_A)
print("Utilidad esperada de la loter�a B:", utility_B)

# Tomar la decisi�n basada en la utilidad esperada
if utility_A > utility_B:
    print("Se recomienda elegir la loter�a A.")
elif utility_A < utility_B:
    print("Se recomienda elegir la loter�a B.")
else:
    print("Ambas loter�as tienen la misma utilidad esperada. La elecci�n depende de otras consideraciones.")
