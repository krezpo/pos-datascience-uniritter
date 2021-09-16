# Processamento Massivo de Dados na Expertise PMD

A Expertise PMD é uma das maiores empresas de desenvolvimento de soluções de tecnologia no Brasil. Esta empresa passa por um grande crescimento e tem como objetivo aprimorar seus serviços, no que se refere a gerência e processamento massivo de dados em _clusters_ para então, oferecer aos seus clientes orientações na tomada de decisão em diferentes áreas. Como consultor de tecnologia da Expertise PMD, tenho como responsabilidade auxiliar na construção de uma estratégia que contribua com o objetivo da empresa.

Existem muitas ferramentas para processamento massivo de dados, das quais podemos citar Hadoop, Spark, Hive, Pig, Yarn, Zookeper. Além disso, a cada dia surgem novas ferramentas com grande potencial para resolução de problemas em ambientes distribuídos. Após um tempo entendo o cenário da Expertise PMD, propomos a utilização de uma _stack_ que vem ganhando bastante notoriedade nos últimos anos, a ELK Stack. Esta _stack_ para processamento massivo de dados nasceu como ElasticSearch, onde o foco era a busca e análise de dados distribuídos. Desenvolvido sobre o Apache Lucene, a Elastic incorporou novos componentes ao seu produto, e o renomeou para ELK Stack.

A ELK Stack se tornou popular por possuir APIs de simples utilização. Além disso, esta _stack_ foi concebida para atuar de forma escalável, veloz e distribuída. Apesar do ElasticSearch ser o componente principal da ELK Stack, ela também possui ferramentas gratuitas e _open-source_ para ingestão, enriquecimento, armazenamento, análise e visualização de dados. Os componentes da ELK Stack são:

- **ElasticSearch**: Mecanismo de armazenamento e busca que utiliza uma estrutura de dados baseado em índice invertido, projetada para buscas de texto rápidas;
    
- **Logstash**: Pipeline para ingestão de dados do lado do servidor. O Logstash pode receber, tratar e enriquecer dados de diversas fontes;
    
- **Kibana**: Ferramenta da ELK Stack responsável pela visualização e gerenciamento dos dados. Com o Kibana é possível criar histogramas, mapas e diferentes tipos de gráficos com base nos dados armazenados no ElasticSearch;
    
- **Beats**: Por fim, os Beats são microagentes de coleta de dados que ficam em aplicações clientes. Os Beats podem enviar dados de diversos dispositivos ou sistemas para o Logstash ou ElasticSearch.
    
A ELK Stack é uma boa opção para a Expertise PMD atingir seu objetivo, pois possui ferramentas especificas para coleta, enriquecimento, ingestão, análise, busca e visualização dos dados. Por sua natureza distribuída, a ELK Stack pode trabalhar em clusters, o que garante a resiliência das informações armazenadas. Por fim, adotar esta stack tecnologica pode ajudar a Expertise PMD a atingir seu objetivo de oferecer aos seus clientes orientações na tomada de decisão _data-driven_ e, se manter como uma das principais empresas de tecnologia do Brasil.
