<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Portfólio Acadêmico</title>

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
}

header{
    background:#0d47a1;
    color:white;
    text-align:center;
    padding:60px 20px;
}

header h1{
    font-size:3rem;
}

header p{
    margin-top:10px;
}

nav{
    background:#08306b;
    padding:15px;
    text-align:center;
}

nav a{
    color:white;
    text-decoration:none;
    margin:0 15px;
    font-weight:bold;
}

section{
    max-width:1200px;
    margin:auto;
    padding:50px 20px;
}

h2{
    color:#0d47a1;
    margin-bottom:20px;
}

.cards{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(300px,1fr));
    gap:20px;
}

.card{
    background:white;
    border-radius:10px;
    padding:20px;
    box-shadow:0 3px 10px rgba(0,0,0,.1);
    transition:.3s;
}

.card:hover{
    transform:translateY(-5px);
}

.card h3{
    color:#1565c0;
}

.card p{
    margin:10px 0;
}

.btn{
    display:inline-block;
    padding:10px 20px;
    background:#1565c0;
    color:white;
    text-decoration:none;
    border-radius:5px;
}

.btn:hover{
    background:#0d47a1;
}

table{
    width:100%;
    border-collapse:collapse;
    background:white;
}

table th{
    background:#1565c0;
    color:white;
}

table th, table td{
    border:1px solid #ddd;
    padding:12px;
}

footer{
    background:#08306b;
    color:white;
    text-align:center;
    padding:25px;
}

.perfil{
    display:flex;
    gap:30px;
    align-items:center;
    flex-wrap:wrap;
}

.foto{
    width:180px;
    height:180px;
    border-radius:50%;
    background:#ddd;
    display:flex;
    justify-content:center;
    align-items:center;
}

</style>
</head>
<body>

<header>
    <h1>Portfólio Acadêmico 2026</h1>
    <p>Nome do Aluno - Curso Técnico / Ensino Médio</p>
</header>

<nav>
    <a href="#sobre">Sobre Mim</a>
    <a href="#atividades">Atividades</a>
    <a href="#projetos">Projetos</a>
    <a href="#cronograma">Cronograma</a>
    <a href="#contato">Contato</a>
</nav>

<section id="sobre">

    <h2>Sobre Mim</h2>

    <div class="perfil">

        <div class="foto">
            Sua Foto
        </div>

        <div>
            <p>
                Escreva aqui uma breve apresentação.
                Fale sobre sua escola, curso,
                objetivos e o que aprendeu durante o ano.
            </p>
        </div>

    </div>

</section>

<section id="atividades">

<h2>Atividades Realizadas</h2>

<div class="cards">

    <div class="card">
        <h3>Atividade 01</h3>
        <p>Descrição da atividade.</p>
        <a href="#" class="btn">Ver Arquivo</a>
    </div>

    <div class="card">
        <h3>Atividade 02</h3>
        <p>Descrição da atividade.</p>
        <a href="#" class="btn">Ver Arquivo</a>
    </div>

    <div class="card">
        <h3>Atividade 03</h3>
        <p>Descrição da atividade.</p>
        <a href="#" class="btn">Ver Arquivo</a>
    </div>

    <div class="card">
        <h3>Atividade 04</h3>
        <p>Descrição da atividade.</p>
        <a href="#" class="btn">Ver Arquivo</a>
    </div>

</div>

</section>

<section id="projetos">

<h2>Projetos Desenvolvidos</h2>

<div class="cards">

    <div class="card">
        <h3>Projeto 1</h3>
        <p>
            Explique o objetivo do projeto,
            tecnologias utilizadas e resultados.
        </p>
    </div>

    <div class="card">
        <h3>Projeto 2</h3>
        <p>
            Explique o objetivo do projeto,
            tecnologias utilizadas e resultados.
        </p>
    </div>

    <div class="card">
        <h3>Projeto 3</h3>
        <p>
            Explique o objetivo do projeto,
            tecnologias utilizadas e resultados.
        </p>
    </div>

</div>

</section>

<section id="cronograma">

<h2>Evolução Durante o Ano</h2>

<table>

<tr>
    <th>Mês</th>
    <th>Atividade Principal</th>
    <th>Status</th>
</tr>

<tr>
    <td>Março</td>
    <td>Introdução ao Curso</td>
    <td>Concluído</td>
</tr>

<tr>
    <td>Abril</td>
    <td>Primeiro Projeto</td>
    <td>Concluído</td>
</tr>

<tr>
    <td>Maio</td>
    <td>Relatório Técnico</td>
    <td>Concluído</td>
</tr>

<tr>
    <td>Junho</td>
    <td>Apresentação</td>
    <td>Concluído</td>
</tr>

</table>

</section>

<section>

<h2>Minhas Habilidades</h2>

<ul>
    <li>HTML e CSS</li>
    <li>Python</li>
    <li>Banco de Dados</li>
    <li>Pacote Office</li>
    <li>Trabalho em Equipe</li>
</ul>

</section>

<section id="contato">

<h2>Contato</h2>

<p>Email: seuemail@email.com</p>
<p>Turma: XXXX</p>
<p>Escola: Nome da Escola</p>

</section>

<footer>
    <p>Portfólio Acadêmico - Atualizado em 2026</p>
</footer>

</body>
</html>
