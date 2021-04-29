<template>
<v-app>
  <div  v-if="news.length>0">
  <v-alert
  elevation="22"
  
  type="info"
>Welcome <u><b>{{userdetail.username}}</b></u>.<br>You have {{news.length}} news saved.<br> Scroll down the saved news and learn more</v-alert>
<div v-for="i in news.slice()" :key="i.id">
  <v-card
    class="mx-auto"
    max-width="344"
  >
    <v-card-text>
      <p class="display-1 text--primary">
        {{i.newstitle}}
      </p>
      <p>{{i.source}}</p>
      <div class="text--primary">
        {{i.content}}
      </div>
    </v-card-text>
    <v-card-actions>
      <v-btn
        text
        color="teal accent-4"
        v-bind:href=i.url
        raised
        rounded
      >
        Learn More
      </v-btn>
      <v-btn  
      @click = "addfavourites(i.id)"
      raised
        rounded
      >
      <v-icon v-if="i.favourite.find(id=> id == userdetail.userid)">mdi-bookmark-check</v-icon>
      <v-icon v-else text>mdi-bookmark</v-icon>

      </v-btn>

    </v-card-actions>
    </v-card>
    <br>
</div>

</div>
<div v-else>
    
  <v-alert
  elevation="22"
  
  type="info"
>Welcome <u><b>{{userdetail.username}}</b></u>.<br>You have no news saved get started and save your favorite news</v-alert>
</div>
<div>
  <br><br><br>
</div>
<v-footer paddless fixed>
    <v-col
      class="text-center"
      cols="13"
    >
      <v-btn :to = "{ name:'home' }" rounded><v-icon>mdi-home</v-icon></v-btn>
      <v-btn :to = "{ name:'savednews' }" color="primary" rounded elevation="24"><v-icon>mdi-bookmark-multiple</v-icon></v-btn>

    </v-col>
  </v-footer>



</v-app>



</template>

<script>
import { getAPI } from '../api/axios-base'
  import { mapState } from 'vuex'
  import { axiosBase } from '../api/axios-base.js'

export default {
    
    onIdle () { // dispatch logoutUser if no activity detected
      this.$store.dispatch('logoutUser')
        .then(response => {
          this.$router.push('/welcome')
          console.log(response)
        })
    },
    data(){
      return {
        userdetail:'',
        news:[],
        saveids:[],
        new : {
          url:'',
          content:'',
          newstitle:'',
          source:'',
        },
      }
    },
    computed: mapState(['APIData']), // get APIData from store.state.
    created () {
        getAPI.get('/userdetails/', { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } }) // proof that your access token is still valid; if not the
        // axios getAPI response interceptor will attempt to get a new  access token from the server. check out ../api/axios-base.js getAPI instance response interceptor
          .then(response => {
            console.log('GetAPI successfully got the userdetails')
            this.userdetail = response.data // store the response data in store
            console.log(this.$store.state.APIData)
          })
          .catch(err => { // refresh token expired or some other error status
            console.log(err)
          }),

          this.displayNews()
                    this.addfavourites()

    },
    methods:{
      displayNews() {
        getAPI.get("/getfavourite/", { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } }).then(response => {
        console.log(response)
        this.news = response.data
      })
      .catch(error => {
        console.log(error)
        this.errored = true
      })
      .finally(() => this.loading = false)
      },
      addfavourites(saveid) {
        axiosBase.post('/favourite/', {
         newsid:saveid,
         userid:this.userdetail.userid
        })
          .then(res => {
            console.log(res)
            this.displayNews()
          })
      }
    }
}
</script>