"""
=============================================================
 SISTEMA AVANÇADO DE OTIMIZAÇÃO DE ROTAS
 Engenharia de Produção — Exercício 3
=============================================================
"""

import math

# =========================================================
# CONFIGURAÇÕES
# =========================================================

ORIGEM = (0, 0)
CONSUMO_POR_KM = 0.35
CAPACIDADE_TANQUE = 80.0


# =========================================================
# CLASSE PRINCIPAL
# =========================================================

class CaminhaoEntrega:

    def __init__(self, pontos_entrega):
        self.pontos = pontos_entrega

    # -----------------------------------------------------
    # Distância entre dois pontos
    # -----------------------------------------------------

    def calcular_distancia(self, ponto1, ponto2):

        x1, y1 = ponto1
        x2, y2 = ponto2

        distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        return distancia

    # -----------------------------------------------------
    # Distância total da rota
    # -----------------------------------------------------

    def calcular_distancia_total(self, rota):

        total = 0

        for i in range(len(rota) - 1):

            total += self.calcular_distancia(
                rota[i],
                rota[i + 1]
            )

        return total

    # -----------------------------------------------------
    # Rota original
    # -----------------------------------------------------

    def rota_original(self):

        rota = [ORIGEM]

        for ponto in self.pontos:
            rota.append(ponto)

        rota.append(ORIGEM)

        distancia_total = self.calcular_distancia_total(rota)

        return rota, distancia_total

    # -----------------------------------------------------
    # Algoritmo Vizinho Mais Próximo
    # -----------------------------------------------------

    def rota_otimizada(self):

        nao_visitados = self.pontos.copy()

        rota = [ORIGEM]

        ponto_atual = ORIGEM

        while len(nao_visitados) > 0:

            proximo = min(
                nao_visitados,
                key=lambda ponto:
                self.calcular_distancia(ponto_atual, ponto)
            )

            rota.append(proximo)

            nao_visitados.remove(proximo)

            ponto_atual = proximo

        rota.append(ORIGEM)

        distancia_total = self.calcular_distancia_total(rota)

        return rota, distancia_total

    # -----------------------------------------------------
    # Consumo de combustível
    # -----------------------------------------------------

    def calcular_consumo(self, distancia):

        return distancia * CONSUMO_POR_KM

    # -----------------------------------------------------
    # Comparação das rotas
    # -----------------------------------------------------

    def comparar_rotas(self, dist_original, dist_otimizada):

        consumo_original = self.calcular_consumo(dist_original)

        consumo_otimizado = self.calcular_consumo(dist_otimizada)

        economia = consumo_original - consumo_otimizado

        economia_percentual = (
            economia / consumo_original
        ) * 100

        return (
            consumo_original,
            consumo_otimizado,
            economia,
            economia_percentual
        )

    # -----------------------------------------------------
    # Verificação de combustível
    # -----------------------------------------------------

    def verificar_combustivel(self, rota):

        combustivel = CAPACIDADE_TANQUE

        precisa_reabastecer = False

        for i in range(len(rota) - 1):

            distancia = self.calcular_distancia(
                rota[i],
                rota[i + 1]
            )

            consumo = self.calcular_consumo(distancia)

            combustivel -= consumo

            if combustivel < 0:
                precisa_reabastecer = True

        return precisa_reabastecer, combustivel

    # -----------------------------------------------------
    # Mostrar rota formatada
    # -----------------------------------------------------

    def mostrar_rota(self, rota):

        texto = ""

        for i, ponto in enumerate(rota):

            if ponto == ORIGEM:
                texto += "ORIGEM"
            else:
                texto += str(ponto)

            if i < len(rota) - 1:
                texto += " -> "

        return texto

    # -----------------------------------------------------
    # Relatório completo
    # -----------------------------------------------------

    def gerar_relatorio(self):

        print("\n" + "=" * 70)
        print("SISTEMA DE OTIMIZAÇÃO DE ROTAS")
        print("=" * 70)

        print("\nPONTOS DE ENTREGA:")

        for i, ponto in enumerate(self.pontos, start=1):
            print(f"Ponto {i}: {ponto}")

        # -------------------------------------------------
        # ROTA ORIGINAL
        # -------------------------------------------------

        rota_original, dist_original = self.rota_original()

        print("\n" + "-" * 70)
        print("(a) ROTA ORIGINAL")
        print("-" * 70)

        print("\nSequência da rota:")
        print(self.mostrar_rota(rota_original))

        print(f"\nDistância total: {dist_original:.2f} km")

        # -------------------------------------------------
        # ROTA OTIMIZADA
        # -------------------------------------------------

        rota_otimizada, dist_otimizada = self.rota_otimizada()

        print("\n" + "-" * 70)
        print("(b) ROTA OTIMIZADA")
        print("-" * 70)

        print("\nSequência otimizada:")
        print(self.mostrar_rota(rota_otimizada))

        print(f"\nDistância total: {dist_otimizada:.2f} km")

        # -------------------------------------------------
        # COMPARAÇÃO
        # -------------------------------------------------

        (
            consumo_original,
            consumo_otimizado,
            economia,
            economia_percentual
        ) = self.comparar_rotas(
            dist_original,
            dist_otimizada
        )

        print("\n" + "-" * 70)
        print("(c) COMPARAÇÃO DE CONSUMO")
        print("-" * 70)

        print(
            f"\nConsumo rota original: "
            f"{consumo_original:.2f} litros"
        )

        print(
            f"Consumo rota otimizada: "
            f"{consumo_otimizado:.2f} litros"
        )

        print(
            f"Economia de combustível: "
            f"{economia:.2f} litros"
        )

        print(
            f"Economia percentual: "
            f"{economia_percentual:.2f}%"
        )

        # -------------------------------------------------
        # COMBUSTÍVEL
        # -------------------------------------------------

        (
            precisa_reabastecer,
            combustivel_restante
        ) = self.verificar_combustivel(
            rota_otimizada
        )

        print("\n" + "-" * 70)
        print("(d) VERIFICAÇÃO DO TANQUE")
        print("-" * 70)

        print(
            f"\nCapacidade do tanque: "
            f"{CAPACIDADE_TANQUE:.2f} litros"
        )

        print(
            f"Combustível restante: "
            f"{combustivel_restante:.2f} litros"
        )

        if precisa_reabastecer:
            print("\nO caminhão PRECISA reabastecer.")
        else:
            print("\nO caminhão NÃO precisa reabastecer.")

        print("\n" + "=" * 70)
        print("FIM DO RELATÓRIO")
        print("=" * 70)


# =========================================================
# EXECUÇÃO PRINCIPAL
# =========================================================

pontos_entrega = [
    (2, 4),
    (5, 1),
    (3, 8),
    (7, 3),
    (1, 6),
    (9, 2)
]

sistema = CaminhaoEntrega(pontos_entrega)

sistema.gerar_relatorio()