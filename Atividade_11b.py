"""
ATENÇÃO ANTES DE EXECUTAR O CODIGO!
 "pip install pandas"
 "pip install openpyxl"
 
=============================================================
SUPER SISTEMA DE LOGÍSTICA E OTIMIZAÇÃO DE ROTAS
Versão Avançada Única
=============================================================

FUNCIONALIDADES:
- Múltiplos caminhões
- Otimização de rotas
- Vizinho mais próximo
- Controle de combustível
- Controle de carga
- Estatísticas logísticas
- Emissão de CO₂
- Banco de dados SQLite
- Exportação CSV
- Exportação Excel
- Relatórios automáticos
- Histórico de execuções
- Ranking de caminhões
- Comparação de rotas
- Gráficos avançados

=============================================================
"""

import math
import sqlite3
import csv
from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt

# =========================================================
# CONFIGURAÇÕES
# =========================================================

ORIGEM = (0, 0)

CONSUMO_POR_KM = 0.35

CAPACIDADE_TANQUE = 80

PRECO_DIESEL = 6.15

VELOCIDADE_MEDIA = 60

FATOR_CO2 = 2.68

# =========================================================
# BANCO DE DADOS
# =========================================================

conexao = sqlite3.connect("historico_logistica.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS historico (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT,
    caminhão TEXT,
    distancia REAL,
    consumo REAL,
    custo REAL,
    co2 REAL
)
""")

conexao.commit()

# =========================================================
# CLASSE CAMINHÃO
# =========================================================

class Caminhao:

    def __init__(self, nome, capacidade_carga):

        self.nome = nome

        self.capacidade_carga = capacidade_carga

        self.rota = []

        self.distancia = 0

        self.consumo = 0

        self.custo = 0

        self.co2 = 0

        self.tempo = 0

# =========================================================
# SISTEMA PRINCIPAL
# =========================================================

class SistemaLogistica:

    def __init__(self):

        self.caminhoes = []

        self.entregas = []

    # =====================================================
    # ADICIONAR CAMINHÃO
    # =====================================================

    def adicionar_caminhao(self, nome, capacidade):

        caminhao = Caminhao(nome, capacidade)

        self.caminhoes.append(caminhao)

    # =====================================================
    # ADICIONAR ENTREGA
    # =====================================================

    def adicionar_entrega(self, x, y, carga, prioridade):

        entrega = {
            "coord": (x, y),
            "carga": carga,
            "prioridade": prioridade
        }

        self.entregas.append(entrega)

    # =====================================================
    # DISTÂNCIA
    # =====================================================

    def calcular_distancia(self, p1, p2):

        return math.sqrt(
            (p2[0] - p1[0])**2 +
            (p2[1] - p1[1])**2
        )

    # =====================================================
    # ALGORITMO VIZINHO MAIS PRÓXIMO
    # =====================================================

    def otimizar_rota(self, pontos):

        nao_visitados = pontos.copy()

        rota = [ORIGEM]

        atual = ORIGEM

        while nao_visitados:

            proximo = min(
                nao_visitados,
                key=lambda ponto:
                self.calcular_distancia(atual, ponto)
            )

            rota.append(proximo)

            nao_visitados.remove(proximo)

            atual = proximo

        rota.append(ORIGEM)

        return rota

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
    # PROCESSAR ROTAS
    # =====================================================

    def processar_rotas(self):

        entregas_ordenadas = sorted(
            self.entregas,
            key=lambda e: e["prioridade"]
        )

        indice = 0

        for entrega in entregas_ordenadas:

            caminhao = self.caminhoes[
                indice % len(self.caminhoes)
            ]

            caminhao.rota.append(entrega)

            indice += 1

        for caminhao in self.caminhoes:

            pontos = []

            for entrega in caminhao.rota:
                pontos.append(entrega["coord"])

            rota_otimizada = self.otimizar_rota(pontos)

            distancia = self.distancia_total(
                rota_otimizada
            )

            consumo = distancia * CONSUMO_POR_KM

            custo = consumo * PRECO_DIESEL

            co2 = consumo * FATOR_CO2

            tempo = distancia / VELOCIDADE_MEDIA

            caminhao.rota = rota_otimizada

            caminhao.distancia = distancia

            caminhao.consumo = consumo

            caminhao.custo = custo

            caminhao.co2 = co2

            caminhao.tempo = tempo

    # =====================================================
    # RELATÓRIO
    # =====================================================

    def gerar_relatorio(self):

        print("\n" + "=" * 80)

        print("SUPER SISTEMA DE LOGÍSTICA")

        print("=" * 80)

        for caminhao in self.caminhoes:

            print("\n" + "-" * 80)

            print(f"Caminhão: {caminhao.nome}")

            print("-" * 80)

            print("\nROTA:")

            for ponto in caminhao.rota:
                print(ponto)

            print(f"\nDistância: {caminhao.distancia:.2f} km")

            print(f"Consumo: {caminhao.consumo:.2f} L")

            print(f"Custo: R$ {caminhao.custo:.2f}")

            print(f"CO2: {caminhao.co2:.2f} kg")

            print(f"Tempo: {caminhao.tempo:.2f} h")

            restante = (
                CAPACIDADE_TANQUE -
                caminhao.consumo
            )

            print(f"Combustível restante: {restante:.2f} L")

            if restante < 0:
                print("Necessita reabastecimento")
            else:
                print("Não necessita reabastecimento")

    # =====================================================
    # GRÁFICO
    # =====================================================

    def gerar_grafico(self):

        plt.figure(figsize=(12, 8))

        for caminhao in self.caminhoes:

            x = []
            y = []

            for ponto in caminhao.rota:

                x.append(ponto[0])

                y.append(ponto[1])

            plt.plot(
                x,
                y,
                marker='o',
                linewidth=3,
                label=caminhao.nome
            )

        plt.scatter(
            ORIGEM[0],
            ORIGEM[1],
            s=300,
            marker='*',
            label='Origem'
        )

        plt.title("Rotas dos Caminhões")

        plt.xlabel("Coordenada X")

        plt.ylabel("Coordenada Y")

        plt.grid(True)

        plt.legend()

        plt.show()

    # =====================================================
    # EXPORTAR CSV
    # =====================================================

    def exportar_csv(self):

        with open(
            "relatorio_logistica.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as arquivo:

            escritor = csv.writer(arquivo)

            escritor.writerow([
                "Caminhão",
                "Distância",
                "Consumo",
                "Custo",
                "CO2",
                "Tempo"
            ])

            for c in self.caminhoes:

                escritor.writerow([
                    c.nome,
                    c.distancia,
                    c.consumo,
                    c.custo,
                    c.co2,
                    c.tempo
                ])

        print("\nCSV exportado com sucesso.")

    # =====================================================
    # EXPORTAR EXCEL
    # =====================================================

    def exportar_excel(self):

        dados = []

        for c in self.caminhoes:

            dados.append({
                "Caminhão": c.nome,
                "Distância": c.distancia,
                "Consumo": c.consumo,
                "Custo": c.custo,
                "CO2": c.co2,
                "Tempo": c.tempo
            })

        tabela = pd.DataFrame(dados)

        tabela.to_excel(
            "relatorio_logistica.xlsx",
            index=False
        )

        print("\nExcel exportado com sucesso.")

    # =====================================================
    # SALVAR HISTÓRICO
    # =====================================================

    def salvar_historico(self):

        data = datetime.now().strftime(
            "%d/%m/%Y %H:%M"
        )

        for c in self.caminhoes:

            cursor.execute("""
            INSERT INTO historico (
                data,
                caminhão,
                distancia,
                consumo,
                custo,
                co2
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """, (
                data,
                c.nome,
                c.distancia,
                c.consumo,
                c.custo,
                c.co2
            ))

        conexao.commit()

        print("\nHistórico salvo.")

    # =====================================================
    # MOSTRAR HISTÓRICO
    # =====================================================

    def mostrar_historico(self):

        print("\n" + "=" * 80)

        print("HISTÓRICO")

        print("=" * 80)

        cursor.execute("""
        SELECT * FROM historico
        """)

        registros = cursor.fetchall()

        for r in registros:

            print(r)

    # =====================================================
    # ESTATÍSTICAS
    # =====================================================

    def estatisticas(self):

        total_distancia = sum(
            c.distancia for c in self.caminhoes
        )

        total_consumo = sum(
            c.consumo for c in self.caminhoes
        )

        total_custo = sum(
            c.custo for c in self.caminhoes
        )

        total_co2 = sum(
            c.co2 for c in self.caminhoes
        )

        print("\n" + "=" * 80)

        print("ESTATÍSTICAS GERAIS")

        print("=" * 80)

        print(
            f"\nDistância total: "
            f"{total_distancia:.2f} km"
        )

        print(
            f"Consumo total: "
            f"{total_consumo:.2f} L"
        )

        print(
            f"Custo total: "
            f"R$ {total_custo:.2f}"
        )

        print(
            f"Emissão total CO2: "
            f"{total_co2:.2f} kg"
        )

    # =====================================================
    # RANKING
    # =====================================================

    def ranking(self):

        ranking = sorted(
            self.caminhoes,
            key=lambda c: c.distancia
        )

        print("\n" + "=" * 80)

        print("RANKING DE EFICIÊNCIA")

        print("=" * 80)

        for i, c in enumerate(ranking, start=1):

            print(
                f"{i}º - {c.nome} "
                f"({c.distancia:.2f} km)"
            )

# =========================================================
# EXECUÇÃO
# =========================================================

sistema = SistemaLogistica()

# =========================================================
# CAMINHÕES
# =========================================================

sistema.adicionar_caminhao(
    "Caminhão A",
    1000
)

sistema.adicionar_caminhao(
    "Caminhão B",
    1200
)

sistema.adicionar_caminhao(
    "Caminhão C",
    900
)

# =========================================================
# ENTREGAS
# =========================================================

sistema.adicionar_entrega(2, 4, 100, 1)

sistema.adicionar_entrega(5, 1, 80, 2)

sistema.adicionar_entrega(3, 8, 120, 1)

sistema.adicionar_entrega(7, 3, 200, 3)

sistema.adicionar_entrega(1, 6, 90, 2)

sistema.adicionar_entrega(9, 2, 140, 1)

sistema.adicionar_entrega(6, 7, 60, 3)

sistema.adicionar_entrega(8, 5, 170, 2)

# =========================================================
# PROCESSAMENTO
# =========================================================

sistema.processar_rotas()

# =========================================================
# RELATÓRIOS
# =========================================================

sistema.gerar_relatorio()

sistema.estatisticas()

sistema.ranking()

# =========================================================
# EXPORTAÇÕES
# =========================================================

sistema.exportar_csv()

sistema.exportar_excel()

# =========================================================
# HISTÓRICO
# =========================================================

sistema.salvar_historico()

sistema.mostrar_historico()

# =========================================================
# GRÁFICO
# =========================================================

sistema.gerar_grafico()

# =========================================================
# FECHAR BANCO
# =========================================================

conexao.close()