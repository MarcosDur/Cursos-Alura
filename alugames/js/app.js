function alterarStatus(id){
    let gameClicado = document.getElementById(`game-${id}`);
    let imagem = gameClicado.querySelector('.dashboard__item__img');
    let botao = gameClicado.querySelector('.dashboard__item__button');
    let nomeDoJogo = gameClicado.querySelector('.dashboard__item__name')

    let  confirmacao = confirm(`Você tem certeza?`)
    

    if(confirmacao){
        if(imagem.classList.contains('dashboard__item__img--rented')){
            imagem.classList.remove('dashboard__item__img--rented');
            botao.classList.remove('dashboard__item__button--return');
            botao.textContent = 'Alugar';
        } else{ 
            imagem.classList.add('dashboard__item__img--rented');
            botao.textContent = 'Devolver';
            botao.classList.add('dashboard__item__button--return');
        }   
     } else {
            console.log("Ação cancelada pelo usuário");
        }
   }



// document.getElementById('btn_alugar').addEventListener('click', function(){
//     if(this.style.backgroundColor === '#1875E8'){
//         this.style.backgroundColor = '#041d3b';
//     }else{
//         this.style.backgroundColor === '#1875E8';
//     }
// });s