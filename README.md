# Termoquimica-1.3

Versão com interface em português e inglês

Este código foi desenvolvido para calcular funções termodinâmicas. Para configurá-lo abra um terminal e dê o comando:
                     
                     python3 setup.py
                     
Isso vai verificar se as depêndencias do  programa estão satisfeitas, caso não esteja, vai tentar instalá-las automaticamente. Em caso de falha, faça manualmente um por um,  nesta ordem.
            
                     sudo apt install python3-pip python3-pyqt5 -y
                     python3 -m pip install numpy
                     python3 -m pip install pyqt5
                     chmod u+x termoquimica.py
                     sudo ln -sf $PWD/termoquimica.py /usr/bin/termoquimica
                     
Após concluir a configuração, para executar o programa basta abrir um terminal de digitar: termoquimica

NOTAS DE USO

teclas de atalho para exibir funções separadamente: (Menu Exibir)

F7  = 'Temperatura x E_interna'\
F8  = 'Temperatura x Entropia'\
F9  = 'Temperatura x Entalpia'\
F10 = 'Temperatura x E_Gibbs'\
F11 = 'Temperatura x E_Helmholtz'

Software programado para ler arquivos de saída das versões 6x do Quantum Espresso. Temperatura mínima obrigatóriamente deve ser diferente da temperatura máxima. Caso deseje plotar os resultados para apenas um valor de T, faça da seguinte forma:

  Tmin; (Tmax = Tmin + Delta T); Delta T

Após inserir os dados, basta clicar em calcular que os dados serão exibidos na área de texto. 

Para salvar os dados que estão mostrados na tela basta clicar no botão salvar, fornecer um nome para o arquivo e setar o diretório para ele.
Por padrão, a área de texto é definida como somente leitura. Caso deseje editar os dados basta clicar no botão "Editar".

Caso deseje copiar os dados exibidos na área de texto, basta clicar no botão copiar.

Alternativamente ao uso da gui, o usuário pode optar por uma versão em linha de comando (com funcionalidades reduzidas). Para isso basta executar o código console.py em um terminal. Este módulo necessita apenas da biblioteca matemática numpy, que pode ser instalada com o comando python3 -m pip install numpy
