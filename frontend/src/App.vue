<template>
  <div id="app">

    <form @submit.prevent="submit_form" @submit="checkForm" action="/something" method="post">

        <p v-if="errors.length">
            <b>Please correct the following error(s):</b>
            <ul>
                <li v-for="error in errors" :key="error">{{ error }}</li>
            </ul>
    </p>
        <div class="form-group row">
            <input type="text" class="form-control col-3 mx-2" placeholder="Name" v-model="person.name">
            <input type="text" class="form-control col-3 mx-2" placeholder="Surname" v-model="person.surname">
            <input type="text" class="form-control col-3 mx-2" placeholder="Address" v-model="person.address">
            <input type="text" class="form-control col-3 mx-2" placeholder="Telephone" v-model="person.telephone">
            <input type="text" class="form-control col-3 mx-2" placeholder="URL" v-model="person.url">
            <button class="btn btn-success">Submit changes or add a new person</button>
        </div>
    </form>

    <table class="table">
        <thead>
            <th>Name</th>
            <th>Surname</th>
            <th>Address</th>
            <th>Telephone</th>
            <th>URL</th>
        </thead>
        <tbody>
            <tr v-for="person in people" :key="person.id" @dblclick="$data.person = person">
                <td>{{  person.name  }}</td>
                <td>{{  person.surname  }}</td>
                <td>{{  person.address  }}</td>
                <td>{{  person.telephone  }}</td>
                <td>{{  person.url  }}</td>
                <td>
                    <button class="btn btn-outline-danger btn-sm mx-1"
                    @click="delete_person(person)">x</button>
                </td>
            </tr>
        </tbody>
    </table>

  </div>
</template>

<script>

export default {
  name: 'App',
  data(){
    return{
        errors:[],
        person: {},
        people: []
    }
  },

  async created(){
    await this.get_people();
  },

  methods: {

    checkForm: function (e) {
        if (this.name && this.surname && this.address && this.telephone && this.url) {
            return true;
        }

        this.errors = [];

        if (!this.name) {
            this.errors.push('123.');
        }
        if (!this.surname) {
            this.errors.push('456.');
        }
        if (!this.address) {
            this.errors.push('666.');
        }
        if (!this.telephone) {
            this.errors.push('55.');
        }
        if (!this.url) {
            this.errors.push('553.');
        }

        e.preventDefault();
    },

    submit_form(){
        if (this.person.id === undefined){
        this.create_person();
        } else{
            this.edit_person();
        }
    },
    async get_people(){
        var response = await fetch('http://127.0.0.1:8000/api/people/');

        this.people = await response.json();


    },
    async create_person(){
        await this.get_people();

        await fetch('http://127.0.0.1:8000/api/people/', {
            method: 'post',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(this.person)
        });
        await this.get_people();
    },

    async edit_person(){
        await this.get_people();

        await fetch(`http://127.0.0.1:8000/api/people/${this.person.id}/`, {
            method: 'put',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(this.person)
        });
        await this.get_people();
        this.person = {};
    },

    async delete_person(person){
        await this.get_people();

        await fetch(`http://127.0.0.1:8000/api/people/${person.id}/`, {
            method: 'delete',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(this.person)
        });
        await this.get_people();
        this.person = {};
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
