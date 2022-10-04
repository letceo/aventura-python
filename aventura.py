################################# ACEITAS A AVENTURA?  por Letícia Oliveira     ####################################################

story = {};
story["start"] = ("Bem vindo ao teu maior pesadelo. Perdido na Floresta, tens de tomar uma série de decisões que vão ditar quem vive ou morre. Atreves-te a entrar nesta aventura?",\
["SIM","NÃO"],\
["1","2"])
#--------------------- Inicio aventura ou Inicio Rotina --------------------
story["1"] = ("Era só mais um árduo dia de trabalho, até deixar de o ser. Do nada, acordas na floresta, o céu está cinzento e uma grossa camada de neblina esconde tudo em teu redor. Tens duas opções; ",\
["Ganhar coragem, levantar e atrever a descobrir o caminho para casa","Continuar deitado. Deve ser só um pesadelo, tudo vai ficar bem....certo?"],\
["4","5"])

story["2"] = ("Deixa de ser cobarde e aprende a enfrentar os teus medos. O pesadelo já está a acontecer. Aceitas o desafio?",\
["SIM","NÃO"],\
["1","3"])
#---------------------- Rotina, mas opção aventura --------------------

story["3"] = ("Já que te recusas a fugir à rotina e viver uma aventura, quem sou eu, senão um mero computador, para te obrigar a fazer exatamente tudo o que quero. Se queres ser aborrecido e viver maaaaaaais um dia normal, vou cumprir o teu desejo. É isso que queres? Vamos lá começar. Ou preferes sair?",\
["VOLTAR À ROTINA","MUDEI DE IDEIAS. QUERO AVENTURA","POR FAVOR DEIXA-ME SAIR"],\
["6","start","7"])

#---------------------- Aventura - Arriscar ou Preguiça? --------------------
story["4"] = ("Não querendo aguentar mais um minuto sem saber o que se está a passar, finalmente decides levantar-te e resolver o mistério. Após olhar em teu redor, apesar da neblina, encontras o que parece ser o início de um caminho. Decides enfrentar os teus medos e descobrir o que se esconde em diante. Após uns minutos a caminhar, deparas-te com 3 caminhos: Um à esquerda, onde o nevoeiro se começa a dissipar, penetrado por raios de sol que mostram um caminho de pedra emoldurado por vegetação verdejante. Um caminho ao centro, a continuação do passeio onde estás com as mesmas condições atmosféricas. E um à direita, onde a neblina fica mais densa e escura, o ambiente mais aterrador, e das sombras consegues perceber árvores decrépitas com ramos nus como esqueletos. Por qual te decides aventurar?",\
["Caminho à esquerda, onde o sol brilha","Caminho ao centro. Onde estou não é muito mau, porquê arriscar?", "Caminho assustador à direita. Se é bravura ou estupidez não sei, mas as outras opções parecem demasiado fáceis... talvez uma armadilha?"],\
["8","9", "10"])

story["5"] = ("Esperando que tudo seja um pesadelo, decides continuar deitado, fechar os olhos e voltar a dormir. Passam-se algumas horas, e quanto abres os olhos tudo continua igual. E agora?",\
["*suspiro*, talvez seja melhor ganhar coragem e enfrentar os meus medos","Só mais uns minutinhos, tenho quase a certeza que é um pesadelo"],\
["4","11"])

#---------------------- Rotina - Determinado ou Preguiçoso / FIM COBARDE --------------------
story["6"] = ("Era só mais um árduo dia de trabalho. Mal o despertador toca, apressas-te a desligá-lo. Mas a cama está tão confortável.... De certeza que estás pronto para começar o teu dia?",\
["Sim, não tenho tempo para isto. Há muito para fazer hoje.","Hmmmm... ainda é cedo, só mais uns minutos."],\
["13","14"])

story["7"] = ("Já que quiseste arruinar tudo, Parabéns. Conseguiste. Estás feliz e livre da maldição. Volta lá para a tua rotina agora, já não tenho mais paciência para te aturar. Atingiste o FINAL 1",\
[], []) #FIM DA HISTÓRIA - FINAL 1#

#---------------------- AVENTURA - 3 CAMINHOS -------------------
story["8"] = ("Decides optar pelo caminho à esquerda. É o mais lógico e seria uma opção demasiado clichê para uma armadilha...certo? Pelo menos, o tempo está bom, a paisagem é bonita, e mesmo que não chegue ao fim, a jornada é que importa, e pelo menos esta está a ser agradável. Com o teu estado de espírito mais otimista e aliviado, o teu cansaço parece diminuir. O tempo passa despercebido, e ao fim de algum tempo, encontras um poço e uma mesa com um cesto de piquenique recheado com comida, fruta fresca e vinho. Aproximas-te.",\
["Beber a água do poço", "Comer o que está no cesto de piquenique", "Hmm, demasiado suspeito, prefiro continuar a andar."],\
["15","16", "17"])

story["9"] = ("Preferindo não arriscar, optaste pelo caminho em frente. Continuas a caminhar, e a caminhar, e a caminhar, e nada acontece. Olhas em volta, por entre a neblina, observas árvores, e pouco mais do que isso. De repente, um pensamento passa-te pela cabeça. Será que estás a andar em voltas?",\
["Talvez seja melhor voltar para trás...","Idiotice, todo este caminho, prefiro continuar a andar em frente", "Não será melhor sair do passeio e atravessar pelo meio das árvores?"],\
["20","21", "22"])

story["10"] = ("Enchendo-te de coragem, dás os teus primeiros passos em direção ao caminho da direita, onde tudo é mais escuro e assustador.  O profundo nevoeiro faz com que não consigas distinguir as formas que te rodeiam, só as árvores e o som do vento a passar. Á medida que vais caminhando mais na profundidade da floresta, começas a distinguir uivos e sons de animais. Eventualmente, uma a silhueta de uma mansão aparece à tua frente. É enorme, com dois pisos, e de aparência abandonada. O portão está aberto. Decides entrar? ",\
["Entrar na Mansão","Continuar a andar"],\
["23","9"])

#---------------------- AVENTURA PREGUIÇOSA - TERMINADA -------------------
story["11"] = ("Confiando nos teus instintos de que tudo era um pesadelo, decides voltar a dormir. Passam-se algumas horas. É agora noite profunda, e sentindo algo a mexer-se no fundo das tuas pernas.",\
["Abrir os olhos","Mexer a perna"],\
["12","19"])

story["12"] = ("Sem querer ver a ameaça que se aproxima, decides confiar em ti mesmo e abrir os olhos, confiante de que tudo estaria resolvido. Olhas em volta, e um sorriso aparece nos teus lábios à medida que te apercebes que à paisagem outrora à tua volta tinha desaparecido. Agora, no local da floresta assustadora, as paredes familiares do teu quarto e o conforto da tua cama ocupava-te os sentidos. Estavas em casa. Agora mais aliviado, decides encarar o que o dia te reserva. Começar a tua rotina, ou dar o jogo que é a vida por terminado?",\
["CONTINUAR O DIA","CHEGA DE AVENTURA POR HOJE"],\
["6","18"])

story["18"] = ("Felizmente tinha sido tudo um sonho. Confiaste nos teus instintos e tudo correu pelo melhor. Ou talvez, tenha sido tudo sorte. De qualquer forma, PARABÉNS. Sobreviveste e atingiste o FINAL 2.",\
[], []) #FIM DA HISTÓRIA - FINAL 2#

