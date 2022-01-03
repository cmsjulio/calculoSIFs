# English
This page hosts the codes that were used in the research project named

*"Piping design: ASME B31.3 and ASME B31J stress intensification factors comparison" [written in Portuguese]

the original text can be found [here](https://www.researchgate.net/publication/357299413_Comparacao_dos_fatores_de_intensificacao_de_tensao_das_normas_ASME_B313_e_ASME_B31J_para_dimensionamento_de_tubulacoes?channel=doi&linkId=61c529c8da5d105e55f23292&showFulltext=true).

## Abstract

*This work, at first, historically contextualizes the emergence of the ASME B31.3 code for design of piping systems, following with a brief description of its scope and nature. It then, in order to clarify pertinent but not addressed in the code topics, proceeds in developing a strength of materials and flexibility analysis review. From such development, the means by which B31.3 deals with flexibility analysis is explained, so that, from the exposition of equations presented in the code, the stress intensification factor, the main topic of this work, is introduced. Such factors are important as they allow us to perform stress calculations in piping systems where a variety of components may be present (tees, reducers, elbows etc.). From such introduction and initial exposition, ASME B31.3 Appendix D and B31J are introduced as mutually accepted ways for obtaining values for such factors. The accessories for which stress intensification factors are to be calculated via both codes are then presented: bends, tees, and reducers, with results being shown, compared, and discussed in the following – with multiple points of non conservatism from Appendix D being noted. Flexibility factors are also calculated and compared.*

## Quick guide for the code files

All of the files that were used in there project were made available here. The relation between each case presented in the written work and the files list follows:

**Case 1.1 -> calculo-tcc-1.1-NOVOSPARAMETROS.py**

**Case 1.2 -> calculo-tcc-1.2-NOVOSPARAMETROS.py**

**Case 1.3 -> calculo-tcc-1.3-NOVOSPARAMETROS.py**

**Cases 2.1, 2.2 e 2.3 -> calculo-tcc-2.1a3funcao.py**

**Case 3.1 -> calculo-tcc-3.1comH.py**


# Português
Código utilizado para cálculo dos fatores de intensificação de tensão e de flexibilidade no trabalho de conclusão de curso.

O trabalho, de título:

**"Comparação dos fatores de intensificação de tensão das normas ASME B31.3 e ASME B31J para dimensionamento de tubulações"**, 

pode ser acessado por [aqui](https://www.researchgate.net/publication/357299413_Comparacao_dos_fatores_de_intensificacao_de_tensao_das_normas_ASME_B313_e_ASME_B31J_para_dimensionamento_de_tubulacoes?channel=doi&linkId=61c529c8da5d105e55f23292&showFulltext=true).

## Resumo do trabalho:

*Este trabalho, de início, contextualiza historicamente o surgimento do código de projeto de sistemas de tubulação ASME B31.3; descrevendo de maneira breve, em seguida, seu escopo e sua natureza. A fim de esclarecer pontos não abordados no mesmo, mas pertinentes quanto ao escopo deste trabalho, uma revisão de resistência dos materiais é realizada – bem como um desenvolvimento do tema análise de flexibilidade. A partir de tal desenvolvimento, aborda-se o modo como o código ASME B31.3 lida com a análise de flexibilidade, culminando – a partir da exposição das equações dispostas no código – na introdução do assunto central deste trabalho: os fatores de intensificação de tensão. Tais fatores são de grande importância no projeto de tubulações, pois por meio destes o cálculo de tensão torna-se possível para tubulações onde há a presença dos mais diversos componentes e acessórios (tês, reduções, curvas etc.). Desta introdução e exposição iniciais, apresenta-se as duas maneiras mutuamente aceitáveis para obtenção de tais fatores: Apêndice D do ASME B31.3 e ASME B31J. Delimita-se, então, os componentes cujas fórmulas de ambos códigos serão comparadas: curvas, tês e reduções; seguindo-se com a apresentação efetiva dos resultados obtidos em cada caso, onde notou-se (assumindo mais precisas as equações do B31J) pontos de não conservadorismo por parte do Apêndice D. Fatores de flexibilidade também foram calculados e comparados.*

## Orientação quanto aos códigos

Todo material com o qual se trabalhou foi aqui inserido, inclusive aqueles que depois necessitaram revisão -- e os experimentais.

Os documentos em forma final, qual seja, aqueles que foram utilizados na obtenção dos resultados apresentados no TCC, são:

**Caso 1.1 -> calculo-tcc-1.1-NOVOSPARAMETROS.py**

**Caso 1.2 -> calculo-tcc-1.2-NOVOSPARAMETROS.py**

**Caso 1.3 -> calculo-tcc-1.3-NOVOSPARAMETROS.py**

**Casos 2.1, 2.2 e 2.3 -> calculo-tcc-2.1a3funcao.py**

**Caso 3.1 -> calculo-tcc-3.1comH.py**


Os demais documentos são de etapas anteriores ao resultado final obtido e estão aqui dispostos para quem possa interessar.

Os códigos dos casos 1.1, 1.2 e 1.3 utilizam de uma abordagem passo a passo (com cada linha equivalente a, por assim dizer, uma etapa no processo mateḿático de solução do problema); nos casos 2.1, 2.2 e 2.3, contudo, utiliza-se de uma abordagem funcional (muito devido à maior complexidade destes casos); o caso 3.1 herda a estrutura utilizada nos casos 2.1, 2.2 e 2.3 e possui também uma estrutura de código funcional.
