<template>
  <div class="d-flex align-items-center justify-content-center h-100">
    <div class="bg-primary-subtle p-4 rounded-1">
      <form @submit.prevent="adicionarTarefa" method="post">
        <div class="input-group mb-3">
          <input type="text" class="form-control" name="titulo" placeholder="Adicionar tarefa" v-model="tituloTarefa">
          <button type="submit" class="input-group-text">
            <i class="bi bi-plus-lg"></i>
          </button>
        </div>
      </form>
      <section>
        <div class="d-flex align-items-center justify-content-between bg-black p-2 rounded-1 text-light" v-for="tarefa in tarefas" :key="tarefa.id" v-if="tarefas != ''">
          <input type="checkbox" name="tarefa" role="button">
          <p class="m-0">{{ tarefa.titulo }}</p>
          <div>
            <i class="bi bi-pencil-square text-warning me-3 fs-5" role="button"></i>
            <i class="bi bi-x-circle-fill text-danger fs-5" role="button"></i>
          </div>
        </div>
        <p v-else class="text-center m-0">Nenhuma tarefa cadastrada</p>
      </section>
    </div>
  </div>
</template>

<script setup>

</script>

<style scoped>
form, section {
  min-width: 400px;
}

input[type='checkbox']{
  width: 20px;
  height: 20px;
}
</style>