<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Portfólio Acadêmico - Lucas Viana de Freitas</title>

<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:'Poppins',sans-serif;
}

body{
    min-height:100vh;
    background:linear-gradient(135deg,#0f172a,#1e293b,#2563eb);
    padding:40px 20px;
}

.container{
    max-width:1200px;
    margin:auto;
}

.titulo{
    text-align:center;
    margin-bottom:30px;
}

.titulo h1{
    color:white;
    font-size:3rem;
}

.titulo p{
    color:#cbd5e1;
    margin-top:10px;
}

.menu{
    display:flex;
    justify-content:center;
    flex-wrap:wrap;
    gap:15px;
    margin-bottom:35px;
}

.menu a{
    text-decoration:none;
    color:white;
    background:rgba(255,255,255,0.12);
    padding:12px 20px;
    border-radius:12px;
    transition:.3s;
}

.menu a:hover{
    background:rgba(255,255,255,0.25);
}

.identificacao{
    max-width:800px;
    margin:0 auto 40px;
    background:rgba(255,255,255,0.08);
    backdrop-filter:blur(15px);
    border:1px solid rgba(255,255,255,0.15);
    border-radius:24px;
    padding:25px;
    color:white;
}

.identificacao h2{
    margin-bottom:15px;
    color:#dbeafe;
}

.identificacao p{
    margin:8px 0;
}

.cards{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
    gap:25px;
    margin-top:30px;
}

.card{
    background:rgba(255,255,255,0.08);
    backdrop-filter:blur(15px);
    border:1px solid rgba(255,255,255,0.15);
    border-radius:24px;
    padding:30px;
    transition:.4s;
    position:relative;
    overflow:hidden;
}

.card:hover{
    transform:translateY(-10px);
    box-shadow:0 20px 40px rgba(0,0,0,.25);
}

.numero{
    width:60px;
    height:60px;
    border-radius:18px;
    background:linear-gradient(135deg,#3b82f6,#60a5fa);
    display:flex;
    align-items:center;
    justify-content:center;
    color:white;
    font-size:1.2rem;
    font-weight:bold;
    margin-bottom:20px;
}

.card h2{
    color:white;
    margin-bottom:10px;
}

.card p{
    color:#dbeafe;
    line-height:1.6;
    margin-bottom:20px;
}

.btn{
    display:inline-block;
    padding:12px 20px;
    border-radius:12px;
    text-decoration:none;
    background:white;
    color:#2563eb;
    font-weight:600;
}

.btn:hover{
    background:#dbeafe;
}

.links{
    margin-top:50px;
}

.links a{
    color:#93c5fd;
}

footer{
    text-align:center;
    color:#cbd5e1;
    margin-top:50px;
}

</style>
</head>
<body>

<div class="container">

    <div class="titulo">
        <h1>Portfólio Acadêmico</h1>
        <p>Atividades desenvolvidas durante o semestre</p>
    </div>

    <nav class="menu">
        <a href="#aluno">Aluno</a>
        <a href="#atividades">Atividades</a>
        <a href="#projeto">Projeto</a>
    </nav>

    <section id="aluno" class="identificacao">
        <h2>Identificação do Aluno</h2>

        <p><strong>Nome:</strong> Lucas Viana de Freitas</p>
        <p><strong>Matrícula:</strong> 2610101377</p>
        <p><strong>Professor:</strong> Diego Luis Kreutz</p>
        <p><strong>Disciplina:</strong> Algoritmos e Programação</p>
        <p><strong>Semestre:</strong> 2026</p>
    </section>

    <section id="atividades">

        <div class="cards">

            <div class="card">
                <div class="numero">01</div>
                <h2>Atividade 01</h2>
                <p>
                    Descrição da primeira atividade realizada durante o semestre.
                </p>
                <a href="SEU_LINK_ATIVIDADE_01"
                   target="_blank"
                   class="btn">
                    Ver Atividade
                </a>
            </div>

            <div class="card">
                <div class="numero">02</div>
                <h2>Atividade 02</h2>
                <p>
                    Descrição da segunda atividade realizada durante o semestre.
                </p>
                <a href="SEU_LINK_ATIVIDADE_02"
                   target="_blank"
                   class="btn">
                    Ver Atividade
                </a>
            </div>

            <div class="card">
                <div class="numero">03</div>
                <h2>Atividade 03</h2>
                <p>
                    Descrição da terceira atividade realizada durante o semestre.
                </p>
                <a href="SEU_LINK_ATIVIDADE_03"
                   target="_blank"
                   class="btn">
                    Ver Atividade
                </a>
            </div>

            <div class="card">
                <div class="numero">04</div>
                <h2>Atividade 04</h2>
                <p>
                    Descrição da quarta atividade realizada durante o semestre.
                </p>
                <a href="SEU_LINK_ATIVIDADE_04"
                   target="_blank"
                   class="btn">
                    Ver Atividade
                </a>
            </div>

        </div>

    </section>

    <section id="projeto" class="identificacao links">

        <h2>Informações do Projeto</h2>

        <p>
            <strong>Repositório GitHub:</strong><br>
            <a href="https://github.com/algoritimos2/algoritimos2.github.io/tree/main"
               target="_blank">
               https://github.com/algoritimos2/algoritimos2.github.io
            </a>
        </p>

        <br>

        <p>
            <strong>Site Publicado (GitHub.io):</strong><br>
            <a href="algoritimos2.github.io"
               target="_blank">
               algoritimos2.github.io
            </a>
        </p>

        <br>

        <p>
            <strong>Último Commit (Hash):</strong><br>
            fe55057
        </p>

    </section>

    <footer>
        © 2026 • Portfólio Acadêmico • Lucas Viana de Freitas
    </footer>

</div>

</body>
</html>
