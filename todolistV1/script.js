const form = document.querySelector("form");
const semTarefa = document.getElementById("sem-tarefa");
let tarefas = JSON.parse(localStorage.getItem("tarefas")) || [];
const sectionTarefas = document.getElementById("tarefas")

renderizarTarefas(tarefas);

form.addEventListener("submit", (event) => {
    event.preventDefault();
    
    const inputTarefa = document.getElementById("tarefaId");
    
    if (inputTarefa) {
        if (document.querySelector(".text-danger-emphasis")) {
            document.querySelector(".text-danger-emphasis").setAttribute("class", "d-none");
        } 

        tarefas.push({ id: tarefas.length +1, titulo: inputTarefa.value });
        
        localStorage.setItem("tarefas", JSON.stringify(tarefas));

        renderizarTarefas(tarefas);

        inputTarefa.value = "";
        inputTarefa.focus();

    } else {
        if (document.querySelector(".text-danger-emphasis")) {
           return; 
        } else {
            const textoValidacao = document.createElement("p");
            textoValidacao.setAttribute("class", "text-danger-emphasis bg-danger-subtle border border-danger rounded-1 p-1 mt-2");
            textoValidacao.innerText = "Campo não pode estar vazio";
            form.insertAdjacentElement("afterend", textoValidacao);
        }
    }
});

function renderizarTarefas(tarefas) {   
    if (tarefas.length != 0) {
        sectionTarefas.innerHTML = "";
        
        semTarefa.classList.add("d-none");
        
        tarefas.forEach(tarefa => {
            const divContainer = document.createElement("div");
            divContainer.className = "p-2 bg-info bg-opacity-10 border border-info rounded-1 d-flex justify-content-between align-items-center shadow-sm";
            divContainer.setAttribute("id", `${tarefa.id}`);
            
            const input = document.createElement("input");
            input.setAttribute("type", "checkbox");
    
            const texto = document.createElement("p");
            texto.className = "m-0";
            texto.textContent = tarefa.titulo;
    
            const divBotoes = document.createElement("div");
            divBotoes.className = "d-flex align-items-center gap-2";
    
            const btnEdit = document.createElement("span");
            btnEdit.className = "material-symbols-outlined text-warning-emphasis";
            btnEdit.textContent = "edit_square";
            btnEdit.setAttribute("role", "button");
    
            const btnDelete = document.createElement("span");
            btnDelete.className = "material-symbols-outlined text-danger";
            btnDelete.textContent = "delete_forever";
            btnDelete.setAttribute("role", "button");
    
            divBotoes.append(btnEdit, btnDelete);
            divContainer.append(input, texto, divBotoes);
            
            sectionTarefas.appendChild(divContainer);
        });
    }
}

document.addEventListener("click", (event) => {
    if (event.target.textContent == "delete_forever") {
        const idTarefa = event.target.parentElement.parentElement.id;
        const tarefasAtualizadas = tarefas.filter(tarefa => tarefa.id != idTarefa);
        tarefas = tarefasAtualizadas;

        localStorage.setItem("tarefas", JSON.stringify(tarefas));
        renderizarTarefas(tarefas);
    }
})
