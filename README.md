# API PIX GERENCIANET

A API Pix Gerencianet disponibiliza o serviço de pagamento através do pix. Com essa API é possível criar cobranças e utilizar o webhook.

## Configurações
Para integrar a API Pix Gerencianet ao seu sistema ou sua plataforma, é necessário ter uma Conta Digital Gerencianet.


### Para criar uma aplicação para utilização da API Pix siga os passos abaixo:

Acesse sua conta e clique no item "API" no menu superior da conta Gerencianet;
No menu à esquerda, clique em "Minhas Aplicações" e "Nova Aplicação"
Habilite a API Pix e escolha os escopos que deseja liberar em ambiente de Produção e Homologação (você pode editá-los no futuro);
Com os escopos selecionados, clique em "Criar nova aplicação".

![alt text](https://github.com/patrick3s/ApiPixGerenciaNet/blob/main/assets/step1.png)

### Gerando um certificado P12

Todas as requisições devem conter um certificado de segurança que será fornecido pela Gerencianet dentro da sua conta, no formato PFX(.p12). Essa exigência está descrita na íntegra no manual de segurança do PIX.

Para gerar o seu certificado, basta seguir os passos abaixo:

 - 1.Acesse o item "API" no menu superior da conta Gerencianet;
 - 2.No menu à esquerda, clique em "Meus Certificados";
 - 3.Na nova janela selecione o ambiente ao qual pertencerá o certificado (Produção ou Homologação)
 - 4.Clique em "Novo Certificado" (botão laranja);
 - 5.Atribua uma descrição ao certificado para identificá-lo no futuro;
 - 6.Confirme a criação do certificado;
 - 7.Por fim, baixe o certificado.
Os passos para a criação de um certificado estão ilustrados na imagem a seguir.

![alt text](https://github.com/patrick3s/ApiPixGerenciaNet/blob/main/assets/step2.png)

### Conversão de certificado P12 para o formato PEM
 Dica:
 Em algumas linguagens as chaves precisarão ser convertidas para o formato .pem. Utilize as informações desta seção apenas se esse for o seu caso.

Em algumas linguagens você deve converter o certificado .p12 para o formato .pem. Para converter seu certificado, você pode baixar o conversor de certificados disponibilizado pela Gerencianet.

É possível utilizar também, o comando o OpenSSL para realizar essa conversão de formato entre as chaves:

Gerar certificado e chave em único arquivo
 - openssl pkcs12 -in certificado.p12 -out certificado.pem -nodes

após gerar o certificado, cole esse certificado em "projeto/src/"

### CONFIGURAÇÔES AMBIENTE
No caminho "projeto/src/utils/constants.py" .
No site do gerencia net você acessa o clientID e o ClientSecret

![alt text](https://github.com/patrick3s/ApiPixGerenciaNet/blob/main/assets/step3.png)



