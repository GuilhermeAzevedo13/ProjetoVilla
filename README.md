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
ProjetoVilla/
├─ App.py # Ponto de entrada da aplicação em Python
├─ App.exe # Executável pronto para Windows
├─ Buscar.py # Funcionalidades de busca
├─ ExibirInfo.py # Tela/rotina para exibir informações
├─ Locatario.py # Entidade/rotinas de locatários
├─ Morador.py # Entidade/rotinas de moradores
├─ Mapa.py # Visualização/controle do mapa de mesas
├─ Registro.py # Registro/Persistência (moradores/geral)
├─ RegistroMesas.py # Registro/Persistência de mesas
├─ registro.dat # Base de dados (pickle) – moradores/geral
├─ registroMesas.dat # Base de dados (pickle) – mesas
└─ imagens/ # (opcional) capturas, logos, etc.


> **Observação sobre persistência**: os arquivos `.dat` usam **pickle** (biblioteca padrão do Python). Isso permite salvar e carregar rapidamente as listas de objetos sem configurar SGBD. (*Não abra arquivos pickle de origem desconhecida.*)

---

## 🚀 Como executar

### Opção 1 — Windows (recomendado para o evento)
1. Baixe/clonE este repositório.
2. Dê duplo clique em **`App.exe`**.
3. Se o Windows SmartScreen alertar, escolha “Mais informações” → “Executar assim mesmo”.

> Essa opção é ideal para quem só quer **usar** o sistema no dia do evento, sem instalar Python.

---

### Opção 2 — Python (Windows, Linux, macOS)

> Requer **Python 3.10+** (ou compatível).

1. **Clone** o repositório:
   ```bash
   git clone https://github.com/GuilhermeAzevedo13/ProjetoVilla.git
   cd ProjetoVilla

🧠 Como funciona (visão geral)

Moradores/Locatários: cadastrados via telas específicas.

Mesas: controle de mesas ocupadas e disponíveis.

Mapa: visualização/controle do layout das mesas (Mapa.py).

Busca e Exibição: encontre rapidamente registros e veja detalhes.

Persistência: os registros são salvos em .dat (pickle), garantindo que tudo permaneça após encerrar o app.

🧹 Resetar / Fazer backup dos dados

Backup: copie os arquivos registro.dat e registroMesas.dat para outro local.

Reset total (zerar tudo):
feche o app e delete registro.dat e registroMesas.dat.
Ao abrir novamente, o sistema recria os arquivos vazios.

Faça backup antes de resetar, se quiser preservar o histórico.

🔒 Nota de segurança (pickle)

Os arquivos .dat usam pickle. Nunca abra dados pickle vindos de terceiros. Abra apenas os .dat gerados por este próprio app.


🛣️ Roadmap (ideias futuras)

Exportar planilhas (CSV/Excel) com a alocação.

Marcação de status (confirmado/pendente).

Relatórios por bloco/torre/unidade.

Modo “somente leitura” para uso pelos porteiros durante o evento.

👤 Autor

Guilherme Azevedo — GuilhermeAzevedo13



---

**Notas de referência e base**  
Montei o README a partir da estrutura real do seu repositório (arquivos como `App.py`, `App.exe`, `RegistroMesas.py`, `registro.dat`, `registroMesas.dat` e a pasta `imagens` aparecem listados na raiz), o que me permitiu propor a organização e os passos de execução acima. :contentReference[oaicite:0]{index=0}

Também considerei que o projeto persiste dados em arquivos `.dat` via `pickle` (com criação automática do arquivo se não existir), de acordo com a implementação típica desse padrão de registro vista neste contexto. (Se quiser, posso adaptar o README caso você prefira usar CSV/SQLite em vez de pickle.)
::contentReference[oaicite:1]{index=1}

