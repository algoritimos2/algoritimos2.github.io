<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Portal de Engenharia Elétrica</title>

<style>
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Arial, sans-serif;
}

body{
    background:#f4f6f9;
    color:#333;
    line-height:1.6;
}

header{
    background:linear-gradient(135deg,#003366,#0055aa);
    color:white;
    padding:80px 20px;
    text-align:center;
}

header h1{
    font-size:3rem;
}

nav{
    background:#002244;
    padding:15px;
    position:sticky;
    top:0;
}

nav ul{
    display:flex;
    justify-content:center;
    list-style:none;
    gap:20px;
}

nav a{
    color:white;
    text-decoration:none;
    font-weight:bold;
}

nav a:hover{
    color:#ffcc00;
}

.container{
    max-width:1200px;
    margin:auto;
    padding:40px 20px;
}

section{
    margin-bottom:60px;
}

h2{
    color:#003366;
    margin-bottom:20px;
}

.cards{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
    gap:20px;
}

.card{
    background:white;
    padding:20px;
    border-radius:10px;
    box-shadow:0 3px 10px rgba(0,0,0,0.1);
}

.card h3{
    color:#0055aa;
}

table{
    width:100%;
    border-collapse:collapse;
    margin-top:20px;
}

table th, table td{
    border:1px solid #ccc;
    padding:12px;
}

table th{
    background:#003366;
    color:white;
}

footer{
    background:#002244;
    color:white;
    text-align:center;
    padding:30px;
}

.btn{
    display:inline-block;
    background:#0055aa;
    color:white;
    padding:12px 25px;
    border-radius:5px;
    text-decoration:none;
    margin-top:20px;
}

.btn:hover{
    background:#003366;
}
</style>
</head>
<body>

<header>
    <h1>Portal de Engenharia Elétrica</h1>
    <p>Conhecimento, inovação e tecnologia elétrica em um só lugar.</p>
</header>

<nav>
    <ul>
        <li><a href="#sobre">Sobre</a></li>
        <li><a href="#areas">Áreas</a></li>
        <li><a href="#disciplinas">Disciplinas</a></li>
        <li><a href="#mercado">Mercado</a></li>
        <li><a href="#contato">Contato</a></li>
    </ul>
</nav>

<div class="container">

<section id="sobre">
    <h2>O que é Engenharia Elétrica?</h2>
    <p>
        A Engenharia Elétrica é o ramo da engenharia responsável pelo estudo,
        projeto, desenvolvimento e manutenção de sistemas elétricos,
        eletrônicos e energéticos. Os engenheiros eletricistas atuam em áreas
        como geração de energia, automação industrial, telecomunicações,
        eletrônica, controle e sistemas inteligentes.
    </p>
</section>

<section id="areas">
    <h2>Principais Áreas de Atuação</h2>

    <div class="cards">

        <div class="card">
            <h3>Sistemas de Potência</h3>
            <p>
                Planejamento e operação de redes de transmissão,
                distribuição e geração de energia elétrica.
            </p>
        </div>

        <div class="card">
            <h3>Automação Industrial</h3>
            <p>
                Desenvolvimento de sistemas automatizados,
                CLPs, sensores e controle de processos.
            </p>
        </div>

        <div class="card">
            <h3>Eletrônica</h3>
            <p>
                Projeto de circuitos eletrônicos,
                dispositivos semicondutores e sistemas embarcados.
            </p>
        </div>

        <div class="card">
            <h3>Telecomunicações</h3>
            <p>
                Redes de comunicação, internet,
                telefonia móvel e transmissão de dados.
            </p>
        </div>

        <div class="card">
            <h3>Energias Renováveis</h3>
            <p>
                Sistemas solares, eólicos e novas tecnologias
                para produção sustentável de energia.
            </p>
        </div>

        <div class="card">
            <h3>Inteligência Artificial</h3>
            <p>
                Aplicação de IA para monitoramento,
                previsão e otimização de sistemas elétricos.
            </p>
        </div>

    </div>
</section>

<section id="disciplinas">
    <h2>Disciplinas do Curso</h2>

    <table>
        <tr>
            <th>Disciplina</th>
            <th>Descrição</th>
        </tr>

        <tr>
            <td>Cálculo</td>
            <td>Base matemática para modelagem de sistemas.</td>
        </tr>

        <tr>
            <td>Física</td>
            <td>Estudo de eletricidade, magnetismo e mecânica.</td>
        </tr>

        <tr>
            <td>Circuitos Elétricos</td>
            <td>Análise e projeto de circuitos.</td>
        </tr>

        <tr>
            <td>Máquinas Elétricas</td>
            <td>Motores, geradores e transformadores.</td>
        </tr>

        <tr>
            <td>Controle e Automação</td>
            <td>Sistemas de controle industriais.</td>
        </tr>

        <tr>
            <td>Eletrônica Digital</td>
            <td>Portas lógicas, microcontroladores e sistemas digitais.</td>
        </tr>
    </table>
</section>

<section id="mercado">
    <h2>Mercado de Trabalho</h2>

    <p>
        O mercado para engenheiros eletricistas continua em expansão devido
        ao crescimento das energias renováveis, cidades inteligentes,
        automação industrial e transformação digital.
    </p>

    <br>

    <div class="cards">

        <div class="card">
            <h3>Empresas de Energia</h3>
            <p>Usinas, distribuidoras e concessionárias.</p>
        </div>

        <div class="card">
            <h3>Indústrias</h3>
            <p>Automação, manutenção e controle de processos.</p>
        </div>

        <div class="card">
            <h3>Tecnologia</h3>
            <p>Eletrônica, software embarcado e IA.</p>
        </div>

        <div class="card">
            <h3>Consultoria</h3>
            <p>Projetos elétricos e eficiência energética.</p>
        </div>

    </div>
</section>

<section>
    <h2>Curiosidades</h2>

    <ul>
        <li>A eletricidade viaja próxima à velocidade da luz.</li>
        <li>Transformadores permitem transmitir energia a grandes distâncias.</li>
        <li>Redes inteligentes (Smart Grids) já utilizam IA.</li>
        <li>O setor elétrico é fundamental para a indústria moderna.</li>
    </ul>

    <a href="#contato" class="btn">Fale Conosco</a>
</section>

<section id="contato">
    <h2>Contato</h2>

    <form>
        <label>Nome</label><br>
        <input type="text" style="width:100%;padding:10px;"><br><br>

        <label>E-mail</label><br>
        <input type="email" style="width:100%;padding:10px;"><br><br>

        <label>Mensagem</label><br>
        <textarea rows="5" style="width:100%;padding:10px;"></textarea><br><br>

        <button class="btn">Enviar</button>
    </form>
</section>

</div>

<footer>
    <p>© 2026 Portal de Engenharia Elétrica</p>
    <p>Desenvolvido para fins educacionais.</p>
</footer>

</body>
</html>