story["19"] = ("Ao sentires um movimento brusco no fundo do teu corpo, decides abanar as tuas pernas sem abrir os olhos, para afastar a ameaça. É provavelmente o teu cão que, ao ver o tempo passar, te decidiu acordar do teu sonho profundo para ver se estavas bem. Até que...  com horror, te apercebes que não podia ser o teu cão porque ele já não existia mais. Surgiu-te um peso no coração, a respiração tornou-se pesada, e os batimentos cardíacos acelerados. O que quer que tenhas afastado com as pernas momentos antes, não ficou feliz com a tua decisão. Os seus movimentos tornaram-se mais bruscos, e, finalmente decidiste abrir os olhos. Os teus instintos estavam errados. No fundo do teu corpo estava uma criatura da noite, um lobo gigante que, fixando os seus olhos avermelhados nos teus, cravou os seus dentes pontiagudos e chacinantes na tua carne. A dor era intensa, a pior que alguma vez sentiste. E nos teus últimos momentos, os mais dolorosos da tua vida, enquanto sentias cadan pedacinho teu ser arrancado e decimado por dentes selvagens na escuridão da floresta, pensaste  para ti mesmo 'E se eu não tivesse sido tão pouco cuidadoso e preguiçoso?'. PERDESTE - FINAL 3",\
[], []) #FIM DA HISTÓRIA - FINAL 3#

#---------------------- ROTINA ------------------- -PARADO POR AGORA
story["13"] = ("Cheio de coragem e força de vontade, decides levantar-te e começar o teu dia com tempo. Na hora de tomar o pequeno-almoço, hesitas:",\
["Tomar o Pequeno-Almoço em casa", "Tomar o pequeno-almoço pelo caminho", "Ver Televisão"],\
["84","85","86"])

story["14"] = ("Confortável no quentinho da tua cama, decides desligar o despertador e fechar os olhos, pensando para ti mesmo 'Só mais uns minutinhos'. Quanto dás por ti, já se passaram 20 minutos e está na hora de saíres de casa:",\
["Sair a correr","Sair normalmente e tomar pequeno-almoço pelo caminho", "Sair a passo normal"],\
["87","85", "89"]) 

story["84"] = ("Ainda com tempo, e para evitar qualquer confusão, sarilho ou chegar atrasado, optas por tomar o pequeno-almoço em casa. Pode ser aborrecido, mas ninguém disse que a vida precisava de tanta agitação e AVENTURA. Depois de tomares o pequenni-almolo, ainda tens algum tempo. Preferes:",\
["Ir calmamente para o trabalho", "Ir ao café na mesma", "Ver Televisão"],\
["89","85","86"])

story["85"] = ("Ainda com algum tempo optas por tomar o pequeno-almoço pelo caminho. Entras no teu café habitual, onde já conheces o barista e alguns dos clientes regulares. Pedes o teu pequeno-almoço habitual, e assim que o recebes vais para a tua mesa habitual. Enquanto tomas calmamente o pequeno-almoço, és abordado por um homem que já tinhas visto algumas vezes. Ele inicia uma conversa banal, sobre o tempo, o jogo de ontem, sobre as novidades do café, tudo assuntos habituais. Na tua hora de abandonar, tu e Homem despedem-se com um toque no ombro. 'Até à próxima disse ele.'. Apesar desta interação fora do habitual, o momento até correu bem - pensas. Decides continuar com a tua rotina.",\
["Ir para o trabalho calmamente","Ir para o trabalho apressado"],\
["start", "start"]) 

story["86"] = ("Como ainda tens tempo, decides aproveitar um momento para ver televisão. O que pode acontecer de mal certo? Ligas nas notícias locais. Esperando as rubricas habituais do telejornal ficas surpreendido a ver o que aparece no ecrã: 'ULTIMA HORA: Vários desaparecimentos tem acontecido nesta zona. Ainda não se conseguiu identificar o suspeito, mas até agora há pistas de vários avistamentos na floresta mais próxima. Tentamos saber mais mas até agora os nossos jornalistas ainda não voltaram com qualquer informação. Não houve sucesso nas tentativas de contacto a moradores. O coveiro da zona confirma vários corpos de desconhecidos têm aparecido no local, mas não conseguimos confirmar com 100 por cento de certeza a sua relação a este caso. Tenha cuidado'. Olhas para o relógio. O tempo de ir para o trabalho aproxima-se:",\
["Continuar a ver televisão","Ir para o trabalho"],\
["88", "89"]) 

story["87"] = ("Graças ao teu atraso, tens de sair de casa a correr para chegar a horas ao trabalho. Detestas estar atrasado. Nem sabes como é que deixaste isto acontecer, é tão fora da rotina. Sem tempo para mais nada, e sem tomar o pequeno-almoço, simplesmente sais de casa a correr, só focado numa coisa: Chegar ao trabalho. Infelizmente, no teu momento de pressa e aflição, esqueceste-te totalmente de prestar atenção ao que te rodeia e, sem te aperceberes, estás no meio da rua, a atravessar fora da passadeira. Nos teus últimos momentos de vida, viste um camião a alta velocidade a ir contra ti. O condutor também estar atrasado para alguma coisa. PERDESTE. Atingiste o final 14. Um conselho: É melhor perder um minuto da vida do que a vida num minuto.",\
[], []) #FIM DA HISTÓRIA - FINAL 14#

story["88"] = ("Após a notícia chocante deixas-te simplesmente ficar sentado, com demasiado medo sequer de sair de casa. Optas simplesmente por ficar em casa e vês televisão, esperando que ao longo do o telejornal local seja atualizado com mais informações da situação suspeita. Ao fim de algumas horas, recebes uma chamada do teu patrão. Reluntantemente atendes. Quando terminou, ficaste a contemplar o teto. Tinhas sido despedido. Mas ao menos, continuavas vivo. E por outro lado, ao menos vais ter de mudar de rotina. Quem sabe não haja um psicopata por aí algures que te tenha estado a observar e anotar a tua rotina para fazer de ti a próxima vítima?. ATINGISTE O FINAL 15. ",\
[], []) #FIM DA HISTÓRIA - FINAL 15#

story["89"] = ("Apesar de tudo, decidiste seguir com a tua rotina e vida e ir para o trabalho. Foi um dia normal. Fizeste a mesma coisa que absolutamente fazes todos os dias. Chegaste a casa, viste televisão sozinho e foste dormir. Nas notícias locais, dizia que mais uma pessoa tinha desaparecido. Do que é que interessa? É mais uma aventura em que não me apetece intrometer. Desligas a televisão e vais dormir. Para retomares exatamente a mesma rotina amanhã. Espero que estejas feliz. Quiseste ser aborrecido e escolher as opções aborrecidas então obviamente atingiste o FINAL 16- O MAIS ABORRECIDO. Nem te atrevas a considerar que ganhas o jogo, porque nunca chegaste a jogar.",\
[], []) #FIM DA HISTÓRIA - FINAL 16#

#---------------------- AVENTURA - CAMINHO DA ESQUERDA - POÇO -------------------

story["15"] = ("Cansado e com sede da longa caminhada ao sol, decides abençoar a tua sorte e aproveitar para te refrescar com a água. Assim que olhas para dentro do poço, preparando-te para pegar no balde e puxar o cesto com a água com a alavanca, reparas, no fundo do poço, num objeto à superficie:",\
["Ignorar o objeto e Beber a água do poço", "Tentar investigar e levantar o objeto com a alavanca do poço"],\
["68","69"])

story["16"] = ("Cansado e com fome da longa caminhada ao sol, decides aproveitar a tua sorte e ver o que está dentro do cesto. Lá dentro encontras uma vasta quantidade de comida para duas pessoas com doces e salgados, de muito bom aspeto, fruta fresca e uma garrafa de vinho. Antes de tomares uma decisão, decides refletir sobre o que fazer. Comer tudo agora ou deixar para depois?",\
["Comer Tudo o que está no cesto","Beber o Vinho e levar a comida contigo para depois", "Comer a Comida e levar o vinho para depois"],\
["75","76","77"])

story["17"] = ("Observando bem a cena à tua frente - um poço e um cesto de piquenique - decides questionar-te. Não será esta situação demasiado suspeita? Encontrar comida e bebida ao fim de uma longa e dura caminhada ao sol? Ou será uma miragem? De qualquer forma, decides não arriscar e continuar o teu caminho.",\
["Tentar investigar a zona para descobrir quem deixou o cesto","Continuar a andar em frente"],\
["64","12"])


#18 JÁ ESTÁ
#19 JÁ ESTÁ

