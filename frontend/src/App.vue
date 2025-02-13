<template>
  <div class="d-flex align-items-center justify-content-center h-100">
    <div class="bg-primary-subtle p-4 rounded-1">
      <form>
        <div class="input-group mb-3">
          <input type="text" class="form-control" placeholder="Adicionar tarefa" aria-label="Adicionar tarefa" aria-describedby="adicionar tarefa">
          <span class="input-group-text" role="button">
            <i class="bi bi-plus-lg"></i>
          </span>
        </div>
      </form>
      <section>
        <div class="d-flex align-items-center justify-content-between bg-black p-2 rounded-1 text-light">
          <input type="checkbox" name="" id="" role="button">
          <p class="m-0">Tarefa</p>
          <div>
            <i class="bi bi-pencil-square text-warning me-3 fs-5"></i>
            <i class="bi bi-x-circle-fill text-danger fs-5"></i>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';

const tasks = axios.get('http://127.0.0.1:5000')
console.log(tasks)
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