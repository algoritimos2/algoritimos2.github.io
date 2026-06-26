"""
ATENÇÃO ANTES DE EXECUTAR O CODIGO!
 "pip install matplotlib"

=============================================================
 SISTEMA PROFISSIONAL DE OTIMIZAÇÃO DE ROTAS
 Engenharia de Produção — Exercício 3
=============================================================
"""

import math
import matplotlib.pyplot as plt

# =========================================================
# CONFIGURAÇÕES
# =========================================================

ORIGEM = (0, 0)
CONSUMO_POR_KM = 0.35
CAPACIDADE_TANQUE = 80
PRECO_DIESEL = 6.15
VELOCIDADE_MEDIA = 60

# =========================================================
# CLASSE PRINCIPAL
# =========================================================

class SistemaLogistica:

    def __init__(self, pontos_entrega):
        self.pontos = pontos_entrega

    # =====================================================
    # DISTÂNCIA ENTRE DOIS PONTOS
    # =====================================================

    def calcular_distancia(self, p1, p2):

        x1, y1 = p1
        x2, y2 = p2

        distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        return distancia

    # =====================================================
    # DISTÂNCIA TOTAL
    # =====================================================

    def distancia_total(self, rota):

        total = 0

        for i in range(len(rota) - 1):

            total += self.calcular_distancia(
                rota[i],
                rota[i + 1]
            )

        return total

    # =====================================================
    # ROTA ORIGINAL
    # =====================================================

    def rota_original(self):

        rota = [ORIGEM]

        for ponto in self.pontos:
            rota.append(ponto)

        rota.append(ORIGEM)

        distancia = self.distancia_total(rota)

        return rota, distancia

    # =====================================================
    # ROTA OTIMIZADA
    # =====================================================

    def rota_otimizada(self):

        nao_visitados = self.pontos.copy()

        rota = [ORIGEM]

        atual = ORIGEM

        while len(nao_visitados) > 0:

            mais_proximo = min(
                nao_visitados,
                key=lambda ponto:
                self.calcular_distancia(atual, ponto)
            )

            rota.append(mais_proximo)

            nao_visitados.remove(mais_proximo)

            atual = mais_proximo

        rota.append(ORIGEM)

        distancia = self.distancia_total(rota)

        return rota, distancia

    # =====================================================
    # CONSUMO
    # =====================================================

    def calcular_consumo(self, distancia):

        return distancia * CONSUMO_POR_KM

    # =====================================================
    # CUSTO DO COMBUSTÍVEL
    # =====================================================

    def calcular_custo(self, litros):

        return litros * PRECO_DIESEL

    # =====================================================
    # TEMPO DE VIAGEM
    # =====================================================

    def calcular_tempo(self, distancia):

        return distancia / VELOCIDADE_MEDIA

    # =====================================================
    # VERIFICAÇÃO DO TANQUE
    # =====================================================

    def verificar_tanque(self, rota):

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

    # =====================================================
    # FORMATAR ROTA
    # =====================================================

    def formatar_rota(self, rota):

        texto = ""

        for i, ponto in enumerate(rota):

            if ponto == ORIGEM:
                texto += "ORIGEM"
            else:
                texto += str(ponto)

            if i < len(rota) - 1:
                texto += " -> "

        return texto

    # =====================================================
    # GRÁFICO DAS ROTAS
    # =====================================================

    def gerar_grafico(self, rota_original, rota_otimizada):

        plt.figure(figsize=(10, 8))

        # -----------------------------
        # ROTA ORIGINAL
        # -----------------------------

        x_original = []
        y_original = []

        for ponto in rota_original:
            x_original.append(ponto[0])
            y_original.append(ponto[1])

        plt.plot(
            x_original,
            y_original,
            marker='o',
            linestyle='--',
            label='Rota Original'
        )

        # -----------------------------
        # ROTA OTIMIZADA
        # -----------------------------

        x_otimizada = []
        y_otimizada = []

        for ponto in rota_otimizada:
            x_otimizada.append(ponto[0])
            y_otimizada.append(ponto[1])

        plt.plot(
            x_otimizada,
            y_otimizada,
            marker='s',
            linewidth=3,
            label='Rota Otimizada'
        )

        # -----------------------------
        # NOMES DOS PONTOS
        # -----------------------------

        for i, ponto in enumerate(self.pontos, start=1):

            plt.text(
                ponto[0],
                ponto[1],
                f'P{i}',
                fontsize=10
            )

        # -----------------------------
        # ORIGEM
        # -----------------------------

        plt.scatter(
            ORIGEM[0],
            ORIGEM[1],
            s=250,
            marker='*',
            label='Origem'
        )

        plt.title('Comparação das Rotas')
        plt.xlabel('Coordenada X')
        plt.ylabel('Coordenada Y')

        plt.grid(True)

        plt.legend()

        plt.show()

    # =====================================================
    # RELATÓRIO COMPLETO
    # =====================================================

    def gerar_relatorio(self):

        print("\n" + "=" * 80)
        print("SISTEMA PROFISSIONAL DE OTIMIZAÇÃO DE ROTAS")
        print("=" * 80)

        print("\nPONTOS DE ENTREGA:")

        for i, ponto in enumerate(self.pontos, start=1):
            print(f"Ponto {i}: {ponto}")

        # =================================================
        # ROTA ORIGINAL
        # =================================================

        rota_original, dist_original = self.rota_original()

        consumo_original = self.calcular_consumo(dist_original)

        custo_original = self.calcular_custo(consumo_original)

        tempo_original = self.calcular_tempo(dist_original)

        print("\n" + "-" * 80)
        print("(a) ROTA ORIGINAL")
        print("-" * 80)

        print("\nSequência da rota:")
        print(self.formatar_rota(rota_original))

        print(f"\nDistância total: {dist_original:.2f} km")
        print(f"Consumo: {consumo_original:.2f} litros")
        print(f"Custo estimado: R$ {custo_original:.2f}")
        print(f"Tempo estimado: {tempo_original:.2f} horas")

        # =================================================
        # ROTA OTIMIZADA
        # =================================================

        rota_otimizada, dist_otimizada = self.rota_otimizada()

        consumo_otimizado = self.calcular_consumo(dist_otimizada)

        custo_otimizado = self.calcular_custo(consumo_otimizado)

        tempo_otimizado = self.calcular_tempo(dist_otimizada)

        print("\n" + "-" * 80)
        print("(b) ROTA OTIMIZADA")
        print("-" * 80)

        print("\nSequência otimizada:")
        print(self.formatar_rota(rota_otimizada))

        print(f"\nDistância total: {dist_otimizada:.2f} km")
        print(f"Consumo: {consumo_otimizado:.2f} litros")
        print(f"Custo estimado: R$ {custo_otimizado:.2f}")
        print(f"Tempo estimado: {tempo_otimizado:.2f} horas")

        # =================================================
        # COMPARAÇÃO
        # =================================================

        economia_km = dist_original - dist_otimizada

        economia_combustivel = (
            consumo_original - consumo_otimizado
        )

        economia_dinheiro = (
            custo_original - custo_otimizado
        )

        economia_percentual = (
            economia_combustivel / consumo_original
        ) * 100

        print("\n" + "-" * 80)
        print("(c) COMPARAÇÃO ENTRE ROTAS")
        print("-" * 80)

        print(f"\nEconomia de distância: {economia_km:.2f} km")

        print(
            f"Economia de combustível: "
            f"{economia_combustivel:.2f} litros"
        )

        print(
            f"Economia financeira: "
            f"R$ {economia_dinheiro:.2f}"
        )

        print(
            f"Redução percentual: "
            f"{economia_percentual:.2f}%"
        )

        # =================================================
        # TANQUE
        # =================================================

        precisa_reabastecer, restante = (
            self.verificar_tanque(rota_otimizada)
        )

        print("\n" + "-" * 80)
        print("(d) ANÁLISE DO COMBUSTÍVEL")
        print("-" * 80)

        print(f"\nCapacidade do tanque: {CAPACIDADE_TANQUE:.2f} L")
        print(f"Combustível restante: {restante:.2f} L")

        if precisa_reabastecer:
            print("\nO caminhão PRECISA reabastecer.")
        else:
            print("\nO caminhão NÃO precisa reabastecer.")

        # =================================================
        # ESTATÍSTICAS
        # =================================================

        media_entrega = (
            dist_otimizada / len(self.pontos)
        )

        print("\n" + "-" * 80)
        print("(e) ESTATÍSTICAS LOGÍSTICAS")
        print("-" * 80)

        print(f"\nNúmero de entregas: {len(self.pontos)}")

        print(
            f"Distância média por entrega: "
            f"{media_entrega:.2f} km"
        )

        print(
            f"Eficiência operacional: "
            f"{100 - economia_percentual:.2f}% "
            f"do consumo original"
        )

        print("\n" + "=" * 80)
        print("GERANDO GRÁFICO DAS ROTAS...")
        print("=" * 80)

        self.gerar_grafico(
            rota_original,
            rota_otimizada
        )

# =========================================================
# EXECUÇÃO PRINCIPAL
# =========================================================

pontos_entrega = [
    (2, 4),
    (5, 1),
    (3, 8),
    (7, 3),
    (1, 6),
    (9, 2),
    (6, 7),
    (8, 5)
]

sistema = SistemaLogistica(pontos_entrega)

sistema.gerar_relatorio()