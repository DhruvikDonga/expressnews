

<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      app
    >
      <!--  -->
    </v-navigation-drawer>

    <v-app-bar app>
      <v-app-bar-nav-icon @click="drawer = !drawer">
       
      </v-app-bar-nav-icon>

      <v-toolbar-title>Expressnews:-be fast</v-toolbar-title>
    </v-app-bar>
     <v-navigation-drawer
      v-model="drawer"
      absolute
      temporary
    >
      <v-list
        nav
        dense
      >
        <v-list-item-group
          
          active-class="deep-purple--text text--accent-4"
        >

        <v-list-item  v-if="accessToken!=null" disable>
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title><h1>Welcome </h1></v-list-item-title>
          </v-list-item>

          <v-list-item  v-if="accessToken==null">
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title><router-link :to = "{ name:'login' }">Login</router-link></v-list-item-title>
          </v-list-item>

          

          <v-list-item  v-if="accessToken!=null">
            <v-list-item-icon>
              <v-icon>mdi-account</v-icon>
            </v-list-item-icon>
            <v-list-item-title><router-link :to = "{ name:'logout' }">Logout</router-link></v-list-item-title>
          </v-list-item>

          <v-list-item  v-if="accessToken==null">
            <v-list-item-icon>
              <v-icon>mdi-account</v-icon>
            </v-list-item-icon>
            <v-list-item-title><router-link :to = "{ name:'register' }">Register</router-link></v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
    <v-main>
      <!--  -->
      <router-view/>

    </v-main>

  </v-app>
</template>

<script>
  import { mapState } from 'vuex'
  export default {
    data: () => ({ drawer: null}),
    computed:mapState(
      ['accessToken'],
      ),
    
    }
  

</script>