story["68"] = ("Sem aguentar mais o sol escaldante, decides aproveitar o poço e saciar-te com a sua água refrescante. Agora com as energias renovadas, decides continuar o teu caminho. Ao fim de algumas horas a caminhar ao sol escaldante, o mundo à tua volta começa a desvanecer. As cores frescas da natureza dão lugar a visões psicadélicas das mais variadas cores; o caminho começa a girar, e em menos de 20 minutos estás deitado no chão a delirar. Num dos teus últimos pensamentos coerentes, ocorre-te que a água devia estar contaminada. 'Agora aquele sabor amargo faz sentido'-lembras-te de pensar antes de fechar os olhos pela última vez. PERDESTE. Atingiste o FINAL 8 ",\
[], []) #FIM DA HISTÓRIA - FINAL 8#

story["69"] = ("Intrigado com o objeto escondido no fundo do poço e com os segredos que ele esconde, optas por tentar puxá-lo para fora. Quem sabe, talvez seja a resposta para o mistério do teu desaparecimento. Agradecendo aos céus por todos os filmes e jogos de terror que mostram como funcionam os poços, decidiste aplicar esse conhecimento, ignorando provavelmente a mensagem principal dessas histórias de TERROR. Tudo parecia estar a correr bem, até o cesto do mecanismo ficar preço no tal objeto que, afinal, era bem maior do que aparentava. Mas não eras pessoa de desistir, então voltaste a insistir, puxando a alavanca com tal força que, graças à força da gravidade, acabaste por tropeçar para dentro do poço. A queda parecia nunca mais acabar, mas quando finalmente o teu corpo atingiu a água gelada, um fio de esperança preencheu a tua mente: talvez ainda houvesse salvação. Gritaste e gritaste, tentaste trepar o poço, mas nada funcionou. Agora preso, e sem mais nada para fazer decides investigar o tal objeto que te colocou nesta situação e que, ironicamente, tinha sido colocado para segundo plano. Mas assim que, ajustando o teu olhar à escuridão, pousaste os olhos no tal objeto, tudo se desmoronou. Era uma cabeça humana. Aliás, observando o que sobrava à tua volta, no meio da água de aparência não tão cristalina, submergiam várias partes humanas e esqueletos. Mais uma vez, tentaste escapar, mas ninguém te ouviu. Passado alguns dias, no meio da podridão, falta de água e comida, e consumido por tóxicos, acabaste por te juntar aos teus amigos do poço no doce embraço da morte. PERDESTE. FINAL 9",\
[], []) #FIM DA HISTÓRIA - FINAL 9#

#---------------------- AVENTURA - CAMINHO EM FRENTE - VOLTAS -------------------

story["20"] = ("Cansado de andar às voltas, decides voltar para trás, e achar o cruzamento por onde tinhas passado anteriormente. Após algum tempo a caminhar, ao contrário do que estavas à espera não encontraste o cruzamento onde tinhas iniciado o teu percurso, mas, talvez por influência do destino, tenhas encontrado algo ainda melhor. Da floresta escurecida pela neblina começam a emergir raios de sol, e dás por ti no passei de pedra, no local da vegetação verde reconfortante. Era um local mais verde e aberto à natureza, com uma mesa de piquenique no centro e um poço. Decides investigar.",\
["Beber água do Poço", "Investigar mesa de Piquenique"],\
["15","64"])

story["21"] = ("Pensando em todo o caminho que até agora percorreste, voltar para trás não parecia a melhor ideia. E quem sabe o que se esconderia no interior da floresta. Optaste então pela última solução: Caminhar em frente. Ao fim do que parecem ser horas a caminhar, com o céu já escuro e um nevoeiro denso e cinzento, deparas-te com uma espécie de jardim, rodeado por grades metalizadas escuras. Decides entrar e descansar, com esperança de encontrar um banco onde pudesses repousar o resto da noite. E quem sabe, normalmente um jardim no meio da floresta indica civilização já próxima!",\
["Dormir","Continuar a andar"],\
["70","71"])

story["22"] = ("Cansado de andar às voltas, e com receio de voltar para trás e ficar sem energia, acabas por tentar fugir do caminho na esperança de encontrar outro caminho, ou pelo menos, civilização algures com alguém capaz de te ajudar. Passado uns minutos, dás por ti numa zona nova da floresta, rodeado por árvores e arbustos, mas o que capta a tua atenção é uma pequena gruta no limiar do terreno. Decides aproximar-te, pensando que no pior dos casos serviria de abrigo na noite escura que se aproximava. Mas és interrompido por um rosnas nas proximidades. Decides investigar e deparas-te com um pequeno lobo:",\
["Fugir para a floresta","Aproximar do Lobo", "Assustar o Lobo"],\
["60","61"])

story["60"] = ("Com medo de ser devorado pelo Lobo a apenas alguns metros de ti, optas por te virar e desatar a correr o mais rápido possível em direção às profundezas da floresta. Agora, estás totalmente perdido, rodeado por árvores de folhagem vasta e escura. Em pânico, tentas relembrar-te de alguns dos ensinamentos dos tempos dos escuteiros, mas só um te passava pela cabeça: Prestar atenção aos sentidos. Decides, então, ficar atento aos sons,  tentando perceber qual o melhor caminho a seguir:",\
["Seguir a melodia dos pássaros a cantar","Seguir o aroma a carne assada", "Seguir o toque do Sino"],\
["74","80", "78"])

story["61"] = ("Perante a visão do adorável animal selvagem, o teu primeiro instinto foi imobilizar-te, para não assustares o animal com nenhum reflexo brusco. Ao ver que o seu olhar passara de susto e ameaça, para mera curiosidade, em passos lentos e suaves decides aproximar-te muito  cuidadosamente. Ao mesmo tempo, a criatura fazia o mesmo, até se encontrarem a meio do caminho. Sem te ver como uma ameaça, o lobo continuou a aproximar-se, e ao contrário do que esperavas, enroscou-se no teu corpo como que a oferecer a  sua amizade. A partir deste momento, ganhaste um fiel companheiro nesta aventura de vida ou morte. ",\
["Adotar o Lobo","Abandonar o Lobo", "Atacar o Lobo"],\
["65","63","62"])

story["62"] = ("Perante a visão da criatura aparentemente feroz, o teu primeiro instinto, sem pensar duas vezes graças ao choque de adrenalina foi, numa atitude de defesa, pegar na maior pedra à tua volta e atirá-la na direção do lobo. Infelizmente, com horror, passado uns segundos, apercebeste-te que foi uma reação muito estúpida e que provocou exatamente o efeito contrário. A criatura anteriormente assustada apresentada agora uma posição de ataque. Em poucos segundos, sentiste um grupo de unhas afiadas e dentes cravarem-se na tua carne, enquanto que um corpo pesado e felpudo se atirava oara cima de ti, tentando desfazer cada pedaço do teu corpo. Em pouco tempo, para além de toda a dor dos ferimentos, começaste a esvair-te em sangue, no que queria uma morte bastante dolorosa. PERDESTE. Atingiste o FINAL 5. Conclusão - não maltrates animais.",\
[], []) #FIM DA HISTÓRIA - FINAL 5#

story["63"] = ("Apesar do adorável momento com o Lobo, e da repentina oferta de amizade, decidis-te recusar e continuar a andar. Adotar um Lobo desconhecido na floresta parece ser uma atitude um pouco impulsiva e que pode ter consequências drásticas na tua vida... ou morte. Com esta decisão tomada, decidiste-te continuar caminho pela floresta, ignorando os últimos acontecimentos. Eventualmente, dás por ti numa zona mais escura e assustadora da floresta. O profundo nevoeiro faz com que não consigas distinguir as formas que te rodeiam, só as árvores e o som do vento a passar. Á medida que vais caminhando mais na profundidade da floresta, começas a distinguir uivos e sons de animais. Eventualmente, uma a silhueta de uma mansão aparece à tua frente. É enorme, com dois pisos, e de aparência abandonada. O portão está aberto. Decides entrar?",\
["Entrar na Mansão","Continuar a andar"],\
["23","74",])

