# Ingestão e Coleta de Dados na Alimentos LTDA


A Alimentos LTDA é uma das maiores empresas do ramo alimentício Brasil. A Alimentos LTDA está na busca de agilidade, qualidade e economia nos projetos de inovação, de produtos e processos, em que cada vez mais orçamentos são enxutos, e informações instantâneas, seguras e de qualidade são essenciais para a tomada de decisão. Contudo, a empresa não consegue visualizar cenários prospectivos, tendo em vista a instabilidade econômica e de saúde no mundo. Diante desse cenário, são necessários grande volume, variedade, velocidade e veracidade de dados, que devem ser ingeridos pela organização. Como especialista em arquitetura e modelos de dados da Alimentos LTDA, tenho como responsabilidade auxiliar na construção de uma estratégia que contribua com o objetivo da empresa.


Para resolver este problema, devemos em um primeiro momento, elaborar ações estratégicas para auxiliar o negócio através da ingestão de dados em um _datalake_. Um _datalake_ é um repositório de dados centralizado, que permite a ingestão de dados estruturados, semi-estruturados e não estruturados, de qualquer escala. A primeira ação para inserir dados em um _datalake_ é mapear as fontes de dados da empresa, além de seus respectivos tipos de dados.

A cada dia surgem novas ferramentas com grande potencial para resolução de problemas em ambientes _big data_ e _fast data_. Após um tempo entendendo o cenário da Alimentos LTDA, propomos a utilização de uma _stack_ que vem ganhando bastante notoriedade nos últimos anos, a ELK Stack. Esta _stack_ nasceu com o ElasticSearch, onde o foco era a busca e análise de dados distribuídos. Desenvolvido sobre o Apache Lucene, a Elastic incorporou novos componentes ao seu produto, e o renomeou para ELK Stack. Atualmente, a ELK Stack possui componentes que facilitam a tanto a ingestão de dados, quanto o processo de ETL, através dos componentes Logstash e Beats. 

A ELK Stack se tornou popular por possuir APIs de simples utilização. Além disso, esta _stack_ foi concebida para atuar de forma escalável, veloz e distribuída. Apesar do ElasticSearch ser o componente principal da ELK Stack, ela também possui ferramentas gratuitas e _open-source_ para ingestão, enriquecimento, armazenamento, análise e visualização de dados. Os componentes da ELK Stack são:

- **ElasticSearch**: Mecanismo de armazenamento e busca que utiliza uma estrutura de dados baseado em índice invertido, projetada para buscas de texto rápidas;
    
- **Logstash**: Pipeline para ingestão de dados do lado do servidor. O Logstash pode receber, tratar e enriquecer dados de diversas fontes;
    
- **Kibana**: Ferramenta da ELK Stack responsável pela visualização e gerenciamento dos dados. Com o Kibana é possível criar histogramas, mapas e diferentes tipos de gráficos com base nos dados armazenados no ElasticSearch;
    
- **Beats**: Por fim, os Beats são microagentes de coleta de dados que ficam em aplicações clientes. Os Beats podem enviar dados de diversos dispositivos ou sistemas para o Logstash ou ElasticSearch.

A ELK Stack é uma boa opção para a Alimentos LTDA atingir seu objetivo, pois possui ferramentas especificas para coleta, enriquecimento, ingestão, análise, busca e visualização dos dados. Por sua natureza distribuída, a ELK Stack utiliza _sharding_ para particionamento horizontal, podendo trabalhar em _clusters_, o que garante a resiliência das informações armazenadas. Por fim, adotar esta _stack_ tecnológica pode ajudar a Alimentos LTDA a atingir seu objetivo de ter dados em real-time para auxiliar na tomada de decisão _data-driven_ e, se manter como uma das principais empresas do ramo alimentício nacional.
