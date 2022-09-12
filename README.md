<h1>STAR JEANS - WEB SCRAPING</h1>

<p align="center">
<img src="https://user-images.githubusercontent.com/76838937/189499048-c9f576f0-4add-487a-9cf0-547deff18fd3.png">
</p>

> Status do Projeto: Concluído :heavy_check_mark:
<!-- > Status do Projeto: Conluído :heavy_check_mark: -->
<!-- > Status do Projeto: Em andamento :warning: -->

**Observação**: A Star Jeans é uma empresa fictícia, criada somente para dar contexto a esse projeto. Os dados que serão apresentados foram extraídos dos sites de duas lojas reais, utilizando ferramentas de web scraping. O intuito desse projeto é inteiramente de aprendizado e toda situação que será discutida aqui é para esse fim. Ao final da apresentação do projeto, será possível visualizar um dashboard com as principais informações!


**Acesso ao Projeto**: Caso tenha interesse em acessar o projeto completo, basta clicar aqui --> [Star Jeans - Web Scraping](https://github.com/Mat004/Web-Scraping-Star-Jeans/blob/main/p02_webscraping.ipynb)
</br>

<h1> Sobre a Star Jeans </h1>

<p align='justify'> A Star Jeans é uma empresa que está ingressando no mercado americano de confecção de calças jeans, com foco inicial no público masculino. O seu objetivo é entrar nesse mercado com um modelo de negócio do tipo E-commerce, com produtos que sejam acessíveis e que tenham uma boa qualidade de construção. </p>
</br>

<h1> Problema de negócio </h1>
<p align='justify'> Os sócios Eduardo e Marcelo estão planejando entrar no mercado de moda dos USA, como um modelo de negócio do tipo E-commerce. O produto inicial que eles decidem vender é um tipo de calça jeans masculina. No entanto, eles não possuem expertise nesse nicho, principalmente no funcionamento do mercado local, os sócios decidem contratar uma consultoria de Ciência de Dados para solucionarem as seguintes perguntas: </p>
<ul>
  <li> Qual o melhor preço de venda para as calças? </li>
  <li> Quantos tipos de calças e suas cores para o produto inicial? </li>
  <li> Quais as matérias-primas necessárias para confeccionar as calças? </li>
</ul>
</br>

<h1> Planejamento da solução </h1>

<p align='justify'> A solução para os questionamentos apresentados acima seguiu os seguintes passos: </p>
<ol type='I'>
  <li> <b>Questão e entendimento do negócio:</b> </li>
    <ul>
      <li> Qual o melhor preço de venda para as calças? <i>R: Mediana dos preços das concorrentes</i> </li>
      <li> Quantos tipos de calças e suas cores para o produto inicial? <i>R: Selecionar os 5 com maior quantidade</i> </li>
      <li> Quais as matérias-primas necessárias para confeccionar as calças? <i>R: Extrair o material de composição dos sites</i> </li>
    </ul>
    </br>
  <li> <b>Planejamento da entrega:</b> </li>
    <ul>
      <li> Será gerado ao final um arquivo com o resumo dos principais items, preços, cores e matéria-prima a serem considerados </li>
      <li> Os principais insights dos dados extraídos com um aplicativo no Steamlit </li>
    </ul>
    </br>
  <li> <b>Coleta de dados:</b> </li>
    <ul>
      <li> As principais concorrentes da Star Jeans são a: H&M e a Macy's </li>
      <li> Tendo conhecimento de quais são as páginas da internet de cada concorrente, extrair os dados com <i>Selenium</i> e/ou <i>Beautiful Soup</i>         </li>
      <li> Os dados foram coletados durante 12 dias, para ter um perfil de evolução dos preços e gerar outros insights </li>
    </ul>
    </br>
  <li> <b>Limpeza dos dados:</b> </li>
    <ul>
      <li> Ao final da extração utilizar <i>regular expression</i> para ajustar os dados para posterior análise </li>
      <li> Outra forma de tratar os dados é com as próprias ferramentas da biblioteca <i>Pandas</i> </li>
    </ul>
    </br>
  <li> <b>Exploração e análise dos dados:</b> </li>
     <ul>
      <li> Usar as principais bibliotecas do <i>Python</i> para analisar os dados extraídos: <i>Pandas</i>, <i>Seaborn</i> e <i>Matplotlib</i> </li>
    </ul>
    </br>
  <li> <b>Deploy do projeto no streamlit</b> </li>
  </br>
  <li> <b>Entrega do projeto</b> </li>

</ol>
</br>

<h1> Análise exploratória de dados </h1>
<h2> 1 - Descrição geral dos dados </h2>
<h3> 1.1 - H&M </h3>
<p align='justify'> Após as etapas de coleta e limpeza de dados, foi realizado uma descrição geral dos resultados com o intuito de inferir alguns fenômenos. Abaixo está a descrição dos dados para a coleta da H&M:
</p>

</br>
<p>Imagem 1: Dados H&M</p>
<p align="center">
<img src="https://user-images.githubusercontent.com/76838937/167298729-140ed370-514a-4f0e-a54a-6631d7083ddd.png">
</p>
<ul>
  <li> product_price: Preço do produto </li>
  <li> product_price_new: Preço de promoção do produto </li>
  <li> cotton: Porcentagem de algodão no produto </li>
  <li> spandex: Porcentagem de spandex no produto </li>
  <li> polyester: Porcentagem de polyester no produto </li>
  <li> elastomultiester: Porcentagem de elastomultiester no produto </li>
</ul>
<p align='justify'> Analisando os principais campos <i>product_price</i> e <i>product_price_new</i>, podemos observar que na H&M tem-se produtos custando no máximo US$ 119,99 e no mínimo US$ 11,99, enquanto os produtos em promoção custam no máximo US$ 39,99. É válido ressaltar os valores de média e mediana do <i>product_price</i>, que são respectivamente US$ 44,62 e US$ 39,99, isso nos indica que a grande maioria dos produtos estão concentradas em valores em torno de US$ 40,00. Como se trata de uma situação em que não haverá distruibuição normal dos dados, a mediana é a mais adequada para analisar o comportamento dos preços. </p>
</br>

<h3> 1.2 - Macy's </h3>
<p align='justify'> Seguindo a mesma linha de raciocínio, após a extração e limpeza dos dados do site, foi realizado a descrição geral dos dados, sendo possível observar na imagem abaixo:
</p>

</br>
<p>Imagem 2: Dados Macy's</p>
<p align="center">
<img src="https://user-images.githubusercontent.com/76838937/167299480-423ca29a-02b4-46d6-9559-375bf433007c.png">
</p>
<ul>
  <li> product_price: Preço do produto </li>
  <li> product_sale: Preço de promoção do produto </li>
</ul>
<p align='justify'> Na Macy's temos o <i>product_price</i> tendo o máximo em US$ 348,00 e o preço mínimo US$ 29,50, a mediana dos preços ficou em torno de US$ 89,00. Nos preços das calças em promoção, encontramos preços de no máximo US$ 167,30. </p>

<!-- quebra de linha-->
</br>

<!--
<h3> 1.3 - Comparação </h3>
<p align='justify'> A principal diferença entre os dados das duas concorrentes é na informação de composição do que compõe as calças. Na H&M há os valores das porcentagens de cada componente, enquanto na Macy's as informações que são fornecidas sobre composição são somente quais componentes estão presentes. Porém, a informação mais crucial está nos preços de vendas. É notório a grande diferença entre os valores dos produtos vendidos entre as duas empresas, na H&M temos produtos mais baratos enquanto na Macy's mais caros, o que nos leva a inferir que a segunda fornece produtos de <i>grife</i> e consequentemente a primeira com produtos mais acessíveis.</p>
<p align='justify'> Esse fator não descredibiliza e descarta o que foi extraído da Macy's. Podendo ser usado para melhor compreensão do comportamento dos preços e dessa forma analisar, de forma adequada, o mercado de calças e seus fenômenos. </p>
-->

<h2>2 - Hipóteses </h2>
<h3>2.1 - O dia com mais promoções é na sexta-feira </h3>
  <p align='justify'> Analisando os dados extraídos das duas empresas, temos que há comportamentos similares quanto a quantidade de
    promoções durante a semana. Abaixo temos as imagens do perfil de promoções para cada empresa:
  </p>
  </br>
  <p>Imagem 3: Quantidade de descontos H&M </p>
  <p align="center">
  <img src="https://user-images.githubusercontent.com/76838937/189499770-c8cb0d53-bb19-4b86-845f-6ba9e003ca28.png">
  </p>

</br>
<p>Imagem 4: Quantidade de descontos Macy's </p>
<p align="center">
<img src="https://user-images.githubusercontent.com/76838937/189499819-c2f8367e-116f-4f7b-9e15-cecf1115460d.png">
</p>

</br>
  <p>Algumas pontos que podem explicar o comportamento das promoções: </p>
  <ul>
    <li>Há uma grande queda de <i>Domingo</i> para <i>Segunda-feira</i>, comportamento explicado pelo fato das pessoas voltarem para suas rotinas
      (trabalho, faculdade, etc) às Segundas, tendo menos tempo para acessar internet;</li>
    <li>Os maiores valores podem ser encontrado na Sexta-feira na H&M, na Macy's observa-se a maior quantidade na
      Terça-feira, no entanto os valores na Sexta são bem próximos. Esse comportamento é explicado pelo oposto do
      que ocorre de Domingo para Segunda. Nessa situação, as pessoas estão entrando no "final de semana",
      tendo mais tempo para navegação na internet e dessa forma passar mais tempo escolhendo algum produto que deseje comprar.</li>

  </ul>
<p><b>Apesar de termos um valor diferente na Macy's, mas bem próximo da H&M, essa hipóteses é VERDADEIRA. A maior quantidade de descontos
é encontrado na Sexta-feira</b></p>
</br>

<h3>2.2 - O máximo de desconto que pode ser encontrado é de 60% </h3>
<p align='justify'> A partir dos dados de preço de venda, em que se extraiu tanto o preço normal quanto o preço em promoção,
  foi possível obter a porcentagem de desconto concedido aos itens em promoção.
</p>

<p align='justify'> Na H&M, o maior desconto encontrado foi de <b>66,67%</b>, no produto <i>Slim Tapered Jeans</i>. O preço inicial do
  produto era de <b>US&#36; 89,99</b> e foi para <b>US&#36; 29,99</b>.
</p>

<p align='justify'> No caso da Macy's, o maior desconto encontrado foi de <b>49,70%</b>, no produto <i>INC International Concepts</i>.
  O preço inicial do produto era de <b>US&#36; 79,50</b> e foi para <b>US&#36; 39,99</b>.
</p>

<p><b>A hipóteses é FALSA, tendo em vista que o desconto máximo observado foi de aproximadamente 67%.</b></p>
</br>

<h3>2.3 - Os 5 modelos com maiores quantidades de calças, são as que possuem o valor em torno da mediana total</h3>
<p align='justify'> Com os dados da H&M e da Macy's, foi possível realizar o top 5 das calças com maior quantidade e seus
  respectivos valores medianos.
</p>

</br>
<p>Imagem 5: Tabela H&M </p>
<p align="center">
<img src="https://user-images.githubusercontent.com/76838937/189504264-77170f68-124f-4aa0-9d1a-850d016234b6.jpeg">
</p>

</br>
<p>Imagem 6: Tabela Macy's </p>
<p align="center">
<img src="https://user-images.githubusercontent.com/76838937/189504270-d9046d9b-2e7f-4a3d-bd13-96767f43596e.jpeg">
</p>

</br>

<p><b>A hipóteses é FALSA, pois os valores diferem em um grau alto da mediana geral do preços das calças.</b></p>
</br>


<h3>2.4 - Calças com composição de algodão acima de 90%, custam acima do preço mediano</h3>
<p align='justify'> As informações para essa hipótese foram bem equilibradas, tendo 9 estilos de calças com preço acima ou igual a mediana
  geral e 9 estilgos de calças com preço menor que a mediana. No entanto, a quantidade de calças é maior no segundo caso.
</p>

</br>
<p>Imagem 7: Calças com preço acima da mediana </p>
<p align="center">
<img src="https://user-images.githubusercontent.com/76838937/189504557-2fc9bcf6-3ba2-4c94-befe-3f5fc1fc47d7.png">
</p>

</br>
<p>Imagem 8: Calças com preço abaixo da mediana</p>
<p align="center">
<img src="https://user-images.githubusercontent.com/76838937/189504567-ab0244eb-cfa2-4611-8426-c059c3d30a74.png">
</p>

</br>

<p><b>A hipóteses é FALSA, pois a maior quantidade de calças está com preços abaixo da mediana geral.</b></p>
</br>


<h3>2.5 - Items em promoção possuem cor clara</h3>
<p align='justify'> As cores das calças são parâmetros utilizados na hora da compra, algumas pessoas preferem cores mais escuras
  outras mais claras. Nesse caso, os dados estão de certo modo equilibrados, há tanto cores claras quanto escuras na lista abaixo:
</p>

</br>
<p>Imagem 9: Calças e suas cores</p>
<p align="center">
<img src="https://user-images.githubusercontent.com/76838937/189504744-c97f41bc-3476-40a1-bc0e-53e450871ad7.png">
</p>

</br>

<p><b>A hipóteses é FALSA, a quantidade de calças de cor clara em promoção, não superou as de cores escuras. Pelo contrário,
ficaram com valores próximos.</b></p>
</br>


<h1> Problema de negócio </h1>

**A solução completa do problema, com os detalhes, pode ser encontrado no tópico 7 do projeto**: [Star Jeans - Web Scraping](https://github.com/Mat004/Web-Scraping-Star-Jeans/blob/main/p02_webscraping.ipynb)
</br>

<p align='justify'>O grande objetivo do projeto é responder as perguntas dos sócios da Star Jeans:
</p

<ul>
  <li> Qual o melhor preço de venda para as calças? </li>
  <li> Quantos tipos de calças e suas cores para o produto inicial? </li>
  <li> Quais as matérias-primas necessárias para confeccionar as calças? </li>
</ul>

<p align='justify'>Além da resposta para esses questionamentos, qual seria o investimento inicial no negócio?
  Para entender melhor qual o investimento que será feito, a matéria-prima e os custos que há na confecção das roupas,
  é preciso analisar os processos de fabricação. Na confecção de roupas, é possível observar que há os seguintes custos:
</p>

<ul>
  <li> Custos com matéria-prima: </li>
    <ul>
      <li> Tecido; </li>
      <li> Entretela; </li>
      <li> Botão; </li>
      <li> Zíper; </li>
      <li> Linha; </li>
      <li> Etiqueta; </li>
      <li> Tag; </li>
      <li> Embalagem. </li>
    </ul>

  <li> Custos com mão de obra; </li>
  <li> Custos com energia; e </li>
  <li> Custos com impostos. </li>

</ul>

<p align='justify'>Em cada um dos items acima, há uma forma de estimar os custos e serão descritos abaixo.
</p>

<h2>1 - Custos com matéria-prima </h2>
<p align='justify'>Todos os preços que serão mencionados aqui, foram retirados de lojas online especializadas
  em vendas de produtos para confecção. O que isso significa? Que o valor final será uma estimativa, na realidade
  as matérias-primas são compradas em atacado, com preços bem menores, fazendo assim com que haja um custo inferior nessa etapa.
</p>

<p align='justify'>Considerando todos os itens citados acima, que compoẽm a matéria-prima, o custo final estimado para a calça
  ficou aproximadamente <b>R$20,89</b>.
</p>

**O objetivo aqui é mostrar o resumo de todo o processo que foi feito durante o projeto. Dessa forma caso haja o interesse em compreender melhor o racional, basta acessar o resumo da solução**: [Resumo - Business case](https://github.com/Mat004/Web-Scraping-Star-Jeans/blob/main/resumo%20business%20case.ipynb)
</br>


<h2>2 - Custos da mão-de-obra </h2>
<p align='justify'>Os custos com mão-de-obra, começa no mapeamento da peça até a embalagem. Os processos e o tempo estimado são:
</p>

<ul>
  <li> Mapear e cortar: 5min; </li>
  <li> Costurar: 30min; </li>
  <li> Passar e embalar: 5min. </li>
</ul>

<p align='justify'>Dessa forma temos que o tempo estimado para a confeção de uma calça e o tempo de embalo, é de aproximadamente
  40 minutos. Considerando o salário mínimo atual (ano de 2022), um colaborador recebe <b>R$ 1.212,00</b>. A partir desse valor teremos a
  estimativa de quanto será aplicado na mão-de-obra de uma calça.
</p>

<p align='justify'>Como o nosso objetivo é estimar o valor gasto para confecção de uma calça, transformaremos os 21 dias em minutos.
  Considerando uma jornada de trabalho de 8h por dia, temos que ao final de 21 dias a pessoa trabalhou <b>168h</b>.
</p>

<p align='justify'>Como há aproximadamente 40min para fazer uma peça e embalar, o valor final com mão-de-obra fica <b>R$ 4,80</b>.
</p>

</br>


<h2>3 - Custo com energia </h2>
<p align='justify'>No custo com energia elétrica, temos que ter os valores para 1 kwh (kilo-watt hora). O valor utilizado,
  será baseado nos valores aplicados na cidade de Fortaleza/CE. A última atualização mostra que são <b>R$ 73,00</b> para cada 100kwh,
  o que nos leva a <b>R$ 0,73 / kwh</b>.
</p>

<p align='justify'>Alguns equipamentos são necessários para a confecção das roupas, como lâmpadas, máquinas de costura e ferros
  de passar. Cada um possui uma determinada potência. Abaixo há uma breve descrição de cada um:
</p>

<ul>
  <li> Lâmpada LED: 8W; </li>
  <li> Máquina de costura industrial: 550W; </li>
  <li> Ferro de passar: 1200W. </li>
</ul>

<p align='justify'>Com o somatório dos 3 principais custos com energia, temos o valor total de 958,4 kwh.
  Aplicando o valor de 1 kwh adotado para esse problema, tem-se o custo de energia aproximadamente de <b>R$ 699</b>.
</p>

</br>


<h2>4 - Total do investimento inicial</h2>
<p align='justify'>Nessa última etapa faremos a estimativa de investimento inicial para a entrada no mercado de
  calças jeans masculinas e o preço que deverá ser praticado.
</p>

</br>

<h3>4.1 - Investimento</h3>
<p align='justify'>Será considerado uma situação em que há somente um turno de trabalho, ou seja, há somente
  <b>8h</b> sendo trabalhadas por dia. A quantidade de <b>funcionários</b> é de 10 e os dias úteis serão 21.
</p>

<p align='justify'>Primeiro faremos o cálculo do salário do colaborador. O salário mínimo em 2022 é de
  R$ 1.212,00 para os 10 colaboradores, há um investimento mensal de <b>R$ 12.120,00</b>.
</p>

<p align='justify'>Segundo, os custo com energia elétrica ficou aproximadamente <b>R$ 699,63</b>.
</p>

<p align='justify'>Terceiro, considerando que em um dia haja a confecção de 120 calças, no final de 21 dias serão
  2520 calças no total. Como o custo com matéria-prima para uma calça é de R$ 20,89, o investimento final
  será de <b>R$ 52.642,80</b>.
</p>

<p align='justify'>Dessa forma temos que em um mês, o valor mínimo a ser investido é de <b>R$ 65.642,43</b> para que
  haja o pagamento dos custos básicos com matéria-prime, colaboradores e energia elétrica.
</p>

</br>


<h3>4.2 - Preço praticado</h3>
<p align='justify'>Considerando o valor acima, para o pagamentos dos custos básicos, qual seria o preço de uma calça
  capaz de suprir ao menos esses custos?
</p>

<p align='justify'>Para isso faremos o valor total inicial, dividido pela estimativa de calças no mês que é de 2520.
  O valor de uma calça ficaria de R$ 26,04. Esse é o valor que deve ser vendido uma calça caso haja apenas a pretensão
  de pagar os custos básicos.
</p>

<p align='justify'>Pegando como referência os dados coletados da H&M, temos que para uma calça 100% de algodão, o preço
  praticado é de US$ 39,99, convertendo para reais usando a cotação de R$ 5,15, o preço final é de R$ <b>205,94</b>.
</p>

<p align='justify'>Com o objetivo de seguir o mercado americano, com os preços dos players, o valor inicial será
  de <b>R$ 189,99</b>, o que em dólar seria de <b>US$ 36,89</b>.
</p>


</br>


<h3>4.3 - Faturamento bruto</h3>
<p align='justify'>Considerando a situação de produção mensal de <b>2520</b> calças, sendo vendidas cada uma por R$ 189,99, o
  faturamento da empresa será de R$ 478.774,80 no mês, considerando o ano o valor acumulado seria de <b>R$ 5.745.297,60</b>.
  A quantidade de impostos que iria incidir seria de <b>19%</b>.
</p>


</br>


<h1>Conclusão e próximos passos</h1>
<p align='justify'>Dessa forma o preço praticado será de <b>US$ 36,89</b>. Com um investimento inicial de <b>US$ 12.746,10</b>.
</p>

<p align='justify'><b>OBS.:</b> É válido ressaltar que todos os valores aqui abordados, além de terem sido considerados como preços de
  varejo, os valores analisados refletem a realidade do mercado brasileiro, enquanto toda a extração de dados foi realizada com
  um player americano. Tendo em vista isso, é proposto alguns passos para que haja uma melhor acurácia nas estimativas de preços:
</p>

<ul>
  <li> Analisar períodos maiores para identificar sazonalidades e comportamentos do mercado de calças; </li>
  <li> Buscas outros players para extração de dados; </li>
  <li> Construção de um mapa com a localização dos players; </li>
  <li> Extrair dados de composição das roupas para avaliar a venda de produtos mais variados; </li>
  <li> A partir dos dados "históricos", criar um algoritmo de previsão de preços; </li>
  <li> Analisar os preços praticados no mercado americano para energia, mão-de-obra e matéria-prima,
    para que haja uma estimativa de preço mais condizente com a realidade. </li>
</ul>
