# README
<h1 align="center">
☠️<br>Piratas da Guanabara
</h1>

## 📚 Introdução

> Este repositório é um projeto da matéria de CSI-22 de desenvolvimento de um jogo em linguagem Python com auxílio da biblioteca Pygame para renderização 
de gráficos em um ambiente 2D. O objetivo do projeto é desenvolver habilidades em um dos paradigmas mais importantes da áre de programação denominado de Programação Orientada a Objetos (POO), assim como a aplicação de conceitos derivados da mesma, a exemplo da herança e do polimorfismo.  


## ⚙️ Pré-requisitos e instalação
> Python 3 com uma instalação de PyGame. Para que o jogo funcione corretamente, descompacte o conteúdo de 
``data/kenney_pirate-ack.zip`` diretamente em ``data/`` (usuários de Windows podem ter demudar o comportamento padrão do
"Extrair tudo" para que o conteúdo seja extraído para ``data/`` e **não** para ``data/kenney_pirate-ack/``).
> 
> Em seguida baixa a [imagem de liuzishan no Freepik](https://br.freepik.com/fotos-gratis/pintura-digital-de-antigos-navios-de-guerra-viajando-em-mares-agitados_14402173.htm#query=guerra%20de%20navios&position=1&from_view=search&track=robertav1_2_sidr) como ``data/PNG/Retina/Menu/background.jpg``.
> 
> Criamos o script ``data/setup_data.sh`` para facilitar estes procedimentos (precisa de ``curl`` instalado)
---

## 🦜 Tema

> O presente jogo denominado Piratas tem como inspiração Asteroids do Atari e busca introduzir novas mecânicas de jogo para melhorar jogabilidade em uma temática ambientada nas porfundezas do oceano atlântico em meio às expedições do século XVI de expansão marítima e descobrimento de novas terras. O personagem principal que será controlado por meio de teclas de movimento é um navio que se perdeu em busca do fim do mundo - acreditava-se na época que a terra fosse plana - enquanto se depara com a invasão de uma frota de navios piratas.  

## 🥅 Objetivo
> Piratas é um jogo de infinita duração enquanto o jogador principal conseguir se manter vivo. No entanto, a dificuldade aumenta á medida que a pontuação
do navio principal aumenta. Essa dificuldade crescente será feita na forma acréscimo na geração de navios inimgos e também em suas velocidades. O navio controlável possuirá mecânicas - descritas no próximo tópico - de modo a manter-se vivo pela maior duração de tempo. 

## 📐 Mecânicas
> Navio principal: aceleração apenas no sentido da proa com auxílio de rotação em ambos sentidos (horário e anti-horário); disparo de canhões para destruição da frota inimiga que utilizar-se-ão de princípios físicos de conservação de energia e de quantidade de movimento de modo a possibilitar ao navio um terceiro grau de liberdade em movimentação e adicionar jogabilidade com diversas estratégias de movimentação; carregamento de um especial baseado no tempo de utilização de um canhão de tamanho maior que tem maior poder destrutivo.; pode se deslocar de um lado tela para outro
>Frota inimiga: gerada aleatoriamente nos cantos da tela, e cada navio depois de gerado se movimenta em uma linha reta e elimina o personagem principal
em caso de colisão. A frota será composta de navios piratas e piratas propriamente ditos nadando em alto-mar. Caso o navio pirata seja destruído, o mesmo será dividido em dois piratas. Ambos são eliminados pelo personagem principal caso sejam atingidos por uma bala de canhão.


## ☕ Contribuidores

Este projeto foi realizado em colaboração com: Daniel Quintão(https://github.com/danielquintao), Giuseppe Vicente(https://github.com/giuseppevb) e Gustavo Beato(https://github.com/urc4)

## 🎨 Atribuições da arte usada

Veja ``data/License.txt``. Para a imagem de fundo do menu, temos uma [imagem de liuzishan no Freepik](https://br.freepik.com/fotos-gratis/pintura-digital-de-antigos-navios-de-guerra-viajando-em-mares-agitados_14402173.htm#query=guerra%20de%20navios&position=1&from_view=search&track=robertav1_2_sidr)

---
