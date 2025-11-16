from langchain_core.prompts import ChatPromptTemplate


prompt_score = """
Você deve calcular uma pontuação final (de 0.0 a 10.0) baseada nos seguintes critérios:

1. Experiência (Peso: 35%): ...
2. Habilidades Técnicas (Peso: 25%): ...
3. Educação (Peso: 15%): ...
4. Pontos Fortes (Peso: 15%): ...
5. Pontos Fracos (Desconto de até 10%): ...

A nota final deve refletir a média ponderada desses fatores.

⚠️ IMPORTANTE:
- Retorne APENAS a pontuação final.
- Retorne SOMENTE um número decimal.
- Não retorne texto, justificativa, JSON, explicação ou qualquer outro conteúdo.
- Apenas o número, exemplo: 7.2
"""


prompt_template = ChatPromptTemplate.from_template("""
Você é um especialista em Recursos Humanos.

Analise o currículo e a vaga usando os critérios fornecidos.

{prompt_score}

Currículo:
'''{cv}'''

Vaga:
'''{job}'''
""")