story["65"] = ("Após encontrares o teu novo amigo na floresta, na sua companhia decidiste retomar a aventura e tentar encontrar o caminho para casa, ou pelo menos, alguma forma de resolver o mistério. Menos assustado e com um melhor estado de espírito graças ao novo companheiro, decides voltar a caminhar pela floresta. Eventualmente, dás por ti numa zona mais escura e assustadora da floresta. O profundo nevoeiro faz com que não consigas distinguir as formas que te rodeiam, só as árvores e o som do vento a passar. Á medida que vais caminhando mais na profundidade da floresta, começas a distinguir uivos e sons de animais. Eventualmente, uma a silhueta de uma mansão aparece à tua frente. É enorme, com dois pisos, e de aparência abandonada. O portão está aberto. Decides entrar? ",\
["Entrar na Mansão","Continuar a andar"],\
["25","74"])

story["64"] = ("Decides aproximar-te da mesa de Piquenique, para ver se conseguias encontrar alguma comida que te repusesse as forças da longa caminhada que até agora tinhas feito. Infelizmente, o cesto estava vazio,e à medida que olhas em teu redor, encontras vários alimentos no chão. 'Deve ter sido algum animal que ande por aqui' - pensas. Desanimado, pôes-te pronto para iniciar caminho, até que do canto do olho vês um quintal. Decides aproximar-te, pronto a pedir ajuda para retornar para casa. Até que, mal te aproximas do portão, vês uma cena mórbida de chocar qualquer pessoa: do outro lado da cerca, consegues identificar os corpos do que aparenta ser um casal, totalmente chacinados. Dos poucos minutos que olhaste, pareciam esfaqueados, e com algumas partes do corpo a faltar. Agora uma coisa era certa. Era preciso sair daqui e encontrar o caminho para casa - o mais rapidamente possível.",\
["Fugir", "Entrar dentro da casa"],\
["66","67"])

story["66"] = ("No meio do choque, desatas a correr. Infelizmente, a falta de alimento e água, associado ao estado de adrenalina, fez com que não aguentasses mais. No meio da correria, tropeças numa pedra, bates com a cabeça e perdes os sentidos. Acabas por morrer devido à perda de sangue. PERDESTE. Atingiste o Final 6.",\
[], []) #FIM DA HISTÓRIA - FINAL 6#

story["67"] = ("Após a visão chocante, tentas decidir o melhor plano de ação. Entrar em pânico provavelmente só levaria a mais problemas, e neste momento o importante é sobreviver e chegar a casa. Para além de alertar as autoridades para resolver o mistério. Optas por entrar dentro da casa do recém-falecido casal. Logo à entrada deparas-te com um telefone, e marcas o número das autoridades. Em pouco tempo, uma equipa de socorro apressa-se a levar-te a casa, enquanto tentam resolver o crime que tinha acabado de acontecer. Parabéns. Sobreviveste e chegaste ao fim. Conseguiste o Final 7.",\
[], []) #FIM DA HISTÓRIA - FINAL 7

story["70"] = ("Sem saber o que te reservaria para o dia seguinte, e com medo da noite que se aproximava, optaste por te deitar no banco e ganhar forças. Apesar da exaustão, demorou um pouco para pegar o sono, mas quando finalmente entraste no mundo dos sonhos, era dificil sair. Com toda esta agitação, o teu subconsciente parecia também ter sido afetado. As imagem que dominavam o teu estado imaginativo era de figuras de briçho branco semi translúcidas que tentatvam comunicar-te uma mensagem que não conseguias apanhar. 'Encontra-me na água', era o que pareciam dizer, mas não parecia fazer grande sentido. Eventualmente, o sonho parecia tornar-se mais real, tinhas a sensação de levitar... seria das criaturas pseudo-fantasmagóricas? ",\
["Confiar nos fantasmas","Acordar"],\
["72","73"])

story["71"] = ("Com receito de adormecer e nunca mais acordar, optaste por continuar o teu caminho. A este ponto, estavas só a suprimir toda a tua dor e exaustão, tinhas só um objetivo em mente: sobreviver e voltar para casa e para a tua confortável ROTINA. Enquanto caminhavas pelo jardim misterioso, olhando em volta para captar tudo o que te rodeava, toda as pesquenas pistas, mas também a beleza natural do local, acabas por te aperceber que afinal não era um jardim, mas sim um cemitério, enquadrado no ambiente florestal. Ao longe, voltas a ouvir a melodia do sino. Segues o som e apercebes-te de uma pequena capela escondida na vegetação. Sorriste. Talvez ainda haja salvação. Bates à porta, e és recebido um um idoso desconhecido. Ele olha para ti com surpresa mas recebe-te calorosamente. Não é costume receber visitantes nesta zona remota, e ultimamente aparecem mais os vivos que mortes. Oferece-te comida quente e bebida, e com a receção calorosa sentes a tua alma regenerar. No fim da refeição, começa a conversa séria, enquanto tu explicas a situação em que te encontraste, e ele responde com a história trágica da floresta. Já há vários anos que vários corpos têm sito encontrados nas redondezas. Ora mortos por criaturas selvagens, alguns violentamente desmembrados, outros mortos pelo frio e pela fome. De onde os corpos vêm, ninguém sabe, provavelmente de fugitivos, vítimas ou raptados, mas tudo parece estar conectado a uma única casa na floresta. Quando explicaste que também tu tinhas vindo parar à floresta sem saber como, apercebeste-te do terror a que tinhas escapado. 'És o primeiro sobrevente até agora, talvez ainda haja esperança.' - disse o homem. Após a refeição, não tardaram a ligar às autoridades. Talvez ainda fosse possível de resolver este mistério. PARABENS. VENCESTE. Não só conseguiste sobreviver como ajudar a resolver o mistério. Atingiste o FINAL 11. ",\
[], []) #FIM DA HISTÓRIA - FINAL 11

story["72"] = ("Decides confiar na experiência fantasmagórica e continuar a dormir. Afinal, até agora as criaturas pareciam afáveis, e por estranho que pareça, as suas mensagens misteriosas pareciam dar-te pistas sobre como sair do pesadelo. Após a sensação de levitar, veio outra muito menos agradável, a sensação de cair interminável. Mas esta, parecia mais real... e dolorosa. Após o momento de embate, o teu sonho tornou-se ainda mais pesado, mas também mais desfocado. Parecias ouvir vozes à distância, mas sem conseguir fazer sentido do que diziam. Quando passado algum tempo indeterminado recuperaste os sentidos, tentaste abrir os olhos, mas só a escuridão te rodeava? Estarias ainda a dormir? O ar parecia também tornar-se mais pesado e escasso, dificil de respirar. Tentaste-te mexer, mas parecias confinado, como se preso numa caixa. Os teus movimentos de nada serviram. Tentaste gritar, dar pontapés e murros, arranhar as paredes, tudo para sair do que quer que te estivesse a prender. Mas nada serviu. Eventualmente, morreste por falta de ar, assustado e sozinho, numa caixa de madeira que mais se assemelhava a um caixão. Alguns metros acima, um homem idoso olhava para o buraco na terra que tinha acabado de tapar, enquanto o Sino da capela anunciava a mais recente morte. À sua frente, uma lápide improvisada em madeira dizia 'Aqui jaz o jovem desconhecido, com a vida tirada pela gélida da noite'. Mal sabia ele, que responsável pela tua morte não era a calada da noite, mas sim o sufoco por ter sido enterrado vivo. PERDESTE. Atingiste o FINAL 10. Sugestão para o futuro: Não adormeças num banco de cemitério.",\
[], []) #FIM DA HISTÓRIA - FINAL 10

