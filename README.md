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
    
.desc{
    max-height:0;
    overflow:hidden;
    transition:0.4s ease;
    color:#dbeafe;
    margin-top:10px;
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
        <h2>Preenchimento do formulário de diagnóstico inicial</h2>
        <p><strong>Data:</strong> 17/03/2026</p>

        <div class="desc">
            Descrição da atividade desenvolvida. Explique os objetivos, conteúdos estudados e resultados obtidos.
        </div>

        <a href="#" class="btn">Ver Atividade</a>
    </div>

    <div class="card">
        <div class="numero">02</div>
        <h2>QUIZ – Lógica de Programação (Preparatório em aula)</h2>
        <p><strong>Data:</strong> 20/03/2026</p>

        <div class="desc">
            Descrição da atividade desenvolvida. Explique os objetivos, conteúdos estudados e resultados obtidos.
        </div>

        <a href="#" class="btn">Ver Atividade</a>
    </div>

    <div class="card">
        <div class="numero">03</div>
        <h2>QUIZ – Diagnóstico de Lógica de Programação</h2>
        <p><strong>Data:</strong> 27/03/2026</p>

        <div class="desc">
            Descrição da atividade desenvolvida. Explique os objetivos, conteúdos estudados e resultados obtidos.
        </div>

        <a href="#" class="btn">Ver Atividade</a>
    </div>

    <div class="card">
        <div class="numero">04</div>
        <h2>Lista de 15 exercícios: escolher e resolver</h2>
        <p><strong>Data:</strong> 31/03/2026</p>

        <div class="desc">
            Descrição da atividade desenvolvida. Explique os objetivos, conteúdos estudados e resultados obtidos.
        </div>

        <a href="#" class="btn">Ver Atividade</a>
    </div>

    <div class="card">
        <div class="numero">05</div>
        <h2>Lista de 10 Exercícios da Introdução a Algoritmos com Python</h2>
        <p><strong>Data:</strong> 10/04/2026</p>

        <div class="desc">
            Descrição da atividade desenvolvida. Explique os objetivos, conteúdos estudados e resultados obtidos.
        </div>

        <a href="#" class="btn">Ver Atividade</a>
    </div>

    <div class="card">
        <div class="numero">06</div>
        <h2>Geração e Avaliação de Exercícios de Algoritmos com LLMs</h2>
        <p><strong>Data:</strong> 10/04/2026</p>

        <div class="desc">
            Descrição da atividade desenvolvida. Explique os objetivos, conteúdos estudados e resultados obtidos.
        </div>

        <a href="#" class="btn">Ver Atividade</a>
    </div>

    <div class="card">
        <div class="numero">07</div>
        <h2>Quiz de Avaliação da Atividade: Uso de LLMs em Algoritmos</h2>
        <p><strong>Data:</strong> 10/04/2026</p>

        <div class="desc">
            Descrição da atividade desenvolvida. Explique os objetivos, conteúdos estudados e resultados obtidos.
        </div>

        <a href="#" class="btn">Ver Atividade</a>
    </div>

    <div class="card">
        <div class="numero">08</div>
        <h2>Resolver os 5 exercícios em papel</h2>
        <p><strong>Data:</strong> 21/04/2026</p>

        <div class="desc">
            Descrição da atividade desenvolvida. Explique os objetivos, conteúdos estudados e resultados obtidos.
        </div>

        <a href="#" class="btn">Ver Atividade</a>
    </div>

    <div class="card">
        <div class="numero">09</div>
        <h2>Resolver os exercícios de listas/vetores/arrays em Python</h2>
        <p><strong>Data:</strong> 24/04/2026</p>

        <div class="desc">
            Descrição da atividade desenvolvida. Explique os objetivos, conteúdos estudados e resultados obtidos.
        </div>

        <a href="#" class="btn">Ver Atividade</a>
    </div>

    <div class="card">
        <div class="numero">10</div>
        <h2>Formulação e Resolução de Problemas com Vetores/Listas</h2>
        <p><strong>Data:</strong> 24/04/2026</p>

        <div class="desc">
            Descrição da atividade desenvolvida. Explique os objetivos, conteúdos estudados e resultados obtidos.
        </div>

        <a href="#" class="btn">Ver Atividade</a>
    </div>

    <div class="card">
        <div class="numero">11</div>
        <h2>Gerar versões do código com resultados visuais</h2>
        <p><strong>Data:</strong> 05/05/2026</p>

        <div class="desc">
            Descrição da atividade desenvolvida. Explique os objetivos, conteúdos estudados e resultados obtidos.
        </div>

        <a href="#" class="btn">Ver Atividade</a>
    </div>

    <div class="card">
        <div class="numero">12</div>
        <h2>Problemas de outras disciplinas – múltiplas abordagens</h2>
        <p><strong>Data:</strong> 08/05/2026</p>

        <div class="desc">
            Descrição da atividade desenvolvida. Explique os objetivos, conteúdos estudados e resultados obtidos.
        </div>

        <a href="#" class="btn">Ver Atividade</a>
    </div>

    <div class="card">
        <div class="numero">13</div>
        <h2>Escolher e entregar problema de engenharia</h2>
        <p><strong>Data:</strong> 12/05/2026</p>

        <div class="desc">
            Descrição da atividade desenvolvida. Explique os objetivos, conteúdos estudados e resultados obtidos.
        </div>

        <a href="#" class="btn">Ver Atividade</a>
    </div>

    <div class="card">
        <div class="numero">14</div>
        <h2>Entregar outro problema de engenharia</h2>
        <p><strong>Data:</strong> 15/05/2026</p>

        <div class="desc">
            Descrição da atividade desenvolvida. Explique os objetivos, conteúdos estudados e resultados obtidos.
        </div>

        <a href="#" class="btn">Ver Atividade</a>
    </div>

    <div class="card">
        <div class="numero">15</div>
        <h2>Escolher e resolver problema de engenharia</h2>
        <p><strong>Data:</strong> 19/05/2026</p>

        <div class="desc">
            Descrição da atividade desenvolvida. Explique os objetivos, conteúdos estudados e resultados obtidos.
        </div>

        <a href="#" class="btn">Ver Atividade</a>
    </div>

    <div class="card">
        <div class="numero">16</div>
        <h2>Evolução técnica da solução anterior</h2>
        <p><strong>Data:</strong> 22/05/2026</p>

        <div class="desc">
            Descrição da atividade desenvolvida. Explique os objetivos, conteúdos estudados e resultados obtidos.
        </div>

        <a href="#" class="btn">Ver Atividade</a>
    </div>

    <div class="card">
        <div class="numero">17</div>
        <h2>Relato sobre entrevistas</h2>
        <p><strong>Data:</strong> 09/06/2026</p>

        <div class="desc">
            Descrição da atividade desenvolvida. Explique os objetivos, conteúdos estudados e resultados obtidos.
        </div>

        <a href="#" class="btn">Ver Atividade</a>
    </div>

    <div class="card">
        <div class="numero">18</div>
        <h2>Modularização de Código e LLMs</h2>
        <p><strong>Data:</strong> 09/06/2026</p>

        <div class="desc">
            Descrição da atividade desenvolvida. Explique os objetivos, conteúdos estudados e resultados obtidos.
        </div>

        <a href="#" class="btn">Ver Atividade</a>
    </div>

    <div class="card">
        <div class="numero">19</div>
        <h2>Avaliar site alegrete.org</h2>
        <p><strong>Data:</strong> 16/06/2026</p>

        <div class="desc">
            Descrição da atividade desenvolvida. Explique os objetivos, conteúdos estudados e resultados obtidos.
        </div>

        <a href="#" class="btn">Ver Atividade</a>
    </div>

    <div class="card">
        <div class="numero">20</div>
        <h2>Desenvolvimento com IA – Alegrete.org</h2>
        <p><strong>Data:</strong> 16/06/2026</p>

        <div class="desc">
            Descrição da atividade desenvolvida. Explique os objetivos, conteúdos estudados e resultados obtidos.
        </div>

        <a href="#" class="btn">Ver Atividade</a>
    </div>

    <div class="card">
        <div class="numero">21</div>
        <h2>Postar link e print do GitHub.io</h2>
        <p><strong>Data:</strong> 19/06/2026</p>

        <div class="desc">
            Descrição da atividade desenvolvida. Explique os objetivos, conteúdos estudados e resultados obtidos.
        </div>

        <a href="#" class="btn">Ver Atividade</a>
    </div>

    <div class="card">
        <div class="numero">22</div>
        <h2>Projeto Final (Versão 1)</h2>
        <p><strong>Data:</strong> 23/06/2026</p>

        <div class="desc">
            Descrição da atividade desenvolvida. Explique os objetivos, conteúdos estudados e resultados obtidos.
        </div>

        <a href="#" class="btn">Ver Atividade</a>
    </div>

    <div class="card">
        <div class="numero">23</div>
        <h2>Entrega Final do Portfólio GitHub.io</h2>
        <p><strong>Data:</strong> 30/06/2026</p>

        <div class="desc">
            Descrição da atividade desenvolvida. Explique os objetivos, conteúdos estudados e resultados obtidos.
        </div>

        <a href="#" class="btn">Ver Atividade</a>
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

<script>
document.querySelectorAll(".btn").forEach(btn => {
    btn.addEventListener("click", function(e){
        e.preventDefault();
        const desc = this.parentElement.querySelector(".desc");
        desc.style.maxHeight = desc.style.maxHeight ? null : desc.scrollHeight + "px";
    });
});
</script>
</body>
</html>
