from flask import Flask, render_template
import plotly.graph_objs as go
import plotly.io as pio

app = Flask(__name__)

# Dados embutidos manualmente
data = [
    {"Atividade": "Elaboração de Minuta Recibo - Isa Advogada", "Descrição": "Elaboração de minutas de recibo para documentos", "Tempo de Elaboracao": "1h e 30min", "Quantidade": "36 Minutas", "Tempo Economizado": "2h"},
    {"Atividade": "Elaboração de Minuta Recibo - Lyne Química", "Descrição": "Elaboração de minutas de recibo para documentos", "Tempo de Elaboracao": "1h e 30min", "Quantidade": "36 Minutas", "Tempo Economizado": "2h"},
    {"Atividade": "Elaboração de Minuta Recibo - Suzy Engenheira", "Descrição": "Elaboração de minutas de recibo para documentos", "Tempo de Elaboracao": "1h e 30min", "Quantidade": "36 Minutas", "Tempo Economizado": "2h"},
    {"Atividade": "Adaptação de Tabela Excel Formato Judicial", "Descrição": "Adaptação de tabela Excel para formato judicial", "Tempo de Elaboracao": "2h e 30min", "Quantidade": "2 Planilhas", "Tempo Economizado": "2h"},
    {"Atividade": "Organização (2017-2024)", "Descrição": "Organização de documentos e informações para prestação de contas e folha de pagamento", "Tempo de Elaboracao": "3h", "Quantidade": "-", "Tempo Economizado": "9h"},
    {"Atividade": "Separação de Documentos por Ano (PDF)", "Descrição": "Separação de documentos por ano em formato PDF", "Tempo de Elaboracao": "30min", "Quantidade": "171 Paginas", "Tempo Economizado": "3h"},
    {"Atividade": "Elaboração de Minuta Recibo Compliance", "Descrição": "Elaboração de minutas de recibo para compliance", "Tempo de Elaboracao": "2h", "Quantidade": "8 Paginas", "Tempo Economizado": "6h"},
    {"Atividade": "Suporte Equipe", "Descrição": "Suporte à equipe durante o processo de auditoria", "Tempo de Elaboracao": "Disponivel", "Quantidade": "-", "Tempo Economizado": "-"},
    {"Atividade": "Algoritmo de Identificação e Extração de Notas nos Diretórios", "Descrição": "Algoritmo para identificar e extrair notas fiscais nos diretórios.", "Tempo de Elaboracao": "6h", "Quantidade": "80.000 Notas", "Tempo Economizado": "105 horas"},
    {"Atividade": "Algoritmo de Otimização de Combinações para Soma Alvo", "Descrição": "Algoritmo para otimizar combinações de valores para atingir uma soma alvo.", "Tempo de Elaboracao": "5h e 30min", "Quantidade": "80.000! combinações", "Tempo Economizado": "Incalculavel e Impreciso"},
    {"Atividade": "Reordenação e Reestruturação das Notas Fiscais", "Descrição": "Organizar notas fiscais válidas em pastas de entrada e saída de acordo com a data correta.", "Tempo de Elaboracao": "5h", "Quantidade": "47 pastas", "Tempo Economizado": "174 horas"},
    {"Atividade": "Código de Leitura de Arquivos (PDF)", "Descrição": "Abrir e extrair informações de notas fiscais (PDF) para obter valores e datas, e identificar inválidas.", "Tempo de Elaboracao": "11h", "Quantidade": "Leitura de 80.000 Arquivos", "Tempo Economizado": "600 horas"},
    {"Atividade": "Código de Criação de Diretórios", "Descrição": "Criar pastas para visualização das notas fiscais e planilhas de resumo, com os valores apropriados.", "Tempo de Elaboracao": "2h", "Quantidade": "47 pastas", "Tempo Economizado": "10 horas"},
    {"Atividade": "Código de Criação das Planilhas Reformuladas", "Descrição": "Criar planilhas com valores válidos extraídos das notas fiscais, seguindo o novo modelo estabelecido.", "Tempo de Elaboracao": "3h e 30min", "Quantidade": "5 Planilhas", "Tempo Economizado": "26 horas"},
    {"Atividade": "Algoritmo de Validação e Revisão", "Descrição": "Conferir valores e posições de notas fiscais nas pastas e adicionar ao documento final.", "Tempo de Elaboracao": "9h", "Quantidade": "Revisao de 80.000 Notas, 47 Pastas e todas as linhas de 5 Planilhas", "Tempo Economizado": "Incalculavel e Impreciso"},
    {"Atividade": "Algoritmo de Extração de Dados e Criação de Planilhas Mensais e Anuais", "Descrição": "Manipular dados e criar planilhas para todos os anos e meses especificados, adicionando aos diretórios corretos.", "Tempo de Elaboracao": "4h e 30min", "Quantidade": "5 Planilhas", "Tempo Economizado": "Incalculavel e Impreciso"}
]

# Função para converter tempo no formato '2h e 30min' para minutos
def convert_to_minutes(time_str):
    try:
        if 'Incalculavel' in time_str or 'Disponivel' in time_str:
            return 0
        parts = time_str.split(' e ')
        hours = int(parts[0].replace('h', '').replace(' horas', ''))
        minutes = int(parts[1].replace('min', '')) if len(parts) > 1 else 0
        return hours * 60 + minutes
    except Exception:
        return 0  # Retorna 0 para entradas inválidas

@app.route('/')
def activities():
    activities_list = [row for row in data if row['Tempo de Elaboracao'] not in ['-', ''] and row['Tempo Economizado'] not in ['-', '']]
    
    total_elaboracao_str = f"59h"
    total_economizado_str = f"915h"
    
    # Criar gráfico para tempo total
    fig = go.Figure(data=[
        go.Bar(name='Tempo de Elaboração Total', x=['Total'], y=[59], marker_color='indianred'),
        go.Bar(name='Tempo Economizado Total', x=['Total'], y=[915], marker_color='lightblue')
    ])
    fig.update_layout(
        title='Comparação Total de Tempo de Elaboração e Tempo Economizado', 
        barmode='group', 
        template='plotly_dark', 
        margin=dict(l=0, r=0, t=30, b=0),
        width=1000  # Aumenta a largura do gráfico
    )
    total_comparison_chart = pio.to_html(fig, full_html=False, include_plotlyjs='cdn')

    return render_template('activities.html', activities=activities_list, total_elaboracao=total_elaboracao_str, total_economizado=total_economizado_str, total_comparison_chart=total_comparison_chart)

@app.route('/overall_comparison')
def overall_comparison():
    fig = go.Figure(data=[
        go.Bar(name='Tempo de Elaboração Total', x=['Total'], y=[59], marker_color='indianred'),
        go.Bar(name='Tempo Economizado Total', x=['Total'], y=[915], marker_color='lightblue')
    ])
    fig.update_layout(
        title='Comparação Total de Tempo de Elaboração e Tempo Economizado', 
        barmode='group', 
        template='plotly_dark', 
        margin=dict(l=0, r=0, t=30, b=0),
        width=1000  # Aumenta a largura do gráfico
    )
    comparison_chart = pio.to_html(fig, full_html=False, include_plotlyjs='cdn')
    return render_template('overall_comparison.html', comparison_chart=comparison_chart)

if __name__ == '__main__':
    app.run(debug=True)