story["73"] = ("Assustado por toda a tua nova experiência inconsciente, e desejoso de pôr um fim aos teus pesadelos: reais e imaginários, decides pôr um fim à experiência fantasmagórica da levitação que tinhas acabado de experienciar, que parecia demasiado real. Optas então por acordar e finalmente abrir os olhos para o que te esperava. Mas o que a tua visão te trouxe, surpreendeu-te mais do que quer que tinhas presenciado até agora: um idoso desconhecido carregava-te num carrinho de mão. Ao menos a sensação de levitar estava agora explicada. No teu estado de surpresa, tentaste-te levantar e questionar sobre o que se estava a passar. Após uns momentos de choque por parte do desconhecido, que soltou um grito de surpresa e largou o carrinho que te levava, acabando tu por cair ao chão do que parecia ser na verdade, um cemitério, e não tanto um jardim como inicialmente pensavas, o homem ajudou-te a levantar e não tardou a dar-te uma explicação, pensando que eras apenas mais um dos mortos e preparando para te enterrar. Levou-te a uma pequena capela, escondida no fundo do cemitério. Agora sentado, no quentinho, a saborear uma refeição e um copo de chá, ouvias a explicação para todas as tuas dúvidas, ao mesmo tempo que expunhas o que te tinha acontecido. No momento de conversa, o homem conta-te a história trágica da floresta. Já há vários anos que vários corpos têm sito encontrados nas redondezas. Ora mortos por criaturas selvagens, alguns violentamente desmembrados, outros mortos pelo frio e pela fome. De onde os corpos vêm, ninguém sabe, provavelmente de fugitivos, vítimas ou raptados, mas tudo parece estar conectado a uma única casa na floresta. Quando explicaste que também tu tinhas vindo parar à floresta sem saber como, apercebeste-te do terror a que tinhas escapado. 'És o primeiro sobrevente até agora, talvez ainda haja esperança.' - disse o homem. Após a refeição, não tardaram a ligar às autoridades. Talvez ainda fosse possível de resolver este mistério. PARABENS. VENCESTE. Não só conseguiste sobreviver como ajudar a resolver o mistério. Atingiste o FINAL 11. ",\
[], []) #FIM DA HISTÓRIA - FINAL 11

story["74"] = ("Optas por continuar a caminhar, seguindo a melodia dos pássaros a cantar, até seres conduzido a uma zona da floresta de aparência reconfortante. Era um local mais verde e aberto à natureza, com uma mesa de piquenique no centro e um poço. Decides investigar.",\
["Beber água do Poço", "Investigar mesa de Piquenique"],\
["15","64"])

story["75"] = ("Após analisar os conteúdos no interior do cesto do piquenique, decides aproveitar e comer tudo sem hesitar. Afinal, quem poderia recusar uma oportunidade daquelas? Com a energia restaurada, e um bocado mais alegre com a situção, decides continuar o teu caminho.",\
["Seguir o toque do sino", "Seguir o cheiro a carne assada"],\
["78","64"])

story["76"] = ("Após analisar os conteúdos no interior do cesto do piquenique, decides deixar a comida de lado, e beber apenas o conteúdo da garrafa, porque ao menos esta estava selada, então mais dificilmente seria enveneada, ao contrário do que quer que possa estar escondido na comida deixada ao ar livre que, admitindo a verdade, parece ser um pouco suspeito. Como se alguém nas redondezas estivesse pronto a fazer um piquenique, mas que por qualquer motivo aterrador, tenha decidido desaparecer misteriosamente e deixá-lo para trás. Ou talvez, algo lhes tenha acontecido? Afinal, quem é que deixaria umc esto de piquenique totalmente abandonado. Ainda com fome, mas um bocado mais alegre com a situção, decides continuar o teu caminho.",\
["Seguir o toque do sino", "Seguir o cheiro a carne assada"],\
["79","80"])

story["77"] = ("Após analisar os conteúdos no interior do cesto do piquenique, decides deixar a comida de lado, e levar a garrafa contigo. Isto porque ao menos esta estava selada, então mais dificilmente seria enveneada, ao contrário do que quer que possa estar escondido na comida deixada ao ar livre que, admitindo a verdade, parece ser um pouco suspeito. Como se alguém nas redondezas estivesse pronto a fazer um piquenique, mas que por qualquer motivo aterrador, tenha decidido desaparecer misteriosamente e deixá-lo para trás. Ou talvez, algo lhes tenha acontecido? Afinal, quem é que deixaria um cesto de piquenique totalmente abandonado? De qualquer forma, agora não parecia a melhor altura para beber, as tuas capacidades de sobrevivência tinham de estar ao máximo certo? E seria melhor para festejar assim que chegasses a casa. Com a garrafa de vinho no bolso, decidiste continuar o teu caminho.",\
["Seguir o toque do sino", "Seguir o cheiro a carne assada"],\
["78","82"])

story["78"] = ("Optas por continuar a caminhar, seguindo o toque do sino. Ao fim do que parecem ser horas a caminhar, com o céu já escuro e um nevoeiro denso e cinzento, deparas-te com uma espécie de jardim, rodeado por grades metalizadas escuras. Decides entrar e descansar, com esperança de encontrar um banco onde pudesses repousar o resto da noite. E quem sabe, normalmente um jardim no meio da floresta indica civilização já próxima!",\
["Dormir","Continuar a andar"],\
["70","71"])

story["79"] = ("Optas por continuar a caminhar, seguindo o toque do sino. Ao fim do que parecem ser horas a caminhar, com o céu já escuro e um nevoeiro denso e cinzento, deparas-te com uma espécie de jardim, rodeado por grades metalizadas escuras. Ao fim de algum tempo a caminhar, ainda eufórico pela bebida que tinhas consumido, cujo efeito continuava ainda bastante forte, começaste-te a aperceber do que te rodeava, flora selvagem e umas pedras com inscrições no meio... que decoração esquisita para um jardim? Decidiste aproximar-te para leres o que dizia. 'Aqui jaz o corpo do jovem desconhecido ...'. O resto das letras pareciam estar a dançar, não conseguias fazer sentido do que dizia. Tentaste-te baixar para fazer sentido do resto das palavras, mas infelizmente, sem prestar atenção onde punhas os pés, acabaste por cair no grande buraco de terra destapada mesmo ao lado da lápide. PERDESTE. Atingiste o FINAL 12. Da próxima vez aconselho-te a teres cuidado com o que pôes no organismo para não acabares com os pés na cova.",\
[], []) #FIM DA HISTÓRIA - FINAL 12

story["80"] = ("Optas por continuar a caminhar, seguindo o delicioso aroma a carne assada. Eventualmente, dás por ti numa zona mais escura e assustadora da floresta. O profundo nevoeiro faz com que não consigas distinguir as formas que te rodeiam, só as árvores e o som do vento a passar. Á medida que vais caminhando mais na profundidade da floresta, começas a distinguir uivos e sons de animais. Eventualmente, uma a silhueta de uma mansão aparece à tua frente. É enorme, com dois pisos, e de aparência abandonada. O portão está aberto. Decides entrar? ",\
["Entrar na Mansão","Continuar a andar"],\
["23","9"])

story["81"] = ("Optas por continuar a caminhar, seguindo o delicioso aroma a carne assada. Eventualmente, dás por ti numa zona mais escura e assustadora da floresta. O profundo nevoeiro faz com que não consigas distinguir as formas que te rodeiam, só as árvores e o som do vento a passar. Á medida que vais caminhando mais na profundidade da floresta, começas a distinguir uivos e sons de animais. Eventualmente, uma a silhueta de uma mansão aparece à tua frente. É enorme, com dois pisos, e de aparência abandonada. O portão está aberto. No teu estado de euforia, todo o teu possível receio de entrar numa mansão abandonada tinha-se dissipado, pois o teu único pensamento neste momento era descobrir de onde vinha o delicioso aroma. Entras na casa sem pensar duas vezes e dás por ti numa cozinha, a origem do cheiro. Lá, encontras um Homem, em estado de choque por te ver ali. O seu aspeto era assustador, tinha na mão uma faca gigante, pedaços enormes de carne em cima da mesa, e a roupa toda ensanguentada. Do nada ele adquire uma postura de ataque, murmurando apenas 'Tu ainda não devias estar acordado. Como é que já estás aqui?' Agora com medo, tentas fugir, mas infelizmente o álcool no teu organismo afetou os teus movimentos, reflexos e tempo de reação. O agressor não tardou a aproximar-se, saltou para cima de ti. Nem tens tempo de reagir. Ele apanha-te, e antes de te aperceberes, a luta está já perdida. Fraco, desidratado e sem companhia, morres às mãos do homem, que com a faca acaba o serviço e a tua aventura. PERDESTE - Final 13  ",\
[], []) #FIM DA HISTÓRIA - FINAL 13

