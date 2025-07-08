
# 📌 Salesforce Composite Mapper

Este projeto é um utilitário em Python para **mapear dados de entrada em JSON** para os formatos esperados pela **Salesforce Composite API**, usando JWT para autenticação sem interação humana.

---

## 🚀 Visão Geral

O objetivo é receber um JSON genérico, aplicar um **mapeamento de campos** (ex.: `Pessoa.PrimeiroNome` ➜ `Contact.FirstName`), construir uma **Composite Request** e enviá-la à Salesforce, criando registros relacionados como **Account** e **Contact** de forma automática.

---

## 📂 Estrutura do Projeto

```
mapper.py          # Dicionário de mapeamento de campos de entrada ➜ destino Salesforce
mapping_utils.py   # Funções utilitárias para extrair valores e aplicar o mapeamento
create_record.py   # Função para executar o Composite API na Salesforce
auth_salesforce.py # Autenticação JWT com Salesforce (JWT Bearer Flow)
run.py             # Exemplo de execução ponta a ponta
```

---

## ⚙️ Como Funciona

1. **Entrada:**  
   Você envia um JSON com campos em uma estrutura mista:
   - Chaves diretas: `Id`, `Observacao`  
   - Listas de pares chave-valor: `Pessoa`, `Empresa`  

2. **Mapeamento:**  
   O `mapper.py` define **de onde vem ➜ para onde vai**:
   ```python
   mapper = {
       'Pessoa.PrimeiroNome': 'Contact.FirstName',
       'Empresa.Nome': 'Account.Name',
       ...
   }
   ```

3. **Transformação:**  
   O `apply_mapper` organiza os dados em objetos (`Contact`, `Account`).

4. **Composite Request:**  
   O `run.py` monta uma requisição `compositeRequest`:
   - Cria `Account`
   - Cria `Contact` vinculado ao `Account`

5. **Autenticação JWT:**  
   O `auth_salesforce.py` usa JWT para obter um token de acesso sem precisar de login interativo.

6. **Envio:**  
   O `create_record.py` envia a `Composite Request` para a Salesforce.

---

## 📌 Exemplo de JSON de Entrada

```json
{
  "Id": 1,
  "Observacao": "Teste mapper",
  "Pessoa": [
    { "chave": "PrimeiroNome", "valor": "João" },
    { "chave": "SegundoNome", "valor": "Silva" },
    { "chave": "Contato", "valor": "bre_ab@hotmail.com" }
  ],
  "Empresa": [
    { "chave": "Nome", "valor": "Empresa do Breno" },
    { "chave": "Telefone", "valor": "995404125" },
    { "chave": "Site", "valor": "teste.com" }
  ]
}
```

---

## 🔑 Autenticação

Este projeto usa **JWT Bearer Flow**.  
Você precisa de:

- Um **certificado digital** (`KEY_FILE`) para assinar o JWT.
- As variáveis de ambiente:
  - `IS_SANDBOX` ➜ `True` ou `False`
  - `KEY_FILE` ➜ caminho para seu arquivo `.key`
  - `ISSUER` ➜ Consumer Key do seu app Salesforce Connected App
  - `SUBJECT` ➜ Username da sua conta Salesforce

Crie um arquivo `.env`:
```
IS_SANDBOX=True
KEY_FILE=private.key
ISSUER=YOUR_CONNECTED_APP_ID
SUBJECT=seu_usuario@sandbox.com
```

---

## ▶️ Como Executar

1. Instale as dependências:
   ```bash
   pip install requests python-dotenv pyjwt
   ```

2. Rode o script de teste:
   ```bash
   python run.py
   ```

   O script irá:
   - Autenticar na Salesforce
   - Aplicar o mapeamento
   - Montar e executar o Composite API
   - Mostrar a resposta

---

## 📌 Principais Funcionalidades

✅ Mapeamento dinâmico de campos  
✅ Extração de valores em estruturas mistas (dict + lista de pares)  
✅ Autenticação JWT com Salesforce  
✅ Composite API: cria múltiplos objetos encadeados em uma única chamada  
✅ Código modular e reutilizável

---

## 🛠️ Requisitos

- Python 3.8+
- Um **Connected App** configurado no Salesforce com **JWT Bearer Flow** habilitado.
- Chave privada RSA (`.key`) correspondente à chave pública carregada no Connected App.

---

## ⚠️ Avisos

- Garanta que seu `KEY_FILE` seja mantido seguro!
- Teste em um **Sandbox** antes de rodar em Produção.
- O script é um exemplo de referência: adapte as URLs, versões da API e objetos conforme seu caso de uso.

---

## 📬 Contato

💼 Desenvolvido por Breno Alberto Braguim 
📧 Email: bre_ab@hotmail.com

---

🚀 **Happy Mapping!**
