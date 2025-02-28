const form = document.querySelector("form");
let tarefas = JSON.parse(localStorage.getItem("tarefas")) || [];
const sectionTarefas = document.getElementById("tarefas")

const divSemtarefa = document.createElement("div");
divSemtarefa.className = "text-center m-0 bg-info bg-opacity-10 border border-info rounded-3 p-2";
divSemtarefa.setAttribute("id", "sem-tarefa");
divSemtarefa.textContent = "Nenhuma tarefa adicionada";

sectionTarefas.appendChild(divSemtarefa);

renderizarTarefas(tarefas);

tarefas.forEach(tarefa => {
    if (tarefa.concluida) {
        concluirTarefa(tarefa.id);
    }
})

form.addEventListener("submit", (event) => {
    event.preventDefault();
    
    const inputTarefa = document.getElementById("tarefaId");
    
    if (inputTarefa.value.trim()) {
        if (document.querySelector(".text-danger-emphasis")) {
            document.querySelector(".text-danger-emphasis").setAttribute("class", "d-none");
        } 

        tarefas.push({ id: tarefas.length +1, titulo: inputTarefa.value, concluida: false });
        
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
        
        divSemtarefa.classList.add("d-none");

        tarefas.forEach(tarefa => {
            const divContainer = document.createElement("div");
            divContainer.className = "p-2 bg-info bg-opacity-10 border border-info rounded-1 d-flex justify-content-between align-items-center shadow-sm";
            divContainer.setAttribute("id", `${tarefa.id}`);
            
            const input = document.createElement("input");
            input.setAttribute("type", "checkbox");
            input.checked = tarefa.concluida;
    
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
    } else {
        sectionTarefas.innerHTML = ""; 
        sectionTarefas.appendChild(divSemtarefa); 
        divSemtarefa.classList.remove("d-none")
    }
}

document.addEventListener("click", (event) => {
    if (event.target.textContent == "delete_forever") {
        const idTarefa = event.target.parentElement.parentElement.id;
        const tarefasAtualizadas = tarefas.filter(tarefa => tarefa.id != idTarefa);
        tarefas = tarefasAtualizadas;
        
        localStorage.setItem("tarefas", JSON.stringify(tarefas));
        
        renderizarTarefas(tarefas);

        if (document.getElementById(idTarefa)) {
            document.getElementById(idTarefa).remove();
        }
    }
})

document.addEventListener("click", (event) => {
    if (event.target.type == "checkbox") {
        const idTarefa = event.target.parentElement.id;
        const tarefa = tarefas.find(tarefa => tarefa.id == idTarefa);

        tarefa.concluida = event.target.checked;

        localStorage.setItem("tarefas", JSON.stringify(tarefas));

        concluirTarefa(idTarefa);
    }
})

function concluirTarefa(idTarefa) {
    document.getElementById(idTarefa).classList.toggle("bg-success")
    document.getElementById(idTarefa).classList.toggle("bg-info")
    document.getElementById(idTarefa).classList.toggle("bg-opacity-10")
    document.getElementById(idTarefa).classList.toggle("bg-opacity-50")
    document.getElementById(idTarefa).classList.toggle("text-decoration-line-through")
}