story["82"] = ("Optas por continuar a caminhar, seguindo o delicioso aroma a carne assada. Eventualmente, dás por ti numa zona mais escura e assustadora da floresta. O profundo nevoeiro faz com que não consigas distinguir as formas que te rodeiam, só as árvores e o som do vento a passar. Á medida que vais caminhando mais na profundidade da floresta, começas a distinguir uivos e sons de animais. Eventualmente, uma a silhueta de uma mansão aparece à tua frente. É enorme, com dois pisos, e de aparência abandonada. O portão está aberto. Decides entrar? ",\
["Entrar na Mansão","Continuar a andar"],\
["24","9"])

story["83"] = ("Achando toda a situação do cesto de piquenique demasiado suspeita, afastas-te o mais daquela zona possível até chegares a uma zona mais profunda da floresta. Apercebes-te que estás perdido. Decides então dar vida aos teus ensinamentos dos escuteiros e prestar atenção aos teus sentidos para descobrir o melhor caminho:",\
["Seguir o aroma a carne assada", "Seguir o toque do Sino"],\
["80", "78"])


#---------------------- AVENTURA - CAMINHO DIREITA - MANSÃO -------------------

#RONDA 1
story["23"] = ("Após uma pausa para respirar fundo, decides entrar na mansão. Totalmente sozinho, sem comida ou bebida, não sabes quanto mais tempo és capaz de durar, então focas os teus esforços em encontrar um telefone para ligar para a família, ou encontrar alguém que te dê informações ou leve a casa.  A mansão é enorme, a porta está aberta, o chão de madeira desgastado range a cada passo, e não sabes por onde começar. ",\
["Investigar a Sala", "Investigar a Cozinha", "Investigar o Quarto"],\
["26","35", "38"]) #normal

story["24"] = ("Após uma pausa para respirar fundo, decides entrar na mansão. Totalmente sozinho, não sabes quanto mais tempo és capaz de durar, então focas os teus esforços em encontrar um telefone para ligar para a família, ou encontrar alguém que te dê informações ou leve a casa.  A mansão é enorme, a porta está aberta, o chão de madeira desgastado range a cada passo, e não sabes por onde começar. ",\
["Investigar a Sala", "Investigar a Cozinha", "Investigar o Quarto"],\
["27","36", "45"]) #bebado

story["25"] = ("Agora com a companhia do teu novo amigo Lobo, decides entrar na mansão. Totalmente sozinho, sem comida ou bebida, não sabes quanto mais tempo és capaz de durar, então focas os teus esforços em encontrar um telefone para ligar para a família, ou encontrar alguém que te dê informações ou leve a casa.  A mansão é enorme, a porta está aberta, o chão de madeira desgastado range a cada passo, e não sabes por onde começar. Já o teu companheiro parece ter outros planos. Bastante inquieto, tenta dar passos na direção do jardim, mas primeiro olha para ti para permissão:",\
["Investigar a Sala", "Investigar a Cozinha", "Investigar o Quarto", "Seguir o Lobo para o Jardim"],\
["28","37", "46", "47"]) #lobo

#INVESTIGAR SALA

story["26"] = ("Após breves segundos, decides que terias melhor chances de encontrar informações na Sala. Ao olhar encontras a divisão num estado de profunda desarrumação. A mobília é antiga, escura, com alguns sinais de degradação. Na mesa central, vários recortes de jornais aparecem espalhados. O sofá tem aparentes sinais de ter sido usado recentemente. Mas tudo passa para segundo plano quando encostado à parede vês um telefone. Aproveitas a ocasião para ligar alguém, ou será melhor investigar o resto?",\
["Ligar para alguém", "Investigar a Cozinha", "Investigar o Quarto", "Investigar Jornais"],\
["29","35", "40","32"])#normal

story["27"] = ("Após breves segundos, decides que terias melhor chances de encontrar informações na Sala. Ao olhar encontras a divisão num estado de profunda desarrumação. A mobília é antiga, escura, com alguns sinais de degradação. Na mesa central, vários recortes de jornais aparecem espalhados. O sofá tem aparentes sinais de ter sido usado recentemente. Mas tudo passa para segundo plano quando encostado à parede vês um telefone. Aproveitas a ocasião para ligar alguém, ou será melhor investigar o resto?",\
["Ligar para alguém", "Investigar a Cozinha", "Investigar o Quarto", "Investigar Jornais"],\
["30","36","42", "33"])#bebado

story["28"] = ("Após breves segundos, decides que terias melhor chances de encontrar informações na Sala. Ao olhar encontras a divisão num estado de profunda desarrumação. A mobília é antiga, escura, com alguns sinais de degradação. Na mesa central, vários recortes de jornais aparecem espalhados. O sofá tem aparentes sinais de ter sido usado recentemente. Mas tudo passa para segundo plano quando encostado à parede vês um telefone. Aproveitas a ocasião para ligar alguém, ou será melhor investigar o resto?",\
["Ligar para alguém", "Investigar a Cozinha", "Investigar o Quarto", "Investigar Jornais"],\
["31","37", "41","34"])#lobo

story["29"] = ("Apesar da tua curiosidade em ler os jornais, decides que o melhor plano de ação seria ligar para alguém que te pudesse ajudar. Marcas o número da casa dos teus pais, mas assim que atendem do outro lado e começas a falar, provavelmente atraído pelo som da tua voz, ouves os passos de um homem a dirigir-se na tua direção. Mal tens tempo de te despedir e desligar o telefone, quando vês um homem de aparência furiosa, com manchas vermelhas na roupa e uma faca na mão a caminhar apressadamente na tua direção. Mal tens tempo de reagir:",\
["Fugir da Casa", "Lutar com o Homem"],\
["49","40"])#normal

story["30"] = ("Apesar da tua curiosidade em ler os jornais, decides que o melhor plano de ação seria ligar para alguém que te pudesse ajudar. Marcas o número da casa dos teus pais, mas assim que atendem do outro lado e começas a falar, provavelmente atraído pelo som da tua voz, ouves os passos de um homem a dirigir-se na tua direção. Mal tens tempo de te despedir e desligar o telefone, quando vês um homem de aparência furiosa, com manchas vermelhas na roupa e uma faca na mão a caminhar apressadamente na tua direção. Mal tens tempo de reagir:",\
["Fugir da Casa", "Bater com a garrafa de vinho na cabeça do homem"],\
["50","42"])#bebado

story["31"] = ("Apesar da tua curiosidade em ler os jornais, decides que o melhor plano de ação seria ligar para alguém que te pudesse ajudar. Marcas o número da casa dos teus pais, mas assim que atendem do outro lado e começas a falar, provavelmente atraído pelo som da tua voz, ouves os passos de um homem a dirigir-se na tua direção. Mal tens tempo de te despedir e desligar o telefone, quando vês um homem de aparência furiosa, com manchas vermelhas na roupa e uma faca na mão a caminhar apressadamente na tua direção. Mal tens tempo de reagir:",\
["Fugir da Casa","Ordenar Lobo para atacar o homem"],\
["51","41"])#lobo

story["32"] = ("Antes de pegares no telefone, com medo de que alguém te pudesse ouvir, sentes-te, em vez disso, atraído pelos jornais pousados em cima da mesa. Mal pegas neles, consegues identificar um tema comum: Adultos desaparecidos, cujos corpos são encontrados desmembrados no meio da floresta. São vários o conjunto desses artigos, todos recortados e com anotações a vermelho: 'Tratar dos Vizinhos - Feito','Atenção a visitantes para piqueniques','Usar drogas mais fortes', 'Usar mais Sal e Pimenta para o próximo', e várias igualmente aterrorizantes apareciam espalhadas. Um único pensamento passava na tua cabeça: Tenho de escapar desta casa. Infelizmente, a fuga  foi interrompida por passos que se aproximavam cada vez mais. E de repente, um homem com manchas vermelhas na roupa, de faca na mão e aparência furiosa, caminhava na tua direção.'",\
["Fugir da Casa", "Lutar com o Homem"],\
["43","40"])#normal

