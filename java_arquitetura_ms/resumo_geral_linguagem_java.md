# Revisão Geral da Linguagem Java

> Resumo direto e prático da linguagem Java e de seu ecossistema backend, com explicações dentro dos exemplos.

> Exemplos executáveis e isolados apresentam **Resultado**. Recortes de frameworks mostram a estrutura essencial e dependem das bibliotecas e configurações do projeto.

> O escopo é somente backend. Docker, Kubernetes e ferramentas de qualidade aparecem apenas por apoiarem a construção, execução e entrega da aplicação Java.

---

## Sumário

1. [Java, JDK, JRE e JVM](#1-java-jdk-jre-e-jvm)
2. [Estrutura básica](#2-estrutura-básica)
3. [Variáveis e tipos](#3-variáveis-e-tipos)
4. [Operadores](#4-operadores)
5. [Controle de fluxo](#5-controle-de-fluxo)
6. [Métodos](#6-métodos)
7. [Arrays](#7-arrays)
8. [POO Orientação a objetos](#8-poo-orientação-a-objetos)
9. [Encapsulamento](#9-encapsulamento)
10. [Herança, polimorfismo e composição](#10-herança-polimorfismo-e-composição)
11. [Interfaces e classes abstratas](#11-interfaces-e-classes-abstratas)
12. [Record, Enum e classes seladas](#12-record-enum-e-classes-seladas)
13. [Strings](#13-strings)
14. [equals e hashCode](#14-equals-e-hashcode)
15. [Collections](#15-collections)
16. [Generics](#16-generics)
17. [Exceptions](#17-exceptions)
18. [Optional](#18-optional)
19. [Lambdas e interfaces funcionais](#19-lambdas-e-interfaces-funcionais)
20. [Streams API](#20-streams-api)
21. [BigDecimal](#21-bigdecimal)
22. [Datas e horários](#22-datas-e-horários)
23. [Arquivos e I/O](#23-arquivos-e-io)
24. [Annotations](#24-annotations)
25. [Threads e concorrência](#25-threads-e-concorrência)
26. [JDBC](#26-jdbc)
27. [Maven e Gradle](#27-maven-e-gradle)
28. [Testes com JUnit](#28-testes-com-junit)
29. [SOLID](#29-solid)
30. [Clean Code e refatoração](#30-clean-code-e-refatoração)
31. [Recursos do Java moderno](#31-recursos-do-java-moderno)
32. [Quarkus e Jakarta EE](#32-quarkus-e-jakarta-ee)
33. [APIs REST com JAX-RS](#33-apis-rest-com-jax-rs)
34. [CDI, configuração e validação](#34-cdi-configuração-e-validação)
35. [JPA, Hibernate e transações](#35-jpa-hibernate-e-transações)
36. [Integração entre serviços](#36-integração-entre-serviços)
37. [Kafka, Redis e jobs](#37-kafka-redis-e-jobs)
38. [Segurança no backend](#38-segurança-no-backend)
39. [Documentação e observabilidade](#39-documentação-e-observabilidade)
40. [Testes do backend](#40-testes-do-backend)
41. [Relatórios com JasperReports](#41-relatórios-com-jasperreports)
42. [Containers e deploy](#42-containers-e-deploy)
43. [Checklist final](#43-checklist-final)

---

# 1. Java, JDK, JRE e JVM

```text
Java      → linguagem de programação
JDK       → ferramentas para desenvolver e compilar
JRE       → ambiente necessário para executar aplicações
JVM       → máquina virtual que executa o bytecode
Bytecode  → código intermediário gerado pelo compilador
```

```text
Main.java
   ↓ javac
Main.class
   ↓ JVM
Aplicação executada
```

```bash
# Compila
javac Main.java

# Executa
java Main
```


**O que acontece:** `javac` gera `Main.class`; `java Main` executa a classe e exibe a saída definida no método `main`.

---

# 2. Estrutura básica

```java
// Arquivo: Main.java
public class Main {

    // Ponto de entrada da aplicação
    public static void main(String[] args) {
        System.out.println("Olá, Java!");
    }
}
```


**Resultado:**

```text
Olá, Java!
```

```text
public  → acessível por outras classes
static  → pertence à classe
void    → não retorna valor
main    → método inicial
args    → argumentos recebidos pelo terminal
```


```text
Sistema de CamelCase

1- Classe/Interface                sempre Iniciam com Letra Maiúscula.  Ex.: TesteInicial
2- Atributo/Variável/Métodos       sempre Iniciam com Letra minúscula.  Ex.: testeInicial
3- Pacotes ou Packages             sempre tudo com Letra minúscula.     Ex.: testeinicial
4- Constante                       sempre tudo com Letra Maiúscula.     Ex.: TESTE_INICIAL
```

---

# 3. Variáveis e tipos

## Tipos primitivos

```java
byte pequeno = 100;            // 8 bits
short quantidade = 1_000;      // 16 bits
int idade = 30;                // 32 bits
long populacao = 8_000_000L;   // 64 bits

float altura = 1.75F;          // 32 bits
double peso = 78.5;            // 64 bits

char letra = 'A';              // Um caractere
boolean ativo = true;          // true ou false
```


**O que acontece:** as variáveis primitivas são criadas com os valores `100`, `1000`, `30`, `8000000`, `1.75`, `78.5`, `A` e `true`. Nenhum texto é exibido.

## Tipos por referência

```java
String nome = "Gabriel";           // Objeto String
Integer numero = 10;               // Wrapper de int
List<String> nomes = List.of();     // Coleção
```


**O que acontece:** são criadas três referências: uma `String`, um `Integer` e uma lista vazia. Nenhum texto é exibido.

## Constante

```java
final double PI = 3.14159;

// PI = 10; // Erro: final não pode ser alterado
```


**O que acontece:** `PI` recebe `3.14159` e não pode ser reatribuída. Se a linha comentada for ativada, ocorrerá erro de compilação.

## Inferência com `var`

```java
var nome = "Gabriel"; // O compilador entende que é String
var idade = 30;       // O compilador entende que é int

// var valor; // Erro: precisa ser inicializado
```


**O que acontece:** o compilador infere `String` para `nome` e `int` para `idade`. A declaração sem valor inicial não compila.

## Conversões

```java
int numero = 10;
double valor = numero; // Conversão implícita: int → double

double preco = 19.99;
int inteiro = (int) preco; // Cast explícito: resultado 19
```


**O que acontece:** `valor` recebe `10.0` e `inteiro` recebe `19`, pois o cast remove a parte decimal.

## Wrappers

```java
Integer numero = 10;       // Wrapper de int
Double valor = 20.5;       // Wrapper de double
Boolean ativo = true;      // Wrapper de boolean

int convertido = Integer.parseInt("123");
String texto = String.valueOf(123);
```


**O que acontece:** `convertido` recebe o número `123` e `texto` recebe a string `"123"`. Nenhum texto é exibido.

---

# 4. Operadores

```java
int soma = 10 + 5;
int subtracao = 10 - 5;
int multiplicacao = 10 * 5;
int divisao = 10 / 5;
int resto = 10 % 3;
```


**O que acontece:** os valores calculados são: `soma = 15`, `subtracao = 5`, `multiplicacao = 50`, `divisao = 2` e `resto = 1`.

```java
boolean igual = 10 == 10;
boolean diferente = 10 != 5;
boolean maior = 10 > 5;
boolean menor = 5 < 10;
boolean maiorOuIgual = 10 >= 10;
boolean menorOuIgual = 5 <= 10;
```


**O que acontece:** todas as seis variáveis recebem `true`.

```java
boolean possuiAcesso = true;
boolean contaAtiva = true;

boolean podeEntrar = possuiAcesso && contaAtiva; // E
boolean algumaCondicao = possuiAcesso || contaAtiva; // OU
boolean negacao = !possuiAcesso; // NÃO
```


**O que acontece:** `podeEntrar = true`, `algumaCondicao = true` e `negacao = false`.

## Operador ternário

```java
int idade = 20;

String resultado = idade >= 18
        ? "Maior de idade"
        : "Menor de idade";
```


**O que acontece:** `resultado` recebe `"Maior de idade"`.

---

# 5. Controle de fluxo

## if, else if e else

```java
int nota = 8;

if (nota >= 9) {
    System.out.println("Excelente");
} else if (nota >= 7) {
    System.out.println("Aprovado");
} else {
    System.out.println("Reprovado");
}
```


**Resultado:**

```text
Aprovado
```

## switch expression

```java
int dia = 2;

String nomeDia = switch (dia) {
    case 1 -> "Domingo";
    case 2 -> "Segunda-feira";
    case 3 -> "Terça-feira";
    default -> "Dia inválido";
};
```


**O que acontece:** `nomeDia` recebe `"Segunda-feira"`. Nenhum texto é exibido porque não há `println`.

## for

```java
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}
```


**Resultado:**

```text
0
1
2
3
4
```

## for-each

```java
List<String> nomes = List.of("Ana", "Bruno");

for (String nome : nomes) {
    System.out.println(nome);
}
```


**Resultado:**

```text
Ana
Bruno
```

## while e do-while

```java
int contador = 0;

while (contador < 3) {
    System.out.println(contador);
    contador++;
}
```


**Resultado:**

```text
0
1
2
```

```java
int numero = 0;

do {
    System.out.println(numero);
    numero++;
} while (numero < 3);
```


**Resultado:**

```text
0
1
2
```

## break e continue

```java
for (int i = 0; i < 10; i++) {

    if (i == 2) {
        continue; // Pula esta repetição
    }

    if (i == 5) {
        break; // Encerra o laço
    }

    System.out.println(i);
}
```


**Resultado:**

```text
0
1
3
4
```

---

# 6. Métodos

```java
public class Calculadora {

    // Recebe dois inteiros e retorna um inteiro
    public int somar(int numero1, int numero2) {
        return numero1 + numero2;
    }

    // Não retorna valor
    public void exibir(String mensagem) {
        System.out.println(mensagem);
    }

    // Pertence à classe, não ao objeto
    public static int multiplicar(int a, int b) {
        return a * b;
    }
}
```


**O que acontece:** a classe passa a oferecer os métodos `somar`, `exibir` e `multiplicar`. Definir a classe não gera saída.

```java
Calculadora calculadora = new Calculadora();

int soma = calculadora.somar(10, 5);
calculadora.exibir("Resultado: " + soma);

int resultado = Calculadora.multiplicar(2, 3);
```


**Resultado:**

```text
Resultado: 15
```

**O que acontece:** a variável `resultado` recebe `6`, mas esse valor não é impresso.

## Sobrecarga

```java
public int somar(int a, int b) {
    return a + b;
}

// Mesmo nome, parâmetros diferentes
public double somar(double a, double b) {
    return a + b;
}
```


**O que acontece:** o compilador escolhe a versão do método conforme os tipos dos argumentos: `int` ou `double`.

## Varargs

```java
public int somar(int... numeros) {
    int total = 0;

    for (int numero : numeros) {
        total += numero;
    }

    return total;
}
```


**O que acontece:** o método aceita qualquer quantidade de inteiros e retorna a soma. Por exemplo, `somar(1, 2, 3)` retorna `6`.

---

# 7. Arrays

```java
// Tamanho fixo de três posições
int[] numeros = new int[3];

numeros[0] = 10;
numeros[1] = 20;
numeros[2] = 30;
```


**O que acontece:** o array passa a conter `[10, 20, 30]`. Nenhum valor é impresso.

```java
String[] nomes = {"Ana", "Bruno", "Carlos"};

System.out.println(nomes[0]);     // Ana
System.out.println(nomes.length); // 3
```


**Resultado:**

```text
Ana
3
```

```java
for (String nome : nomes) {
    System.out.println(nome);
}
```


**Resultado:**

```text
Ana
Bruno
Carlos
```

## Matriz

```java
int[][] matriz = {
    {1, 2},
    {3, 4}
};

System.out.println(matriz[1][0]); // 3
```


**Resultado:**

```text
3
```

---

# 8. POO Orientação a objetos

POO significa Programação Orientada a Objetos.

## Ideia central

POO organiza o sistema em objetos que possuem estado e comportamento.

## Pilares da POO

```text
Encapsulamento → protege os dados internos do objeto
Herança        → permite reaproveitar comportamento
Polimorfismo   → permite o mesmo contrato com comportamentos diferentes
Abstração      → mostra o essencial e esconde detalhes
```

## Classe e objeto

Classe é o molde; objeto é a instância criada a partir desse molde.

```java
public class Pessoa {

    // Atributos
    String nome;
    int idade;

    // Comportamento
    void apresentar() {
        System.out.println("Meu nome é " + nome);
    }
}
```


**O que acontece:** a classe `Pessoa` é definida com os atributos `nome`, `idade` e o método `apresentar`. Nenhum objeto é criado ainda.

```java
Pessoa pessoa = new Pessoa(); // Criação do objeto

pessoa.nome = "Gabriel";
pessoa.idade = 30;
pessoa.apresentar();
```


**Resultado:**

```text
Meu nome é Gabriel
```

## Construtor

```java
public class Pessoa {

    private String nome;
    private int idade;

    public Pessoa(String nome, int idade) {
        this.nome = nome;   // this representa o objeto atual
        this.idade = idade;
    }
}
```


**O que acontece:** o construtor obriga a informar nome e idade ao criar uma pessoa. Definir o construtor não produz saída.

```java
Pessoa pessoa = new Pessoa("Gabriel", 30);
```


**O que acontece:** um objeto é criado com `nome = "Gabriel"` e `idade = 30`. Nenhum texto é exibido.

## static

```java
public class Contador {

    // Compartilhado por todos os objetos
    private static int total;

    public Contador() {
        total++;
    }

    public static int getTotal() {
        return total;
    }
}
```


**O que acontece:** cada `new Contador()` incrementa o mesmo atributo estático. Após três objetos, `Contador.getTotal()` retorna `3`.

---

# 9. Encapsulamento

Protege o estado interno do objeto.

```java
public class Conta {

    private BigDecimal saldo = BigDecimal.ZERO;

    public BigDecimal getSaldo() {
        return saldo;
    }

    public void depositar(BigDecimal valor) {
        if (valor.signum() <= 0) {
            throw new IllegalArgumentException("Valor inválido");
        }

        saldo = saldo.add(valor);
    }

    public void sacar(BigDecimal valor) {
        if (saldo.compareTo(valor) < 0) {
            throw new IllegalArgumentException("Saldo insuficiente");
        }

        saldo = saldo.subtract(valor);
    }
}
```


**O que acontece:** a conta começa com saldo zero; depósitos positivos aumentam o saldo e saques acima do saldo lançam uma exceção.

| Modificador | Acesso |
|---|---|
| `public` | Qualquer classe |
| `protected` | Mesmo pacote e subclasses |
| Sem modificador | Mesmo pacote |
| `private` | Apenas a própria classe |

---

# 10. Herança, polimorfismo e composição

## Herança

```java
public class Animal {

    public void emitirSom() {
        System.out.println("Som genérico");
    }
}
```


**O que acontece:** a classe base define um comportamento padrão. A saída `Som genérico` só aparece quando `emitirSom()` é chamado em um `Animal` que não sobrescreve o método.

```java
public class Cachorro extends Animal {

    @Override
    public void emitirSom() {
        System.out.println("Latido");
    }
}
```


**O que acontece:** `Cachorro` herda de `Animal` e substitui `emitirSom()` para imprimir `Latido`.

## Polimorfismo

```java
Animal animal = new Cachorro();

// Executa o método sobrescrito de Cachorro
animal.emitirSom();
```


**Resultado:**

```text
Latido
```

## super

```java
public class Funcionario {

    protected String nome;

    public Funcionario(String nome) {
        this.nome = nome;
    }
}
```


**O que acontece:** a classe pai armazena o nome recebido pelo construtor. Nenhum objeto ou saída é produzido neste trecho.

```java
public class Desenvolvedor extends Funcionario {

    private String linguagem;

    public Desenvolvedor(String nome, String linguagem) {
        super(nome); // Chama o construtor da classe pai
        this.linguagem = linguagem;
    }
}
```


**O que acontece:** o construtor de `Desenvolvedor` chama primeiro o construtor de `Funcionario` com `super(nome)` e depois armazena a linguagem.

## Composição

```java
public class Motor {

    public void ligar() {
        System.out.println("Motor ligado");
    }
}
```


**O que acontece:** o método `ligar()` imprimirá `Motor ligado` quando for chamado.

```java
public class Carro {

    private final Motor motor;

    public Carro(Motor motor) {
        this.motor = motor;
    }

    public void ligar() {
        motor.ligar();
    }
}
```


**O que acontece:** o carro recebe um motor por composição. Ao chamar `carro.ligar()`, o método do motor é acionado e imprime `Motor ligado`.

```text
Herança   → Carro É um Veículo
Composição → Carro TEM um Motor
```

---

# 11. Interfaces e classes abstratas

## Interface

Define um contrato.

```java
public interface Pagamento {

    void pagar(BigDecimal valor);

    default void imprimirComprovante() {
        System.out.println("Comprovante emitido");
    }
}
```


**O que acontece:** a interface exige a implementação de `pagar` e já fornece o método padrão `imprimirComprovante`. Definir o contrato não gera saída.

```java
public class PagamentoPix implements Pagamento {

    @Override
    public void pagar(BigDecimal valor) {
        System.out.println("PIX: " + valor);
    }
}
```


**O que acontece:** ao chamar `pagar(new BigDecimal("100.00"))`, será exibido `PIX: 100.00`.

## Classe abstrata

```java
public abstract class Funcionario {

    protected String nome;

    public Funcionario(String nome) {
        this.nome = nome;
    }

    // Obrigatório nas subclasses
    public abstract BigDecimal calcularSalario();

    // Método já implementado
    public void exibirNome() {
        System.out.println(nome);
    }
}
```


**O que acontece:** a classe abstrata não pode ser instanciada diretamente; subclasses devem implementar `calcularSalario()`.

| Interface | Classe abstrata |
|---|---|
| Define contrato | Define uma base comum |
| Usa `implements` | Usa `extends` |
| Permite várias interfaces | Só permite uma classe pai |
| Normalmente não mantém estado | Pode manter estado |

---

# 12. Record, Enum e classes seladas

## Record

Ideal para objetos simples e imutáveis.

```java
public record Usuario(
        Long id,
        String nome,
        String email
) {
}
```


**O que acontece:** o compilador gera construtor, acessores, `equals`, `hashCode` e `toString` para o record.

```java
Usuario usuario = new Usuario(
        1L,
        "Gabriel",
        "gabriel@email.com"
);

System.out.println(usuario.nome());
```


**Resultado:**

```text
Gabriel
```

## Enum

```java
public enum StatusPedido {
    CRIADO,
    PAGO,
    ENVIADO,
    ENTREGUE,
    CANCELADO
}
```


**O que acontece:** o enum passa a aceitar somente os cinco status declarados.

```java
StatusPedido status = StatusPedido.PAGO;

if (status == StatusPedido.PAGO) {
    System.out.println("Pedido pago");
}
```


**Resultado:**

```text
Pedido pago
```

Enum com atributo:

```java
public enum Perfil {

    ADMIN("Administrador"),
    CLIENTE("Cliente");

    private final String descricao;

    Perfil(String descricao) {
        this.descricao = descricao;
    }

    public String getDescricao() {
        return descricao;
    }
}
```


**O que acontece:** cada constante possui uma descrição. `Perfil.ADMIN.getDescricao()` retorna `Administrador`.

## Classes seladas

```java
public sealed class Forma
        permits Circulo, Retangulo {
}
```


**O que acontece:** somente `Circulo` e `Retangulo` podem herdar diretamente de `Forma`.

```java
public final class Circulo extends Forma {
}
```


**O que acontece:** `Circulo` pode herdar de `Forma`, mas nenhuma outra classe pode herdar de `Circulo` porque ele é `final`.

```java
public non-sealed class Retangulo extends Forma {
}
```


**O que acontece:** `Retangulo` herda de `Forma` e volta a permitir subclasses por ser `non-sealed`.

---

# 13. Strings

Strings são imutáveis.

```java
String nome = "Gabriel";

String completo = nome + " Lima";
String maiusculo = nome.toUpperCase();
String minusculo = nome.toLowerCase();
int tamanho = nome.length();
boolean contem = nome.contains("bri");
boolean vazio = nome.isBlank();
```


**O que acontece:** os valores são `completo = "Gabriel Lima"`, `maiusculo = "GABRIEL"`, `minusculo = "gabriel"`, `tamanho = 7`, `contem = true` e `vazio = false`.

## Comparação

```java
String nome1 = new String("Java");
String nome2 = new String("Java");

// Compara referências
System.out.println(nome1 == nome2); // false

// Compara conteúdo
System.out.println(nome1.equals(nome2)); // true
```


**Resultado:**

```text
false
true
```

## Formatação

```java
String mensagem = String.format(
        "Nome: %s | Idade: %d",
        "Gabriel",
        30
);
```


**O que acontece:** `mensagem` recebe `"Nome: Gabriel | Idade: 30"`.

## Text block

```java
String json = """
        {
          "nome": "Gabriel",
          "idade": 30
        }
        """;
```


**O que acontece:** `json` recebe uma string multilinha contendo o objeto JSON formatado.

## StringBuilder

```java
StringBuilder builder = new StringBuilder();

builder.append("Java");
builder.append(" ");
builder.append("Backend");

String resultado = builder.toString();
```


**O que acontece:** `resultado` recebe `"Java Backend"`.

Use `StringBuilder` ao realizar muitas concatenações.

---

# 14. equals e hashCode

```text
equals   → compara o conteúdo lógico dos objetos
hashCode → gera um código usado por coleções baseadas em hash
```

Objetos considerados iguais devem possuir o mesmo `hashCode`.

```java
import java.util.Objects;

public class Produto {

    private Long id;
    private String nome;

    @Override
    public boolean equals(Object objeto) {

        if (this == objeto) {
            return true;
        }

        if (objeto == null || getClass() != objeto.getClass()) {
            return false;
        }

        Produto produto = (Produto) objeto;

        return Objects.equals(id, produto.id);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id);
    }
}
```


**O que acontece:** dois produtos com o mesmo `id` serão considerados iguais e produzirão o mesmo `hashCode`.

Isso é importante em:

```text
HashSet
HashMap
LinkedHashSet
ConcurrentHashMap
```

---

# 15. Collections

## List

Mantém ordem, permite repetidos e usa índice.

```java
List<String> nomes = new ArrayList<>();

nomes.add("Ana");
nomes.add("Bruno");
nomes.add("Ana");

System.out.println(nomes.get(0));
nomes.remove("Bruno");
```


**Resultado:**

```text
Ana
```

**O que acontece:** após remover `Bruno`, a lista fica `[Ana, Ana]`.

## Set

Não permite elementos duplicados.

```java
Set<String> nomes = new HashSet<>();

nomes.add("Ana");
nomes.add("Ana"); // Não será duplicado
nomes.add("Bruno");
```


**O que acontece:** o segundo `Ana` é ignorado; o conjunto contém apenas `Ana` e `Bruno`, sem ordem garantida.

```java
Set<String> hashSet = new HashSet<>();       // Sem ordem garantida
Set<String> linked = new LinkedHashSet<>();  // Ordem de inserção
Set<String> tree = new TreeSet<>();          // Ordem natural
```


**O que acontece:** são criados três conjuntos vazios com comportamentos diferentes de ordenação.

## Map

Armazena chave e valor.

```java
Map<Long, String> usuarios = new HashMap<>();

usuarios.put(1L, "Gabriel");
usuarios.put(2L, "Ana");

String nome = usuarios.get(1L);

boolean possuiChave = usuarios.containsKey(1L);

usuarios.forEach((id, usuario) ->
        System.out.println(id + ": " + usuario)
);
```


**Resultado esperado:**

```text
1: Gabriel
2: Ana
```

**O que acontece:** em `HashMap`, a ordem de iteração não é garantida e pode variar.

## Queue

Fila: primeiro a entrar, primeiro a sair.

```java
Queue<String> fila = new LinkedList<>();

fila.offer("Primeiro");
fila.offer("Segundo");

String removido = fila.poll(); // Remove o primeiro
String atual = fila.peek();     // Consulta sem remover
```


**O que acontece:** `removido` recebe `"Primeiro"`; depois disso, `atual` recebe `"Segundo"`.

## Deque

```java
Deque<String> deque = new ArrayDeque<>();

deque.addFirst("Início");
deque.addLast("Fim");

deque.removeFirst();
deque.removeLast();
```


**O que acontece:** os dois elementos são adicionados e depois removidos; ao final, o deque fica vazio.

## Coleções imutáveis

```java
List<String> nomes = List.of("Ana", "Bruno");
Set<Integer> numeros = Set.of(1, 2, 3);
Map<Long, String> usuarios = Map.of(1L, "Gabriel");

// nomes.add("Carlos"); // Erro em execução
```


**O que acontece:** as três coleções são imutáveis. Se `nomes.add("Carlos")` for executado, ocorrerá `UnsupportedOperationException`.

## Comparable

Ordenação natural da própria classe.

```java
public class Produto implements Comparable<Produto> {

    private String nome;

    @Override
    public int compareTo(Produto outro) {
        return this.nome.compareTo(outro.nome);
    }
}
```


**O que acontece:** ao ordenar uma lista de produtos, a ordem natural será alfabética pelo nome.

## Comparator

Ordenação externa e flexível.

```java
produtos.sort(
        Comparator.comparing(Produto::getNome)
);

produtos.sort(
        Comparator.comparing(Produto::getPreco)
                  .reversed()
);
```


**O que acontece:** a primeira ordenação usa nome crescente; a segunda usa preço decrescente.

---

# 16. Generics

Permitem reutilização com segurança de tipo.

```java
public class Caixa<T> {

    private T valor;

    public void guardar(T valor) {
        this.valor = valor;
    }

    public T obter() {
        return valor;
    }
}
```


**O que acontece:** a classe pode armazenar qualquer tipo definido em `T`, mantendo verificação de tipos em compilação.

```java
Caixa<String> caixaTexto = new Caixa<>();
caixaTexto.guardar("Java");

Caixa<Integer> caixaNumero = new Caixa<>();
caixaNumero.guardar(10);
```


**O que acontece:** `caixaTexto.obter()` retorna `"Java"` e `caixaNumero.obter()` retorna `10`.

## Método genérico

```java
public static <T> void imprimir(T valor) {
    System.out.println(valor);
}
```


**O que acontece:** o método aceita valores de qualquer tipo e os imprime. Por exemplo, `imprimir(10)` exibe `10`.

## Restrição

```java
public class Calculadora<T extends Number> {

    private final T numero;

    public Calculadora(T numero) {
        this.numero = numero;
    }
}
```


**O que acontece:** a classe só aceita tipos que herdam de `Number`, como `Integer`, `Long`, `Double` e `BigDecimal`.

## Wildcards

```java
// Aceita Number ou subclasses
public double somar(List<? extends Number> numeros) {
    return numeros.stream()
            .mapToDouble(Number::doubleValue)
            .sum();
}
```


**O que acontece:** o método lê números de uma lista de qualquer subtipo de `Number` e devolve a soma como `double`.

```java
// Aceita Integer, Number ou Object
public void adicionar(List<? super Integer> lista) {
    lista.add(10);
}
```


**O que acontece:** o método pode adicionar o inteiro `10` em uma lista de `Integer`, `Number` ou `Object`.

```text
? extends T → normalmente leitura
? super T   → normalmente escrita
```

---

# 17. Exceptions

## Checked Exception

Precisa ser tratada ou declarada.

```java
public String lerArquivo(Path caminho) throws IOException {
    return Files.readString(caminho);
}
```


**O que acontece:** o conteúdo do arquivo é retornado; se a leitura falhar, o método propaga uma `IOException`.

## Unchecked Exception

Herda de `RuntimeException`.

```java
throw new IllegalArgumentException("Valor inválido");
```


**O que acontece:** a execução é interrompida imediatamente com `IllegalArgumentException: Valor inválido`.

## try-catch-finally

```java
try {
    int resultado = 10 / 0;

} catch (ArithmeticException exception) {
    System.out.println("Divisão por zero");

} finally {
    System.out.println("Sempre será executado");
}
```


**Resultado:**

```text
Divisão por zero
Sempre será executado
```

## Exceção personalizada

```java
public class SaldoInsuficienteException
        extends RuntimeException {

    public SaldoInsuficienteException(String mensagem) {
        super(mensagem);
    }
}
```


**O que acontece:** é criada uma exceção específica de negócio que pode receber uma mensagem descritiva.

```java
if (valor.compareTo(saldo) > 0) {
    throw new SaldoInsuficienteException(
            "Saldo insuficiente"
    );
}
```


**O que acontece:** quando o valor for maior que o saldo, a operação é interrompida com `SaldoInsuficienteException`.

## try-with-resources

Fecha recursos automaticamente.

```java
try (BufferedReader reader =
             Files.newBufferedReader(Path.of("arquivo.txt"))) {

    String linha = reader.readLine();
    System.out.println(linha);

} catch (IOException exception) {
    exception.printStackTrace();
}
```


**Resultado esperado:**

```text
Primeira linha do arquivo
```

**O que acontece:** o conteúdo depende do arquivo; o leitor é fechado automaticamente.

Boas práticas:

```text
- Use exceções específicas.
- Não esconda erros silenciosamente.
- Escreva mensagens claras.
- Não use exceção como fluxo normal.
- Preserve a causa original quando necessário.
```

---

# 18. Optional

Representa um valor que pode não existir.

```java
Optional<String> nome = Optional.of("Gabriel");
Optional<String> vazio = Optional.empty();
Optional<String> possivelNulo = Optional.ofNullable(null);
```


**O que acontece:** `nome` contém `Gabriel`; `vazio` e `possivelNulo` ficam vazios.

## ifPresent

```java
usuarioOptional.ifPresent(usuario ->
        System.out.println(usuario.getNome())
);
```


**Resultado esperado:**

```text
Nome do usuário presente no Optional
```

**O que acontece:** nada é impresso quando o `Optional` está vazio.

## map e orElse

```java
String nome = usuarioOptional
        .map(Usuario::getNome)
        .orElse("Usuário não encontrado");
```


**O que acontece:** `nome` recebe o nome do usuário quando presente; caso contrário, recebe `"Usuário não encontrado"`.

## orElseGet

```java
String nome = usuarioOptional
        .map(Usuario::getNome)
        .orElseGet(() -> buscarNomePadrao());
```


**O que acontece:** `buscarNomePadrao()` só é chamado quando o `Optional` está vazio.

## orElseThrow

```java
Usuario usuario = usuarioOptional
        .orElseThrow(() ->
                new UsuarioNaoEncontradoException(
                        "Usuário não encontrado"
                )
        );
```


**O que acontece:** o usuário é retornado quando existe; caso contrário, a exceção personalizada é lançada.

Evite:

```java
// Pode lançar NoSuchElementException
Usuario usuario = usuarioOptional.get();
```


**O que acontece:** o valor é retornado quando presente; se estiver vazio, ocorre `NoSuchElementException`.

---

# 19. Lambdas e interfaces funcionais

```java
List<String> nomes = List.of("Ana", "Bruno");

// Lambda
nomes.forEach(nome -> System.out.println(nome));

// Method reference
nomes.forEach(System.out::println);
```


**Resultado:**

```text
Ana
Bruno
Ana
Bruno
```

**O que acontece:** a lista é percorrida duas vezes: uma pela lambda e outra pelo method reference.

## Predicate

Recebe um valor e retorna `boolean`.

```java
Predicate<Integer> maiorDeIdade =
        idade -> idade >= 18;

boolean resultado = maiorDeIdade.test(20);
```


**O que acontece:** `resultado` recebe `true`, pois `20 >= 18`.

## Function

Recebe um valor e retorna outro.

```java
Function<String, Integer> tamanho =
        texto -> texto.length();

int resultado = tamanho.apply("Java");
```


**O que acontece:** `resultado` recebe `4`, o tamanho da string `Java`.

## Consumer

Recebe valor e não retorna.

```java
Consumer<String> imprimir =
        texto -> System.out.println(texto);

imprimir.accept("Java");
```


**Resultado:**

```text
Java
```

## Supplier

Não recebe valor e retorna um valor.

```java
Supplier<UUID> gerarId =
        () -> UUID.randomUUID();

UUID id = gerarId.get();
```


**Resultado esperado:**

```text
Um UUID aleatório, como 550e8400-e29b-41d4-a716-446655440000
```

---

# 20. Streams API

Stream processa dados de forma declarativa.

```java
List<Integer> numeros =
        List.of(1, 2, 3, 4, 5, 6);

List<Integer> pares = numeros.stream()
        .filter(numero -> numero % 2 == 0)
        .toList();
```


**O que acontece:** `pares` recebe `[2, 4, 6]`.

## map

```java
List<String> maiusculos = nomes.stream()
        .map(String::toUpperCase)
        .toList();
```


**O que acontece:** cada nome é convertido para letras maiúsculas; por exemplo, `[ANA, BRUNO]`.

## filter

```java
List<Usuario> ativos = usuarios.stream()
        .filter(Usuario::isAtivo)
        .toList();
```


**O que acontece:** a nova lista contém somente usuários para os quais `isAtivo()` retorna `true`.

## sorted

```java
List<Usuario> ordenados = usuarios.stream()
        .sorted(Comparator.comparing(Usuario::getNome))
        .toList();
```


**O que acontece:** a nova lista contém os usuários ordenados pelo nome em ordem crescente.

## distinct

```java
List<Integer> unicos = numeros.stream()
        .distinct()
        .toList();
```


**O que acontece:** a nova lista mantém apenas a primeira ocorrência de cada número.

## skip e limit

```java
List<Integer> pagina = numeros.stream()
        .skip(10)  // Ignora os dez primeiros
        .limit(10) // Retorna os dez seguintes
        .toList();
```


**O que acontece:** com a lista de seis números usada anteriormente, o resultado é `[]`, pois `skip(10)` ignora todos os elementos.

## findFirst

```java
Optional<Usuario> primeiro = usuarios.stream()
        .filter(Usuario::isAtivo)
        .findFirst();
```


**O que acontece:** o `Optional` contém o primeiro usuário ativo; fica vazio quando não há usuário ativo.

## Match

```java
boolean algumAtivo = usuarios.stream()
        .anyMatch(Usuario::isAtivo);

boolean todosAtivos = usuarios.stream()
        .allMatch(Usuario::isAtivo);

boolean nenhumAtivo = usuarios.stream()
        .noneMatch(Usuario::isAtivo);
```


**O que acontece:** os três booleanos indicam, respectivamente, se existe algum ativo, se todos são ativos e se nenhum é ativo. Os valores dependem da lista.

## reduce

```java
int total = numeros.stream()
        .reduce(0, Integer::sum);
```


**O que acontece:** com `[1, 2, 3, 4, 5, 6]`, `total` recebe `21`.

## Agrupamento

```java
Map<StatusPedido, List<Pedido>> porStatus =
        pedidos.stream()
                .collect(
                    Collectors.groupingBy(Pedido::getStatus)
                );
```


**O que acontece:** é criado um `Map` em que cada status aponta para a lista de pedidos daquele grupo.

## Soma com BigDecimal

```java
BigDecimal total = pedidos.stream()
        .map(Pedido::getValor)
        .reduce(BigDecimal.ZERO, BigDecimal::add);
```


**O que acontece:** `total` recebe a soma exata dos valores de todos os pedidos.

## flatMap

```java
List<String> telefones = clientes.stream()
        .flatMap(cliente ->
                cliente.getTelefones().stream()
        )
        .toList();
```


**O que acontece:** todas as listas de telefones são achatadas em uma única `List<String>`.

## Stream paralelo

```java
numeros.parallelStream()
        .map(this::processar)
        .toList();
```


**O que acontece:** os números podem ser processados por várias threads. O resultado depende de `processar`, e efeitos colaterais podem ocorrer em ordem diferente.

Use com cuidado:

```text
- Nem sempre é mais rápido.
- Evite estado compartilhado.
- Avalie o custo da operação.
- Não use automaticamente.
```

---

# 21. BigDecimal

Use em valores monetários.

```java
BigDecimal preco = new BigDecimal("19.90");
BigDecimal quantidade = new BigDecimal("2");

BigDecimal total = preco.multiply(quantidade);
```


**O que acontece:** `total` recebe `39.80`.

Evite:

```java
// Pode carregar imprecisão do double
BigDecimal valor = new BigDecimal(0.1);
```


**O que acontece:** o objeto pode armazenar uma representação decimal extensa por herdar a imprecisão do `double`.

Prefira:

```java
BigDecimal valor1 = new BigDecimal("0.1");
BigDecimal valor2 = BigDecimal.valueOf(0.1);
```


**O que acontece:** os dois objetos representam o valor decimal `0.1` de forma adequada.

## Operações

```java
BigDecimal soma = valor1.add(valor2);
BigDecimal subtracao = valor1.subtract(valor2);
BigDecimal multiplicacao = valor1.multiply(valor2);

BigDecimal divisao = valor1.divide(
        valor2,
        2,
        RoundingMode.HALF_UP
);
```


**O que acontece:** considerando ambos como `0.1`: soma `0.2`, subtração `0.0`, multiplicação `0.01` e divisão `1.00`.

## Comparação

```java
BigDecimal saldo = new BigDecimal("100.00");
BigDecimal valor = new BigDecimal("50.00");

if (saldo.compareTo(valor) >= 0) {
    System.out.println("Saldo suficiente");
}
```


**Resultado:**

```text
Saldo suficiente
```

```text
compareTo retorna:
- valor negativo → menor
- zero           → igual
- valor positivo → maior
```

---

# 22. Datas e horários

Prefira a API `java.time`.

## LocalDate

```java
LocalDate hoje = LocalDate.now();
LocalDate nascimento = LocalDate.of(1996, 5, 10);

LocalDate amanha = hoje.plusDays(1);
LocalDate mesPassado = hoje.minusMonths(1);
```


**O que acontece:** `hoje` recebe a data atual; `amanha` fica um dia depois e `mesPassado`, um mês antes. Os valores variam conforme a execução.

## LocalTime

```java
LocalTime agora = LocalTime.now();
LocalTime inicio = LocalTime.of(9, 0);
```


**O que acontece:** `agora` recebe o horário atual e `inicio` recebe `09:00`.

## LocalDateTime

```java
// Data e horário sem informação de fuso
LocalDateTime dataHora = LocalDateTime.now();
```


**O que acontece:** `dataHora` recebe a data e o horário locais do momento da execução, sem armazenar fuso horário.

## ZonedDateTime

```java
ZonedDateTime maceio = ZonedDateTime.now(
        ZoneId.of("America/Maceio")
);
```


**O que acontece:** `maceio` recebe a data, o horário e o fuso de `America/Maceio` no momento da execução.

## Instant

```java
// Momento absoluto em UTC
Instant agora = Instant.now();
```


**O que acontece:** `agora` recebe um instante em UTC, como `2026-07-22T19:00:00Z`; o valor exato varia.

## Formatação

```java
DateTimeFormatter formato =
        DateTimeFormatter.ofPattern("dd/MM/yyyy");

String texto = hoje.format(formato);

LocalDate data = LocalDate.parse(
        "22/07/2026",
        formato
);
```


**O que acontece:** `texto` recebe a data atual em `dd/MM/yyyy`; `data` recebe `22 de julho de 2026`.

## Diferença

```java
Period periodo = Period.between(
        nascimento,
        hoje
);

System.out.println(periodo.getYears());
```


**O que acontece:** é calculada a diferença em anos, meses e dias entre o nascimento e hoje; o valor impresso depende da data atual.

```java
Duration duracao = Duration.between(
        LocalTime.of(9, 0),
        LocalTime.of(18, 0)
);

System.out.println(duracao.toHours());
```


**Resultado:**

```text
9
```

---

# 23. Arquivos e I/O

## Escrever

```java
Path caminho = Path.of("dados.txt");

Files.writeString(
        caminho,
        "Conteúdo do arquivo"
);
```


**O que acontece:** o arquivo `dados.txt` é criado ou sobrescrito com o texto `Conteúdo do arquivo`.

## Ler

```java
String conteudo =
        Files.readString(Path.of("dados.txt"));

System.out.println(conteudo);
```


**Resultado esperado:**

```text
Conteúdo do arquivo
```

## Todas as linhas

```java
List<String> linhas =
        Files.readAllLines(Path.of("dados.txt"));
```


**O que acontece:** `linhas` recebe uma lista em que cada elemento representa uma linha do arquivo.

## Linha por linha

```java
try (Stream<String> linhas =
             Files.lines(Path.of("dados.txt"))) {

    linhas.forEach(System.out::println);
}
```


**Resultado esperado:**

```text
Cada linha existente em dados.txt
```

**O que acontece:** o stream é fechado automaticamente.

---

# 24. Annotations

Annotations adicionam metadados ao código.

```java
@Override
public String toString() {
    return "Objeto";
}
```


**O que acontece:** ao chamar `objeto.toString()`, o método retorna `"Objeto"`.

## Annotation personalizada

```java
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
public @interface EntidadeAuditavel {

    String descricao() default "";
}
```


**O que acontece:** é criada uma annotation disponível em tempo de execução e aplicável a classes.

```java
@EntidadeAuditavel(
        descricao = "Registra alterações do usuário"
)
public class Usuario {
}
```


**O que acontece:** a classe `Usuario` recebe o metadado `descricao = "Registra alterações do usuário"`.

## Leitura por reflexão

```java
Class<Usuario> classe = Usuario.class;

EntidadeAuditavel annotation =
        classe.getAnnotation(EntidadeAuditavel.class);

System.out.println(annotation.descricao());
```


**Resultado:**

```text
Registra alterações do usuário
```

```text
SOURCE  → existe somente no código-fonte
CLASS   → permanece no bytecode
RUNTIME → pode ser lida durante a execução
```

## Annotation Processor

```text
- Executa durante a compilação.
- Pode validar código.
- Pode gerar classes.
- Exemplos: Lombok e MapStruct.
```

---

# 25. Threads e concorrência

## Thread

```java
Thread thread = new Thread(() -> {
    System.out.println("Outra thread");
});

thread.start();
```


**Resultado esperado:**

```text
Outra thread
```

**O que acontece:** a linha é executada pela nova thread; o momento exato em relação à thread principal pode variar.

## ExecutorService

```java
ExecutorService executor =
        Executors.newFixedThreadPool(3);

executor.submit(() ->
        System.out.println("Tarefa executada")
);

executor.shutdown();
```


**Resultado esperado:**

```text
Tarefa executada
```

## Callable e Future

```java
ExecutorService executor =
        Executors.newSingleThreadExecutor();

Future<Integer> future = executor.submit(() -> {
    return 10 + 20;
});

Integer resultado = future.get();

executor.shutdown();
```


**O que acontece:** `future.get()` aguarda a tarefa e `resultado` recebe `30`. Nenhum texto é impresso.

## CompletableFuture

```java
CompletableFuture<String> future =
        CompletableFuture.supplyAsync(() ->
                "Resultado"
        );

future.thenApply(String::toUpperCase)
      .thenAccept(System.out::println)
      .exceptionally(exception -> {
          exception.printStackTrace();
          return null;
      });
```


**Resultado esperado:**

```text
RESULTADO
```

## synchronized

```java
public synchronized void incrementar() {
    contador++;
}
```


**O que acontece:** somente uma thread por vez pode executar o método no mesmo objeto, reduzindo condições de corrida.

## AtomicInteger

```java
AtomicInteger contador =
        new AtomicInteger(0);

contador.incrementAndGet();
```


**O que acontece:** o incremento é atômico e o contador passa de `0` para `1`.

## Coleções concorrentes

```java
Map<Long, Usuario> usuarios =
        new ConcurrentHashMap<>();

Queue<String> fila =
        new ConcurrentLinkedQueue<>();
```


**O que acontece:** são criadas coleções vazias adequadas para acesso concorrente.

## Virtual Threads

```java
try (ExecutorService executor =
             Executors.newVirtualThreadPerTaskExecutor()) {

    executor.submit(() ->
            System.out.println(
                    Thread.currentThread()
            )
    );
}
```


**Resultado esperado:**

```text
Representação da virtual thread atual
```

**O que acontece:** o texto exato inclui identificadores definidos pela JVM.

Boas práticas:

```text
- Evite estado mutável compartilhado.
- Prefira objetos imutáveis.
- Use estruturas concorrentes.
- Trate timeout e cancelamento.
- Não crie threads manualmente sem necessidade.
```

---

# 26. JDBC

JDBC significa **Java Database Connectivity**.

É a API padrão do Java para comunicação com bancos relacionais.

```text
Aplicação Java
      ↓
API JDBC
      ↓
Driver JDBC
      ↓
Banco de dados
```

Exemplos de bancos usados com JDBC:

```text
MySQL
PostgreSQL
Oracle Database
SQL Server
MariaDB
H2
```

---

## 26.1 Principais responsabilidades do JDBC

```text
- Abrir conexões.
- Executar comandos SQL.
- Enviar parâmetros com segurança.
- Ler resultados.
- Controlar transações.
- Executar operações em lote.
- Chamar procedures e functions.
- Obter metadados do banco.
```

O JDBC não substitui o SQL.

```text
JDBC → comunicação Java com o banco
SQL  → linguagem usada pelo banco
```

---

## 26.2 Principais interfaces

```text
DriverManager       → cria conexões diretamente
DataSource          → fornece conexões e permite uso de pool
Connection          → representa uma conexão
Statement           → executa SQL simples
PreparedStatement   → executa SQL parametrizado
CallableStatement   → chama procedures e functions
ResultSet           → representa o resultado de uma consulta
Savepoint           → marca um ponto dentro da transação
DatabaseMetaData    → informações sobre o banco
ResultSetMetaData   → informações sobre as colunas retornadas
```

Importações principais:

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.CallableStatement;
import java.sql.Statement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Savepoint;
import java.sql.Types;
import javax.sql.DataSource;
```


**O que acontece:** as principais interfaces e classes JDBC ficam disponíveis para uso no arquivo. Importar não abre conexão nem executa SQL.

---

## 26.3 Driver JDBC

Cada banco possui seu próprio driver.

Para MySQL, utiliza-se o **MySQL Connector/J**.

### Maven

```xml
<dependency>
    <groupId>com.mysql</groupId>
    <artifactId>mysql-connector-j</artifactId>
    <version>VERSAO_ATUAL</version>
</dependency>
```


**O que acontece:** o Maven adiciona o driver JDBC do MySQL ao classpath do projeto.

### Gradle

```groovy
dependencies {
    implementation "com.mysql:mysql-connector-j:VERSAO_ATUAL"
}
```


**O que acontece:** o Gradle adiciona o driver JDBC do MySQL ao projeto.

Não fixe uma versão apresentada em material antigo.

Use uma versão estável compatível com:

```text
- A versão do Java do projeto.
- A versão do MySQL.
- O framework utilizado.
- As políticas de segurança do projeto.
```

Os drivers modernos são descobertos automaticamente.

```java
// Normalmente não é mais necessário:
Class.forName("com.mysql.cj.jdbc.Driver");
```


**O que acontece:** a linha carregaria o driver manualmente, mas normalmente é desnecessária em drivers JDBC modernos.

---

## 26.4 Connection String

Formato básico para MySQL:

```text
jdbc:mysql://HOST:PORTA/BANCO
```

Exemplo:

```text
jdbc:mysql://localhost:3306/sistema
```

Com parâmetros:

```text
jdbc:mysql://localhost:3306/sistema?useSSL=true&serverTimezone=UTC
```

Partes:

```text
jdbc:mysql  → protocolo e driver
localhost   → servidor
3306        → porta
sistema     → banco de dados
```

Não coloque usuário e senha diretamente no código.

```java
// Ruim: credenciais fixas
String usuario = "root";
String senha = "123456";
```


**O que acontece:** as credenciais ficam expostas no código-fonte e podem chegar ao repositório. O trecho funciona tecnicamente, mas não deve ser usado em uma aplicação real.

Prefira variáveis de ambiente ou gerenciadores de segredo:

```java
String url = System.getenv("DB_URL");
String usuario = System.getenv("DB_USER");
String senha = System.getenv("DB_PASSWORD");
```


**O que acontece:** as configurações são lidas do ambiente; nenhum segredo fica fixado no código.

---

## 26.5 Criando conexão com DriverManager

```java
String url = System.getenv("DB_URL");
String usuario = System.getenv("DB_USER");
String senha = System.getenv("DB_PASSWORD");

try (Connection connection =
             DriverManager.getConnection(
                     url,
                     usuario,
                     senha
             )) {

    System.out.println("Conexão aberta");

} catch (SQLException exception) {
    System.err.println(
            "Erro ao conectar: " + exception.getMessage()
    );
}
```


**Resultado esperado:**

```text
Conexão aberta
```

**O que acontece:** se a URL ou credenciais estiverem incorretas, será impressa a mensagem do `SQLException`.

O `try-with-resources` fecha a conexão automaticamente.

---

## 26.6 DriverManager versus DataSource

### DriverManager

```text
- Simples.
- Útil em exemplos e aplicações pequenas.
- Abre uma conexão diretamente.
```

### DataSource

```text
- Recomendado em aplicações reais.
- Pode trabalhar com pool de conexões.
- Facilita configuração e testes.
- Evita espalhar credenciais pelo código.
```

Exemplo:

```java
public class ConnectionFactory {

    private final DataSource dataSource;

    public ConnectionFactory(DataSource dataSource) {
        this.dataSource = dataSource;
    }

    public Connection getConnection()
            throws SQLException {

        return dataSource.getConnection();
    }
}
```


**O que acontece:** a fábrica centraliza a obtenção de conexões por meio do `DataSource`.

Uso:

```java
try (Connection connection =
             connectionFactory.getConnection()) {

    // Usa a conexão
}
```


**O que acontece:** uma conexão é obtida, usada dentro do bloco e fechada automaticamente ao final.

---

## 26.7 Pool de conexões

Abrir uma conexão física para cada operação é caro.

Um pool mantém conexões prontas para reutilização.

```text
Sem pool:
requisição → abre conexão → usa → fecha conexão física

Com pool:
requisição → pega conexão → usa → devolve ao pool
```

Bibliotecas comuns:

```text
HikariCP
Apache DBCP
Pool fornecido pelo servidor ou framework
```

Exemplo conceitual com HikariCP:

```java
HikariConfig config = new HikariConfig();

config.setJdbcUrl(System.getenv("DB_URL"));
config.setUsername(System.getenv("DB_USER"));
config.setPassword(System.getenv("DB_PASSWORD"));

// Limite de conexões simultâneas no pool
config.setMaximumPoolSize(10);

DataSource dataSource =
        new HikariDataSource(config);
```


**O que acontece:** é criado um `DataSource` com pool de até dez conexões. A URL, o usuário e a senha são lidos das variáveis de ambiente.

Ao fechar a conexão obtida do pool:

```java
connection.close();
```


**O que acontece:** em um pool, a conexão normalmente é devolvida para reutilização.

normalmente ela é devolvida ao pool, e não destruída fisicamente.

---

## 26.8 Connection

`Connection` representa uma sessão com o banco.

Operações importantes:

```java
connection.prepareStatement(sql);
connection.prepareCall(sql);

connection.setAutoCommit(false);
connection.commit();
connection.rollback();

connection.setTransactionIsolation(
        Connection.TRANSACTION_READ_COMMITTED
);

connection.isClosed();
connection.isValid(2);
connection.close();
```


**O que acontece:** o trecho lista operações disponíveis na conexão; nenhuma é executada neste exemplo isolado.

Evite manter uma conexão aberta por mais tempo que o necessário.

---

## 26.9 Statement, PreparedStatement e CallableStatement

### Statement

Executa SQL sem parâmetros.

```java
try (Statement statement =
             connection.createStatement()) {

    ResultSet resultSet =
            statement.executeQuery(
                    "SELECT id, nome FROM usuario"
            );
}
```


**O que acontece:** a consulta retorna um `ResultSet` com `id` e `nome` de todos os usuários; os dados dependem do banco.

Use apenas quando o SQL for completamente controlado pela aplicação.

### PreparedStatement

Executa SQL com parâmetros.

```java
String sql = """
        SELECT id, nome
        FROM usuario
        WHERE email = ?
        """;

try (PreparedStatement statement =
             connection.prepareStatement(sql)) {

    statement.setString(1, "usuario@email.com");
}
```


**O que acontece:** o valor do e-mail é enviado separadamente do SQL e usado para filtrar o resultado com segurança.

Vantagens:

```text
- Reduz risco de SQL Injection.
- Separa SQL dos valores.
- Faz conversão de tipos.
- Pode ser reutilizado.
- Pode melhorar a execução dependendo do banco e driver.
```

### CallableStatement

Chama procedures e functions.

```java
String sql = "{call atualizar_status(?, ?)}";

try (CallableStatement statement =
             connection.prepareCall(sql)) {

    statement.setLong(1, 10L);
    statement.setString(2, "PAGO");

    statement.execute();
}
```


**O que acontece:** a procedure é chamada com o ID `10` e o status `PAGO`. O registro alterado depende do banco.

---

## 26.10 executeQuery, executeUpdate e execute

### executeQuery

Usado quando existe um `ResultSet`.

```java
ResultSet resultSet =
        statement.executeQuery();
```


**O que acontece:** a consulta é executada e devolve um `ResultSet` para leitura.

Normalmente usado em:

```sql
SELECT
```


**Resultado esperado:**

```text
Linhas que atendem às condições da consulta
```

### executeUpdate

Retorna a quantidade de linhas afetadas.

```java
int linhasAfetadas =
        statement.executeUpdate();
```


**O que acontece:** a operação é executada e `linhasAfetadas` recebe a quantidade de registros alterados.

Normalmente usado em:

```sql
INSERT
UPDATE
DELETE
CREATE
ALTER
DROP
```


**O que acontece:** o comando é executado pelo banco; o efeito depende do schema e dos dados existentes.

### execute

Use quando o comando pode retornar tipos diferentes de resultado.

```java
boolean retornouResultSet =
        statement.execute();
```


**O que acontece:** o booleano recebe `true` quando o primeiro resultado é um `ResultSet`; caso contrário, recebe `false`.

```text
true  → existe ResultSet
false → existe contador de atualização ou nenhum resultado
```

---

## 26.11 Exemplo de tabela

```sql
CREATE TABLE usuario (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(150) NOT NULL,
    email VARCHAR(200) NOT NULL UNIQUE,
    ativo BOOLEAN NOT NULL DEFAULT TRUE,
    data_cadastro TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```


**O que acontece:** a tabela `usuario` é criada com chave primária automática, e-mail único e valores padrão para atividade e data de cadastro.

Conceitos SQL presentes:

```text
PRIMARY KEY    → identifica o registro
AUTO_INCREMENT → gera ID automaticamente no MySQL
NOT NULL       → valor obrigatório
UNIQUE         → impede duplicidade
DEFAULT        → valor padrão
```

---

## 26.12 Modelo Java

```java
public record Usuario(
        Long id,
        String nome,
        String email,
        boolean ativo,
        LocalDateTime dataCadastro
) {
}
```


**O que acontece:** é definido um modelo imutável para representar uma linha da tabela `usuario`.

---

## 26.13 INSERT

```java
String sql = """
        INSERT INTO usuario (
            nome,
            email,
            ativo
        )
        VALUES (?, ?, ?)
        """;

try (
    Connection connection =
            dataSource.getConnection();

    PreparedStatement statement =
            connection.prepareStatement(sql)
) {
    statement.setString(1, usuario.nome());
    statement.setString(2, usuario.email());
    statement.setBoolean(3, usuario.ativo());

    int linhasAfetadas =
            statement.executeUpdate();

    if (linhasAfetadas != 1) {
        throw new SQLException(
                "O usuário não foi inserido"
        );
    }
}
```


**O que acontece:** um usuário é inserido. Em caso normal, `linhasAfetadas` recebe `1`; caso contrário, a exceção é lançada.

---

## 26.14 INSERT retornando chave gerada

```java
String sql = """
        INSERT INTO usuario (
            nome,
            email,
            ativo
        )
        VALUES (?, ?, ?)
        """;

try (
    Connection connection =
            dataSource.getConnection();

    PreparedStatement statement =
            connection.prepareStatement(
                    sql,
                    Statement.RETURN_GENERATED_KEYS
            )
) {
    statement.setString(1, usuario.nome());
    statement.setString(2, usuario.email());
    statement.setBoolean(3, usuario.ativo());

    int linhasAfetadas =
            statement.executeUpdate();

    if (linhasAfetadas != 1) {
        throw new SQLException(
                "Falha ao inserir usuário"
        );
    }

    try (ResultSet chaves =
                 statement.getGeneratedKeys()) {

        if (chaves.next()) {
            long idGerado = chaves.getLong(1);

            System.out.println(
                    "ID gerado: " + idGerado
            );
        }
    }
}
```


**Resultado esperado:**

```text
ID gerado: <número>
```

**O que acontece:** o número depende do próximo valor `AUTO_INCREMENT` do banco.

---

## 26.15 SELECT por ID

```java
String sql = """
        SELECT
            id,
            nome,
            email,
            ativo,
            data_cadastro
        FROM usuario
        WHERE id = ?
        """;

try (
    Connection connection =
            dataSource.getConnection();

    PreparedStatement statement =
            connection.prepareStatement(sql)
) {
    statement.setLong(1, id);

    try (ResultSet resultSet =
                 statement.executeQuery()) {

        if (!resultSet.next()) {
            return Optional.empty();
        }

        Usuario usuario = mapearUsuario(resultSet);

        return Optional.of(usuario);
    }
}
```


**O que acontece:** retorna `Optional.empty()` quando o ID não existe; quando existe, retorna o usuário mapeado.

Método de mapeamento:

```java
private Usuario mapearUsuario(
        ResultSet resultSet
) throws SQLException {

    return new Usuario(
            resultSet.getLong("id"),
            resultSet.getString("nome"),
            resultSet.getString("email"),
            resultSet.getBoolean("ativo"),
            resultSet.getObject(
                    "data_cadastro",
                    LocalDateTime.class
            )
    );
}
```


**O que acontece:** a linha atual do `ResultSet` é convertida em um objeto `Usuario`.

---

## 26.16 SELECT de vários registros

```java
String sql = """
        SELECT
            id,
            nome,
            email,
            ativo,
            data_cadastro
        FROM usuario
        ORDER BY nome
        """;

List<Usuario> usuarios =
        new ArrayList<>();

try (
    Connection connection =
            dataSource.getConnection();

    PreparedStatement statement =
            connection.prepareStatement(sql);

    ResultSet resultSet =
            statement.executeQuery()
) {
    while (resultSet.next()) {
        usuarios.add(
                mapearUsuario(resultSet)
        );
    }
}

return usuarios;
```


**O que acontece:** todos os registros retornados são mapeados e adicionados à lista na ordem do nome.

---

## 26.17 UPDATE

```java
String sql = """
        UPDATE usuario
        SET
            nome = ?,
            email = ?,
            ativo = ?
        WHERE id = ?
        """;

try (
    Connection connection =
            dataSource.getConnection();

    PreparedStatement statement =
            connection.prepareStatement(sql)
) {
    statement.setString(1, usuario.nome());
    statement.setString(2, usuario.email());
    statement.setBoolean(3, usuario.ativo());
    statement.setLong(4, usuario.id());

    int linhasAfetadas =
            statement.executeUpdate();

    if (linhasAfetadas == 0) {
        throw new UsuarioNaoEncontradoException(
                "Usuário não encontrado"
        );
    }
}
```


**O que acontece:** o usuário é retornado quando existe; caso contrário, a exceção personalizada é lançada.

---

## 26.18 DELETE

```java
String sql = """
        DELETE FROM usuario
        WHERE id = ?
        """;

try (
    Connection connection =
            dataSource.getConnection();

    PreparedStatement statement =
            connection.prepareStatement(sql)
) {
    statement.setLong(1, id);

    int linhasAfetadas =
            statement.executeUpdate();

    boolean removido =
            linhasAfetadas > 0;
}
```


**O que acontece:** `removido` recebe `true` quando algum registro é apagado e `false` quando o ID não existe.

Em sistemas reais, pode ser melhor usar exclusão lógica:

```sql
UPDATE usuario
SET ativo = FALSE
WHERE id = ?;
```


**O que acontece:** o comando é executado pelo banco; o efeito depende do schema e dos dados existentes.

Isso preserva o histórico.

---

## 26.19 Índices dos parâmetros

Os parâmetros começam em `1`.

```java
statement.setString(1, nome);
statement.setString(2, email);
statement.setBoolean(3, ativo);
```


**O que acontece:** os três valores são associados aos placeholders `?` nas posições `1`, `2` e `3`.

Não começam em `0`.

```java
// Erro
statement.setString(0, nome);
```


**O que acontece:** a execução lança `SQLException`, pois os parâmetros JDBC começam na posição `1`.

---

## 26.20 Principais métodos set

```java
statement.setString(indice, texto);
statement.setInt(indice, numero);
statement.setLong(indice, numero);
statement.setDouble(indice, numero);
statement.setBigDecimal(indice, valor);
statement.setBoolean(indice, ativo);

statement.setDate(indice, sqlDate);
statement.setTime(indice, sqlTime);
statement.setTimestamp(indice, timestamp);

statement.setObject(indice, objeto);
statement.setNull(indice, Types.VARCHAR);
```


**O que acontece:** o método `set` adequado envia cada tipo Java ao parâmetro correspondente do SQL.

Com a API moderna de datas:

```java
statement.setObject(
        1,
        LocalDate.now()
);

statement.setObject(
        2,
        LocalDateTime.now()
);
```


**O que acontece:** a data e a data/hora modernas são enviadas ao driver, que as converte para tipos SQL compatíveis.

---

## 26.21 Principais métodos get

```java
String nome =
        resultSet.getString("nome");

int quantidade =
        resultSet.getInt("quantidade");

long id =
        resultSet.getLong("id");

BigDecimal valor =
        resultSet.getBigDecimal("valor");

boolean ativo =
        resultSet.getBoolean("ativo");

LocalDate data =
        resultSet.getObject(
                "data",
                LocalDate.class
        );

LocalDateTime dataHora =
        resultSet.getObject(
                "data_hora",
                LocalDateTime.class
        );
```


**O que acontece:** cada coluna da linha atual é lida e convertida para o tipo Java indicado.

Prefira acessar pelo nome da coluna:

```java
resultSet.getString("nome");
```


**O que acontece:** a coluna `nome` é lida pelo rótulo, o que torna o código mais legível.

em vez da posição:

```java
resultSet.getString(2);
```


**O que acontece:** a segunda coluna é lida pela posição; o código fica mais frágil se a ordem do `SELECT` mudar.

O nome é mais legível e menos frágil.

---

## 26.22 Mapeamento de tipos

| SQL | Java recomendado |
|---|---|
| `VARCHAR`, `CHAR`, `TEXT` | `String` |
| `INTEGER` | `Integer` ou `int` |
| `BIGINT` | `Long` ou `long` |
| `DECIMAL`, `NUMERIC` | `BigDecimal` |
| `BOOLEAN`, `BIT` | `Boolean` ou `boolean` |
| `DATE` | `LocalDate` |
| `TIME` | `LocalTime` |
| `TIMESTAMP` | `LocalDateTime` |
| Timestamp com fuso | `OffsetDateTime` |
| `BINARY`, `BLOB` | `byte[]`, `Blob` ou stream |
| `CLOB`, texto grande | `String`, `Clob` ou reader |

Evite `double` para dinheiro.

```java
BigDecimal valor =
        resultSet.getBigDecimal("valor");
```


**O que acontece:** o valor monetário é lido com precisão decimal, sem os erros comuns de `double`.

---

## 26.23 Valores nulos

Métodos de tipos primitivos podem devolver valores padrão.

```java
int quantidade =
        resultSet.getInt("quantidade");

// Pode ser necessário verificar se era NULL
if (resultSet.wasNull()) {
    System.out.println("Quantidade era nula");
}
```


**O que acontece:** quando a coluna SQL era `NULL`, a mensagem `Quantidade era nula` é exibida.

Alternativa moderna:

```java
Integer quantidade =
        resultSet.getObject(
                "quantidade",
                Integer.class
        );
```


**O que acontece:** `quantidade` recebe um `Integer` ou `null`, preservando corretamente a nulidade do banco.

Enviando `NULL`:

```java
if (telefone == null) {
    statement.setNull(
            1,
            Types.VARCHAR
    );
} else {
    statement.setString(
            1,
            telefone
    );
}
```


**O que acontece:** um `NULL` SQL é enviado quando `telefone` é nulo; caso contrário, o texto é enviado normalmente.

---

## 26.24 Alias em consultas

Use alias para evitar ambiguidades.

```sql
SELECT
    u.id AS usuario_id,
    u.nome AS usuario_nome,
    p.id AS pedido_id
FROM usuario u
JOIN pedido p
    ON p.usuario_id = u.id;
```


**Resultado esperado:**

```text
<id do pedido> | <valor> | <nome do usuário>
...
```

```java
long usuarioId =
        resultSet.getLong("usuario_id");

String usuarioNome =
        resultSet.getString("usuario_nome");
```


**O que acontece:** os valores são lidos pelos aliases, evitando conflito entre colunas com nomes iguais.

---

## 26.25 Relacionamentos e JOIN

Exemplo:

```sql
CREATE TABLE pedido (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    usuario_id BIGINT NOT NULL,
    valor DECIMAL(12, 2) NOT NULL,

    CONSTRAINT fk_pedido_usuario
        FOREIGN KEY (usuario_id)
        REFERENCES usuario(id)
);
```


**O que acontece:** a tabela `pedido` é criada com chave estrangeira para `usuario`.

Consulta:

```sql
SELECT
    p.id,
    p.valor,
    u.id AS usuario_id,
    u.nome AS usuario_nome
FROM pedido p
JOIN usuario u
    ON u.id = p.usuario_id
WHERE p.id = ?;
```


**Resultado esperado:**

```text
<id do pedido> | <valor> | <nome do usuário>
...
```

---

## 26.26 DAO e Repository

DAO significa **Data Access Object**.

Responsabilidade:

```text
- Executar SQL.
- Converter dados do banco em objetos.
- Persistir objetos.
- Isolar detalhes de acesso a dados.
```

Contrato:

```java
public interface UsuarioRepository {

    Usuario salvar(Usuario usuario);

    Optional<Usuario> buscarPorId(Long id);

    List<Usuario> buscarTodos();

    void atualizar(Usuario usuario);

    boolean remover(Long id);
}
```


**O que acontece:** é definido o contrato de persistência com operações de salvar, buscar, atualizar e remover.

Implementação JDBC:

```java
public class UsuarioRepositoryJdbc
        implements UsuarioRepository {

    private final DataSource dataSource;

    public UsuarioRepositoryJdbc(
            DataSource dataSource
    ) {
        this.dataSource = dataSource;
    }

    // Métodos JDBC ficam nesta classe
}
```


**O que acontece:** a implementação concreta recebe o `DataSource` e concentra nela os comandos JDBC.

O serviço não deve conhecer detalhes SQL:

```java
public class UsuarioService {

    private final UsuarioRepository repository;

    public UsuarioService(
            UsuarioRepository repository
    ) {
        this.repository = repository;
    }

    public Usuario cadastrar(
            NovoUsuario comando
    ) {
        Usuario usuario =
                validarECriar(comando);

        return repository.salvar(usuario);
    }
}
```


**O que acontece:** o serviço aplica a regra de negócio e delega a persistência ao repository, sem conhecer SQL.

---

## 26.27 SQLException

`SQLException` contém informações importantes.

```java
catch (SQLException exception) {

    System.err.println(
            "Mensagem: " + exception.getMessage()
    );

    System.err.println(
            "SQLState: " + exception.getSQLState()
    );

    System.err.println(
            "Código do fornecedor: "
                    + exception.getErrorCode()
    );

    throw new PersistenciaException(
            "Falha ao acessar o banco",
            exception
    );
}
```


**O que acontece:** são registrados mensagem, SQLState e código do fornecedor; depois, o erro é encapsulado em `PersistenciaException`.

Exceção de aplicação:

```java
public class PersistenciaException
        extends RuntimeException {

    public PersistenciaException(
            String mensagem,
            Throwable causa
    ) {
        super(mensagem, causa);
    }
}
```


**O que acontece:** é criada uma exceção de aplicação que mantém a causa original do erro JDBC.

Não revele detalhes internos do banco para o usuário final.

---

## 26.28 SQL Injection

Código vulnerável:

```java
String sql = """
        SELECT *
        FROM usuario
        WHERE email = '""" + email + "'";
```


**O que acontece:** o SQL é montado com entrada do usuário e fica vulnerável a SQL Injection. Este exemplo não deve ser usado.

Entrada maliciosa pode alterar a consulta.

Código correto:

```java
String sql = """
        SELECT *
        FROM usuario
        WHERE email = ?
        """;

try (PreparedStatement statement =
             connection.prepareStatement(sql)) {

    statement.setString(1, email);
}
```


**O que acontece:** o valor do e-mail é enviado separadamente do SQL e usado para filtrar o resultado com segurança.

Importante:

`PreparedStatement` protege valores.

Ele não parametriza nomes de tabela, coluna ou direção de ordenação.

```java
// Isto não funciona como nome de coluna
SELECT * FROM usuario ORDER BY ?
```


**O que acontece:** o placeholder seria tratado como um valor, não como nome de coluna; portanto, não resolve ordenação dinâmica.

Para partes estruturais, use uma lista permitida:

```java
String colunaOrdenacao = switch (ordenacao) {
    case NOME -> "nome";
    case DATA_CADASTRO -> "data_cadastro";
};

String sql = """
        SELECT id, nome
        FROM usuario
        ORDER BY %s
        """.formatted(colunaOrdenacao);
```


**O que acontece:** somente colunas previamente autorizadas podem entrar no SQL final.

---

## 26.29 Transações

Uma transação agrupa operações que devem funcionar como uma unidade.

```text
Tudo funciona → COMMIT
Algo falha    → ROLLBACK
```

Exemplo: transferência bancária.

```java
try (Connection connection =
             dataSource.getConnection()) {

    try {
        // Desativa o commit automático
        connection.setAutoCommit(false);

        debitar(connection, contaOrigem, valor);
        creditar(connection, contaDestino, valor);

        // Confirma todas as operações
        connection.commit();

    } catch (Exception exception) {

        // Desfaz todas as operações
        connection.rollback();

        throw exception;

    } finally {

        // Importante ao usar pool
        connection.setAutoCommit(true);
    }
}
```


**O que acontece:** se débito e crédito funcionarem, ocorre `commit`; se qualquer etapa falhar, ocorre `rollback`.

Todas as operações da mesma transação precisam usar a mesma `Connection`.

```java
debitar(connection, origem, valor);
creditar(connection, destino, valor);
```


**O que acontece:** os dois métodos recebem a mesma conexão e participam da mesma transação.

Não abra uma nova conexão dentro de cada método transacional.

---

## 26.30 Auto-commit

Por padrão, uma nova conexão normalmente trabalha com auto-commit.

```java
connection.getAutoCommit();
```


**O que acontece:** retorna `true` ou `false` conforme o modo atual da conexão.

Com auto-commit:

```text
Cada comando concluído é confirmado separadamente.
```

Para uma transação manual:

```java
connection.setAutoCommit(false);
```


**O que acontece:** os próximos comandos deixam de ser confirmados automaticamente.

Depois:

```java
connection.commit();
```


**O que acontece:** todas as alterações pendentes da transação são confirmadas.

ou:

```java
connection.rollback();
```


**O que acontece:** todas as alterações pendentes da transação são desfeitas.

---

## 26.31 Savepoint

Savepoint cria um ponto intermediário na transação.

```java
try (Connection connection =
             dataSource.getConnection()) {

    connection.setAutoCommit(false);

    atualizarPedido(connection);

    Savepoint depoisDoPedido =
            connection.setSavepoint(
                    "depois_do_pedido"
            );

    try {
        atualizarEstoque(connection);

    } catch (SQLException exception) {

        // Desfaz somente até o savepoint
        connection.rollback(
                depoisDoPedido
        );
    }

    connection.commit();
}
```


**O que acontece:** se a atualização de estoque falhar, somente as alterações posteriores ao savepoint são desfeitas; a atualização do pedido pode ser mantida.

Liberando:

```java
connection.releaseSavepoint(
        depoisDoPedido
);
```


**O que acontece:** o savepoint é liberado e não pode mais ser usado para rollback parcial.

---

## 26.32 Níveis de isolamento

Controlam como transações simultâneas enxergam alterações.

```java
connection.setTransactionIsolation(
        Connection.TRANSACTION_READ_COMMITTED
);
```


**O que acontece:** a conexão passa a usar o nível `READ_COMMITTED`, impedindo leitura de dados ainda não confirmados por outras transações.

Níveis:

```text
TRANSACTION_READ_UNCOMMITTED
TRANSACTION_READ_COMMITTED
TRANSACTION_REPEATABLE_READ
TRANSACTION_SERIALIZABLE
```

Problemas possíveis:

```text
Dirty Read
Non-repeatable Read
Phantom Read
```

Regra prática:

```text
Maior isolamento:
+ mais consistência
- menor concorrência
- maior possibilidade de bloqueio
```

Não escolha um nível sem considerar o comportamento do banco.

---

## 26.33 Batch Processing

Batch envia várias operações em conjunto.

```java
String sql = """
        INSERT INTO usuario (
            nome,
            email,
            ativo
        )
        VALUES (?, ?, ?)
        """;

try (
    Connection connection =
            dataSource.getConnection();

    PreparedStatement statement =
            connection.prepareStatement(sql)
) {
    connection.setAutoCommit(false);

    try {
        for (Usuario usuario : usuarios) {
            statement.setString(
                    1,
                    usuario.nome()
            );

            statement.setString(
                    2,
                    usuario.email()
            );

            statement.setBoolean(
                    3,
                    usuario.ativo()
            );

            statement.addBatch();
        }

        int[] resultados =
                statement.executeBatch();

        connection.commit();

    } catch (SQLException exception) {
        connection.rollback();
        throw exception;
    }
}
```


**O que acontece:** todos os usuários são adicionados ao lote, executados em conjunto e confirmados com `commit`; falhas provocam `rollback`.

Métodos:

```text
addBatch()     → adiciona comando ao lote
executeBatch() → executa o lote
clearBatch()   → limpa o lote
```

Em lotes muito grandes, execute em blocos:

```java
int tamanhoLote = 500;
int contador = 0;

for (Usuario usuario : usuarios) {

    preencherStatement(statement, usuario);
    statement.addBatch();
    contador++;

    if (contador % tamanhoLote == 0) {
        statement.executeBatch();
        statement.clearBatch();
    }
}

// Executa o restante
statement.executeBatch();
```


**O que acontece:** o lote é enviado a cada 500 registros e, ao final, o restante também é executado.

---

## 26.34 Paginação

Exemplo no MySQL:

```sql
SELECT
    id,
    nome,
    email
FROM usuario
ORDER BY id
LIMIT ? OFFSET ?;
```


**O que acontece:** retorna uma página de usuários conforme o limite e o deslocamento enviados pelo Java.

```java
int tamanhoPagina = 20;
int pagina = 3;

int offset =
        pagina * tamanhoPagina;

statement.setInt(1, tamanhoPagina);
statement.setInt(2, offset);
```


**O que acontece:** para `pagina = 3`, `offset` recebe `60`; a consulta ignora 60 linhas e retorna até 20.

Para grandes volumes, paginação por cursor pode ser mais eficiente:

```sql
SELECT
    id,
    nome,
    email
FROM usuario
WHERE id > ?
ORDER BY id
LIMIT ?;
```


**O que acontece:** retorna os próximos registros após o último ID conhecido, técnica de paginação por cursor.

---

## 26.35 Limite e timeout

Limitar resultados:

```java
statement.setMaxRows(100);
```


**O que acontece:** o driver limita o resultado a no máximo 100 linhas.

Timeout da consulta:

```java
// Tempo em segundos
statement.setQueryTimeout(10);
```


**O que acontece:** a consulta poderá ser cancelada se ultrapassar aproximadamente dez segundos, conforme suporte do driver.

Timeout de rede e conexão dependem do driver, `DataSource` e pool.

Não deixe consultas lentas executarem indefinidamente.

---

## 26.36 ResultSet

O cursor começa antes da primeira linha.

```java
while (resultSet.next()) {
    // Agora o cursor está em uma linha válida
}
```


**O que acontece:** o laço avança linha por linha até não haver mais registros.

Por padrão, geralmente é:

```text
Somente leitura
Movimento para frente
```

Nunca use o `ResultSet` depois de fechar o `Statement` ou a conexão.

```java
try (
    PreparedStatement statement =
            connection.prepareStatement(sql);

    ResultSet resultSet =
            statement.executeQuery()
) {
    // Consumir aqui
}
```


**O que acontece:** o `ResultSet` deve ser totalmente consumido dentro do bloco, antes do fechamento dos recursos.

---

## 26.37 ResultSetMetaData

Permite inspecionar as colunas retornadas.

```java
ResultSetMetaData metadata =
        resultSet.getMetaData();

int quantidadeColunas =
        metadata.getColumnCount();

for (int i = 1;
     i <= quantidadeColunas;
     i++) {

    System.out.println(
            metadata.getColumnLabel(i)
    );

    System.out.println(
            metadata.getColumnTypeName(i)
    );
}
```


**Resultado esperado:**

```text
<nome da coluna>
<tipo SQL>
...
```

**O que acontece:** uma dupla de linhas é impressa para cada coluna retornada.

---

## 26.38 DatabaseMetaData

Obtém informações sobre o banco e o driver.

```java
DatabaseMetaData metadata =
        connection.getMetaData();

System.out.println(
        metadata.getDatabaseProductName()
);

System.out.println(
        metadata.getDatabaseProductVersion()
);

System.out.println(
        metadata.getDriverName()
);

System.out.println(
        metadata.supportsTransactions()
);
```


**Resultado esperado:**

```text
<nome do banco>
<versão do banco>
<nome do driver>
true ou false
```

Consultando tabelas:

```java
try (ResultSet tabelas =
             metadata.getTables(
                     null,
                     null,
                     "%",
                     new String[]{"TABLE"}
             )) {

    while (tabelas.next()) {
        System.out.println(
                tabelas.getString(
                        "TABLE_NAME"
                )
        );
    }
}
```


**Resultado esperado:**

```text
<nome de cada tabela>
```

---

## 26.39 Stored Procedure

Procedure executa um conjunto de comandos no banco.

Exemplo MySQL:

```sql
DELIMITER //

CREATE PROCEDURE atualizar_status_pedido(
    IN pedido_id BIGINT,
    IN novo_status VARCHAR(30)
)
BEGIN
    UPDATE pedido
    SET status = novo_status
    WHERE id = pedido_id;
END //

DELIMITER ;
```


**O que acontece:** a procedure é criada e, quando chamada, atualiza o status do pedido informado.

Chamada com JDBC:

```java
String sql =
        "{call atualizar_status_pedido(?, ?)}";

try (
    Connection connection =
            dataSource.getConnection();

    CallableStatement statement =
            connection.prepareCall(sql)
) {
    statement.setLong(1, pedidoId);
    statement.setString(2, novoStatus);

    statement.execute();
}
```


**O que acontece:** a procedure é chamada com o ID `10` e o status `PAGO`. O registro alterado depende do banco.

---

## 26.40 Procedure com parâmetro OUT

SQL:

```sql
DELIMITER //

CREATE PROCEDURE contar_usuarios_ativos(
    OUT total_ativos INT
)
BEGIN
    SELECT COUNT(*)
    INTO total_ativos
    FROM usuario
    WHERE ativo = TRUE;
END //

DELIMITER ;
```


**O que acontece:** a procedure é criada com um parâmetro de saída que recebe a quantidade de usuários ativos.

Java:

```java
String sql =
        "{call contar_usuarios_ativos(?)}";

try (
    Connection connection =
            dataSource.getConnection();

    CallableStatement statement =
            connection.prepareCall(sql)
) {
    statement.registerOutParameter(
            1,
            Types.INTEGER
    );

    statement.execute();

    int total =
            statement.getInt(1);
}
```


**O que acontece:** a procedure preenche o parâmetro de saída e `total` recebe a quantidade de usuários ativos.

---

## 26.41 Stored Function

Function retorna um valor.

SQL:

```sql
DELIMITER //

CREATE FUNCTION calcular_desconto(
    valor DECIMAL(12, 2),
    percentual DECIMAL(5, 2)
)
RETURNS DECIMAL(12, 2)
DETERMINISTIC
RETURN valor * percentual / 100 //

DELIMITER ;
```


**O que acontece:** a function é criada e retorna `valor × percentual ÷ 100`.

Java:

```java
String sql =
        "{? = call calcular_desconto(?, ?)}";

try (
    Connection connection =
            dataSource.getConnection();

    CallableStatement statement =
            connection.prepareCall(sql)
) {
    // Primeiro parâmetro recebe o retorno
    statement.registerOutParameter(
            1,
            Types.DECIMAL
    );

    statement.setBigDecimal(
            2,
            valor
    );

    statement.setBigDecimal(
            3,
            percentual
    );

    statement.execute();

    BigDecimal desconto =
            statement.getBigDecimal(1);
}
```


**O que acontece:** `desconto` recebe o valor calculado pela function, conforme os argumentos enviados.

---

## 26.42 Triggers

Trigger é executado automaticamente pelo banco após ou antes de um evento.

Exemplo de auditoria:

```sql
CREATE TABLE auditoria_usuario (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    usuario_id BIGINT NOT NULL,
    operacao VARCHAR(20) NOT NULL,
    data_operacao TIMESTAMP NOT NULL
        DEFAULT CURRENT_TIMESTAMP
);
```


**O que acontece:** a tabela de auditoria é criada para registrar operações realizadas em usuários.

```sql
DELIMITER //

CREATE TRIGGER trg_usuario_atualizado
AFTER UPDATE ON usuario
FOR EACH ROW
BEGIN
    INSERT INTO auditoria_usuario (
        usuario_id,
        operacao
    )
    VALUES (
        NEW.id,
        'UPDATE'
    );
END //

DELIMITER ;
```


**O que acontece:** o trigger é criado; cada `UPDATE` em `usuario` insere automaticamente uma linha de auditoria.

A aplicação não chama o trigger diretamente.

```text
Aplicação executa UPDATE
           ↓
Banco dispara o trigger
           ↓
Auditoria é registrada
```

Cuidados:

```text
- Triggers criam comportamento implícito.
- Documente claramente.
- Versione com migrations.
- Evite regras complexas escondidas.
- Considere impacto em performance.
```

---

## 26.43 BLOB e arquivos binários

Gravando:

```java
String sql = """
        INSERT INTO documento (
            nome,
            conteudo
        )
        VALUES (?, ?)
        """;

try (
    InputStream input =
            Files.newInputStream(caminho);

    PreparedStatement statement =
            connection.prepareStatement(sql)
) {
    statement.setString(
            1,
            caminho.getFileName().toString()
    );

    statement.setBinaryStream(
            2,
            input
    );

    statement.executeUpdate();
}
```


**O que acontece:** o arquivo é enviado como fluxo binário e salvo na coluna `conteudo`.

Lendo:

```java
try (InputStream input =
             resultSet.getBinaryStream(
                     "conteudo"
             )) {

    Files.copy(
            input,
            arquivoDestino
    );
}
```


**O que acontece:** o conteúdo binário é lido do banco e copiado para o arquivo de destino.

Avalie se o arquivo deve ficar no banco ou em armazenamento externo.

---

## 26.44 Consultas dinâmicas

Monte apenas os trechos necessários.

```java
StringBuilder sql = new StringBuilder("""
        SELECT id, nome, email
        FROM usuario
        WHERE 1 = 1
        """);

List<Object> parametros =
        new ArrayList<>();

if (nome != null && !nome.isBlank()) {
    sql.append(" AND nome LIKE ?");
    parametros.add("%" + nome + "%");
}

if (ativo != null) {
    sql.append(" AND ativo = ?");
    parametros.add(ativo);
}
```


**O que acontece:** as cláusulas são adicionadas somente quando os filtros correspondentes foram informados; os valores ficam em uma lista separada.

Preenchimento:

```java
try (PreparedStatement statement =
             connection.prepareStatement(
                     sql.toString()
             )) {

    for (int i = 0;
         i < parametros.size();
         i++) {

        statement.setObject(
                i + 1,
                parametros.get(i)
        );
    }
}
```


**O que acontece:** cada filtro é associado ao `PreparedStatement` na mesma ordem dos placeholders adicionados.

Não concatene os valores diretamente.

---

## 26.45 Flyway

Flyway controla a evolução do banco com migrations.

Estrutura comum:

```text
src/main/resources/db/migration/
├── V1__criar_tabela_usuario.sql
├── V2__criar_tabela_pedido.sql
├── V3__adicionar_status_pedido.sql
└── R__atualizar_views.sql
```

Convenção:

```text
V1__descricao.sql → migration versionada
R__descricao.sql  → migration repetível
```

Exemplo:

```sql
-- V1__criar_tabela_usuario.sql

CREATE TABLE usuario (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(150) NOT NULL,
    email VARCHAR(200) NOT NULL UNIQUE
);
```


**O que acontece:** a tabela `usuario` é criada com chave primária automática, e-mail único e valores padrão para atividade e data de cadastro.

Princípios:

```text
- Migrations ficam no controle de versão.
- Cada alteração recebe uma nova migration.
- Não altere uma migration já executada em produção.
- Use uma nova migration para corrigir o schema.
- Valide migrations no pipeline.
```

Comandos comuns:

```bash
flyway info
flyway validate
flyway migrate
```


**O que acontece:** o Flyway mostra o histórico, valida os arquivos e aplica as migrations pendentes.

A tabela de histórico registra migrations aplicadas.

---

## 26.46 Liquibase

Liquibase organiza alterações em changelogs e changesets.

Exemplo YAML:

```yaml
databaseChangeLog:
  - changeSet:
      id: 001-criar-usuario
      author: equipe
      changes:
        - createTable:
            tableName: usuario
            columns:
              - column:
                  name: id
                  type: BIGINT
                  autoIncrement: true
                  constraints:
                    primaryKey: true
                    nullable: false
              - column:
                  name: nome
                  type: VARCHAR(150)
                  constraints:
                    nullable: false
      rollback:
        - dropTable:
            tableName: usuario
```


**O que acontece:** o Liquibase cria a tabela `usuario`; o bloco de rollback define como removê-la.

Conceitos:

```text
changelog  → arquivo principal de alterações
changeset  → unidade individual de mudança
rollback   → operação inversa
context    → restringe execução por ambiente
label      → organiza e seleciona mudanças
```

Comandos comuns:

```bash
liquibase status
liquibase validate
liquibase update
liquibase rollback TAG
```


**O que acontece:** o Liquibase mostra alterações pendentes, valida o changelog, aplica updates e executa rollback até a tag informada.

Não use Flyway e Liquibase juntos no mesmo projeto sem uma estratégia muito clara.

---

## 26.47 Flyway versus Liquibase

| Flyway | Liquibase |
|---|---|
| Foco simples em migrations | Changelogs estruturados |
| Muito usado com SQL puro | XML, YAML, JSON e SQL |
| Convenção de nomes | Changesets identificados |
| Curva inicial menor | Mais recursos declarativos |
| Rollback depende da estratégia e edição | Suporte explícito a rollback |

Escolha de acordo com o projeto.

```text
Flyway:
- simples
- direto
- SQL-first

Liquibase:
- declarativo
- mais controle
- rollback estruturado
```

---

## 26.48 Datafaker

Datafaker gera dados fictícios para testes e desenvolvimento.

Dependência conceitual:

```xml
<dependency>
    <groupId>net.datafaker</groupId>
    <artifactId>datafaker</artifactId>
    <version>VERSAO_ATUAL</version>
    <scope>test</scope>
</dependency>
```


**O que acontece:** o Maven adiciona o Datafaker para gerar dados fictícios durante os testes.

Uso:

```java
Faker faker =
        new Faker(
                new Locale("pt", "BR")
        );

String nome =
        faker.name().fullName();

String email =
        faker.internet().emailAddress();
```


**Resultado esperado:**

```text
Nome e e-mail fictícios diferentes a cada execução
```

Gerando objetos:

```java
List<Usuario> usuarios =
        IntStream.range(0, 100)
                .mapToObj(indice ->
                        new Usuario(
                                null,
                                faker.name()
                                     .fullName(),
                                faker.internet()
                                     .emailAddress(),
                                true,
                                LocalDateTime.now()
                        )
                )
                .toList();
```


**O que acontece:** é criada uma lista com 100 usuários fictícios, pronta para ser persistida em batch.

Depois, use batch para persistir.

Não use dados fictícios como se fossem dados reais de produção.

---

## 26.49 Testes de integração

Teste de integração deve validar o comportamento real do banco.

```text
Teste unitário:
- não precisa de banco
- testa regra isolada

Teste de integração:
- usa banco
- executa SQL real
- valida mapeamento e transação
```

Estratégia moderna:

```text
- Banco descartável para cada suíte.
- Migrations executadas antes do teste.
- Dados controlados.
- Limpeza ou recriação entre testes.
```

Testcontainers pode subir um banco real em contêiner durante os testes.

Exemplo conceitual:

```java
@Container
static MySQLContainer<?> mysql =
        new MySQLContainer<>(
                "mysql:VERSAO_COMPATIVEL"
        );
```


**O que acontece:** o teste inicia um contêiner MySQL descartável compatível com a versão definida.

Evite depender de um banco compartilhado por toda a equipe.

---

## 26.50 Padrão de teste de repository

```java
@Test
void deveSalvarEBuscarUsuario() {

    // Arrange
    Usuario usuario = new Usuario(
            null,
            "Gabriel",
            "gabriel@email.com",
            true,
            LocalDateTime.now()
    );

    // Act
    Usuario salvo =
            repository.salvar(usuario);

    Optional<Usuario> encontrado =
            repository.buscarPorId(
                    salvo.id()
            );

    // Assert
    assertTrue(encontrado.isPresent());

    assertEquals(
            "Gabriel",
            encontrado.orElseThrow().nome()
    );
}
```


**Resultado esperado:**

```text
Teste aprovado
```

**O que acontece:** isso ocorre quando o usuário salvo pode ser localizado e possui o nome esperado.

---

## 26.51 Arquitetura recomendada

```text
Controller / Resource
        ↓
Service
        ↓
Repository
        ↓
JDBC
        ↓
Banco
```

Responsabilidades:

```text
Controller → entrada e saída
Service    → regras de negócio
Repository → acesso aos dados
Banco      → persistência e integridade
```

Evite:

```text
- SQL dentro do controller.
- Regra de negócio dentro do repository.
- Connection espalhada pela aplicação.
- Credenciais dentro das classes.
```

---

## 26.52 JDBC puro versus ORM

### JDBC puro

```text
+ Controle total do SQL
+ Menos abstração
+ Bom para aprender persistência
+ Bom para consultas específicas

- Mais código manual
- Mapeamento manual
- Gerenciamento manual de operações
```

### ORM

Exemplos:

```text
JPA
Hibernate
EclipseLink
```

```text
+ Automatiza mapeamentos
+ Reduz CRUD repetitivo
+ Gerencia entidades

- Pode esconder SQL
- Exige conhecimento de persistência
- Pode gerar problemas de performance
```

Mesmo usando ORM, conhecer JDBC e SQL continua sendo essencial.

---

## 26.53 Checklist de segurança

```text
- Usar PreparedStatement.
- Não concatenar entrada do usuário no SQL.
- Não registrar senhas em logs.
- Usar usuário de banco com menor privilégio.
- Guardar credenciais fora do código.
- Usar conexão segura quando necessária.
- Atualizar o driver JDBC.
- Definir timeout.
- Limitar tamanho dos resultados.
- Validar uploads e BLOBs.
- Tratar mensagens de erro.
```

---

## 26.54 Checklist de performance

```text
- Usar pool de conexões.
- Fechar Connection, Statement e ResultSet.
- Criar índices adequados.
- Evitar SELECT *.
- Buscar somente as colunas necessárias.
- Usar batch em operações massivas.
- Paginar resultados.
- Analisar consultas lentas.
- Evitar N+1 consultas.
- Definir tamanho adequado do pool.
- Não manter transações abertas.
```

Exemplo ruim:

```java
for (Pedido pedido : pedidos) {
    // Uma consulta para cada pedido
    buscarUsuario(pedido.usuarioId());
}
```


**O que acontece:** uma consulta é executada para cada pedido, caracterizando o problema de N+1 consultas.

Melhor:

```sql
SELECT
    p.id,
    p.valor,
    u.nome
FROM pedido p
JOIN usuario u
    ON u.id = p.usuario_id;
```


**Resultado esperado:**

```text
<id do pedido> | <valor> | <nome do usuário>
...
```

---

## 26.55 Erros comuns

```text
1. Não fechar recursos.
2. Concatenar SQL.
3. Usar double para dinheiro.
4. Fazer commit antes de todas as operações.
5. Abrir conexão dentro de cada método transacional.
6. Retornar ResultSet para outras camadas.
7. Misturar SQL e regra de negócio.
8. Alterar migration já executada.
9. Deixar transações abertas.
10. Usar SELECT * sem necessidade.
11. Ignorar índices.
12. Não tratar valores NULL.
13. Fixar credenciais no código.
14. Não configurar timeout.
15. Criar um pool grande demais.
```

---

## 26.56 Exemplo completo de Repository

```java
public class UsuarioRepositoryJdbc
        implements UsuarioRepository {

    private final DataSource dataSource;

    public UsuarioRepositoryJdbc(
            DataSource dataSource
    ) {
        this.dataSource = dataSource;
    }

    @Override
    public Usuario salvar(
            Usuario usuario
    ) {
        String sql = """
                INSERT INTO usuario (
                    nome,
                    email,
                    ativo
                )
                VALUES (?, ?, ?)
                """;

        try (
            Connection connection =
                    dataSource.getConnection();

            PreparedStatement statement =
                    connection.prepareStatement(
                            sql,
                            Statement.RETURN_GENERATED_KEYS
                    )
        ) {
            statement.setString(
                    1,
                    usuario.nome()
            );

            statement.setString(
                    2,
                    usuario.email()
            );

            statement.setBoolean(
                    3,
                    usuario.ativo()
            );

            int linhas =
                    statement.executeUpdate();

            if (linhas != 1) {
                throw new SQLException(
                        "Quantidade inesperada: "
                                + linhas
                );
            }

            try (ResultSet chaves =
                         statement.getGeneratedKeys()) {

                if (!chaves.next()) {
                    throw new SQLException(
                            "ID não retornado"
                    );
                }

                return new Usuario(
                        chaves.getLong(1),
                        usuario.nome(),
                        usuario.email(),
                        usuario.ativo(),
                        usuario.dataCadastro()
                );
            }

        } catch (SQLException exception) {
            throw new PersistenciaException(
                    "Falha ao salvar usuário",
                    exception
            );
        }
    }

    @Override
    public Optional<Usuario> buscarPorId(
            Long id
    ) {
        String sql = """
                SELECT
                    id,
                    nome,
                    email,
                    ativo,
                    data_cadastro
                FROM usuario
                WHERE id = ?
                """;

        try (
            Connection connection =
                    dataSource.getConnection();

            PreparedStatement statement =
                    connection.prepareStatement(sql)
        ) {
            statement.setLong(1, id);

            try (ResultSet resultSet =
                         statement.executeQuery()) {

                if (!resultSet.next()) {
                    return Optional.empty();
                }

                return Optional.of(
                        mapear(resultSet)
                );
            }

        } catch (SQLException exception) {
            throw new PersistenciaException(
                    "Falha ao buscar usuário",
                    exception
            );
        }
    }

    private Usuario mapear(
            ResultSet resultSet
    ) throws SQLException {

        return new Usuario(
                resultSet.getLong("id"),
                resultSet.getString("nome"),
                resultSet.getString("email"),
                resultSet.getBoolean("ativo"),
                resultSet.getObject(
                        "data_cadastro",
                        LocalDateTime.class
                )
        );
    }
}
```


**Resultado esperado:**

```text
ID gerado: <número>
```

**O que acontece:** o número depende do próximo valor `AUTO_INCREMENT` do banco.

---

## 26.57 Resumo mental do JDBC

```text
1. Obter uma Connection.
2. Definir o SQL.
3. Criar PreparedStatement.
4. Preencher os parâmetros.
5. Executar.
6. Ler o ResultSet, quando houver.
7. Mapear para objetos.
8. Confirmar ou desfazer a transação.
9. Fechar os recursos.
10. Traduzir erros de persistência.
```

Fluxo de consulta:

```text
Connection
    ↓
PreparedStatement
    ↓
executeQuery()
    ↓
ResultSet
    ↓
Objeto Java
```

Fluxo de alteração:

```text
Connection
    ↓
PreparedStatement
    ↓
executeUpdate()
    ↓
Quantidade de linhas afetadas
```

Fluxo transacional:

```text
setAutoCommit(false)
        ↓
Operação 1
        ↓
Operação 2
        ↓
commit() ou rollback()
```

---
# 27. Maven e Gradle

## Maven

Arquivo principal:

```text
pom.xml
```

Dependência:

```xml
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>VERSAO_ATUAL</version>
    <scope>test</scope>
</dependency>
```


**O que acontece:** o Maven adiciona o JUnit Jupiter somente ao classpath de testes.

Comandos:

```bash
mvn clean
mvn compile
mvn test
mvn package
mvn install
```


**O que acontece:** os comandos limpam, compilam, testam, empacotam e instalam o projeto Maven, respectivamente.

Estrutura:

```text
src/
├── main/
│   ├── java/
│   └── resources/
└── test/
    ├── java/
    └── resources/
```

## Gradle

Arquivo principal:

```text
build.gradle
```

Dependência:

```groovy
dependencies {
    testImplementation 'org.junit.jupiter:junit-jupiter:VERSAO_ATUAL'
}
```


**O que acontece:** o Gradle adiciona o JUnit Jupiter às dependências de teste.

Comandos:

```bash
./gradlew clean
./gradlew build
./gradlew test
```


**O que acontece:** os comandos limpam, constroem e testam o projeto Gradle, respectivamente.

---

# 28. Testes com JUnit

```java
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class CalculadoraTest {

    @Test
    void deveSomarDoisNumeros() {

        // Arrange
        Calculadora calculadora =
                new Calculadora();

        // Act
        int resultado =
                calculadora.somar(2, 3);

        // Assert
        assertEquals(5, resultado);
    }
}
```


**Resultado:**

```text
Teste aprovado
```

## Teste de exceção

```java
@Test
void deveLancarExcecaoParaDivisaoPorZero() {

    Calculadora calculadora =
            new Calculadora();

    assertThrows(
            ArithmeticException.class,
            () -> calculadora.dividir(10, 0)
    );
}
```


**Resultado:**

```text
Teste aprovado
```

**O que acontece:** o teste passa porque a divisão por zero lança `ArithmeticException`.

```text
AAA:
Arrange → prepara
Act     → executa
Assert  → verifica
```

---

# 29. SOLID

## S — Single Responsibility Principle

Uma classe deve ter uma responsabilidade principal.

```java
// Cada classe possui uma responsabilidade
public class PedidoService {
}

public class PedidoRepository {
}

public class EmailService {
}
```


**O que acontece:** as responsabilidades ficam separadas em serviço, persistência e envio de e-mail. Definir as classes não gera saída.

## O — Open/Closed Principle

Aberto para extensão e fechado para alteração.

```java
public interface CalculadoraDesconto {
    BigDecimal calcular(Pedido pedido);
}
```


**O que acontece:** é criado um contrato que permite adicionar novos tipos de desconto sem alterar os consumidores.

```java
public class DescontoClienteVip
        implements CalculadoraDesconto {

    @Override
    public BigDecimal calcular(Pedido pedido) {
        return pedido.getValor()
                .multiply(new BigDecimal("0.10"));
    }
}
```


**O que acontece:** para um pedido de `R$ 100,00`, o método retorna `R$ 10,00` de desconto.

## L — Liskov Substitution Principle

Subclasses devem substituir a classe pai sem quebrar o comportamento.

```java
Animal animal = new Cachorro();
animal.emitirSom();
```


**Resultado:**

```text
Latido
```

## I — Interface Segregation Principle

Prefira interfaces pequenas e específicas.

```java
public interface Imprimivel {
    void imprimir();
}

public interface Digitalizavel {
    void digitalizar();
}
```


**O que acontece:** cada implementação depende apenas do contrato que realmente utiliza.

## D — Dependency Inversion Principle

Dependa de abstrações.

```java
public interface UsuarioRepository {
    void salvar(Usuario usuario);
}
```


**O que acontece:** o código de negócio pode depender da abstração sem conhecer a tecnologia de persistência.

```java
public class UsuarioService {

    private final UsuarioRepository repository;

    public UsuarioService(
            UsuarioRepository repository
    ) {
        this.repository = repository;
    }
}
```


**O que acontece:** o repository é recebido pelo construtor, permitindo trocar a implementação e facilitar testes.

---

# 30. Clean Code e refatoração

## Nomes claros

```java
// Ruim
int x;

// Melhor
int quantidadeDeUsuarios;
```


**O que acontece:** os dois códigos compilam, mas `quantidadeDeUsuarios` comunica melhor a intenção.

## Métodos pequenos

```java
public void finalizarPedido(Pedido pedido) {
    validarPedido(pedido);
    calcularTotal(pedido);
    salvarPedido(pedido);
    enviarConfirmacao(pedido);
}
```


**O que acontece:** o método principal apenas organiza quatro etapas com nomes claros; os efeitos dependem das implementações chamadas.

## Evite números mágicos

```java
private static final int MAXIMO_TENTATIVAS = 3;

if (tentativas > MAXIMO_TENTATIVAS) {
    bloquearAcesso();
}
```


**O que acontece:** quando `tentativas` for maior que `3`, `bloquearAcesso()` será chamado.

## Retorno antecipado

```java
public void processar(Usuario usuario) {

    if (usuario == null) {
        return;
    }

    if (!usuario.isAtivo()) {
        return;
    }

    executarProcessamento(usuario);
}
```


**O que acontece:** o método termina imediatamente para usuário nulo ou inativo; somente usuários ativos são processados.

## Imutabilidade

```java
public final class Produto {

    private final Long id;
    private final String nome;

    public Produto(Long id, String nome) {
        this.id = id;
        this.nome = nome;
    }
}
```


**O que acontece:** o objeto não pode ser herdado e seus atributos não podem ser reatribuídos após o construtor.

## Evite booleanos pouco claros

```java
// Pouco claro
gerarRelatorio(true);

// Melhor
gerarRelatorio(FormatoRelatorio.PDF);
```


**O que acontece:** as duas chamadas podem executar a mesma regra, mas o enum deixa explícito que o formato desejado é PDF.

## Refatorações comuns

```text
- Extrair método.
- Extrair classe.
- Renomear variável.
- Remover duplicação.
- Encapsular atributos.
- Simplificar condições.
- Substituir herança por composição.
- Criar constantes.
```

---

# 31. Recursos do Java moderno

## Pattern matching com instanceof

```java
Object objeto = "Java";

if (objeto instanceof String texto) {
    System.out.println(texto.toUpperCase());
}
```


**Resultado:**

```text
JAVA
```

## Pattern matching com switch

```java
static String descrever(Object valor) {
    return switch (valor) {
        case Integer numero ->
                "Inteiro: " + numero;

        case String texto ->
                "Texto: " + texto;

        case null ->
                "Valor nulo";

        default ->
                "Outro tipo";
    };
}
```


**O que acontece:** o método retorna `Inteiro: n`, `Texto: valor`, `Valor nulo` ou `Outro tipo`, conforme o argumento.

## Record pattern

```java
record Ponto(int x, int y) {
}

Object objeto = new Ponto(10, 20);

if (objeto instanceof Ponto(int x, int y)) {
    System.out.println(x + ", " + y);
}
```


**Resultado:**

```text
10, 20
```

## Text blocks

```java
String sql = """
        SELECT id, nome
        FROM usuario
        WHERE ativo = true
        ORDER BY nome
        """;
```


**O que acontece:** `sql` recebe a consulta multilinha preservando a formatação de forma legível.

## Virtual Threads

```java
Thread.startVirtualThread(() ->
        System.out.println(
                "Executando em virtual thread"
        )
);
```


**Resultado esperado:**

```text
Executando em virtual thread
```

---

# 32. Quarkus e Jakarta EE

Quarkus é o framework que inicializa a aplicação e integra as tecnologias do backend.

Jakarta EE fornece especificações usadas pelo código:

| Tecnologia | Responsabilidade |
|---|---|
| CDI | Criação e injeção de objetos |
| JAX-RS | Endpoints HTTP |
| Bean Validation | Validação declarativa |
| JPA | Persistência de entidades |
| Jakarta Transactions | Controle transacional |

MicroProfile complementa a aplicação:

| Tecnologia | Responsabilidade |
|---|---|
| Config | Configuração externa |
| REST Client | Cliente HTTP tipado |
| Fault Tolerance | Timeout, retry e circuit breaker |
| OpenAPI | Documentação da API |
| Reactive Messaging | Integração com Kafka |

Para APIs migradas do Java EE para Jakarta EE, use imports `jakarta.*`:

~~~java
import jakarta.enterprise.context.ApplicationScoped;
import jakarta.inject.Inject;
import jakarta.transaction.Transactional;
import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;
~~~

Não troque todo `javax.*` automaticamente. Pacotes do Java SE, como `javax.sql.DataSource`, continuam corretos. Evite apenas as versões antigas das APIs que migraram para Jakarta e não misture annotations Spring em um projeto Jakarta sem necessidade comprovada.

## Fluxo de um backend

~~~text
Requisição HTTP
    → Resource
    → Service
    → Repository ou DAO
    → Banco de dados
~~~

| Camada | Faz | Não deve fazer |
|---|---|---|
| Resource | Traduz HTTP para Java | Conter regra complexa |
| Service | Coordena o caso de uso | Conhecer detalhes da tela |
| Repository/DAO | Acessa dados | Decidir resposta HTTP |
| DTO | Transporta dados | Abrir transação ou acessar banco |
| Entity | Representa persistência | Ser exposta diretamente pela API |

## Execução com Maven

~~~bash
./mvnw quarkus:dev
./mvnw test
./mvnw clean verify
~~~

`quarkus:dev` oferece recarregamento durante o desenvolvimento. `verify` executa as verificações configuradas até a fase de validação do projeto.

O Maven Wrapper fixa a distribuição do Maven, não a JVM:

~~~bash
java -version
./mvnw -version
~~~

As duas saídas precisam indicar a versão de Java esperada pelo `pom.xml`.

## Maven multi-módulo

Separe módulos somente quando houver contratos realmente compartilhados:

~~~text
catalogo/
├── pom.xml
├── catalogo-api/       DTOs e contratos públicos
├── catalogo-client/    cliente Java da API
└── catalogo-service/   implementação do backend
~~~

O `pom.xml` raiz agrega os módulos:

~~~xml
<packaging>pom</packaging>

<modules>
    <module>catalogo-api</module>
    <module>catalogo-client</module>
    <module>catalogo-service</module>
</modules>
~~~

Evite dependências circulares. O módulo de contrato não deve depender da implementação.

---

# 33. APIs REST com JAX-RS

JAX-RS transforma métodos Java em operações HTTP.

~~~java
@Path("/produtos")
@Produces(MediaType.APPLICATION_JSON)
@Consumes(MediaType.APPLICATION_JSON)
public class ProdutoResource {

    @Inject
    ProdutoService produtoService;

    @GET
    @Path("/{id}")
    public ProdutoResponse buscar(@PathParam("id") long id) {
        return produtoService.buscar(id);
    }

    @POST
    public Response criar(@Valid CriarProdutoRequest request) {
        ProdutoResponse produto = produtoService.criar(request);

        return Response.status(Response.Status.CREATED)
                .entity(produto)
                .build();
    }
}
~~~

## Annotations principais

| Annotation | Função |
|---|---|
| `@Path` | Define a rota |
| `@GET`, `@POST`, `@PUT`, `@DELETE` | Define o verbo HTTP |
| `@PathParam` | Lê parte da rota |
| `@QueryParam` | Lê parâmetro da URL |
| `@HeaderParam` | Lê um header |
| `@Consumes` | Define o formato recebido |
| `@Produces` | Define o formato devolvido |
| `@Valid` | Executa Bean Validation |

## DTOs por operação

Entrada e saída possuem contratos diferentes:

~~~java
public record CriarProdutoRequest(
        String nome,
        BigDecimal preco
) {
}
~~~

~~~java
public record ProdutoResponse(
        long id,
        String nome,
        BigDecimal preco
) {
}
~~~

~~~text
Request  → dados aceitos pela operação
Response → dados públicos devolvidos pela API
Entity   → formato interno de persistência
~~~

Evite usar uma entidade JPA como request ou response. Isso pode expor colunas internas, relacionamentos lazy e detalhes do banco.

## Status HTTP

| Status | Uso comum |
|---|---|
| `200 OK` | Consulta ou alteração concluída |
| `201 Created` | Recurso criado |
| `204 No Content` | Sucesso sem corpo |
| `400 Bad Request` | Entrada inválida |
| `401 Unauthorized` | Não autenticado |
| `403 Forbidden` | Sem permissão |
| `404 Not Found` | Recurso inexistente |
| `409 Conflict` | Conflito de estado ou unicidade |
| `500 Internal Server Error` | Falha inesperada |

## Tratamento centralizado de erros

Uma exceção de domínio não deve espalhar `try-catch` pelos endpoints.

~~~java
public class RecursoNaoEncontradoException extends RuntimeException {

    public RecursoNaoEncontradoException(String mensagem) {
        super(mensagem);
    }
}
~~~

~~~java
@Provider
public class RecursoNaoEncontradoMapper
        implements ExceptionMapper<RecursoNaoEncontradoException> {

    @Override
    public Response toResponse(RecursoNaoEncontradoException exception) {
        ErroResponse erro = new ErroResponse(
                "RECURSO_NAO_ENCONTRADO",
                exception.getMessage()
        );

        return Response.status(Response.Status.NOT_FOUND)
                .entity(erro)
                .build();
    }
}
~~~

~~~java
public record ErroResponse(
        String codigo,
        String mensagem
) {
}
~~~

O mapper mantém a resposta de erro consistente e deixa o endpoint pequeno.

---

# 34. CDI, configuração e validação

## CDI

CDI administra o ciclo de vida e as dependências dos objetos.

| Escopo | Duração |
|---|---|
| `@ApplicationScoped` | Uma instância compartilhada pela aplicação |
| `@RequestScoped` | Uma instância por requisição HTTP |
| `@Dependent` | Acompanha o objeto que a recebeu |

~~~java
@ApplicationScoped
public class CalculadoraFrete {

    public BigDecimal calcular(BigDecimal valor) {
        return valor.multiply(new BigDecimal("0.05"));
    }
}
~~~

Injeção por construtor deixa a dependência explícita:

~~~java
@ApplicationScoped
public class PedidoService {

    private final CalculadoraFrete calculadoraFrete;

    @Inject
    public PedidoService(CalculadoraFrete calculadoraFrete) {
        this.calculadoraFrete = calculadoraFrete;
    }
}
~~~

## MicroProfile Config

`application.properties` contém valores externos ao código:

~~~properties
catalogo.consulta.limite=100
catalogo.cache.ttl-segundos=300
catalogo.integracao.url=https://servico.exemplo
~~~

Injeção de valores:

~~~java
@Inject
@ConfigProperty(
        name = "catalogo.consulta.limite",
        defaultValue = "100"
)
int limiteConsulta;

@Inject
@ConfigProperty(name = "catalogo.integracao.url")
URI urlIntegracao;
~~~

Regras:

~~~text
Obrigatório   → tipo direto e sem valor padrão
Opcional      → Optional<T>
Padrão seguro → defaultValue
Segredo       → variável ou secret do ambiente
~~~

Muitas propriedades relacionadas podem formar uma configuração tipada:

~~~java
@ConfigMapping(prefix = "catalogo.cache")
public interface CacheConfig {

    long ttlSegundos();
}
~~~

Nunca coloque senha, token ou chave privada no código ou no repositório.

## Perfis

~~~properties
%dev.quarkus.log.console.json=false
%test.quarkus.datasource.db-kind=h2
~~~

O prefixo escolhe um valor específico do perfil. Mantenha a mesma chave lógica em todos os ambientes.

## Bean Validation

Bean Validation protege o formato de entrada:

~~~java
public record CriarProdutoRequest(
        @NotBlank
        @Size(max = 120)
        String nome,

        @NotNull
        @Positive
        BigDecimal preco
) {
}
~~~

| Annotation | Regra |
|---|---|
| `@NotNull` | Não aceita `null` |
| `@NotBlank` | Texto não pode estar vazio |
| `@Size` | Limita tamanho |
| `@Positive` | Número deve ser positivo |
| `@Email` | Valida formato de e-mail |
| `@Pattern` | Valida expressão regular |

~~~text
Bean Validation → formato e restrições simples
Service         → regra que depende do caso de uso
Banco           → integridade final com constraints
~~~

---

# 35. JPA, Hibernate e transações

JPA é a especificação. Hibernate ORM é a implementação que converte entidades Java em operações no banco.

~~~java
@Entity
@Table(name = "produto")
public class Produto {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, length = 120)
    private String nome;

    @Column(nullable = false, precision = 15, scale = 2)
    private BigDecimal preco;

    protected Produto() {
    }

    public Produto(String nome, BigDecimal preco) {
        this.nome = nome;
        this.preco = preco;
    }

    public Long getId() {
        return id;
    }

    public String getNome() {
        return nome;
    }

    public BigDecimal getPreco() {
        return preco;
    }
}
~~~

## Repository com EntityManager

~~~java
@ApplicationScoped
public class ProdutoRepository {

    @Inject
    EntityManager entityManager;

    public Produto buscar(long id) {
        return entityManager.find(Produto.class, id);
    }

    public List<Produto> buscarTodos() {
        return entityManager.createQuery(
                        "select p from Produto p order by p.nome",
                        Produto.class
                )
                .getResultList();
    }

    public void persistir(Produto produto) {
        entityManager.persist(produto);
    }
}
~~~

JPQL consulta entidades e atributos Java. SQL nativo consulta tabelas e colunas.

~~~text
JPQL       → portátil e orientado a entidades
SQL nativo → útil para recursos específicos ou consultas complexas
~~~

Use parâmetros em consultas. Não concatene entrada do usuário.

## Transações

~~~java
@ApplicationScoped
public class ProdutoService {

    @Inject
    ProdutoRepository produtoRepository;

    @Transactional
    public Produto criar(
            String nome,
            BigDecimal preco
    ) {
        Produto produto = new Produto(nome, preco);
        produtoRepository.persistir(produto);
        return produto;
    }
}
~~~

`@Transactional` confirma a operação quando o método termina normalmente e faz rollback em falhas compatíveis com a política transacional.

Mantenha a transação no service porque ele conhece o caso de uso completo.

## Datasource e Agroal

Agroal fornece o pool de conexões usado pelo Quarkus.

~~~properties
quarkus.datasource.db-kind=mssql
quarkus.datasource.username=${DB_USERNAME}
quarkus.datasource.password=${DB_PASSWORD}
quarkus.datasource.jdbc.url=${DB_URL}
quarkus.datasource.jdbc.min-size=2
quarkus.datasource.jdbc.max-size=20
~~~

~~~text
Pool pequeno demais → requisições esperam conexão
Pool grande demais  → banco pode ser sobrecarregado
~~~

Defina tamanho com métricas e testes de carga, não por palpite.

## Banco de teste

| Opção | Vantagem | Risco |
|---|---|---|
| H2 | Rápido e simples | SQL e tipos podem diferir da produção |
| Testcontainers | Usa banco real | Teste inicia mais devagar |

Use H2 para testes simples. Use o mesmo banco da produção quando dialeto, índices, constraints ou tipos fizerem parte do comportamento.

Migrations com Flyway e Liquibase já são estudadas no capítulo de JDBC.

---

# 36. Integração entre serviços

MicroProfile REST Client cria um cliente HTTP a partir de uma interface.

~~~java
@Path("/produtos")
@RegisterRestClient(configKey = "catalogo-api")
@Produces(MediaType.APPLICATION_JSON)
public interface CatalogoClient {

    @GET
    @Path("/{id}")
    ProdutoResponse buscar(@PathParam("id") long id);
}
~~~

~~~java
@ApplicationScoped
public class ConsultaCatalogoService {

    @Inject
    @RestClient
    CatalogoClient catalogoClient;

    public ProdutoResponse buscar(long id) {
        return catalogoClient.buscar(id);
    }
}
~~~

~~~properties
quarkus.rest-client.catalogo-api.url=${CATALOGO_URL}
quarkus.rest-client.catalogo-api.connect-timeout=2000
quarkus.rest-client.catalogo-api.read-timeout=5000
~~~

## Resiliência

MicroProfile Fault Tolerance possui annotations para falhas transitórias:

~~~java
@Timeout(2000)
@Retry(maxRetries = 2, delay = 200)
@CircuitBreaker(
        requestVolumeThreshold = 10,
        failureRatio = 0.5
)
public ProdutoResponse buscar(long id) {
    return catalogoClient.buscar(id);
}
~~~

| Recurso | Função |
|---|---|
| Timeout | Limita o tempo de espera |
| Retry | Repete uma falha transitória |
| Circuit breaker | Interrompe chamadas para um destino falhando |
| Fallback | Entrega uma alternativa segura |
| Bulkhead | Limita concorrência sobre um recurso |

Não aplique retry automaticamente em operações que criam ou alteram dados. Primeiro garanta idempotência.

## Identidade da chamada

~~~text
Em nome do usuário → propaga identidade quando o destino precisa dela
Rotina técnica      → usa identidade própria da aplicação
~~~

Não copie tokens manualmente sem entender expiração, audiência e permissões.

---

# 37. Kafka, Redis e jobs

## Kafka com SmallRye Reactive Messaging

Kafka transporta eventos de forma assíncrona:

~~~text
Produtor → tópico → grupo consumidor → consumidor
~~~

Evento:

~~~java
public record ProdutoCriadoEvento(
        long id,
        String nome
) {
}
~~~

Produtor:

~~~java
@ApplicationScoped
public class ProdutoEventoProducer {

    @Inject
    @Channel("produto-criado")
    Emitter<ProdutoCriadoEvento> emitter;

    public CompletionStage<Void> publicar(
            ProdutoCriadoEvento evento
    ) {
        return emitter.send(evento);
    }
}
~~~

Consumidor:

~~~java
@ApplicationScoped
public class ProdutoEventoConsumer {

    @Incoming("produto-criado")
    @Blocking
    @Transactional
    public void processar(ProdutoCriadoEvento evento) {
        processarUmaUnicaVez(evento);
    }
}
~~~

`@Transactional` controla a transação do banco. Ela não transforma, sozinha, o consumo Kafka e a gravação no banco em uma única transação distribuída. Use idempotência e, quando necessário, padrões como Outbox.

Antes de criar um fluxo, defina:

- contrato e versão da mensagem;
- chave de particionamento;
- grupo consumidor;
- confirmação da mensagem;
- retry e dead-letter queue;
- ordenação necessária;
- idempotência;
- métricas e alertas.

~~~text
Confirmar antes  → falha posterior pode perder a mensagem
Confirmar depois → pode ocorrer reentrega
~~~

O consumidor precisa suportar reentrega sem duplicar o efeito.

## Redis

Redis guarda dados temporários e rápidos:

~~~text
cache
sessão
rate limit
marca de idempotência
lock distribuído bem projetado
~~~

Exemplo simples:

~~~java
@ApplicationScoped
public class ProdutoCache {

    private final ValueCommands<String, String> valores;

    public ProdutoCache(RedisDataSource redisDataSource) {
        this.valores = redisDataSource.value(String.class);
    }

    public void salvar(long id, String json) {
        valores.setex("produto:" + id, 300, json);
    }

    public String buscar(long id) {
        return valores.get("produto:" + id);
    }
}
~~~

Toda chave precisa de:

~~~text
nome previsível
TTL
responsável
formato do valor
comportamento quando não existir
~~~

Redis não substitui automaticamente o banco principal.

## Jobs

Quarkus Scheduler executa tarefas periódicas:

~~~java
@ApplicationScoped
public class LimpezaJob {

    @Scheduled(every = "10m")
    void removerDadosExpirados() {
        executarLimpeza();
    }
}
~~~

Em mais de uma réplica, o mesmo job pode executar simultaneamente. Use Quartz com armazenamento compartilhado, lock distribuído ou CronJob do Kubernetes quando precisar de coordenação.

## Fila em memória

`BlockingQueue` e `ExecutorService` servem para trabalho local:

~~~text
reinício perde itens
cada réplica possui sua fila
não existe histórico automático
escalar muda a distribuição
~~~

Use Kafka quando a mensagem precisar sobreviver ao processo ou ser consumida por outros serviços.

---

# 38. Segurança no backend

~~~text
OAuth 2.0 → autorização delegada
OpenID Connect → identidade sobre OAuth 2.0
JWT → formato comum de token
OIDC Provider → autentica e emite tokens
~~~

O backend precisa validar assinatura, emissor, audiência e expiração do token.

~~~properties
quarkus.oidc.auth-server-url=${OIDC_URL}
quarkus.oidc.client-id=catalogo-api
quarkus.oidc.application-type=service
~~~

Uma API que apenas valida bearer tokens normalmente não precisa guardar um segredo de cliente. Fluxos que chamam o provedor podem exigir credenciais, conforme a configuração adotada.

Proteção por papel:

~~~java
@GET
@Path("/{id}")
@RolesAllowed("produto-consulta")
public ProdutoResponse buscar(@PathParam("id") long id) {
    return produtoService.buscar(id);
}
~~~

Identidade atual:

~~~java
@Inject
SecurityIdentity identidade;

public String usuarioAtual() {
    return identidade.getPrincipal().getName();
}
~~~

Regras:

- negar acesso por padrão;
- aplicar menor privilégio;
- diferenciar identidade humana e técnica;
- validar autorização no backend;
- não registrar token, senha ou chave;
- auditar operações sensíveis.

~~~text
401 → identidade ausente ou inválida
403 → identidade válida, mas sem permissão
~~~

---

# 39. Documentação e observabilidade

## OpenAPI

MicroProfile OpenAPI documenta o contrato da API.

~~~java
@GET
@Path("/{id}")
@Operation(summary = "Busca um produto")
@APIResponse(
        responseCode = "200",
        description = "Produto encontrado"
)
@APIResponse(
        responseCode = "404",
        description = "Produto não encontrado"
)
public ProdutoResponse buscar(@PathParam("id") long id) {
    return produtoService.buscar(id);
}
~~~

OpenAPI descreve rotas, parâmetros, corpos e respostas. Swagger UI apresenta essa documentação de forma navegável.

## Health checks

~~~text
Liveness  → o processo precisa reiniciar?
Readiness → pode receber tráfego?
Startup   → ainda está inicializando?
~~~

Exemplo de readiness:

~~~java
@Readiness
@ApplicationScoped
public class AplicacaoHealthCheck implements HealthCheck {

    @Override
    public HealthCheckResponse call() {
        return HealthCheckResponse.named("aplicacao")
                .up()
                .build();
    }
}
~~~

Não marque readiness como saudável quando uma dependência obrigatória impede o atendimento das requisições.

## Logs, métricas e traces

| Pilar | Pergunta respondida |
|---|---|
| Logs | O que aconteceu? |
| Métricas | Quanto, com que frequência e por quanto tempo? |
| Traces | Por quais serviços a requisição passou? |

~~~java
private static final Logger LOG =
        Logger.getLogger(ProdutoService.class);

LOG.infof(
        "Produto criado. produtoId=%d",
        produto.getId()
);

LOG.errorf(
        exception,
        "Falha ao consultar catálogo. produtoId=%d",
        produtoId
);
~~~

Um log útil contém operação, identificador técnico, resultado, duração, correlation id e exceção original.

Nunca registre:

~~~text
senha
token completo
chave privada
dados pessoais desnecessários
payload sensível
~~~

OpenTelemetry correlaciona logs, métricas e traces quando as extensões e o exportador estão configurados.

~~~text
Log técnico → explica uma falha do sistema
Auditoria   → registra quem realizou uma ação sensível
~~~

Um não substitui o outro.

---

# 40. Testes do backend

JUnit já foi apresentado. No backend, ele costuma trabalhar com Mockito, Quarkus Test, RestAssured e Testcontainers.

## Teste unitário com Mockito

~~~java
@ExtendWith(MockitoExtension.class)
class ProdutoServiceTest {

    @Mock
    ProdutoRepository produtoRepository;

    @InjectMocks
    ProdutoService produtoService;

    @Test
    void deveCriarProduto() {
        Produto produto = produtoService.criar(
                "Teclado",
                new BigDecimal("100.00")
        );

        verify(produtoRepository).persistir(produto);
        assertEquals("Teclado", produto.getNome());
    }
}
~~~

O teste unitário não inicia o Quarkus. Ele verifica uma classe isolada e substitui dependências por mocks.

## Teste de integração com Quarkus

~~~java
@QuarkusTest
class ProdutoResourceTest {

    @Test
    void deveBuscarProduto() {
        RestAssured.given()
                .when()
                .get("/produtos/1")
                .then()
                .statusCode(200)
                .body("id", equalTo(1));
    }
}
~~~

`@QuarkusTest` pode validar CDI, HTTP, JSON, configuração, segurança, transação e persistência.

## Testcontainers

~~~text
Teste inicia container
    → aplica estrutura e dados controlados
    → executa o backend
    → valida o resultado
    → encerra o container
~~~

Use para comportamentos dependentes de SQL Server, PostgreSQL, Kafka ou Redis reais.

## Escolha do teste

| Teste | Use para |
|---|---|
| Unitário | Regra isolada e rápida |
| Integração | Framework, banco, HTTP e serialização |
| Contrato | Compatibilidade entre serviços |
| End-to-end da API | Fluxo backend completo e crítico |

~~~text
Muitos testes unitários
Alguns testes de integração
Poucos testes completos
~~~

Teste falhou é falha. Teste ignorado ou não executado não pode ser relatado como aprovado.

---

# 41. Relatórios com JasperReports

JasperReports gera documentos a partir de templates e dados Java.

~~~text
Template .jrxml
    → compilação
    → preenchimento com dados
    → JasperPrint
    → PDF, XLSX ou outro formato
~~~

~~~java
public byte[] gerarPdf(List<ProdutoRelatorio> produtos)
        throws JRException, IOException {

    try (InputStream template = getClass()
            .getResourceAsStream("/relatorios/produtos.jrxml")) {

        JasperReport relatorio =
                JasperCompileManager.compileReport(template);

        JRBeanCollectionDataSource dados =
                new JRBeanCollectionDataSource(produtos);

        Map<String, Object> parametros =
                Map.of("TITULO", "Produtos");

        JasperPrint preenchido =
                JasperFillManager.fillReport(
                        relatorio,
                        parametros,
                        dados
                );

        return JasperExportManager
                .exportReportToPdf(preenchido);
    }
}
~~~

`ProdutoRelatorio` deve expor getters com os mesmos nomes dos fields declarados no template.

Cuidados:

- valide parâmetros recebidos;
- versione os templates;
- pré-compile templates estáveis quando fizer sentido;
- não carregue milhões de registros em memória;
- execute relatórios pesados de forma assíncrona;
- teste o conteúdo essencial, não somente a existência do arquivo.

---

# 42. Containers e deploy

Estas ferramentas não fazem parte da linguagem Java, mas executam e entregam o backend.

## Docker

Depois de `./mvnw clean package`, uma aplicação Quarkus no formato fast-jar pode ser executada assim:

~~~dockerfile
FROM eclipse-temurin:25-jre

WORKDIR /app
COPY target/quarkus-app/ ./

EXPOSE 8080
ENTRYPOINT ["java", "-jar", "quarkus-run.jar"]
~~~

Use uma imagem compatível com a versão de Java do projeto. Não coloque segredos na imagem.

## Kubernetes e Helm

| Objeto | Função |
|---|---|
| Deployment | Define pods e atualização |
| Service | Fornece endereço interno estável |
| Ingress | Expõe entrada HTTP |
| ConfigMap | Guarda configuração não sensível |
| Secret | Entrega dados sensíveis |
| CronJob | Dispara rotina agendada |

Helm transforma manifests em templates reutilizáveis:

~~~text
chart/
├── Chart.yaml
├── values.yaml
└── templates/
    ├── deployment.yaml
    ├── service.yaml
    ├── ingress.yaml
    └── secret.yaml
~~~

Para cada backend, defina:

- liveness, readiness e startup probes;
- requests e limits de CPU e memória;
- número de réplicas;
- timeout de encerramento;
- graceful shutdown;
- autoscaling quando necessário;
- configuração externa por ambiente.

## Pipeline

~~~text
checkout
    → compilar
    → testes unitários
    → testes de integração
    → análise do SonarQube
    → quality gate
    → construir imagem
    → scan de segurança
    → publicar
    → deploy
~~~

O pipeline deve interromper a entrega quando uma etapa obrigatória falhar.

---

# 43. Checklist final

## Fundamentos

- [ ] JDK, JRE, JVM e bytecode.
- [ ] Tipos primitivos e wrappers.
- [ ] Variáveis, constantes e operadores.
- [ ] if, switch, for e while.
- [ ] Métodos e arrays.

## Orientação a objetos

- [ ] Classe e objeto.
- [ ] Construtor.
- [ ] Encapsulamento.
- [ ] Herança.
- [ ] Polimorfismo.
- [ ] Composição.
- [ ] Interface.
- [ ] Classe abstrata.
- [ ] Record.
- [ ] Enum.
- [ ] Classes seladas.

## APIs principais

- [ ] String e StringBuilder.
- [ ] equals e hashCode.
- [ ] List, Set, Map, Queue e Deque.
- [ ] Comparable e Comparator.
- [ ] Generics.
- [ ] Exceptions.
- [ ] Optional.
- [ ] Lambdas.
- [ ] Streams API.
- [ ] BigDecimal.
- [ ] Java Time API.
- [ ] Arquivos e I/O.

## Backend e ferramentas

- [ ] Annotations.
- [ ] Threads e concorrência.
- [ ] Arquitetura e interfaces JDBC.
- [ ] DriverManager, DataSource e pool de conexões.
- [ ] Connection String e configuração segura.
- [ ] Statement, PreparedStatement e CallableStatement.
- [ ] CRUD e chaves geradas.
- [ ] ResultSet e mapeamento de tipos.
- [ ] Valores nulos e Java Time.
- [ ] Relacionamentos e JOIN.
- [ ] DAO e Repository.
- [ ] SQLException e SQL Injection.
- [ ] Transações, isolamento e Savepoint.
- [ ] Batch Processing.
- [ ] Paginação, timeout e performance.
- [ ] DatabaseMetaData e ResultSetMetaData.
- [ ] Procedures, Functions e Triggers.
- [ ] BLOB e consultas dinâmicas.
- [ ] Flyway e Liquibase.
- [ ] Datafaker.
- [ ] Testes de integração e Testcontainers.
- [ ] Maven.
- [ ] Gradle.
- [ ] JUnit.
- [ ] Quarkus e Jakarta EE.
- [ ] CDI e escopos.
- [ ] JAX-RS, DTOs e status HTTP.
- [ ] Bean Validation e ExceptionMapper.
- [ ] MicroProfile Config e perfis.
- [ ] JPA, Hibernate ORM e Agroal.
- [ ] REST Client e Fault Tolerance.
- [ ] Kafka e SmallRye Reactive Messaging.
- [ ] Redis, TTL e idempotência.
- [ ] Scheduler e processamento assíncrono.
- [ ] OAuth 2.0, OpenID Connect e JWT.
- [ ] OpenAPI e Swagger UI.
- [ ] Health checks e OpenTelemetry.
- [ ] Mockito, Quarkus Test e RestAssured.
- [ ] JasperReports.
- [ ] Docker, Kubernetes e Helm.
- [ ] SonarQube e quality gate.

## Qualidade

- [ ] SOLID.
- [ ] Clean Code.
- [ ] Refatoração.
- [ ] Imutabilidade.
- [ ] Tratamento de erros.
- [ ] Testes automatizados.

---

# Resumo final

```text
Java é:

- Fortemente tipada.
- Orientada a objetos.
- Multiplataforma por meio da JVM.
- Muito usada em sistemas backend.
- Adequada para sistemas corporativos.
- Possui gerenciamento automático de memória.
- Possui recursos modernos de concorrência.
- Possui um grande ecossistema de bibliotecas e frameworks.
```

```text
Fluxo para desenvolver:

1. Entenda a regra de negócio.
2. Modele as classes.
3. Defina responsabilidades.
4. Use interfaces para contratos.
5. Encapsule o estado.
6. Trate os erros.
7. Escolha as coleções corretas.
8. Escreva código legível.
9. Crie testes.
10. Refatore continuamente.
```

```text
Fluxo de um backend Java:

HTTP
  → JAX-RS
  → Service
  → JPA ou JDBC
  → Banco

Integrações:

REST Client → comunicação síncrona
Kafka       → eventos assíncronos
Redis       → dados temporários

Operação:

Config externa
  → segurança
  → logs, métricas e traces
  → testes
  → container
  → deploy
```
