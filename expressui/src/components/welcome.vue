<template>
  <v-card
    class="mx-auto"
    max-width="344"
  >
    <v-card-text>
      <div>Word of the Day</div>
      <p class="display-1 text--primary">
        Welcome to expressnews
      </p>
      <p>watch the news snippets without wasting time</p>
      <div class="text--primary">
        Interested to see the news snippets from standard news sources without wasting time<br>
        Login or register to get yourself updated with news
      </div>
    </v-card-text>
    
      <v-btn
        text
        color="teal accent-4"
       
      >
        <router-link :to = "{ name:'login' }">Login</router-link>
      </v-btn>
      <router-link :to = "{ name:'register' }"><v-btn>Register</v-btn></router-link>
  </v-card>

    
</template>