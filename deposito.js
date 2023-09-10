const prompt = require("prompt-sync")();

// Classe para representar uma venda
class Venda {
  constructor(produto, quantidade, data, valor) {
    this.produto = produto;
    this.quantidade = quantidade;
    this.data = data;
    this.valor = valor;
  }
}

const vendas = []; // Array para armazenar as vendas
const estoque = [ // Estoque de bebidas
  { produto: "Cerveja", quantidade: 10 },
  { produto: "Refrigerante", quantidade: 15 },
  { produto: "Agua", quantidade: 20 },
  { produto: "Vodka", quantidade: 5 },
];

// Função para registrar uma venda
function registrarVenda() {
  const { produto, quantidade } = promptDadosVenda();
  // Verificar se o produto está disponível no estoque
  const itemEstoque = estoque.find(({ produto: p }) => p === produto);

  if (itemEstoque && itemEstoque.quantidade >= quantidade) {
    const data = prompt("Digite a data da venda: ");
    const valor = parseFloat(prompt("Digite o valor unitário da venda: "));
    // Cria uma nova instância da classe Venda e adiciona ao array vendas
    vendas.push(new Venda(produto, quantidade, data, valor));
    console.log("Venda registrada com sucesso!");
    console.log();
    // Atualiza o estoque
    itemEstoque.quantidade -= quantidade;
  } else {
    console.log("Produto indisponível no estoque.");
    console.log();
  }
}


function promptDadosVenda() {
  // Solicita ao usuário os dados da venda e retorna um objeto com as informações
  const produto = prompt("Digite o nome do produto: ");
  const quantidade = parseInt(prompt("Digite a quantidade vendida: "));
  return { produto, quantidade };
}

// Função para exibir o resumo das vendas
function exibirResumoVendas() {
  console.log("Resumo das Vendas:");
  console.log("-------------------");

  // Percorre o array de vendas e exibe as informações de cada venda
  vendas.forEach(({ data, produto, quantidade, valor }) => {
    console.log(`Data: ${data}`);
    console.log(`Produto: ${produto}`);
    console.log(`Quantidade: ${quantidade}`);
    console.log(`Valor unitário: R$ ${valor}`);
    console.log("-------------------");
  });

  // Calcula o total de vendas utilizando o método reduce
  const totalVendas = vendas.reduce((total, { valor, quantidade }) => total + valor * quantidade, 0);
  console.log(`Total de Vendas: R$ ${totalVendas}`);
  console.log();

  // Utiliza o método map para criar um novo array com os produtos vendidos
  const produtosVendidos = vendas.map(({ produto }) => produto);
  // Utiliza o objeto Set para armazenar apenas os produtos únicos
  const produtosUnicos = [...new Set(produtosVendidos)];
  console.log("Produtos Vendidos:");
  console.log(produtosUnicos);
  console.log();

  // Utiliza o método filter para criar um novo array com as vendas que possuem quantidade acima de 10
  const vendasAcimaDe10 = vendas.filter(({ quantidade }) => quantidade > 10);
  console.log("Vendas com Quantidade Acima de 10:");
  console.log(vendasAcimaDe10);
  console.log();
}

// Função principal
function main() {
  let opcao;

  do {
    console.log('---------- PRODUTOS EM ESTOQUE ----------');
    console.log(estoque);
    console.log('-----------------------------------------');
    console.log("1 - Registrar Venda");
    console.log("2 - Exibir Resumo das Vendas");
    console.log("0 - Sair");
    opcao = parseInt(prompt("Digite a opção desejada: "));

    switch (opcao) {
      case 1:
        registrarVenda();
        break;
      case 2:
        exibirResumoVendas();
        break;
      case 0:
        console.log("Programa encerrado.");
        break;
      default:
        console.log("Opção inválida.");
        console.log();
    }
  } while (opcao !== 0);
}

// Executa o programa
main();