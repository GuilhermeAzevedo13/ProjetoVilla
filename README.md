# ProjetoVilla — Cadastro de Mesas do Réveillon do Condomínio Villas

Aplicativo simples e direto ao ponto para **cadastrar e gerenciar mesas** do evento de Ano Novo no condomínio. O foco é permitir o controle prático das mesas (ocupadas/livres), moradores/locatários e visualização rápida do mapa.

> Plataforma-alvo: **Windows** (executável pronto) e **qualquer SO** com **Python 3**.

---

## ✨ Destaques

- **Pronto para uso no Windows**: `App.exe` incluído na raiz.
- **Sem dependências externas**: roda com a biblioteca padrão do Python.
- **Dados persistidos em arquivo** (`.dat`) para manter o estado entre execuções.
- **Organização por módulos**: entidades (morador/locatário), cadastro/registro, busca, mapa e exibição.

---

## 📦 Estrutura do projeto

```text
ProjetoVilla/
├── App.py                 # Ponto de entrada da aplicação (Python)
├── App.exe                # Executável pronto para Windows
├── Buscar.py              # Funcionalidades de busca
├── ExibirInfo.py          # Exibição de informações
├── Locatario.py           # Entidade/rotinas de locatários
├── Morador.py             # Entidade/rotinas de moradores
├── Mapa.py                # Visualização/controle do mapa de mesas
├── Registro.py            # Persistência (moradores/geral)
├── RegistroMesas.py       # Persistência de mesas
├── registro.dat           # Base de dados (pickle) – moradores/geral
├── registroMesas.dat      # Base de dados (pickle) – mesas
└── imagens/               # Capturas (screenshots), logos, etc.
Persistência: os arquivos .dat usam pickle (biblioteca padrão do Python). (Não abra arquivos pickle de origem desconhecida.)
---
🚀 Como executar
Opção 1 — Windows (recomendada para o evento)
Baixe/clone este repositório.

Dê duplo clique em App.exe.

Se o Windows SmartScreen alertar, clique em Mais informações → Executar assim mesmo.

Ideal para quem só quer usar o sistema no dia do evento, sem instalar Python.

Opção 2 — Python (Windows, Linux, macOS)
Requer Python 3.10+.

Clone o repositório:

bash
Copiar código
git clone https://github.com/GuilhermeAzevedo13/ProjetoVilla.git
cd ProjetoVilla
(Opcional) Crie um ambiente virtual:

bash
Copiar código
# Windows
py -m venv .venv && .venv\Scripts\activate
# Linux/macOS
python3 -m venv .venv && source .venv/bin/activate
Dependências
Não há dependências externas (apenas biblioteca padrão do Python). 🎉

Execute:
# Windows
py App.py
# Linux/macOS
python3 App.py
Na primeira execução, registro.dat e registroMesas.dat serão criados automaticamente, se não existirem.
--
🧠 Como funciona (visão geral)
Moradores/Locatários: cadastrados via telas específicas.

Mesas: controle de mesas ocupadas e disponíveis.

Mapa: visualização/controle do layout das mesas (Mapa.py).

Busca e Exibição: encontre rapidamente registros e veja detalhes.

Persistência: os registros são salvos em .dat (pickle), garantindo que tudo permaneça após encerrar o app.
---
🧹 Resetar / Fazer backup dos dados
Backup: copie registro.dat e registroMesas.dat para outro local.

Reset total (zerar tudo):

Feche o app.

Apague registro.dat e registroMesas.dat.

Ao abrir novamente, o sistema recria os arquivos vazios.

Faça backup antes de resetar, se quiser preservar o histórico.
---
🔒 Nota de segurança (pickle)
Os arquivos .dat usam pickle. Nunca abra dados pickle de terceiros. Use apenas os .dat gerados por este app.
---
📸 Fotos do sistema (5 espaços)
Coloque suas imagens em imagens/ com os nomes abaixo (ou ajuste os caminhos).
Dica: para manter o README leve, use .png otimizadas.

Mapa de Mesas	Cadastro de Morador/Locatário	Busca
<img src="imagens/foto1_mapa.png" alt="Mapa de Mesas" width="360"/>	<img src="imagens/foto2_cadastro.png" alt="Cadastro" width="360"/>	<img src="imagens/foto3_busca.png" alt="Busca" width="360"/>

Exibição de Informações	Confirmações/Outros
<img src="imagens/foto4_exibir.png" alt="Exibição de Informações" width="360"/>	<img src="imagens/foto5_outros.png" alt="Outros" width="360"/>
---
🛣️ Roadmap (ideias futuras)
Exportar planilhas (CSV/Excel) com a alocação.

Marcação de status (confirmado/pendente).

Relatórios por bloco/torre/unidade.

Modo “somente leitura” para uso pelos porteiros durante o evento.

👤 Autor
Guilherme Azevedo — GuilhermeAzevedo13

