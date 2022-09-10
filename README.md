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
</p>
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
  <p>Imagem 1: Quantidade de descontos H&M </p>
  <p align="center">
  <img src="https://user-images.githubusercontent.com/76838937/189499770-c8cb0d53-bb19-4b86-845f-6ba9e003ca28.png">
  </p>

</br>
<p>Imagem 2: Quantidade de descontos Macy's </p>
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
