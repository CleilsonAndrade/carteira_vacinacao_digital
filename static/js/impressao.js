// BOTAO PARA REALIZAR A IMPRESÃO DA CARTEIRA DE VACINAÇÃO

// SELECIONA O ELEMENTO IMPRIMIR E SALVA EM UMA VARIÁVEL
const btnInprimir = document.getElementById('imprimir')

// QUANDO O ELEMENTO FOR CLICADO REALIZA A AÇÃO
btnInprimir.addEventListener('click', () => {
  // SELECIONA O CORPO DA PÁGINA E SALVA EM UMA VARIÁVEL
  const body = document.body.innerHTML
  // SELECIONA O FORMULÁRIO DA PÁGINA E SALVA EM UMA VARIÁVEL
  const formPrint = document.querySelector('#form')
  // RETIRA A IMAGEM DE FUNDO DO CORPO DA PÁGINA
  document.body.style.backgroundImage = 'none'
  // SELECIONA O CONTAINER DE BOTÕES
  let btnContainerPrint = document.getElementById('container-print')
  // REMOVE A CLASSE DE DISPLAY FLEX DO CONTAINER
  btnContainerPrint.classList.remove('d-flex')
  // ADICIONE A CLASSE DE DISPLAY NONE
  btnContainerPrint.classList.add('d-none')
  // ATRIBUI VARIÁVEL COM O FORMULÁRIO SALVO NO CORPO DA PÁGINA SUBSTITUINDO-O
  document.body.innerHTML = formPrint.innerHTML
  // EXECUTA A FUNÇÃO DE IMPRESSÃO DA PÁGINA
  window.print()
  // ATRIBUI A VARIÁVEL CONTENDO O CORPO DA PÁGINA SALVO ANTERIORMENTE NO CORPO DA PÁGINA SUBSTITUINDO-O
  document.body.innerHTML = body
  // ATUALIZA A PÁGINA
  location.reload()
})
