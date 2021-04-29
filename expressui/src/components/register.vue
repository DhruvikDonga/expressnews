
<template>
<v-app>
  
  <v-form
    ref="form"
    
    lazy-validation
    @submit.prevent="registerUser"
  >
    <v-text-field
      v-model="name"
      label="Name"
      
      required
    ></v-text-field>
    <v-text-field
      v-model="email"
      label="Email"
      
      required
    ></v-text-field>
    <v-text-field
      v-model="username"
      label="Username"
      
      required
    ></v-text-field>
    <v-text-field
      v-model="password"
      label="Password"
      
      required
    ></v-text-field>
    <v-text-field
      v-model="confirm"
      label="Conform password"
      
      required
    ></v-text-field>

    <v-btn
      color="success"
      class="mr-4"
      type="submit"
    >
      Register
    </v-btn>

  </v-form>

  
</v-app>
</template>
<script>
  export default {
    name: 'register',
    
    data () {
      return {
        name: '',
        email: '',
        username: '',
        password: '',
        confirm: ''
      }
    },
    methods: {
      registerUser () {
        this.$store.dispatch('registerUser', {
          name: this.name, 
          email: this.email,
          username: this.username,
          password: this.password,
          confirm: this.confirm
        }).then(() => {
          this.$router.push({ name: 'login' })
        })
      }
    }
  }
</script>