story["33"] = ("Antes de pegares no telefone, com medo de que alguém te pudesse ouvir, sentes-te, em vez disso, atraído pelos jornais pousados em cima da mesa. Mal pegas neles, consegues identificar um tema comum: Adultos desaparecidos, cujos corpos são encontrados desmembrados no meio da floresta. São vários o conjunto desses artigos, todos recortados e com anotações a vermelho: 'Tratar dos Vizinhos - Feito','Atenção a visitantes para piqueniques','Usar drogas mais fortes', 'Usar mais Sal e Pimenta para o próximo', e várias igualmente aterrorizantes apareciam espalhadas. Um único pensamento passava na tua cabeça: Tenho de escapar desta casa. Infelizmente, a fuga  foi interrompida por passos que se aproximavam cada vez mais. E de repente, um homem com manchas vermelhas na roupa, de faca na mão e aparência furiosa, caminhava na tua direção.'",\
["Fugir da Casa", "Ordenar Lobo para atacar o homem"],\
["48","41"])#lobo

story["34"] = ("Antes de pegares no telefone, com medo de que alguém te pudesse ouvir, sentes-te, em vez disso, atraído pelos jornais pousados em cima da mesa. Mal pegas neles, consegues identificar um tema comum: Adultos desaparecidos, cujos corpos são encontrados desmembrados no meio da floresta. São vários o conjunto desses artigos, todos recortados e com anotações a vermelho: 'Tratar dos Vizinhos - Feito','Atenção a visitantes para piqueniques','Usar drogas mais fortes', 'Usar mais Sal e Pimenta para o próximo', e várias igualmente aterrorizantes apareciam espalhadas. Um único pensamento passava na tua cabeça: Tenho de escapar desta casa. Infelizmente, a fuga  foi interrompida por passos que se aproximavam cada vez mais. E de repente, um homem com manchas vermelhas na roupa, de faca na mão e aparência furiosa, caminhava na tua direção.'",\
["Fugir da Casa", "Bater com a garrafa de vinho na cabeça do homem"],\
["44","42"])#bebado

#INVESTIGAR COZINHA
story["35"] = ("Após breves segundos, decides que terias melhor chances de encontrar informações na Cozinha. Mal entras na divisão, sentes o teu corpo ficar paralisado. Na cozinha antiga, só três coisas se destacam: o sangue nas paredes, o que aparenta ser um pedaço de carne ensanguentado na mesa, e um homem com uma faca, em posição de choque, a olhar para ti surpreso. 'Tu ainda não devias estar acordado' - ouves o homem dizer, enquanto este se prepara para correr na tua direção. Enquanto isso, na tua mente, tentas ver qual a melhor opção para sobrevivência:",\
["Fugir da Casa", "Lutar com o Homem"],\
["43","40"])#normal

story["36"] = ("Após breves segundos, decides que terias melhor chances de encontrar informações na Cozinha. Mal entras na divisão, sentes o teu corpo ficar paralisado. Na cozinha antiga, só três coisas se destacam: o sangue nas paredes, o que aparenta ser um pedaço de carne ensanguentado na mesa, e um homem com uma faca, em posição de choque, a olhar para ti surpreso. 'Tu ainda não devias estar acordado' - ouves o homem dizer, enquanto este se prepara para correr na tua direção. Enquanto isso, na tua mente, tentas ver qual a melhor opção para sobrevivência:",\
["Fugir da Casa", "Lutar com o Homem", "Ordenar Lobo para atacar o homem"],\
["48","41"])#lobo

story["37"] = ("Após breves segundos, decides que terias melhor chances de encontrar informações na Cozinha. Mal entras na divisão, sentes o teu corpo ficar paralisado. Na cozinha antiga, só três coisas se destacam: o sangue nas paredes, o que aparenta ser um pedaço de carne ensanguentado na mesa, e um homem com uma faca, em posição de choque, a olhar para ti surpreso. 'Tu ainda não devias estar acordado' - ouves o homem dizer, enquanto este se prepara para correr na tua direção. Ao teu lado, o teu Lobo pôe-se en posição de ataque à espera do sinal. Enquanto isso, na tua mente, tentas ver qual a melhor opção para sobrevivência:",\
["Fugir da Casa", "Lutar com o Homem", "Bater com a garrafa de vinho na cabeça do homem"],\
["44","42"])#bebado

#INVESTIGAR QUARTO
story["38"] = ("Após breves segundos, decides que terias melhor chances de encontrar informações no Quarto. Ao olhar encontras a divisão num estado de profunda desarrumação. A mobília é antiga, escura, com alguns sinais de degradação. Mas na parede, algo captou a tua atenção. Era um quadro com um esquema, repleto de fotografias de adultos, e várias informações biográficas. Alguns deles, com um X vermelho marcado a delimitar cruzar a fotografia. Após melhor análise, reparas que uma fotografia tua, assim como o teu nome, idade, local de trabalho e rotina, incluindo o sítio onde vais tomar o pequeno-almoço ocasionalmente aparecem também lá escritos.  Um tremor percorre-te a espinha: Definitvamente, quem morava nesta casa era responsável pelo teu desaparecimento. Ainda chocado com a descoberta, não consegues deixar de pensar no que mais poderias descobrir ao investigar o resto da casa. Que outras informações conseguirias descobrir? Seria esta a chave para o mistério de como acabaste abandonado no meio da floresta? Só poderia certo. Mas no fundo da tua cabeça, uma única questão ecoava: e se quem estivesse por detrás disto tudo estivesse na casa? Darias ouvido à tua curiosidade, ou sentido de sobrevivência",\
["Fugir da Casa", "Investigar a Cozinha", "Investigar a Sala"],\
["43","35", "26"])#normal

story["45"] = ("Após breves segundos, decides que terias melhor chances de encontrar informações no Quarto. Ao olhar encontras a divisão num estado de profunda desarrumação. A mobília é antiga, escura, com alguns sinais de degradação. Mas na parede, algo captou a tua atenção. Era um quadro com um esquema, repleto de fotografias de adultos, e várias informações biográficas. Alguns deles, com um X vermelho marcado a delimitar cruzar a fotografia. Após melhor análise, reparas que uma fotografia tua, assim como o teu nome, idade, local de trabalho e rotina, incluindo o sítio onde vais tomar o pequeno-almoço ocasionalmente aparecem também lá escritos.  Um tremor percorre-te a espinha: Definitvamente, quem morava nesta casa era responsável pelo teu desaparecimento. Ainda chocado com a descoberta, não consegues deixar de pensar no que mais poderias descobrir ao investigar o resto da casa. Que outras informações conseguirias descobrir? Seria esta a chave para o mistério de como acabaste abandonado no meio da floresta? Só poderia certo. Mas no fundo da tua cabeça, uma única questão ecoava: e se quem estivesse por detrás disto tudo estivesse na casa? Darias ouvido à tua curiosidade, ou sentido de sobrevivência",\
["Fugir da Casa", "Investigar a Cozinha", "Investigar a Sala"],\
["48","36", "27"])#bebado

story["46"] = ("Após breves segundos, decides que terias melhor chances de encontrar informações no Quarto. Ao olhar encontras a divisão num estado de profunda desarrumação. A mobília é antiga, escura, com alguns sinais de degradação. Mas na parede, algo captou a tua atenção. Era um quadro com um esquema, repleto de fotografias de adultos, e várias informações biográficas. Alguns deles, com um X vermelho marcado a delimitar cruzar a fotografia. Após melhor análise, reparas que uma fotografia tua, assim como o teu nome, idade, local de trabalho e rotina, incluindo o sítio onde vais tomar o pequeno-almoço ocasionalmente aparecem também lá escritos.  Um tremor percorre-te a espinha: Definitvamente, quem morava nesta casa era responsável pelo teu desaparecimento. Ainda chocado com a descoberta, não consegues deixar de pensar no que mais poderias descobrir ao investigar o resto da casa. Que outras informações conseguirias descobrir? Seria esta a chave para o mistério de como acabaste abandonado no meio da floresta? Só poderia certo. Mas no fundo da tua cabeça, uma única questão ecoava: e se quem estivesse por detrás disto tudo estivesse na casa? Darias ouvido à tua curiosidade, ou sentido de sobrevivência",\
["Fugir da Casa", "Investigar a Cozinha", "Investigar a Sala"],\
["44","37", "28"])#lobo


