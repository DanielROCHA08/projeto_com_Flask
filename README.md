## Documentação 

1. Criamos a pasta projeto_com_Flask no VsCode

2. Fizemos a instalação e configuramos o uv na máquina virtual pelo VsCode

- Site: https://docs.astral.sh/uv/getting-started/installation/

- powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"  

3. Alguns comando do uv que ultilizamos:

- uv

- uv -V 

(Mostra a versão do uv instalada no seu computador.)

- uv init 

(Inicializa um novo projeto Python na pasta atual)

- uv venv 

(Cria um ambiente virtual (.venv) isolado para o projeto.)

- uv install python 3.15.0 

(instalação da versão mais recente do python no VsCode)

- uv sync 

(Sincroniza e instala todas as dependências do projeto automaticamente.)

- python -V 

(Verifica qual versão do Python está sendo executada no terminal.)

- uv add (Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& c:\Users\AlunoADS1\Projetos\projeto_com_Flask\.venv\Scripts\Activate.ps1) 

(Altera a permissão de scripts do PowerShell temporariamente e ativa o ambiente virtual manualmente no Windows.)

- uv add Flask 

(Adiciona e instala o framework Flask no seu projeto.)

- uv run flask run 

(Roda o servidor de desenvolvimento do Flask utilizando o ambiente gerenciado pelo uv.)




