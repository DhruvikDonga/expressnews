<template>
<v-app>
  
  <v-form
    ref="form"
    
    lazy-validation
    @submit.prevent="loginUser"
  >
    <v-text-field
      v-model="username"
      label="Name"
      
      required
    ></v-text-field>

    <v-text-field
      v-model="password"
      type="password"
      label="enter password"
      required
    ></v-text-field>


    <v-btn
      color="success"
      class="mr-4"
      type="submit"
    >
      Login
    </v-btn>

  </v-form>

  <v-alert
  color="red"
  dismissible
  elevation="24"
  type="warning"
  v-if="wrongCred==true"
><v-icon>mdi-account</v-icon>Either username or password is wrong please try again </v-alert>
</v-app>
</template>

<script>
  export default {
    name: 'login',
   
    data () {
      return {
        username: '',
        password: '',
        wrongCred: false,
        show:false // activates appropriate message if set to true
      }
    },
    methods: {
      loginUser () { // call loginUSer action
        this.$store.dispatch('loginUser', {
          username: this.username,
          password: this.password
        })
            .then(() => {
              this.wrongCred = false
              this.$router.push({ name: 'home' })
            })
          .catch(err => {
            console.log(err)
            this.wrongCred = true // if the credentials were wrong set wrongCred to true
          })
        }
      }
  }
</script>
