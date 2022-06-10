// API PARA EXIBIÇÃO DA NOTÍCIAS NA TELA DE LOGIN
// CHAVE DA API
const apiKey = 'b6208aa8e7064dcb9be8f2b1051a7939'
// SELECIONA CONTAINER DE CARTÕES
const contCard = document.getElementById('container-card')

window.onload = function pegarNoticias() {
  axios
    // MANDA UMA REQUISIÇÃO AO SERVIDOR DA API
    .get(
      `https://newsapi.org/v2/top-headlines?apiKey=${apiKey}&country=br&category=health&pageSize=3`
    )
    .then(response => {
      // SUCESSO DA RESPOSTA CONTENDO OS DADOS É SALVO NA VARIÁVEL
      const data = response.data.articles
      // REALIZA UM LAÇO DE REPETIÇÃO COM LIMITE COM COMPRIMENTO DO ARRY DA VARIÁVEL
      for (let i = 0; i < data.length; i++) {
        // CRIA UM ELEMENTO INSERINDO OS DA VARIAVÉL
        const card = `<div class="card" style="width: 14rem">
                        <img
                          class="card-img-top"
                          style="height: 9rem;background-color: #fff;"
                          src="${data[i].urlToImage}"
                          alt="Imagem da notícia"
                        />
                        <div class="card-body"
                        style="border-bottom: 2px solid #007bff !important"
                        >
                          <p title="${data[i].description}" class="card-text" style="height: 7.35rem;overflow: hidden;">${data[i].title}</p>
                          <a href="${data[i].url}" target="_blank" class="btn btn-outline-secondary btn-sm w-100"
                            >Ver mais</a
                          >
                        </div>
                      </div>`
        // INSERI SOMANDO A CADA REPETIÇÃO DO LAÇO VARIÁVEL DENTRO DO CONTAINER DE CARTÕES
        contCard.innerHTML += card
      }
    })
    .catch(error => {
      console.log(error)
    })
}
