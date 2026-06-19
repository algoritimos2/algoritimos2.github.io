```html
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
    padding:40px 20px;
}

.container{
    max-width:1200px;
    margin:auto;
}

header{
    text-align:center;
    margin-bottom:40px;
}

header h1{
    color:white;
    font-size:3rem;
    margin-bottom:10px;
}

header p{
    color:#cbd5e1;
}

.formulario{
    background:rgba(255,255,255,0.08);
    backdrop-filter:blur(15px);
    border:1px solid rgba(255,255,255,.15);
    border-radius:25px;
    padding:30px;
    margin-bottom:40px;
}

.formulario h2{
    color:white;
    margin-bottom:20px;
}

.input-group{
    margin-bottom:15px;
}

label{
    display:block;
    color:white;
    margin-bottom:6px;
}

input,
textarea{
    width:100%;
    padding:14px;
    border:none;
    border-radius:12px;
    outline:none;
    font-size:15px;
}

textarea{
    min-height:120px;
    resize:vertical;
}

input[type="file"]{
    background:white;
}

.btn{
    width:100%;
    padding:15px;
    border:none;
    border-radius:12px;
    background:#2563eb;
    color:white;
    font-size:16px;
    font-weight:600;
    cursor:pointer;
    transition:.3s;
}

.btn:hover{
    background:#1d4ed8;
}

.cards{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(300px,1fr));
    gap:25px;
}

.card{
    background:rgba(255,255,255,0.08);
    backdrop-filter:blur(15px);
    border:1px solid rgba(255,255,255,.15);
    border-radius:25px;
    padding:25px;
    transition:.3s;
}

.card:hover{
    transform:translateY(-6px);
}

.numero{
    width:55px;
    height:55px;
    border-radius:15px;
    background:linear-gradient(135deg,#3b82f6,#60a5fa);
    color:white;
    display:flex;
    align-items:center;
    justify-content:center;
    font-weight:bold;
    margin-bottom:15px;
}

.card h3{
    color:white;
    margin-bottom:10px;
}

.card p{
    color:#dbeafe;
    line-height:1.7;
    margin-bottom:15px;
}

.arquivo{
    color:#93c5fd;
    text-decoration:none;
    display:inline-block;
    margin-bottom:15px;
}

.excluir{
    width:100%;
    border:none;
    padding:10px;
    border-radius:10px;
    background:#dc2626;
    color:white;
    cursor:pointer;
}

.excluir:hover{
    background:#b91c1c;
}

.vazio{
    color:white;
    text-align:center;
    opacity:.8;
    margin-top:30px;
}

</style>
</head>
<body>

<div class="container">

<header>
    <h1>Portfólio de Atividades</h1>
    <p>Cadastre suas atividades acadêmicas</p>
</header>

<div class="formulario">

    <h2>Nova Atividade</h2>

    <div class="input-group">
        <label>Nome da atividade</label>
        <input type="text" id="nome">
    </div>

    <div class="input-group">
        <label>Descrição</label>
        <textarea id="descricao"></textarea>
    </div>

    <div class="input-group">
        <label>Arquivo</label>
        <input type="file" id="arquivo">
    </div>

    <button class="btn" onclick="adicionarAtividade()">
        Adicionar Atividade
    </button>

</div>

<div id="lista" class="cards"></div>

<div id="mensagemVazia" class="vazio">
    Nenhuma atividade cadastrada.
</div>

</div>

<script>

let atividades =
JSON.parse(localStorage.getItem("atividades")) || [];

function salvar(){
    localStorage.setItem(
        "atividades",
        JSON.stringify(atividades)
    );
}

function renderizar(){

    const lista =
    document.getElementById("lista");

    const vazio =
    document.getElementById("mensagemVazia");

    lista.innerHTML = "";

    if(atividades.length === 0){
        vazio.style.display = "block";
        return;
    }

    vazio.style.display = "none";

    atividades.forEach((atividade,index)=>{

        lista.innerHTML += `
        <div class="card">

            <div class="numero">
                ${String(index+1).padStart(2,"0")}
            </div>

            <h3>${atividade.nome}</h3>

            <p>${atividade.descricao}</p>

            ${
                atividade.arquivo
                ? `<span class="arquivo">📎 ${atividade.arquivo}</span>`
                : ""
            }

            <button
            class="excluir"
            onclick="remover(${index})">
            Excluir
            </button>

        </div>
        `;
    });
}

function adicionarAtividade(){

    const nome =
    document.getElementById("nome").value.trim();

    const descricao =
    document.getElementById("descricao").value.trim();

    const arquivo =
    document.getElementById("arquivo").files[0];

    if(!nome || !descricao){
        alert("Preencha todos os campos.");
        return;
    }

    atividades.push({
        nome,
        descricao,
        arquivo: arquivo ? arquivo.name : ""
    });

    salvar();
    renderizar();

    document.getElementById("nome").value = "";
    document.getElementById("descricao").value = "";
    document.getElementById("arquivo").value = "";
}

function remover(index){

    if(confirm("Deseja excluir esta atividade?")){

        atividades.splice(index,1);

        salvar();
        renderizar();
    }
}

renderizar();

</script>

</body>
</html>
```
