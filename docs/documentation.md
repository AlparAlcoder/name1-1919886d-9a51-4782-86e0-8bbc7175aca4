# API FastAPI para Manipulação de Itens

Essa API, construída com FastAPI e SQLite, é responsável pela manipulação de itens. Cada item é caracterizado pelos atributos nome, descrição (opcional) e preço.

## Dependências

- FastAPI
- SQLite3
- Pydantic

Para instalar todas as dependências, use o comando pip abaixo:

```bash
pip install fastapi sqlite3 pydantic
```

## Modelos

### Item

O modelo Pydantic `Item` é usado para validação dos dados do item. Ele possui os seguintes campos:

- `name: str` - Nome do item (obrigatório).
- `description: Optional[str] = None` - Descrição do item (opcional).
- `price: float` - Preço do item (obrigatório).

## Rotas

### POST /items/

Cria um novo item e salva no banco de dados SQLite.

#### Parâmetros

- `item: Item` - Um objeto `Item` contendo nome, descrição (opcional) e preço.

#### Respostas

- `200 OK` - Em caso de sucesso, retorna a mensagem "Item created successfully!".
- `400 Bad Request` - Se houver algum problema com a inserção dos dados no banco, uma exceção HTTP será lançada com detalhes do problema.

#### Exemplo de uso

```bash
curl -X POST "http://localhost:8000/items/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"name\":\"item1\",\"price\":10.5}"
```
## Notas importantes

- O banco de dados SQLite é usado para persistência de dados. O arquivo do banco de dados é 'database.db' e a tabela usada para guardar os itens é 'items'.
- Caso a tabela 'items' não exista, ela será criada automaticamente ao executar o script.
- Todas as operações de banco de dados são realizadas usando a conexão `conn` e o cursor `cursor`.
- Erros durante a criação do item são capturados e uma exceção HTTP é lançada com o status 400 e os detalhes do erro.