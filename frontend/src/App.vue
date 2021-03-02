<template>
  <div id="app">
    <div class="form-group row">
        <b>Apply filters</b>
        <input type="text" class="form-control col-3 mx-2" placeholder="Name" v-model="filters.name">
        <input type="text" class="form-control col-3 mx-2" placeholder="Surname" v-model="filters.surname">
        <input type="text" class="form-control col-3 mx-2" placeholder="Telephone" v-model="filters.telephone">
        
        <button class="btn btn-success" @click="reload_people()">Apply</button>
    </div>

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

            <input type="text" class="form-control col-3 mx-2" placeholder="Street" v-model="person.address.street">
            <input type="text" class="form-control col-3 mx-2" placeholder="City" v-model="person.address.city">
            <input type="text" class="form-control col-3 mx-2" placeholder="Country" v-model="person.address.country">
            
            <input type="text" class="form-control col-3 mx-2" placeholder="Telephone" v-model="person.telephone">
            <input type="text" class="form-control col-3 mx-2" placeholder="URL" v-model="person.url">
            <input type="file" ref="file" v-on:change="handleFileUpload()" accept="image/*"/>

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
            <th> Image </th>
            <th> Actions </th>
            
        </thead>
        <tbody>
            <tr v-for="person in people" :key="person.id">
                <td>{{  person.name  }}</td>
                <td>{{  person.surname  }}</td>

                <td v-if="person.address"> 
                    <p>City: {{  person.address.city  }}</p>
                    <p>Street: {{  person.address.street  }}</p>
                    <p>Country: {{  person.address.country  }}</p>
                </td>
                <td v-else>No address was chosen!</td>

                <td>{{  person.telephone  }}</td>
                <td> {{person.url}}</td>
                <td> <img :src="person.image" alt=""></td>
                
                <td>
                    <button class="btn btn-outline-primary btn-sm mx-1"
                    @click="$data.person = person">Edit</button>
                    <button class="btn btn-outline-danger btn-sm mx-1"
                    @click.stop="delete_person(person)">Delete</button>
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
        filters: {
            name: "",
            surname: "",
            telephone: ""
        },
        errors:[],
        person: {
            name: null,
            surname: null,
            address: {
                city: null,
                street: null,
                country: null
            },
            telephone: null,
            url: null,
            image: null
        },
        people: []
    }
  },

  async created(){
    await this.get_people();
  },

  methods: {
    handleFileUpload(){
        console.log(this.$refs.file.files)
        this.person.image = this.$refs.file.files[0];
    },

    checkForm: function (e) {
        if (this.person.name && this.person.surname) {
            return true;
        }

        this.errors = [];

        if (!this.person.name) {
            this.errors.push('123.');
        }
        if (!this.person.surname) {
            this.errors.push('456.');
        }

        e.preventDefault();
    },

    reload_people(){
        this.get_filtered_people();
    },

    submit_form(){
        if (this.person.id === undefined){
            this.create_person();
        } else{
            this.edit_person();
        }
    },
    async get_filtered_people(){
        let strFilters = '';
        for (let key in this.filters) {
            strFilters += `${key}=${this.filters[key]}&`
        }
        strFilters = strFilters.slice(0, -1);

        var response = await fetch(`http://127.0.0.1:8000/api/people/?${strFilters}`);
        this.people = await response.json();
    },
    async get_people(){
        var response = await fetch('http://127.0.0.1:8000/api/people/');
        this.people = await response.json();
    },

    get_form_data(){
        let jsonKeys = ['address'];
        let formData = new FormData();
        for ( var key in this.person ) {
            if (this.person[key]){
                if (this.person[key] instanceof File) {
                    formData.append(key, this.person[key]);
                } else if (jsonKeys.includes(key)) {
                    formData.append(key, JSON.stringify(this.person[key]));
                } else {
                    formData.append(key, this.person[key]);
                }
            }
        }
        return formData
    },
    clear_person(){
        this.person = {
            name: null,
            surname: null,
            address: {
                city: null,
                street: null,
                country: null
            },
            telephone: null,
            url: null,
            image: null
        };
    },
    async create_person(){
        await fetch('http://127.0.0.1:8000/api/people/', {
            method: 'post',
            body: this.get_form_data()
        });
        await this.get_people();
        this.clear_person();
    },

    async edit_person(){
        if (!(this.person.image instanceof File)) {
            this.person.image = null;
        }
        await fetch(`http://127.0.0.1:8000/api/people/${this.person.id}/`, {
            method: 'put',
            body: this.get_form_data()
        });
        await this.get_people();
        this.clear_person();
    },

    async delete_person(person){
        await fetch(`http://127.0.0.1:8000/api/people/${person.id}/`, {
            method: 'delete'
        });
        await this.get_people();
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
