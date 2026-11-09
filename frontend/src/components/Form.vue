<script setup>
import axios, { Axios } from 'axios';
import { reactive } from 'vue'

const form = reactive({
  name: '',
  deadline: '',
  description: '',
  repository: '',
  amount: ''
})

async function handleSubmit() {
  

  try {
    const response = await axios.post(
      "http://localhost:3000/make-project",
      {
        "name": form.name,
        "deadline": form.deadline,
        "description": form.description,
        "repo": form.repository,
        "amount": form.amount
      }
    )
    console.log(response.data)
  }
  catch (error) {
    console.error(error);
  }

  console.log(form.deadline)
}
</script>


<template>
  <div class="container mx-auto max-w-xl p-6">
    <h2 class="mb-6 text-xl font-semibold">Create Project</h2>

    <form @submit.prevent="handleSubmit" class="flex flex-col gap-4">

      <div class="flex flex-col gap-1">
        <label for="name">Name</label>
        <input id="name" type="text" v-model="form.name" />
      </div>

      <div class="flex flex-col gap-1">
        <label for="deadline">Deadline</label>
        <input id="deadline" type="date"  v-model="form.deadline" />
      </div>

      <div class="flex flex-col gap-1">
        <label for="description">Description</label>
        <textarea
          id="description"
          v-model="form.description"
          rows="4"
        ></textarea>
      </div>

      <div class="flex flex-col gap-1">
        <label for="repository">Repository</label>
        <input id="repository" type="url" v-model="form.repository" />
      </div>

      <div class="flex flex-col gap-1">
        <label for="amount">Amount</label>
        <input id="amount" type="number" v-model.number="form.amount" />
      </div>

      <div class="flex justify-end mt-2">
        <button class="text-white bg-blue-600 px-2 py-1 
        rounded-lg hover:bg-blue-700 hover:cursor-pointer" type="submit">Submit</button>
      </div>

    </form>
  </div>
</template>


<style scoped>

input {
  border: 1px solid black;
  border-radius: 5px;
}

textarea {
  border: 1px solid black;
  border-radius: 5px;
}
</style>