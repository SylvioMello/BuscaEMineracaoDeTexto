from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  messages=[
    {"role": "system", "content": "Você é um professor de português com décadas de experiência. Além disso, você é especialista em correção de redações do ENEM. Você domina completamente as cinco competências avaliadas na redação e consegue facilmente identificar erros e acertos."},
    {"role": "user", "content": """Avalie essa redação modelo ENEM. Você deve focar principalmente na competência 5, conclusão. Mais especificamente, você deve verificar se todos os problemas levantados durante os parágrafos anteriores da dissertação foram resolvidos na conclusão. Então, sua resposta deve vir no seguinte formato: 
Problema 1: 
Resumo de poucas palavras do primeiro problema abordado ao longo da dissertação. 
Abordagem na dissertação: [TRECHO CURTO DE POUCAS PALAVRAS ONDE O PROBLEMA É MENCIONADO PELA PRIMEIRA VEZ] 
Abordagem na conclusão: [TRECHO CURTO DE POUCAS PALAVRAS ONDE O PROBLEMA É MENCIONADO NA CONCLUSÃO] 

Problema 2: ... 

Caso algum problema citado ao longo da dissertação não seja resolvido na conclusão, você deve escrever "NAO ENCONTRADO" na parte "Abordagem na conclusão".
Redação:
As dificuldades da ciência brasileira
O incêndio que destruiu o Museu Nacional, uma das mais importantes instituições acadêmicas do país, é o resultado da desvalorização da qual a ciência é vítima. No âmbito político, o setor é alvo de sucessivos cortes de verba, principalmente nos últimos anos, ameaçando o futuro do Brasil. Por outro lado, a ciência é culturalmente menosprezada pela população, que por não ter recebido uma educação científica, desconhece sua importância.
Em primeira análise, os países desenvolvidos aumentam os gastos com ciência em momentos de crise econômica. Isso porque a história mostra que a produção de conhecimento é um eficiente caminho para o enriquecimento de uma nação, como é o caso dos EUA, que enriqueceram vendendo tecnologia para o mundo, principalmente durante a Segunda Guerra Mundial. Além disso, ciência e educação não podem ser dissociadas, já que sem ciência não há produção de conhecimento, e sem educação não há quem produza conhecimento. Portanto, parar de investir em ciência devido a atual crise financeira é uma atitude imediatista e que diminui as possibilidades de desenvolvimento do Brasil.
No entanto, existe uma cultura de amadorismo da ciência no Brasil, na qual produzir conhecimento sequer é visto como um trabalho. Isso devido ao processo de colonização, no qual poucas atividades intelectuais eram exercidas no país. Logo, o senso comum brasileiro foi moldado de forma a enxergar o trabalho exclusivamente como atividade que gera lucro imediato. O resultado disso é precarização da carreira acadêmica, que oferece salários muito inferiores ao mercado, e, portanto, tem dificuldade em atrair bons cientistas, colocando o Brasil nas últimas posições na produção de conhecimento anual.
A fim de tornar a carreira acadêmica mais atrativa financeiramente e auxiliar no desenvolvimento de pesquisas, o Governo Federal através do Ministério da Economia deve, no mínimo, dobrar o atual percentual do PIB destinado à ciência. Isso refletiria rapidamente em desenvolvimento econômico, já que o Brasil atuaria como exportador de tecnologia. Por outro lado, a população precisa compreender a importância da ciência em suas vidas. Para isso os Institutos de Pesquisa devem investir em divulgação científica, que leve o conhecimento através de uma linguagem simples para a população leiga."""}
  ]
)

# Extract the content of the message
correcao = completion.choices[0].message.content

# Print the poem in a more readable format
print(correcao)

# Save the poem to a text file
with open("redacao_teste_correcao.txt", "w") as file:
    file.write(correcao)