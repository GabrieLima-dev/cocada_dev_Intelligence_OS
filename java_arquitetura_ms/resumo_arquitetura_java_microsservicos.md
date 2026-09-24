# Guia Técnico de Aplicações Web e Microsserviços

> Material de estudo sobre uma arquitetura corporativa com Java, Quarkus, Angular, bancos de dados, mensageria, testes e Kubernetes.
>
> O objetivo é explicar **o que cada peça faz**, **como elas se conectam** e **como reproduzir os padrões em projetos pessoais**.

---

## Como usar este guia

```text
Primeira leitura → visão geral e fluxo completo
Implementação    → exemplos de backend e frontend
Revisão          → erros comuns e checklists
Prática          → roteiro de projeto pessoal
```

Regras de leitura:

- Os exemplos usam um domínio neutro de `Produto`.
- Nomes como `BaseEndpoint` e `GenericApplicationDao` representam abstrações corporativas, não classes do Java ou do Quarkus.
- Em projetos pessoais, comece com os recursos nativos do framework e crie abstrações somente quando houver repetição real.
- Versões antigas de ferramentas aparecem como contexto. Para projeto novo, prefira versões atuais e compatíveis entre si.

---

## Sumário

1. [Visão geral](#1-visão-geral)
2. [Tecnologias](#2-tecnologias)
3. [Estrutura dos projetos](#3-estrutura-dos-projetos)
4. [Fluxo completo do backend](#4-fluxo-completo-do-backend)
5. [API e DTOs](#5-api-e-dtos)
6. [Endpoints REST](#6-endpoints-rest)
    - [BaseEndpoint e respostas padrão](#baseendpoint-e-respostas-padrão)
7. [Services, validação e erros](#7-services-validação-e-erros)
8. [Persistência e transações](#8-persistência-e-transações)
    - [Named queries](#named-queries)
    - [Estratégias de identificador](#estratégias-de-identificador)
    - [Constraints e conflitos](#constraints-e-conflitos)
9. [Comunicação, cache e processamento assíncrono](#9-comunicação-cache-e-processamento-assíncrono)
    - [Configuração do cliente interno](#configuração-do-cliente-interno)
10. [Configuração, segurança e observabilidade](#10-configuração-segurança-e-observabilidade)
    - [Injeção com ConfigProperty](#injeção-com-configproperty)
    - [Parâmetros opcionais e valores padrão](#parâmetros-opcionais-e-valores-padrão)
    - [Precedência das fontes](#precedência-das-fontes)
    - [Decisões para novos parâmetros](#decisões-para-novos-parâmetros)
11. [Frontend Angular](#11-frontend-angular)
12. [Estratégia de testes e QA](#12-estratégia-de-testes-e-qa)
13. [Build, pipeline e deploy](#13-build-pipeline-e-deploy)
14. [Exemplo integrado](#14-exemplo-integrado)
15. [Erros comuns](#15-erros-comuns)
16. [Checklists](#16-checklists)
17. [Roteiro de aprendizado](#17-roteiro-de-aprendizado)
18. [Glossário](#18-glossário)
19. [Decisões de implementação e trabalho](#19-decisões-de-implementação-e-trabalho)
    - [Padrões de código adotados](#padrões-de-código-adotados)
    - [Escopo e mudanças](#escopo-e-mudanças)
    - [Investigação eficiente](#investigação-eficiente)
    - [Verificação honesta](#verificação-honesta)
    - [Segurança operacional](#segurança-operacional)

---

# 1. Visão geral

Uma aplicação web corporativa costuma possuir três grandes áreas:

```text
Frontend
  │ interface, estado e experiência do usuário
  │ HTTP/JSON
  ▼
Backend
  │ autenticação, regras, transações e integrações
  ▼
Dados e infraestrutura
  banco, cache, mensageria, logs e deploy
```

## Fluxo síncrono

O usuário espera a resposta na mesma requisição:

```text
Tela
  → Endpoint
  → Service
  → DAO
  → Banco
  → DTO
  → Tela
```

Exemplo: consultar um produto pelo identificador.

## Fluxo assíncrono

O trabalho continua depois da resposta inicial:

```text
Endpoint ou Job
  → publica mensagem
  → Kafka
  → consumidor
  → processamento
  → banco ou nova mensagem
```

Exemplo: importar um arquivo grande sem manter a tela esperando.

## Responsabilidade de cada camada

| Camada | Faz | Não deve fazer |
|---|---|---|
| Componente frontend | Exibe e recebe ações | Acessar banco ou conhecer SQL |
| Serviço frontend | Chama a API | Controlar detalhes visuais |
| Endpoint | Traduz HTTP para o caso de uso | Implementar regra ou SQL |
| Service backend | Valida e coordena a regra | Montar tela ou conhecer CSS |
| Factory/Mapper | Converte objetos | Consultar banco |
| DAO | Consulta e persiste | Decidir regra de negócio |
| Client | Chama outro serviço | Persistir entidade local |

Regra prática:

```text
Cada classe deve ter um motivo principal para mudar.
```

---

# 2. Tecnologias

## Backend

| Tecnologia | Função |
|---|---|
| Java | Linguagem do backend |
| Quarkus | Framework da aplicação |
| Jakarta EE | CDI, JAX-RS, JPA e transações |
| MicroProfile OpenAPI | Documentação da API |
| Hibernate ORM | Mapeamento entre objetos e tabelas |
| Agroal | Pool de conexões |
| SQL Server | Banco relacional principal da arquitetura de referência |
| H2 | Banco leve usado em parte dos testes |
| Redis | Cache e estado temporário |
| Kafka + SmallRye | Mensageria assíncrona |
| JasperReports | Relatórios PDF e planilhas |
| Maven | Build e dependências Java |

Regra importante: use imports `jakarta.*`, não `javax.*`. Exemplos: `jakarta.inject.Inject`, `jakarta.ws.rs.GET` e `jakarta.transaction.Transactional`.

## Frontend

| Tecnologia | Função |
|---|---|
| Angular | Framework da interface web |
| TypeScript | Linguagem do frontend |
| RxJS | Fluxos assíncronos e eventos |
| NGXS | Estado global na arquitetura de referência |
| PrimeNG | Componentes de interface |
| Angular Material | Componentes e acessibilidade |
| Design system | Identidade e componentes reutilizáveis |
| OAuth 2.0, OpenID Connect e JWT | Login e identidade |
| Chart.js | Gráficos |
| Lottie | Animações |
| Jasmine + Karma | Testes unitários da stack Angular tradicional |
| ESLint | Análise estática de TypeScript |

## QA e infraestrutura

| Tecnologia | Função |
|---|---|
| JUnit 5 | Testes Java |
| RestAssured | Testes HTTP do backend |
| Testcontainers | Dependências reais em containers para teste |
| Cypress + TypeScript | Testes E2E web |
| Appium + WebdriverIO | Testes mobile |
| BrowserStack | Dispositivos e navegadores remotos |
| Postman | Coleções e testes exploratórios de API |
| Python + pytest | Automações de engenharia |
| Docker | Imagens e dependências locais |
| Helm + Kubernetes | Deploy e execução em cluster |
| Azure DevOps | Repositórios, boards e pipelines |
| SonarQube | Qualidade e cobertura |
| OpenTelemetry | Logs, métricas e traces |

## Versões observadas na arquitetura de referência

| Tecnologia | Versão ou situação observada |
|---|---|
| Java | JDK 25 na geração mais recente |
| Quarkus | Versão centralizada pelo POM pai; conferir no projeto |
| Angular | 11.2.5 |
| TypeScript | 4.0 |
| NGXS | 3.7.5 |
| PrimeNG | 11.3.1 |
| Angular Material | 11.2.5 |
| Cypress | 13.17.0 |
| WebdriverIO | 8 |
| Python | 3.10 ou superior |

Essas versões descrevem o ambiente estudado. Não são uma recomendação para iniciar um projeto novo.

## O que não faz parte do padrão predominante

```text
Spring MVC
Spring Data
Spring Security
Lombok
MapStruct
Feign
Flyway ou Liquibase dentro do serviço
```

Os microsserviços estudados usam majoritariamente Quarkus e Jakarta EE. Existe também um agente de integração especializado feito com Spring Boot, tratado como exceção e não como modelo para novos microsserviços.

Isso não significa que as ferramentas da lista sejam ruins. Significa que o padrão principal escolheu mecanismos diferentes.

---

# 3. Estrutura dos projetos

## Maven multi-módulo

O formato principal possui três módulos:

```text
produto-ms/
├── pom.xml
├── produto-api/
│   └── DTOs, enums e contratos
├── produto-client/
│   └── cliente Java para outros serviços
├── produto-service/
│   ├── aplicação Quarkus
│   ├── endpoints, services, DAOs e entidades
│   └── testes
├── devops/
│   └── chart Helm e manifestos
└── rundev.ps1 / rundev.sh
```

### Dependências

```text
api
 ▲
 │
client
 ▲
 │
service ─────► clients de outros serviços
```

- `api` não depende de código de negócio.
- `client` depende dos contratos de `api`.
- `service` implementa a aplicação.
- Outro microsserviço consome `api` e `client`, nunca o JAR de `service`.

Não são necessários módulos separados para REST e testes. O deploy fica em `devops/`, e os testes ficam próximos do código testado.

## Organização por funcionalidade

Prefira agrupar classes que mudam juntas:

```text
src/main/java/com/exemplo/catalogo/
├── produto/
│   ├── Produto.java
│   ├── ProdutoDao.java
│   ├── ProdutoQueryDao.java
│   ├── ProdutoFactory.java
│   ├── ProdutoService.java
│   └── ProdutoEndpoint.java
├── categoria/
└── shared/
```

Evite uma pasta global enorme para cada tipo:

```text
controller/ com 80 endpoints
service/    com 90 services
dao/        com 70 DAOs
```

## Convenções de nomes

| Artefato | Exemplo |
|---|---|
| Entidade | `Produto` |
| DTO | `ProdutoDTO` |
| Requisição específica | `CriarProdutoRequest` |
| Service | `ProdutoService` |
| DAO | `ProdutoDao` |
| Consulta complexa | `ProdutoQueryDao` |
| Endpoint | `ProdutoEndpoint` |
| Conversor | `ProdutoFactory` |
| Cliente remoto | `ProdutoClient` |

---

# 4. Fluxo completo do backend

```text
GET /produtos/10
        │
        ▼
ProdutoEndpoint.obter(10)
        │ delega
        ▼
ProdutoService.obter(10)
        │ valida e coordena
        ▼
ProdutoDao.obterPorId(10)
        │ JPQL/SQL
        ▼
SQL Server
        │ Produto
        ▼
ProdutoFactory.toDTO(produto)
        │ ProdutoDTO
        ▼
JSON + HTTP 200
```

Se o produto não existir:

```text
DAO retorna vazio
  → Service lança exceção de negócio
  → mapper central converte a exceção
  → API responde com status e mensagem padronizados
```

O endpoint não precisa conhecer os detalhes do banco ou do tratamento global de erro.

---

# 5. API e DTOs

DTO significa **Data Transfer Object**. Ele transporta dados entre processos e camadas.

```java
public class ProdutoDTO {

    private Integer id;
    private String nome;
    private BigDecimal preco;

    public Integer getId() { return id; }
    public void setId(Integer id) { this.id = id; }
    public String getNome() { return nome; }
    public void setNome(String nome) { this.nome = nome; }
    public BigDecimal getPreco() { return preco; }
    public void setPreco(BigDecimal preco) { this.preco = preco; }
}
```

## O DTO pode

- conter dados simples;
- compor outros DTOs;
- representar entrada ou saída;
- possuir enums de contrato.

## O DTO não deve

- acessar banco;
- iniciar transação;
- chamar outro serviço;
- conter regra de negócio complexa;
- expor uma entidade JPA diretamente.

## DTO específico por operação

Evite um único objeto com muitos campos opcionais:

```java
public class CriarProdutoRequest {
    private String nome;
    private BigDecimal preco;

    public String getNome() { return nome; }
    public void setNome(String nome) { this.nome = nome; }
    public BigDecimal getPreco() { return preco; }
    public void setPreco(BigDecimal preco) { this.preco = preco; }
}
```

```java
public class AtualizarPrecoRequest {
    private BigDecimal novoPreco;

    public BigDecimal getNovoPreco() { return novoPreco; }
    public void setNovoPreco(BigDecimal novoPreco) {
        this.novoPreco = novoPreco;
    }
}
```

Vantagem: o contrato comunica a intenção da operação.

## Entidade não é resposta HTTP

```text
Entidade → representa persistência
DTO      → representa contrato
```

Retornar entidade diretamente pode expor colunas internas, relações lazy e detalhes do banco.

---

# 6. Endpoints REST

O endpoint traduz HTTP para uma chamada Java.

```java
@RequestScoped
@Path("/produtos")
@Produces(MediaType.APPLICATION_JSON)
@Consumes(MediaType.APPLICATION_JSON)
public class ProdutoEndpoint {

    @Inject
    ProdutoService produtoService;

    @GET
    @Path("/{id}")
    @Operation(summary = "Obter produto por id")
    @APIResponse(responseCode = "200", description = "Produto encontrado")
    @APIResponse(responseCode = "404", description = "Produto não encontrado")
    public ProdutoDTO obter(@PathParam("id") int id) {
        return produtoService.obter(id);
    }

    @POST
    @Operation(summary = "Criar produto")
    @APIResponse(responseCode = "201", description = "Produto criado")
    public Response criar(CriarProdutoRequest request) {
        ProdutoDTO criado = produtoService.criar(request);
        return Response.status(Response.Status.CREATED)
                .entity(criado)
                .build();
    }
}
```

## Annotations principais

| Annotation | Função |
|---|---|
| `@Path` | Define a rota |
| `@GET`, `@POST`, `@PUT`, `@DELETE` | Define o verbo HTTP |
| `@PathParam` | Lê um valor da rota |
| `@QueryParam` | Lê um parâmetro de consulta |
| `@HeaderParam` | Lê um header |
| `@Produces` | Define o tipo da resposta |
| `@Consumes` | Define o tipo recebido |
| `@RequestScoped` | Cria uma instância por requisição |
| `@Operation` | Documenta a operação no OpenAPI |
| `@APIResponse` | Documenta possíveis respostas |

## Status HTTP mais usados

| Status | Uso |
|---|---|
| `200 OK` | Consulta ou alteração bem-sucedida |
| `201 Created` | Recurso criado |
| `204 No Content` | Sucesso sem corpo |
| `400 Bad Request` | Entrada ou regra inválida |
| `401 Unauthorized` | Usuário não autenticado |
| `403 Forbidden` | Usuário autenticado sem permissão |
| `404 Not Found` | Recurso não encontrado |
| `409 Conflict` | Conflito de estado ou unicidade |
| `500 Internal Server Error` | Falha inesperada |

## Endpoint fino

```text
Endpoint bom:
recebe → delega → devolve

Endpoint ruim:
valida tudo → consulta DAO → calcula → abre transação → monta SQL
```

## Abstrações corporativas

Uma base de código pode fornecer:

```text
BaseEndpoint            helpers de resposta e usuário
annotation de segurança autenticação e autorização
media type próprio      contrato de conteúdo customizado
mapper de exceções      erro Java para resposta HTTP
```

Essas classes são internas. Em projeto pessoal, use primeiro JAX-RS, Quarkus Security e `application/json`.

## BaseEndpoint e respostas padrão

Uma classe-base pode evitar repetição em endpoints:

```java
public abstract class BaseEndpoint {

    protected Response respostaCriada(Object corpo, URI localizacao) {
        return Response.created(localizacao)
                .entity(corpo)
                .build();
    }

    protected Response semConteudo() {
        return Response.noContent().build();
    }
}
```

Uso:

```java
@Path("/produtos")
public class ProdutoEndpoint extends BaseEndpoint {

    @POST
    public Response criar(CriarProdutoRequest request, @Context UriInfo uriInfo) {
        ProdutoDTO criado = produtoService.criar(request);
        URI localizacao = uriInfo.getAbsolutePathBuilder()
                .path(String.valueOf(criado.getId()))
                .build();
        return respostaCriada(criado, localizacao);
    }
}
```

Use classe-base apenas para comportamento técnico estável, como respostas e acesso ao contexto. Regra de negócio continua no service. Se a abstração apenas esconder uma linha simples, prefira JAX-RS diretamente.

---

# 7. Services, validação e erros

O service implementa o caso de uso.

```java
@Dependent
@Transactional
public class ProdutoService {

    @Inject
    ProdutoDao produtoDao;

    public ProdutoDTO obter(int id) {
        Produto produto = produtoDao.obterPorId(id);

        if (produto == null) {
            throw new RecursoNaoEncontradoException("Produto não encontrado.");
        }

        return ProdutoFactory.toDTO(produto);
    }

    public ProdutoDTO criar(CriarProdutoRequest request) {
        validarCriacao(request);
        Produto produto = ProdutoFactory.novo(request);
        produtoDao.salvar(produto);
        return ProdutoFactory.toDTO(produto);
    }

    private void validarCriacao(CriarProdutoRequest request) {
        if (request == null) {
            throw new RegraNegocioException("Dados do produto são obrigatórios.");
        }

        if (request.getNome() == null || request.getNome().isBlank()) {
            throw new RegraNegocioException("Nome é obrigatório.");
        }

        if (request.getPreco() == null
                || request.getPreco().compareTo(BigDecimal.ZERO) <= 0) {
            throw new RegraNegocioException("Preço deve ser positivo.");
        }
    }
}
```

## Responsabilidades

- validar regras;
- coordenar DAOs e clients;
- escolher a ordem das operações;
- controlar a transação;
- lançar exceções significativas;
- converter o resultado para DTO.

## Validação

Na arquitetura estudada, as validações são feitas no service com uma classe de precondições.

```java
Preconditions.notNull(request, "Dados são obrigatórios.");
Preconditions.notBlank(request.getNome(), "Nome é obrigatório.");
Preconditions.positive(request.getPreco(), "Preço deve ser positivo.");
```

`Preconditions` é uma abstração interna. Em outro projeto, ela pode ser criada ou substituída por Jakarta Bean Validation.

Não misture os dois estilos sem uma decisão arquitetural.

## Exceções

```text
RegraNegocioException
→ erro esperado e mensagem compreensível

RecursoNaoEncontradoException
→ dado solicitado não existe

Exceção técnica
→ banco indisponível, timeout ou defeito inesperado
```

Evite capturar `Exception` apenas para lançar uma exceção genérica. Capture somente quando houver retentativa, fallback, compensação ou contexto realmente útil.

---

# 8. Persistência e transações

## Entidade JPA

```java
@Entity
@Table(name = "CAT_Produto")
public class Produto {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "Id")
    private Integer id;

    @Column(name = "Nome", nullable = false, length = 120)
    private String nome;

    @Column(name = "Preco", nullable = false, precision = 18, scale = 2)
    private BigDecimal preco;

    @Column(name = "Ativo", nullable = false, columnDefinition = "char(1)")
    @Convert(converter = BooleanSimNaoConverter.class)
    private Boolean ativo;

    protected Produto() {
    }

    public Produto(String nome, BigDecimal preco) {
        this.nome = nome;
        this.preco = preco;
        this.ativo = true;
    }

    public Integer getId() { return id; }
    public String getNome() { return nome; }
    public BigDecimal getPreco() { return preco; }

    public void alterarPreco(BigDecimal novoPreco) {
        this.preco = novoPreco;
    }
}
```

## Tipos importantes

| Dado | Tipo Java recomendado |
|---|---|
| Dinheiro | `BigDecimal` |
| Apenas data | `LocalDate` |
| Data e hora sem fuso | `LocalDateTime` |
| Instante global | `Instant` |
| Verdadeiro/falso | `Boolean` ou `boolean` |
| Código fechado | `enum` |

Nunca use `double` ou `float` para valores monetários.

Uma base corporativa também pode exigir que toda entidade estenda uma classe como `EntidadePersistivel` e implemente uma interface marcadora. Isso é convenção interna, não requisito do JPA.

## Boolean armazenado como `S/N`

```java
@Converter
public class BooleanSimNaoConverter
        implements AttributeConverter<Boolean, String> {

    @Override
    public String convertToDatabaseColumn(Boolean valor) {
        return Boolean.TRUE.equals(valor) ? "S" : "N";
    }

    @Override
    public Boolean convertToEntityAttribute(String valor) {
        return "S".equalsIgnoreCase(valor);
    }
}
```

## Enum armazenado como código

```java
public enum SituacaoProduto {
    ATIVO(1),
    INATIVO(2);

    private final int codigo;

    SituacaoProduto(int codigo) {
        this.codigo = codigo;
    }

    public int getCodigo() {
        return codigo;
    }
}
```

Crie um `AttributeConverter<SituacaoProduto, Integer>` para converter o código. Evite persistir a posição ordinal do enum.

## Factory

```java
public final class ProdutoFactory {

    private ProdutoFactory() {
    }

    public static ProdutoDTO toDTO(Produto produto) {
        ProdutoDTO dto = new ProdutoDTO();
        dto.setId(produto.getId());
        dto.setNome(produto.getNome());
        dto.setPreco(produto.getPreco());
        return dto;
    }

    public static Produto novo(CriarProdutoRequest request) {
        return new Produto(request.getNome(), request.getPreco());
    }
}
```

A conversão é manual. Não há dependência de MapStruct.

## DAO

```java
@Dependent
public class ProdutoDao {

    @Inject
    EntityManager entityManager;

    public Produto obterPorId(int id) {
        return entityManager.find(Produto.class, id);
    }

    public List<Produto> buscarPorNome(String nome) {
        return entityManager.createQuery(
                "SELECT p FROM Produto p WHERE LOWER(p.nome) LIKE :nome",
                Produto.class)
            .setParameter("nome", nome.toLowerCase() + "%")
            .getResultList();
    }

    public void salvar(Produto produto) {
        entityManager.persist(produto);
    }
}
```

Uma arquitetura corporativa pode fornecer um `GenericApplicationDao<T, ID>` com helpers como `salvar`, `remover`, `getList` e `getEntidade`. Essa classe não pertence ao JPA.

## DAO de consulta

```text
ProdutoDao       operações simples da entidade
ProdutoQueryDao  joins, relatórios e projeções complexas
```

## JPQL ou SQL nativo

```text
JPQL       consulta entidades e atributos Java
SQL nativo consulta tabelas e recursos específicos do banco
```

Use parâmetros. Nunca concatene entrada do usuário no SQL.

## Named queries

Uma named query recebe um nome fixo e fica declarada junto da entidade:

```java
@Entity
@NamedQuery(
    name = "Produto.buscarAtivos",
    query = "SELECT p FROM Produto p WHERE p.ativo = true ORDER BY p.nome"
)
public class Produto {
    private Boolean ativo;
}
```

Uso no DAO:

```java
public List<Produto> buscarAtivos() {
    return entityManager
            .createNamedQuery("Produto.buscarAtivos", Produto.class)
            .getResultList();
}
```

```text
Named query   → consulta fixa, reutilizada e identificada por nome
JPQL dinâmico → consulta construída para um caso específico
SQL nativo    → recurso próprio do banco ou consulta complexa
```

Não monte JPQL por concatenação. Para filtros opcionais, use parâmetros e uma estratégia de construção segura.

## Estratégias de identificador

| Estratégia | Quando usar | Atenção |
|---|---|---|
| `IDENTITY` | Banco gera o ID na inclusão | Depende do suporte do banco |
| `SEQUENCE` | Banco oferece sequences | Configure nome e allocation size |
| UUID | Identidade antes de persistir ou entre serviços | Índice e tamanho maiores |
| Gerador corporativo | Legado com mais de um banco | É código interno, não padrão JPA |

Exemplo com sequence:

```java
@Id
@SequenceGenerator(
    name = "produtoSequence",
    sequenceName = "Produto_ID_SEQ",
    allocationSize = 1
)
@GeneratedValue(
    strategy = GenerationType.SEQUENCE,
    generator = "produtoSequence"
)
private Long id;
```

A estratégia deve corresponder ao schema real. Não copie `IDENTITY`, `SEQUENCE` ou um gerador personalizado sem conferir o banco e o DDL.

## Constraints e conflitos

A validação no service melhora a mensagem, mas a constraint do banco protege contra concorrência:

```text
Requisição A consulta → nome disponível
Requisição B consulta → nome disponível
A e B tentam inserir
Constraint única     → somente uma inclusão vence
```

Exemplo documental na entidade:

```java
@Table(
    name = "CAT_Produto",
    uniqueConstraints = @UniqueConstraint(
        name = "UK_Produto_Nome",
        columnNames = "Nome"
    )
)
```

Com `database.generation=none`, essa annotation **não cria** a constraint em produção; o DDL precisa seguir o processo de banco.

Uma camada central deve traduzir a violação conhecida para uma resposta de conflito, normalmente HTTP `409`, sem expor SQL, nome de servidor ou stack trace. Constraint desconhecida continua sendo falha técnica e deve aparecer nos logs.

## Transação

```java
@Dependent
@Transactional
public class ProdutoService {
}
```

```text
Endpoint → não abre transação
Service  → fronteira transacional
DAO      → participa da transação do service
```

O tipo padrão é `REQUIRED`: usa a transação existente ou cria uma nova. Exceções não verificadas provocam rollback por padrão. Para exceções verificadas, configure `rollbackOn` quando necessário.

Use `REQUIRES_NEW` somente quando a operação precisar ser independente.

## Geração do schema

Em produção:

```properties
quarkus.hibernate-orm.database.generation=none
```

O serviço não altera o banco automaticamente. Mudanças de schema seguem um processo controlado fora da aplicação.

## H2 versus banco real

```text
Teste rápido        → H2
Compatibilidade SQL → Testcontainers com banco equivalente ao real
```

H2 é rápido, mas não reproduz perfeitamente SQL Server.

## Múltiplos datasources

Use uma unidade nomeada quando a funcionalidade precisar de outro banco:

```java
@Inject
@io.quarkus.hibernate.orm.PersistenceUnit("stage")
EntityManager stageEntityManager;
```

Cada datasource precisa de configuração, pool, unidade de persistência e transação bem definidos. Não escolha o banco dinamicamente por texto recebido do usuário.

---

# 9. Comunicação, cache e processamento assíncrono

## Chamada HTTP entre serviços

Uma base corporativa pode encapsular o cliente HTTP:

```java
@Dependent
public class ProdutoClient {

    @Inject
    @ServiceClientRestParam(
        serviceName = "produto-service",
        propagationAuth = true
    )
    ServiceClientRest serviceClientRest;

    public ProdutoDTO obter(int id) {
        return serviceClientRest.get(
                "/produtos/{id}",
                params -> params.path("id", id),
                ProdutoDTO.class);
    }
}
```

`ServiceClientRest` representa uma abstração interna para descoberta, serialização, headers, autenticação e tratamento de erros.

## Configuração do cliente interno

```text
serviceName
→ nome lógico usado para localizar o serviço de destino.

propagationAuth = true
→ repassa o contexto do usuário autenticado.

propagationAuth = false
→ usa a identidade técnica da aplicação.
```

Escolha `propagationAuth` pela identidade exigida no caso de uso; não use `true` automaticamente. A annotation `@ServiceClientRestParam` e a classe `ServiceClientRest` são abstrações internas.

Em projeto pessoal, use MicroProfile REST Client ou o cliente REST do Quarkus.

## Propagação de autenticação

```text
Em nome do usuário → propaga token/contexto
Rotina interna     → usa identidade técnica controlada
```

Nunca copie token manualmente sem entender expiração, audiência e permissões.

## Timeout, retry e idempotência

| Conceito | Pergunta |
|---|---|
| Timeout | Quanto tempo a chamada pode esperar? |
| Retry | A falha é transitória? |
| Idempotência | Repetir a operação duplica o efeito? |
| Circuit breaker | Quando parar de chamar um destino falhando? |
| Fallback | Existe resposta alternativa segura? |

Não aplique retry automaticamente em criação ou cobrança. Primeiro garanta idempotência.

## Kafka

```text
Produtor
  → tópico
  → grupo consumidor
  → consumidor
  → persistência
```

Exemplo conceitual:

```java
@Incoming("produto-importado")
public void processar(ProdutoImportado mensagem) {
    produtoService.importar(mensagem);
}
```

Antes de criar o consumidor, defina:

- chave e contrato da mensagem;
- versionamento;
- estratégia de confirmação;
- retentativa e dead-letter queue;
- idempotência e ordenação;
- observabilidade.

```text
Confirma antes  → pode perder a mensagem se o código falhar.
Confirma depois → pode haver reentrega; o consumidor deve ser idempotente.
```

## Redis

Use para dados temporários:

```text
cache
sessão
rate limit
lock distribuído bem projetado
marca de idempotência
```

Toda chave precisa ter nome, TTL, dono e comportamento definido quando desaparecer.

## Jobs

```text
CronJob Kubernetes
  → chama endpoint interno
  → serviço executa
```

Cuidados:

- o comando deve falhar quando a chamada falhar;
- o log principal da rotina está no serviço;
- duas execuções simultâneas precisam de controle;
- resposta do disparo não garante conclusão do processamento.

## Fila em memória

```text
ConcurrentLinkedQueue
LinkedBlockingQueue
ExecutorService
```

Limites:

- reinício perde itens;
- cada réplica tem sua fila;
- não há histórico automático;
- escalar pods muda a distribuição.

Use somente quando essas características forem aceitáveis.

---

# 10. Configuração, segurança e observabilidade

## `application.properties`

```properties
quarkus.application.name=produto-service

quarkus.datasource.db-kind=mssql
quarkus.datasource.username=${DB_USERNAME}
quarkus.datasource.password=${DB_PASSWORD}
quarkus.datasource.jdbc.url=${DB_URL}

quarkus.redis.hosts=${REDIS_URL:redis://localhost:6379}

%dev.quarkus.log.console.json=false
%test.quarkus.datasource.db-kind=h2
```

Propriedades mudam entre versões. Consulte a documentação da versão usada.

## Injeção com ConfigProperty

```java
@Inject
@ConfigProperty(name = "catalogo.consulta.limite", defaultValue = "100")
int limiteConsulta;

@Inject
@ConfigProperty(name = "catalogo.integracao.url")
String urlIntegracao;
```

Uma propriedade obrigatória ausente deve impedir a inicialização. Isso é melhor do que descobrir a configuração inválida durante a primeira requisição.

Agrupe as chaves por contexto:

```properties
catalogo.consulta.limite=100
catalogo.integracao.url=https://servico.exemplo
catalogo.integracao.timeout=5s
```

Quando muitas propriedades pertencem ao mesmo grupo, avalie `@ConfigMapping` para ter configuração tipada.

## Parâmetros opcionais e valores padrão

Use `Optional` somente quando a ausência for um estado válido:

```java
@Inject
@ConfigProperty(name = "catalogo.integracao.proxy")
Optional<String> proxy;
```

Use `defaultValue` quando existir um padrão seguro:

```java
@Inject
@ConfigProperty(name = "catalogo.cache.ttl-segundos", defaultValue = "300")
long cacheTtlSegundos;
```

```text
Obrigatório   → tipo direto, sem valor padrão
Opcional      → Optional<T>
Padrão seguro → defaultValue
Segredo       → variável/secret, nunca valor padrão no código
```

## Precedência das fontes

```text
Maior prioridade
  propriedade de sistema da JVM
  variável de ambiente
  application.properties
  defaultValue da annotation
Menor prioridade
```

Essa é a ordem padrão simplificada. Um `ConfigSource` personalizado entra na posição determinada por seu `ordinal`. MicroProfile Config sempre escolhe o valor da fonte com maior ordinal.

Uma configuração fornecida por Kubernetes pode chegar como variável, arquivo montado ou `ConfigSource`; a forma de injeção determina sua prioridade.

Para conferir o valor efetivo, registre apenas propriedades não sensíveis. Nunca escreva senha ou token no log durante diagnóstico.

## Decisões para novos parâmetros

Antes de criar uma chave:

```text
1. Procurar propriedade com o mesmo significado.
2. Conferir o padrão de nomes do projeto.
3. Decidir se o valor é obrigatório, opcional ou possui fallback seguro.
4. Decidir se precisa mudar sem novo deploy.
5. Centralizar a leitura na classe responsável.
```

Prefira `@ConfigProperty` para código novo. Quando o valor precisar mudar sem deploy, use o `ConfigSource` persistido já adotado pelo projeto, mas mantenha a leitura pelo MicroProfile Config.

Evite:

- injetar diretamente uma classe legada como `ParametrosAplicacao` em código novo;
- consultar a tabela de parâmetros dentro da regra de negócio;
- criar loader personalizado sem necessidade documentada;
- repetir a mesma chave em classes sem relação;
- colocar nome de ambiente na chave, como `dev`, `hml` ou `prod`;
- deixar limites, percentuais, timeouts e tamanhos de lote como números mágicos.

Nome estável:

```properties
catalogo.importacao.tamanho-lote=500
```

Nome frágil:

```properties
catalogo.importacao.tamanho-lote-prod=500
```

## Segredos

Nunca versione:

```text
senha
token
API key
connection string com credencial
chave privada
arquivo de credenciais de teste
```

Use secrets do ambiente, cofre de segredos ou variáveis protegidas do pipeline.

## Perfis

```properties
%dev.quarkus.log.console.json=false
%test.quarkus.datasource.db-kind=h2
```

Evite duplicar um arquivo inteiro por ambiente quando apenas alguns valores mudam.

## Segurança

```text
Autenticação → quem é o usuário?
Autorização  → o que ele pode fazer?
```

Exemplo portátil:

```java
@GET
@Path("/{id}")
@RolesAllowed("produto-consulta")
public ProdutoDTO obter(@PathParam("id") int id) {
    return produtoService.obter(id);
}
```

Arquiteturas corporativas podem substituir `@RolesAllowed` por annotations e códigos próprios. O conceito continua o mesmo.

Regras:

- negar por padrão;
- validar token no backend;
- aplicar menor privilégio;
- separar identidade de usuário e de serviço;
- não confiar em ocultar botão no frontend;
- auditar operações sensíveis.

## Logs

```java
private static final Logger LOG = Logger.getLogger(ProdutoService.class);

LOG.infof("Criando produto. nome=%s", request.getNome());
LOG.errorf(exception, "Falha ao criar produto.");
```

Uma arquitetura pode encapsular o logger em `LoggerApp`. O objetivo é padronizar formato e contexto.

Log bom contém operação, identificador técnico, resultado, duração, correlation id e exceção original.

Nunca registre senha, token completo, chave ou payload sensível.

## Observabilidade

| Pilar | Responde |
|---|---|
| Logs | O que aconteceu? |
| Métricas | Quanto e com que frequência? |
| Traces | Por onde a requisição passou? |

OpenTelemetry padroniza a coleta. Ferramentas como Datadog, Grafana ou Jaeger armazenam e exibem os dados.

## Auditoria

```text
Log técnico → timeout ao chamar serviço
Auditoria   → usuário alterou configuração X de A para B
```

Log técnico não substitui auditoria.

---

# 11. Frontend Angular

## Visão geral

```text
Componente
  → Service frontend
  → cliente HTTP
  → API
  → estado global, quando necessário
  → componente renderiza
```

## Estrutura por funcionalidade

```text
src/app/
├── produtos/
│   ├── components/
│   ├── pages/
│   ├── services/
│   ├── state/
│   ├── models/
│   └── produtos.module.ts
├── shared/
└── core/
```

```text
core/   autenticação, interceptors e serviços singleton
shared/ componentes reutilizáveis sem regra específica
feature funcionalidade isolada e lazy-loaded
```

## Model

```typescript
export interface Produto {
  id: number;
  nome: string;
  preco: number;
}
```

No Java, dinheiro usa `BigDecimal`. No JSON ele pode chegar como número ou string; defina o contrato e evite cálculos financeiros imprecisos no navegador.

## Service HTTP

```typescript
@Injectable({ providedIn: 'root' })
export class ProdutoService {
  private readonly url = '/api/produtos';

  constructor(private readonly http: HttpClient) {}

  obter(id: number): Observable<Produto> {
    return this.http.get<Produto>(`${this.url}/${id}`);
  }

  criar(request: CriarProdutoRequest): Observable<Produto> {
    return this.http.post<Produto>(this.url, request);
  }
}
```

Um cliente HTTP próprio pode cuidar de descoberta, autenticação, cache e bloqueio de tela. Não espalhe headers técnicos nos componentes; use client ou interceptor central.

## Componente

```typescript
@Component({
  selector: 'app-produto-detalhe',
  templateUrl: './produto-detalhe.component.html'
})
export class ProdutoDetalheComponent implements OnInit, OnDestroy {
  produto?: Produto;
  carregando = false;

  private readonly subscriptions = new SubSink();

  constructor(private readonly produtoService: ProdutoService) {}

  ngOnInit(): void {
    this.carregar(10);
  }

  ngOnDestroy(): void {
    this.subscriptions.unsubscribe();
  }

  private carregar(id: number): void {
    this.carregando = true;
    this.subscriptions.sink = this.produtoService.obter(id)
      .pipe(finalize(() => this.carregando = false))
      .subscribe(produto => this.produto = produto);
  }
}
```

`SubSink` é útil na stack Angular tradicional. Em Angular atual, avalie `takeUntilDestroyed` e signals.

## Estado com NGXS

```text
Componente despacha Action
  → State chama Service
  → State atualiza Model
  → Selectors alimentam componentes
```

```typescript
export class CarregarProdutos {
  static readonly type = '[Produtos] Carregar';
}

export interface ProdutoStateModel {
  itens: Produto[];
  carregando: boolean;
}
```

Não coloque todo estado no store. Estado local simples permanece no componente.

## Lazy loading

```typescript
const routes: Routes = [
  {
    path: 'produtos',
    loadChildren: () => import('./produtos/produtos.module')
      .then(m => m.ProdutosModule)
  }
];
```

## Design system

Prefira componentes padronizados:

```html
<app-button label="Salvar" (click)="salvar()"></app-button>
<app-feedback [message]="mensagem"></app-feedback>
```

O design system concentra cores, tipografia, acessibilidade, botões, inputs, modais, loading e erros.

Não misture design system, PrimeNG e Material sem uma regra visual clara.

## Tratamento de erro

```text
Interceptor → autenticação e falhas globais
Service     → adapta resposta da API
Componente  → feedback específico da tela
```

Evite `subscribe` dentro de outro `subscribe`. Use `switchMap`, `concatMap` ou `forkJoin`.

## Legado e projeto novo

A arquitetura de referência usa Angular 11, NGXS, Jasmine e Karma. Para projeto novo:

- use versão atual e suportada do Angular;
- avalie standalone components e signals;
- mantenha RxJS para fluxos assíncronos;
- considere Jest ou Vitest conforme o suporte;
- preserve separação, lazy loading e design system.

Não copie uma versão antiga apenas para imitar a estrutura.

---

# 12. Estratégia de testes e QA

## Pirâmide de testes

```text
          E2E
       poucos e críticos
        /         \
   integração de API
      /             \
  muitos testes unitários
```

| Teste | Protege | Velocidade |
|---|---|---|
| Unitário | Regra isolada | Alta |
| Integração | Framework, banco e HTTP | Média |
| Contrato | Compatibilidade entre serviços | Média |
| E2E | Jornada completa | Baixa |

## Teste unitário Java

```java
@ExtendWith(MockitoExtension.class)
class ProdutoServiceTest {

    @Mock
    ProdutoDao produtoDao;

    @InjectMocks
    ProdutoService produtoService;

    @Test
    void deveRejeitarPrecoNaoPositivo() {
        CriarProdutoRequest request = new CriarProdutoRequest();
        request.setNome("Teclado");
        request.setPreco(BigDecimal.ZERO);

        assertThrows(
                RegraNegocioException.class,
                () -> produtoService.criar(request));
    }
}
```

## Teste de integração Quarkus

```java
@QuarkusTest
class ProdutoEndpointTest {

    @Test
    void deveObterProduto() {
        RestAssured.given()
            .when().get("/produtos/1")
            .then().statusCode(200)
            .body("id", equalTo(1));
    }
}
```

Pode validar CDI, JAX-RS, serialização, segurança, transação, persistência e configuração.

## Testcontainers

```text
Teste inicia container
  → aplica massa controlada
  → executa API/DAO
  → valida resultado
  → destrói container
```

Use quando o comportamento depende do banco, Redis ou Kafka reais.

## Cuidados com testes Java

- Ao testar módulo Maven isolado, use `-am` para construir dependências irmãs.
- `@QuarkusTest` pode não contribuir para a cobertura como um teste unitário comum.
- Mocks estáticos podem esconder o comportamento real.
- Definir ID manualmente não simula callbacks JPA.
- Não ligue log SQL no código versionado.

## Teste unitário Angular

```typescript
describe('ProdutoService', () => {
  let service: ProdutoService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule]
    });

    service = TestBed.inject(ProdutoService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  afterEach(() => httpMock.verify());

  it('deve obter um produto', () => {
    service.obter(1).subscribe(produto => {
      expect(produto.nome).toBe('Teclado');
    });

    const request = httpMock.expectOne('/api/produtos/1');
    expect(request.request.method).toBe('GET');
    request.flush({ id: 1, nome: 'Teclado', preco: 150 });
  });
});
```

Teste o contrato HTTP no service e o comportamento visual no componente. Não teste detalhes internos do Angular.

## Cypress em camadas

```text
cypress/
├── selectors/  localizadores
├── commands/   ações reutilizáveis
├── pages/      linguagem da tela
└── e2e/        cenários
```

### Selector

```typescript
export const produtoSelectors = {
  nome: '[data-cy="produto-nome"]',
  preco: '[data-cy="produto-preco"]',
  salvar: '[data-cy="produto-salvar"]'
};

export const loginSelectors = {
  usuario: '[data-cy="login-usuario"]',
  senha: '[data-cy="login-senha"]',
  entrar: '[data-cy="login-entrar"]'
};
```

Prefira `data-cy`. Não use classe visual como contrato de teste.

### Command e Page

```typescript
Cypress.Commands.add('login', () => {
  const usuario = String(Cypress.env('E2E_USER'));
  const senha = String(Cypress.env('E2E_PASSWORD'));

  cy.session(usuario, () => {
    cy.visit('/login');
    cy.get(loginSelectors.usuario).type(usuario);
    cy.get(loginSelectors.senha).type(senha, { log: false });
    cy.get(loginSelectors.entrar).click();
    cy.url().should('not.include', '/login');
  });
});

Cypress.Commands.add('preencherProduto', (nome, preco) => {
  cy.get(produtoSelectors.nome).clear().type(nome);
  cy.get(produtoSelectors.preco).clear().type(preco);
});

Cypress.Commands.add('salvarProduto', () => {
  cy.get(produtoSelectors.salvar).click();
});

export class ProdutoPage {
  visitar(): void {
    cy.visit('/produtos/novo');
  }

  preencher(nome: string, preco: string): void {
    cy.preencherProduto(nome, preco);
  }

  salvar(): void {
    cy.salvarProduto();
  }
}
```

Todo command novo também precisa ser declarado nos tipos do Cypress:

```typescript
declare namespace Cypress {
  interface Chainable {
    login(): Chainable<void>;
    preencherProduto(nome: string, preco: string): Chainable<void>;
    salvarProduto(): Chainable<void>;
  }
}
```

As credenciais vêm de variáveis do ambiente de teste e não são versionadas. Adapte o command ao mecanismo real de autenticação, como OIDC, API ou HTTP Basic.

### Spec

```typescript
describe('Cadastro de produto', () => {
  const page = new ProdutoPage();

  beforeEach(() => {
    cy.login();
    page.visitar();
  });

  it('deve cadastrar produto válido', () => {
    page.preencher('Teclado', '150.00');
    page.salvar();
    cy.contains('Produto criado com sucesso').should('be.visible');
  });
});
```

O spec descreve comportamento; os detalhes de seletor ficam fora dele.

## Appium e WebdriverIO

```text
pages/
specs/
configurações wdio
artifacts/screenshots
artifacts/logs
```

Ordem de seletor:

```text
accessibility id
  → resource id
  → XPath por atributo estável
  → XPath por posição como último recurso
```

Use espera por estado. `pause()` deve ser exceção.

## Automação com Python

Scripts que alteram branches, pipelines ou ambientes precisam de:

```text
dry-run por padrão
allowlist de ambientes
confirmação explícita
logs estruturados
parâmetros por CLI
testes pytest
```

Nunca deixe produção como valor padrão.

---

# 13. Build, pipeline e deploy

## Build Java

```powershell
./mvnw clean verify
./mvnw quarkus:dev
```

O Maven Wrapper fixa a distribuição do Maven, **não a JVM**. O Java ainda é escolhido por `JAVA_HOME`, `PATH`, Maven Toolchains ou pelo ambiente do pipeline.

Confira os dois antes do build:

```powershell
java -version
./mvnw -version
```

Na arquitetura de referência, a geração mais recente usa JDK 25. Confirme a versão no `pom.xml`, no pipeline e na saída de `./mvnw -version`.

## Codificação

Alguns repositórios legados usam ISO-8859-1. Converter acidentalmente para UTF-8 pode corromper acentos.

Para projeto novo:

```xml
<properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
</properties>
```

```text
Legado       → preserve a codificação existente
Projeto novo → use UTF-8 declarado
```

## Pipeline recomendado

```text
1. checkout
2. restaurar cache
3. compilar
4. testes unitários
5. testes de integração
6. análise Sonar
7. quality gate
8. construir imagem
9. scan de segurança
10. publicar artefato
11. deploy por ambiente
```

Todo pull request deve executar build e testes obrigatórios.

No Sonar, associe a análise à branch ou ao PR. Um resultado global pode exibir a análise de outra branch.

## Docker

Docker serve para construir a imagem, iniciar dependências locais e executar Testcontainers. Não é camada de negócio nem módulo Maven.

## Helm

```text
devops/produto-service/
├── Chart.yaml
├── values.yaml
└── templates/
    ├── deployment.yaml
    ├── service.yaml
    ├── ingress.yaml
    ├── configmap.yaml
    ├── secret.yaml
    └── cronjob.yaml
```

| Objeto | Função |
|---|---|
| Deployment | Pods e estratégia de atualização |
| Service | Endereço interno estável |
| Ingress | Entrada HTTP externa |
| ConfigMap | Configuração não sensível |
| Secret | Dado sensível |
| CronJob | Execução agendada |

## Health checks

```text
Liveness  → o processo precisa reiniciar?
Readiness → pode receber tráfego?
Startup   → ainda está inicializando?
```

Defina requests, limits, réplicas, autoscaling, graceful shutdown e timeout de encerramento.

---

# 14. Exemplo integrado

## Cenário

```text
Usuário abre formulário
  → Angular envia POST /produtos
  → endpoint delega
  → service valida
  → DAO persiste
  → API devolve 201
  → frontend exibe feedback
```

## Contrato

```json
{
  "nome": "Teclado",
  "preco": 150.00
}
```

Resposta:

```json
{
  "id": 42,
  "nome": "Teclado",
  "preco": 150.00
}
```

## Caminho do código

```text
produto-form.component.ts
  → ProdutoService.criar()
  → POST /produtos
  → ProdutoEndpoint.criar()
  → ProdutoService.criar()
  → ProdutoFactory.novo()
  → ProdutoDao.salvar()
  → SQL Server
  → ProdutoFactory.toDTO()
  → HTTP 201
  → mensagem de sucesso
```

## O que testar

| Nível | Cenário |
|---|---|
| Unitário backend | preço zero é rejeitado |
| DAO | produto é persistido com precisão decimal |
| API | POST válido retorna 201 |
| Frontend | service envia o contrato correto |
| Componente | loading e mensagem são atualizados |
| E2E | usuário preenche, salva e vê confirmação |

---

# 15. Erros comuns

## Backend

1. Colocar regra no endpoint.
2. Endpoint acessar DAO diretamente.
3. Retornar entidade JPA como contrato.
4. Usar `double` para dinheiro.
5. Concatenar entrada do usuário em SQL.
6. Abrir transação no endpoint.
7. Usar `REQUIRES_NEW` sem entender o efeito.
8. Capturar `Exception` e perder a causa.
9. Fazer retry em operação não idempotente.
10. Criar abstração genérica antes de existir repetição.
11. Manter log SQL ligado no pipeline.
12. Salvar segredo no repositório.
13. Tratar H2 como cópia perfeita do banco real.
14. Criar consumidor Kafka sem estratégia de falha.
15. Usar fila em memória como se fosse durável.

## Frontend

1. Chamar `HttpClient` diretamente em todos os componentes.
2. Esquecer de cancelar subscriptions.
3. Colocar todo estado no store global.
4. Misturar requisição e renderização no componente.
5. Usar `subscribe` dentro de `subscribe`.
6. Exibir mensagem técnica ao usuário.
7. Duplicar componentes do design system.
8. Confiar no frontend para autorização.
9. Não tratar loading, vazio e erro.
10. Copiar versão antiga do Angular sem necessidade.

## QA e infraestrutura

1. E2E depender de classe CSS visual.
2. Repetir seletores diretamente nos specs.
3. Usar espera fixa quando existe condição observável.
4. Compartilhar estado entre testes.
5. Automação executar ação real sem dry-run.
6. Pipeline permitir merge sem build.
7. CronJob terminar com sucesso quando a chamada falha.
8. Readiness responder sucesso antes da aplicação estar pronta.
9. Logar senha, token ou payload sensível.
10. Considerar cobertura alta como prova de qualidade.

---

# 16. Checklists

## Novo endpoint

- [ ] Contrato definido no módulo `api`.
- [ ] DTO diferente da entidade.
- [ ] Endpoint fino e documentado com OpenAPI.
- [ ] Status HTTP coerente.
- [ ] Validação e regra no service.
- [ ] Transação no service quando necessária.
- [ ] Factory ou mapper explícito.
- [ ] DAO com parâmetros seguros.
- [ ] Autenticação e autorização definidas.
- [ ] Erros convertidos por handler central.
- [ ] Teste unitário da regra.
- [ ] Teste de integração da rota quando necessário.
- [ ] Client atualizado se outro serviço consumir a API.

## Nova entidade

- [ ] Tabela e colunas corretas.
- [ ] Estratégia de ID compatível com o banco.
- [ ] `BigDecimal` para dinheiro.
- [ ] Tipo de data coerente.
- [ ] Converter para `S/N` ou enum quando necessário.
- [ ] Relações JPA avaliadas quanto a lazy loading.
- [ ] Entidade não exposta diretamente pela API.
- [ ] Alteração de schema tratada fora da aplicação.

## Nova integração

- [ ] Contrato versionado.
- [ ] Timeout definido.
- [ ] Autenticação definida.
- [ ] Retry apenas se seguro.
- [ ] Idempotência avaliada.
- [ ] Falha e fallback definidos.
- [ ] Logs sem dados sensíveis.
- [ ] Métrica e trace disponíveis.
- [ ] Teste de contrato ou integração.

## Nova configuração

- [ ] Chave agrupada por prefixo da funcionalidade.
- [ ] Tipo compatível com o valor esperado.
- [ ] Obrigatória, opcional ou com padrão definido conscientemente.
- [ ] Segredo fornecido pelo ambiente, nunca pelo repositório.
- [ ] Override de teste configurado quando necessário.
- [ ] Valor sensível não aparece em log ou mensagem de erro.
- [ ] Precedência entre arquivo, ambiente e JVM verificada.

## Nova tela Angular

- [ ] Feature organizada por domínio.
- [ ] Contratos TypeScript tipados.
- [ ] HTTP concentrado no service.
- [ ] Estado local ou global escolhido conscientemente.
- [ ] Subscriptions finalizadas.
- [ ] Loading, vazio, sucesso e erro tratados.
- [ ] Componentes do design system reutilizados.
- [ ] Rota lazy-loaded quando apropriado.
- [ ] Teste do componente e do service.
- [ ] Seletores `data-cy` nos fluxos E2E importantes.

## Antes do merge

- [ ] Build com a mesma JVM do pipeline.
- [ ] Testes relevantes executados.
- [ ] Sem segredo ou credencial.
- [ ] Sem log SQL temporário.
- [ ] Codificação preservada.
- [ ] Quality gate correto para a branch/PR.
- [ ] Helm e variáveis revisados se o deploy mudou.
- [ ] Mudança de banco coordenada se o schema mudou.

---

# 17. Roteiro de aprendizado

## Ordem recomendada

```text
1. HTTP e JSON
2. Java e orientação a objetos
3. Maven
4. CDI e injeção de dependência
5. JAX-RS
6. Service e tratamento de erros
7. JPA, SQL e transações
8. Testes unitários e integração
9. Angular, TypeScript e RxJS
10. Cypress
11. Redis e Kafka
12. Docker, Helm e Kubernetes
13. Logs, métricas e traces
14. Segurança e CI/CD
```

## Projeto pessoal sugerido

```text
Backend
├── CRUD de produtos
├── SQL Server ou PostgreSQL
├── cache Redis
├── evento Kafka ao criar produto
└── JUnit + Testcontainers

Frontend
├── listagem e formulário
├── loading e erros
├── estado local; NGXS apenas se necessário
└── testes de componente + Cypress

Infraestrutura
├── Docker Compose local
├── pipeline de build
├── análise Sonar
├── chart Helm
└── OpenTelemetry
```

Evolua por etapas. Não adicione Kafka, Redis e Kubernetes antes de a API simples funcionar.

## Como estudar um repositório existente

```text
1. Leia README e pom.xml/package.json.
2. Ache um endpoint ou rota pequena.
3. Siga a chamada até o banco.
4. Veja DTO e Factory.
5. Leia os testes da funcionalidade.
6. Confira configurações.
7. Veja o chart Helm.
8. Só depois estude fluxos distribuídos.
```

---

# 18. Glossário

| Termo | Explicação curta |
|---|---|
| API | Contrato usado por aplicações para se comunicar |
| CDI | Injeção de dependência do Jakarta EE |
| DTO | Objeto de transporte de dados |
| Endpoint | Método exposto por HTTP |
| Service | Classe que coordena o caso de uso |
| DAO | Classe de acesso a dados |
| Entity | Objeto mapeado para tabela |
| Factory/Mapper | Converte objetos de formatos diferentes |
| JAX-RS | Especificação Java para APIs REST |
| JPA | Especificação Java de persistência |
| Hibernate | Implementação de ORM usada pelo Quarkus |
| Transação | Operações confirmadas ou desfeitas juntas |
| Cache | Cópia temporária para acesso rápido |
| Broker | Sistema que transporta mensagens |
| Tópico | Canal de mensagens do Kafka |
| Idempotência | Repetir produz o mesmo efeito final |
| Retry | Nova tentativa após falha transitória |
| Timeout | Limite de espera |
| Circuit breaker | Interrompe chamadas para destino falhando |
| E2E | Teste de jornada completa |
| Container | Processo isolado criado de uma imagem |
| Pod | Menor unidade executável do Kubernetes |
| Helm | Template e pacote de recursos Kubernetes |
| Trace | Caminho da requisição entre componentes |
| Quality gate | Critérios mínimos de uma análise |

---

# 19. Decisões de implementação e trabalho

Esta seção registra convenções adotadas para escrever, investigar e alterar código. Elas ajudam a manter mudanças pequenas, previsíveis e fáceis de revisar.

## Padrões de código adotados

| Faça | Evite |
|---|---|
| Use Java 25 nos projetos que adotam essa versão | Compilar sem confirmar a versão ativa do Java |
| Use APIs `jakarta.*` | Adicionar imports antigos de `javax.*` |
| Prefira recursos do Quarkus e Jakarta | Misturar anotações Spring sem necessidade comprovada |
| Escreva nomes claros e métodos pequenos | Explicar código confuso com comentários |
| Use nomes de domínio e mensagens em português | Misturar idiomas no mesmo contexto |
| Preserve o estilo do módulo alterado | Fazer refatorações não relacionadas |
| Escreva getters, setters e construtores necessários | Adicionar Lombok |

Frameworks, protocolos e termos técnicos mantêm seus nomes originais: `Kafka`, `cache`, `endpoint`, `payload` e `commit`.

### Código legível sem comentários explicativos

A convenção é fazer o código explicar a intenção por meio de nomes e funções curtas.

Evite:

```java
public void proc(Pedido p) {
    if (p.getTotal().signum() > 0) {
        enviar(p);
    }
}
```

Prefira:

```java
public void enviarPedidoComValorPositivo(Pedido pedido) {
    if (pedido.possuiValorPositivo()) {
        enviar(pedido);
    }
}
```

Comentários continuam aceitáveis quando uma ferramenta ou um contrato externo os exige. Eles não devem compensar nomes vagos ou métodos grandes.

### Codificação de arquivos

Alguns projetos legados usam `ISO-8859-1`, também chamado de Latin-1. Salvar um único arquivo em UTF-8 pode quebrar acentos, testes e diffs.

```text
Projeto existente → descubra e preserve a codificação atual
Projeto novo      → use UTF-8 de forma explícita e consistente
```

Confira `pom.xml`, `.editorconfig`, configuração da IDE e arquivos vizinhos antes de alterar um arquivo legado.

Resumo das decisões:

```text
Código claro > comentário explicativo
Mudança pequena > refatoração oportunista
Busca direcionada > leitura indiscriminada
Evidência real > suposição
Relato exato > resultado otimista
Segredo em runtime > segredo no código
Autorização explícita > efeito externo presumido
```

---

# Resumo de bolso

```text
Frontend apresenta e coordena a experiência.
Endpoint fala HTTP.
Service aplica regras e controla a transação.
Factory converte objetos.
DAO acessa o banco.
Client chama outro serviço.
Redis guarda dados temporários.
Kafka desacopla processamento.
Testes unitários protegem regras.
Testes de integração protegem conexões.
Cypress e Appium protegem jornadas.
Helm descreve o deploy.
OpenTelemetry ajuda a entender a execução.
```
