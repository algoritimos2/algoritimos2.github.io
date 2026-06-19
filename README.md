<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Portfólio de Atividades</title>

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
    padding:60px 20px;
}

.container{
    max-width:1200px;
    margin:auto;
}

.titulo{
    text-align:center;
    margin-bottom:50px;
}

.titulo h1{
    color:white;
    font-size:3rem;
    font-weight:700;
}

.titulo p{
    color:#cbd5e1;
    margin-top:10px;
    font-size:1.1rem;
}

.cards{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
    gap:25px;
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

.card::before{
    content:'';
    position:absolute;
    width:180px;
    height:180px;
    background:rgba(255,255,255,0.08);
    border-radius:50%;
    top:-80px;
    right:-80px;
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
    font-size:1.3rem;
    font-weight:bold;
    margin-bottom:20px;
}

.card h2{
    color:white;
    margin-bottom:10px;
}

.card p{
    color:#dbeafe;
    line-height:1.7;
    margin-bottom:20px;
}

.btn{
    display:inline-block;
    padding:12px 22px;
    border-radius:12px;
    text-decoration:none;
    background:white;
    color:#2563eb;
    font-weight:600;
    transition:.3s;
}

.btn:hover{
    background:#dbeafe;
}

footer{
    text-align:center;
    color:#cbd5e1;
    margin-top:60px;
}

</style>
</head>
<body>

<div class="container">

    <div class="titulo">
        <h1>Minhas Atividades</h1>
        <p>Portfólio Acadêmico 2026</p>
    </div>

    <div class="cards">

        <div class="card">
            <div class="numero">01</div>
            <h2>Atividade 01</h2>
            <p>
                Descrição da atividade desenvolvida.
                Explique os objetivos, conteúdos estudados
                e resultados obtidos.
            </p>
            <a href="#" class="btn">Abrir Arquivo</a>
        </div>

        <div class="card">
            <div class="numero">02</div>
            <h2>Atividade 02</h2>
            <p>
                Descrição da atividade desenvolvida.
                Explique os objetivos, conteúdos estudados
                e resultados obtidos.
            </p>
            <a href="#" class="btn">Abrir Arquivo</a>
        </div>

        <div class="card">
            <div class="numero">03</div>
            <h2>Atividade 03</h2>
            <p>
                Descrição da atividade desenvolvida.
                Explique os objetivos, conteúdos estudados
                e resultados obtidos.
            </p>
            <a href="#" class="btn">Abrir Arquivo</a>
        </div>

        <div class="card">
            <div class="numero">04</div>
            <h2>Atividade 04</h2>
            <p>
                Descrição da atividade desenvolvida.
                Explique os objetivos, conteúdos estudados
                e resultados obtidos.
            </p>
            <a href="#" class="btn">Abrir Arquivo</a>
        </div>

    </div>

    <footer>
        © 2026 • Portfólio Acadêmico
    </footer>

</div>

</body>
</html>
