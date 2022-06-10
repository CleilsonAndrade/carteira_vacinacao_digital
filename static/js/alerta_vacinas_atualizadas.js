// FECHAMENTO DA EXIBIÇÃO DA MENSAGEM DE SUCESSO DA ATUALIZAÇÃO DO CADASTRO DAS VACINAS
const alerta = document.querySelector('#close')

function fecharAlerta() {
  alerta.style.webkitTransition = 'all 0.5s ease-out'
  alerta.style.display = 'none'
}
// TEMPO PARA A EXECUÇÃO DA FUNÇÃO
setTimeout(fecharAlerta, 4000)
