<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Portfólio Acadêmico - Lucas Viana de Freitas</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

*{margin:0;padding:0;box-sizing:border-box;font-family:'Poppins',sans-serif;}

body{
    min-height:100vh;
    background:linear-gradient(135deg,#0f172a,#1e293b,#2563eb);
    padding:40px 20px;
}

.container{max-width:1200px;margin:auto;}

.titulo{text-align:center;margin-bottom:30px;}
.titulo h1{color:white;font-size:3rem;}
.titulo p{color:#cbd5e1;margin-top:10px;}

.menu{display:flex;justify-content:center;flex-wrap:wrap;gap:15px;margin-bottom:35px;}
.menu a{
    text-decoration:none;color:white;
    background:rgba(255,255,255,0.12);
    padding:12px 20px;border-radius:12px;transition:.3s;
}
.menu a:hover{background:rgba(255,255,255,0.25);}

.identificacao{
    max-width:800px;margin:0 auto 40px;
    background:rgba(255,255,255,0.08);
    backdrop-filter:blur(15px);
    border:1px solid rgba(255,255,255,0.15);
    border-radius:24px;padding:25px;color:white;
}
.identificacao h2{margin-bottom:15px;color:#dbeafe;}
.identificacao p{margin:8px 0;}

.cards{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
    gap:25px;margin-top:30px;
}

.card{
    background:rgba(255,255,255,0.08);
    backdrop-filter:blur(15px);
    border:1px solid rgba(255,255,255,0.15);
    border-radius:24px;padding:30px;
    transition:.4s;position:relative;overflow:hidden;
    display:flex;flex-direction:column;
}
.card:hover{transform:translateY(-10px);box-shadow:0 20px 40px rgba(0,0,0,.25);}

.numero{
    width:60px;height:60px;border-radius:18px;
    background:linear-gradient(135deg,#3b82f6,#60a5fa);
    display:flex;align-items:center;justify-content:center;
    color:white;font-size:1.2rem;font-weight:bold;margin-bottom:20px;
    flex-shrink:0;
}

.card h2{color:white;margin-bottom:10px;font-size:1rem;}
.card .data{color:#94a3b8;font-size:.85rem;margin-bottom:12px;}

.card-body{flex:1;}

/* Viewer panel inside card */
.viewer{
    max-height:0;overflow:hidden;
    transition:max-height 0.45s ease;
    margin-top:12px;
}
.viewer.open{max-height:600px;}

.viewer-inner{
    background:rgba(0,0,0,0.25);
    border-radius:14px;
    padding:14px;
    margin-bottom:12px;
    overflow:auto;
    max-height:420px;
}

.viewer-inner img{
    width:100%;border-radius:10px;display:block;
}

.viewer-inner iframe{
    width:100%;height:380px;border:none;border-radius:10px;
}

.viewer-inner pre{
    color:#dbeafe;font-size:.78rem;white-space:pre-wrap;word-break:break-word;
    line-height:1.6;
}

.file-links{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:14px;}

.file-link{
    display:inline-flex;align-items:center;gap:6px;
    padding:7px 13px;border-radius:10px;
    background:rgba(255,255,255,0.12);
    color:#dbeafe;font-size:.8rem;text-decoration:none;
    border:1px solid rgba(255,255,255,0.18);
    transition:.25s;cursor:pointer;
}
.file-link:hover{background:rgba(255,255,255,0.22);}
.file-link.active{background:rgba(37,99,235,0.55);border-color:#60a5fa;}

.no-file{color:#64748b;font-size:.82rem;margin-bottom:12px;font-style:italic;}

.btn{
    display:inline-block;padding:12px 20px;border-radius:12px;
    text-decoration:none;background:white;color:#2563eb;font-weight:600;
    border:none;cursor:pointer;font-size:.9rem;transition:.2s;
    width:100%;text-align:center;margin-top:auto;
}
.btn:hover{background:#dbeafe;}

.links{margin-top:50px;}
.links a{color:#93c5fd;}

footer{text-align:center;color:#cbd5e1;margin-top:50px;}

/* HEIC notice */
.heic-notice{
    color:#fbbf24;font-size:.78rem;
    background:rgba(251,191,36,0.1);
    border:1px solid rgba(251,191,36,0.3);
    border-radius:8px;padding:8px 10px;margin-top:6px;
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

        <!-- 01 -->
        <div class="card" data-files='[{"name":"Atividade_1.png","type":"image","url":"Atividade_1.png"}]'>
            <div class="numero">01</div>
            <div class="card-body">
                <h2>Preenchimento do formulário de diagnóstico inicial</h2>
                <p class="data"><strong>Data:</strong> 17/03/2026</p>
            </div>
            <button class="btn">Ver Atividade</button>
            <div class="viewer">
                <div class="file-links"></div>
                <div class="viewer-inner"></div>
            </div>
        </div>

        <!-- 02 -->
        <div class="card" data-files='[]'>
            <div class="numero">02</div>
            <div class="card-body">
                <h2>QUIZ – Lógica de Programação (Preparatório em aula)</h2>
                <p class="data"><strong>Data:</strong> 20/03/2026</p>
            </div>
            <p class="no-file">Atividade realizada em aula (sem arquivo digital).</p>
            <button class="btn">Ver Atividade</button>
            <div class="viewer"></div>
        </div>

        <!-- 03 -->
        <div class="card" data-files='[]'>
            <div class="numero">03</div>
            <div class="card-body">
                <h2>QUIZ – Diagnóstico de Lógica de Programação</h2>
                <p class="data"><strong>Data:</strong> 27/03/2026</p>
            </div>
            <p class="no-file">Atividade realizada em aula (sem arquivo digital).</p>
            <button class="btn">Ver Atividade</button>
            <div class="viewer"></div>
        </div>

        <!-- 04 -->
        <div class="card" data-files='[{"name":"Atividade_4.pdf","type":"pdf","url":"Atividade_4.pdf"}]'>
            <div class="numero">04</div>
            <div class="card-body">
                <h2>Lista de 15 exercícios: escolher e resolver</h2>
                <p class="data"><strong>Data:</strong> 31/03/2026</p>
            </div>
            <button class="btn">Ver Atividade</button>
            <div class="viewer">
                <div class="file-links"></div>
                <div class="viewer-inner"></div>
            </div>
        </div>

        <!-- 05 -->
        <div class="card" data-files='[{"name":"Atividade_5.pdf","type":"pdf","url":"Atividade_5.pdf"}]'>
            <div class="numero">05</div>
            <div class="card-body">
                <h2>Lista de 10 Exercícios da Introdução a Algoritmos com Python</h2>
                <p class="data"><strong>Data:</strong> 10/04/2026</p>
            </div>
            <button class="btn">Ver Atividade</button>
            <div class="viewer">
                <div class="file-links"></div>
                <div class="viewer-inner"></div>
            </div>
        </div>

        <!-- 06 -->
        <div class="card" data-files='[{"name":"Atividade_6.pdf","type":"pdf","url":"Atividade_6.pdf"}]'>
            <div class="numero">06</div>
            <div class="card-body">
                <h2>Geração e Avaliação de Exercícios de Algoritmos com LLMs</h2>
                <p class="data"><strong>Data:</strong> 10/04/2026</p>
            </div>
            <button class="btn">Ver Atividade</button>
            <div class="viewer">
                <div class="file-links"></div>
                <div class="viewer-inner"></div>
            </div>
        </div>

        <!-- 07 -->
        <div class="card" data-files='[{"name":"Atividade_7.jpg","type":"image","url":"Atividade_7.jpg"}]'>
            <div class="numero">07</div>
            <div class="card-body">
                <h2>Quiz de Avaliação da Atividade: Uso de LLMs em Algoritmos</h2>
                <p class="data"><strong>Data:</strong> 10/04/2026</p>
            </div>
            <button class="btn">Ver Atividade</button>
            <div class="viewer">
                <div class="file-links"></div>
                <div class="viewer-inner"></div>
            </div>
        </div>

        <!-- 08 -->
        <div class="card" data-files='[
            {"name":"Atividade_8.1.heic","type":"heic","url":"Atividade_8.1.heic"},
            {"name":"Atividade_8.2.heic","type":"heic","url":"Atividade_8.2.heic"},
            {"name":"Atividade_8.3.heic","type":"heic","url":"Atividade_8.3.heic"},
            {"name":"Atividade_8.4.heic","type":"heic","url":"Atividade_8.4.heic"},
            {"name":"Atividade_8.5.heic","type":"heic","url":"Atividade_8.5.heic"},
            {"name":"Atividade_8.6.heic","type":"heic","url":"Atividade_8.6.heic"}
        ]'>
            <div class="numero">08</div>
            <div class="card-body">
                <h2>Resolver os 5 exercícios em papel</h2>
                <p class="data"><strong>Data:</strong> 21/04/2026</p>
            </div>
            <button class="btn">Ver Atividade</button>
            <div class="viewer">
                <div class="file-links"></div>
                <div class="viewer-inner"></div>
            </div>
        </div>

        <!-- 09 -->
        <div class="card" data-files='[{"name":"Atividade_9.pdf","type":"pdf","url":"Atividade_9.pdf"}]'>
            <div class="numero">09</div>
            <div class="card-body">
                <h2>Resolver os exercícios de listas/vetores/arrays em Python</h2>
                <p class="data"><strong>Data:</strong> 24/04/2026</p>
            </div>
            <button class="btn">Ver Atividade</button>
            <div class="viewer">
                <div class="file-links"></div>
                <div class="viewer-inner"></div>
            </div>
        </div>

        <!-- 10 -->
        <div class="card" data-files='[
            {"name":"Atividade_10.1.heic","type":"heic","url":"Atividade_10.1.heic"},
            {"name":"Atividade_10.2.heic","type":"heic","url":"Atividade_10.2.heic"}
        ]'>
            <div class="numero">10</div>
            <div class="card-body">
                <h2>Formulação e Resolução de Problemas com Vetores/Listas</h2>
                <p class="data"><strong>Data:</strong> 24/04/2026</p>
            </div>
            <button class="btn">Ver Atividade</button>
            <div class="viewer">
                <div class="file-links"></div>
                <div class="viewer-inner"></div>
            </div>
        </div>

        <!-- 11 -->
        <div class="card" data-files='[
            {"name":"Atividade_11.py","type":"code","url":"Atividade_11.py"},
            {"name":"Atividade_11a.py","type":"code","url":"Atividade_11a.py"},
            {"name":"Atividade_11b.py","type":"code","url":"Atividade_11b.py"}
        ]'>
            <div class="numero">11</div>
            <div class="card-body">
                <h2>Gerar versões do código com resultados visuais</h2>
                <p class="data"><strong>Data:</strong> 05/05/2026</p>
            </div>
            <button class="btn">Ver Atividade</button>
            <div class="viewer">
                <div class="file-links"></div>
                <div class="viewer-inner"></div>
            </div>
        </div>

        <!-- 12 -->
        <div class="card" data-files='[
            {"name":"Atividade_12.1.png","type":"image","url":"Atividade_12.1.png"},
            {"name":"Atividade_12.2.png","type":"image","url":"Atividade_12.2.png"},
            {"name":"Atividade_12.3.png","type":"image","url":"Atividade_12.3.png"},
            {"name":"Atividade_12.4.png","type":"image","url":"Atividade_12.4.png"}
        ]'>
            <div class="numero">12</div>
            <div class="card-body">
                <h2>Problemas de outras disciplinas – múltiplas abordagens</h2>
                <p class="data"><strong>Data:</strong> 08/05/2026</p>
            </div>
            <button class="btn">Ver Atividade</button>
            <div class="viewer">
                <div class="file-links"></div>
                <div class="viewer-inner"></div>
            </div>
        </div>

        <!-- 13 -->
        <div class="card" data-files='[{"name":"Atividade_13.pdf","type":"pdf","url":"Atividade_13.pdf"}]'>
            <div class="numero">13</div>
            <div class="card-body">
                <h2>Escolher e entregar problema de engenharia</h2>
                <p class="data"><strong>Data:</strong> 12/05/2026</p>
            </div>
            <button class="btn">Ver Atividade</button>
            <div class="viewer">
                <div class="file-links"></div>
                <div class="viewer-inner"></div>
            </div>
        </div>

        <!-- 14 -->
        <div class="card" data-files='[{"name":"Atividade_14.pdf","type":"pdf","url":"Atividade_14.pdf"}]'>
            <div class="numero">14</div>
            <div class="card-body">
                <h2>Entregar outro problema de engenharia</h2>
                <p class="data"><strong>Data:</strong> 15/05/2026</p>
            </div>
            <button class="btn">Ver Atividade</button>
            <div class="viewer">
                <div class="file-links"></div>
                <div class="viewer-inner"></div>
            </div>
        </div>

        <!-- 15 -->
        <div class="card" data-files='[{"name":"Atividade_15.pdf","type":"pdf","url":"Atividade_15.pdf"}]'>
            <div class="numero">15</div>
            <div class="card-body">
                <h2>Escolher e resolver problema de engenharia</h2>
                <p class="data"><strong>Data:</strong> 19/05/2026</p>
            </div>
            <button class="btn">Ver Atividade</button>
            <div class="viewer">
                <div class="file-links"></div>
                <div class="viewer-inner"></div>
            </div>
        </div>

        <!-- 16 -->
        <div class="card" data-files='[{"name":"Atividade_16.pdf","type":"pdf","url":"Atividade_16.pdf"}]'>
            <div class="numero">16</div>
            <div class="card-body">
                <h2>Evolução técnica da solução anterior</h2>
                <p class="data"><strong>Data:</strong> 22/05/2026</p>
            </div>
            <button class="btn">Ver Atividade</button>
            <div class="viewer">
                <div class="file-links"></div>
                <div class="viewer-inner"></div>
            </div>
        </div>

        <!-- 17 -->
        <div class="card" data-files='[]'>
            <div class="numero">17</div>
            <div class="card-body">
                <h2>Relato sobre entrevistas</h2>
                <p class="data"><strong>Data:</strong> 09/06/2026</p>
            </div>
            <p class="no-file">Atividade realizada em aula (sem arquivo digital).</p>
            <button class="btn">Ver Atividade</button>
            <div class="viewer"></div>
        </div>

        <!-- 18 -->
        <div class="card" data-files='[]'>
            <div class="numero">18</div>
            <div class="card-body">
                <h2>Modularização de Código e LLMs</h2>
                <p class="data"><strong>Data:</strong> 09/06/2026</p>
            </div>
            <p class="no-file">Atividade realizada em aula (sem arquivo digital).</p>
            <button class="btn">Ver Atividade</button>
            <div class="viewer"></div>
        </div>

        <!-- 19 -->
        <div class="card" data-files='[{"name":"Atividade_19.pdf","type":"pdf","url":"Atividade_19.pdf"}]'>
            <div class="numero">19</div>
            <div class="card-body">
                <h2>Avaliar site alegrete.org</h2>
                <p class="data"><strong>Data:</strong> 16/06/2026</p>
            </div>
            <button class="btn">Ver Atividade</button>
            <div class="viewer">
                <div class="file-links"></div>
                <div class="viewer-inner"></div>
            </div>
        </div>

        <!-- 20 -->
        <div class="card" data-files='[{"name":"Atividade_20.pdf","type":"pdf","url":"Atividade_20.pdf"}]'>
            <div class="numero">20</div>
            <div class="card-body">
                <h2>Desenvolvimento com IA – Alegrete.org</h2>
                <p class="data"><strong>Data:</strong> 16/06/2026</p>
            </div>
            <button class="btn">Ver Atividade</button>
            <div class="viewer">
                <div class="file-links"></div>
                <div class="viewer-inner"></div>
            </div>
        </div>

        <!-- 21 -->
        <div class="card" data-files='[
            {"name":"Atividade_21.1.png","type":"image","url":"Atividade_21.1.png"},
            {"name":"Atividade_21.2.png","type":"image","url":"Atividade_21.2.png"}
        ]'>
            <div class="numero">21</div>
            <div class="card-body">
                <h2>Postar link e print do GitHub.io</h2>
                <p class="data"><strong>Data:</strong> 19/06/2026</p>
            </div>
            <button class="btn">Ver Atividade</button>
            <div class="viewer">
                <div class="file-links"></div>
                <div class="viewer-inner"></div>
            </div>
        </div>

        <!-- 22 -->
        <div class="card" data-files='[]'>
            <div class="numero">22</div>
            <div class="card-body">
                <h2>Projeto Final (Versão 1)</h2>
                <p class="data"><strong>Data:</strong> 23/06/2026</p>
            </div>
            <p class="no-file">Atividade realizada em aula (sem arquivo digital).</p>
            <button class="btn">Ver Atividade</button>
            <div class="viewer"></div>
        </div>

        <!-- 23 -->
        <div class="card" data-files='[{"name":"Atividade_23.pdf","type":"pdf","url":"Atividade_23.pdf"}]'>
            <div class="numero">23</div>
            <div class="card-body">
                <h2>Entrega Final do Portfólio GitHub.io</h2>
                <p class="data"><strong>Data:</strong> 30/06/2026</p>
            </div>
            <button class="btn">Ver Atividade</button>
            <div class="viewer">
                <div class="file-links"></div>
                <div class="viewer-inner"></div>
            </div>
        </div>

    </div>
    </section>

    <section id="projeto" class="identificacao links" style="margin-top:50px;">
        <h2>Informações do Projeto</h2>
        <p>
            <strong>Repositório GitHub:</strong><br>
            <a href="https://github.com/algoritimos2/algoritimos2.github.io/tree/main" target="_blank">
                https://github.com/algoritimos2/algoritimos2.github.io
            </a>
        </p>
        <br>
        <p>
            <strong>Site Publicado (GitHub.io):</strong><br>
            <a href="https://algoritimos2.github.io" target="_blank">algoritimos2.github.io</a>
        </p>
        <br>
        <p><strong>Último Commit (Hash):</strong><br>fe55057</p>
    </section>

    <footer>© 2026 • Portfólio Acadêmico • Lucas Viana de Freitas</footer>

</div>

<script>
// Track which file is currently shown per card
const state = new WeakMap();

document.querySelectorAll('.card').forEach(card => {
    const btn = card.querySelector('.btn');
    const viewer = card.querySelector('.viewer');
    const fileLinksEl = card.querySelector('.file-links');
    const viewerInner = card.querySelector('.viewer-inner');
    const filesRaw = card.dataset.files || '[]';
    const files = JSON.parse(filesRaw);

    if (!files.length) {
        // No files: just toggle a simple message
        btn.addEventListener('click', () => {
            const open = viewer.classList.toggle('open');
            btn.textContent = open ? 'Fechar' : 'Ver Atividade';
            if (open && !viewer.dataset.built) {
                viewer.dataset.built = '1';
                viewer.innerHTML = '<p style="color:#94a3b8;font-size:.85rem;padding:10px 0;">Sem arquivo digital associado a esta atividade.</p>';
            }
        });
        return;
    }

    // Build file selector tabs
    files.forEach((f, i) => {
        const tab = document.createElement('button');
        tab.className = 'file-link' + (i === 0 ? ' active' : '');
        tab.textContent = f.name;
        tab.dataset.index = i;
        tab.addEventListener('click', () => showFile(card, files, i, fileLinksEl, viewerInner));
        fileLinksEl.appendChild(tab);
    });

    btn.addEventListener('click', () => {
        const isOpen = viewer.classList.toggle('open');
        btn.textContent = isOpen ? 'Fechar' : 'Ver Atividade';
        if (isOpen && !state.has(card)) {
            showFile(card, files, 0, fileLinksEl, viewerInner);
        }
    });
});

function showFile(card, files, index, fileLinksEl, viewerInner) {
    state.set(card, index);

    // Update active tab
    fileLinksEl.querySelectorAll('.file-link').forEach((t, i) => {
        t.classList.toggle('active', i === index);
    });

    const f = files[index];
    viewerInner.innerHTML = '';

    if (f.type === 'image') {
        const img = document.createElement('img');
        img.src = f.url;
        img.alt = f.name;
        img.onerror = () => { viewerInner.innerHTML = notFound(f.url); };
        viewerInner.appendChild(img);

    } else if (f.type === 'pdf') {
        const frame = document.createElement('iframe');
        frame.src = f.url;
        frame.title = f.name;
        viewerInner.appendChild(frame);
        // Fallback link
        const link = document.createElement('a');
        link.href = f.url;
        link.target = '_blank';
        link.className = 'file-link';
        link.style.marginTop = '8px';
        link.textContent = '↗ Abrir PDF em nova aba';
        viewerInner.appendChild(link);

    } else if (f.type === 'code') {
        fetch(f.url)
            .then(r => {
                if (!r.ok) throw new Error();
                return r.text();
            })
            .then(text => {
                const pre = document.createElement('pre');
                pre.textContent = text;
                viewerInner.appendChild(pre);
            })
            .catch(() => {
                viewerInner.innerHTML = notFound(f.url);
            });

    } else if (f.type === 'heic') {
        // HEIC files cannot be shown inline in browsers; offer download link
        viewerInner.innerHTML = `
            <div class="heic-notice">
                ⚠️ Arquivos .heic não são exibidos diretamente no navegador.<br>
                Faça o download para visualizar:
            </div>
            <a href="${f.url}" download class="file-link" style="margin-top:10px;display:inline-flex;">
                ⬇ Baixar ${f.name}
            </a>
        `;
    }
}

function notFound(url) {
    return `<p style="color:#f87171;font-size:.82rem;">
        Arquivo não encontrado: <strong>${url}</strong><br>
        Verifique se o arquivo está na mesma pasta do index.html.
    </p>`;
}
</script>
</body>
</html>