#INVESTIGAR JARDIM
story["47"] = ("Após breves segundos, decides que terias a melhor chance a seguir os instintos do teu companheiro lobo. Mal chegam ao exterior, vês o lobo a correr em direção a um pequeno monte de terra no jardim. Ele começa a escavar, e do nada, pequenos pedaços de ossos aparecem no meio da terra. No meio de todo o choque, olhas em volta e percebes, apenas a alguns metros de distância, um pequeno retângulo cavado na terra, juntamente com uma pá e produtos químicos. Claramente, o responsável por esta atrocidade ficou a meio dos seus planos e não tardaria em voltar. O próximo passo era claro: sair o mais rapidamente dali. Em breves instantes, chamas o teu companheiro lobo:",\
["Fugir da Casa", "Investigar a Cozinha", "Investigar a Sala"],\
["44","37", "28"])

#RONDA 2 INVESTIGAR OUTRA DIVISÃO

story["40"] = ("Agora cara-cara com o Homem ameaçador, tentas reunir toda a tua coragem e adrenalina para sair desta situação aterradora. O homem, de olhar ameaçador e faca na mão dá um passo na tua direção. Nem tens tempo de reagir. Ele apanha-te, e antes de te aperceberes, a luta está já perdida. Fraco, desidratado e sem companhia, morres às mãos do homem, que com a faca acaba o serviço e a tua aventura. PERDESTE - Final 4",\
[], []) #FIM DA HISTÓRIA - FINAL 4#

story["41"] = ("Agora cara-cara com o Homem ameaçador, tentas reunir toda a tua coragem e adrenalina para sair desta situação aterradora. O homem, de olhar ameaçador e faca na mão dá um passo na tua direção. Tentas lutar o melhor que podes, mas felizmente o teu fiel lobo companheiro, ao ver-te em situação de perigo, não hesita em ajudar-te. Atira-se para cima do homem, e num  profundo ataque, deixa-o ferido no chão. Infelizmente, nesta luta renhida, o teu lobo companheiro não resistiu aos sofrimentos, obrigando-te a completar a jornada sozinho. Eventualmente, consegues-te afastar o suficiente para dares por ti no meio da floresta. Após um tempo a caminhar, encontras um passeio com melhor aparência. Era um local mais verde e aberto à natureza, com uma mesa de piquenique no centro e um poço. Decides investigar.",\
["Seguir a melodia dos pássaros a cantar","Seguir o toque do Sino"],\
["74","78"])

story["42"] = ("Agora cara-cara com o Homem ameaçador, tentas reunir toda a tua coragem e adrenalina para sair desta situação aterradora. O homem, de olhar ameaçador e faca na mão dá um passo na tua direção. Por sorte, com a garrafa de vinho na mão, consegues atirá-la à cabeça do homem, deixando-o ferido e inconsciente, e assim, consegues afastar-te o suficiente para dares por ti no meio da floresta. ",\
["Seguir a melodia dos pássaros a cantar","Seguir o toque do Sino"],\
["74","78"])

story["43"] = ("Ainda chocado com a descoberta, achas melhor não arriscar e fugir da casa o quanto antes. Quando estavas quase a atingir o portão, ouves um estrondo atrás de ti. Era um Homem, de aparência agressiva, manchas vermelhas na roupa e uma faca na mão, que olhava para ti com cara de espanto.'Como é que já estás acordado? Ainda devias estar inconsciente!', ouviste dizer, enquanto o homem tentava encurtar a sua distância. Por sorte, sem qualquer distração ou substâncias no organismo, consegues-te afastar o suficiente para dares por ti no meio da floresta. No meio do choque, tentas focar-te nos teus sentidos e achar a melhor opção para garantires a tua sobrevivência. Duas opções destacam-se",\
["Seguir a melodia dos pássaros a cantar","Seguir o toque do Sino"],\
["74","78"])

story["44"] = ("Ainda chocado com a descoberta, achas melhor não arriscar e fugir da casa o quanto antes. Quando estavas quase a atingir o portão, ouves um estrondo atrás de ti. Era um Homem, de aparência agressiva, manchas vermelhas na roupa e uma faca na mão, que olhava para ti com cara de espanto.'Como é que já estás acordado? Ainda devias estar inconsciente!', ouviste dizer, enquanto o homem tentava encurtar a sua distância. Com a visão do homem atrás de ti, tentas correr o máximo que podes, mas felizmente o teu fiel lobo companheiro, ao ver-te em situação de perigo, não hesita em ajudar-te. Atira-se para cima do homem, e num  profundo ataque, deixa-o ferido no chão. Infelizmente, nesta luta renhida, o teu lobo companheiro não resistiu aos sofrimentos, obrigando-te a completar a jornada sozinho. Sais da casa a correr e eventualmente dás por ti no meio da floresta.No meio do choque, tentas focar-te nos teus sentidos e achar a melhor opção para garantires a tua sobrevivência. Duas opções destacam-se:",\
["Seguir a melodia dos pássaros a cantar","Seguir o toque do Sino"],\
["74","78"])

story["48"] = ("Ainda chocado com a descoberta, achas melhor não arriscar e fugir da casa o quanto antes. Quando estavas quase a atingir o portão, ouves um estrondo atrás de ti. Era um Homem, de aparência agressiva, manchas vermelhas na roupa e uma faca na mão, que olhava para ti com cara de espanto.'Como é que já estás acordado? Ainda devias estar inconsciente!', ouviste dizer, enquanto o homem tentava encurtar a sua distância. Por sorte, com a garrafa de vinho na mão, consegues atirá-la à cabeça do homem, deixando-o ferido e inconsciente, e assim, consegues afastar-te o suficiente para dares por ti no meio da floresta. No meio do choque, tentas focar-te nos teus sentidos e achar a melhor opção para garantires a tua sobrevivência. Duas opções destacam-se.",\
["Seguir a melodia dos pássaros a cantar","Seguir o toque do Sino"],\
["74","78"])

#NA SALA E COZINHA - FUGIR
story["49"] = ("Agora cara-cara com o Homem ameaçador, tentas fugir mas em vão. A distância entre vocês é demasiado curta. Ele apanha-te, e antes de te aperceberes, a luta está já perdida. Fraco, desidratado e sem companhia, morres às mãos do homem, que com a faca acaba o serviço e a tua aventura. PERDESTE - Final 4",\
[], []) #FIM DA HISTÓRIA - FINAL 4#





##########################################################################################
#---------------------- AVENTURA - CAMINHO ESQUERDA - AGUA -------------------




#################################      CICLO DE JOGO     ####################################################
def jogo_aventura(livro, estado):
        
    #ESTADO
    
    while estado != "fim":
        # le a cena atual e imprime o texto
        texto, opcoes, prox_estado = livro[estado]
        print(texto)
        
        if opcoes != []:
            for i in range(len(opcoes)):
                print(str(i+1) + "- " + opcoes[i])

            # le opção do jogador e valida-a com o número de opções
            opcao = 0
            while opcao<1 or opcao>len(opcoes):
                opcao = int(input("Selecione a sua opção: "))
                print("")


            # determina a próxima cena de acordo com a opção do jogador
            estado = prox_estado[opcao-1]

        else:   
            print("*** Fim ***")
            estado = "fim" # fim do jogo - sai do ciclo
            
######################################    FIM DO CICLO DE JOGO   #######################################
jogo_aventura(story, "start")