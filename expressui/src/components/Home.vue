<template>
<v-app>
  <v-alert
  elevation="22"
  
  type="info"
>Welcome <u><b>{{userdetail.username}}</b></u> scroll down the news and learn more</v-alert>
<div v-for="i in filterProductsByCategory.slice()" :key="i.id">
  <v-card
    class="mx-auto"
    max-width="344"
  >
    <v-card-text>
      <p class="display-1 text--primary">
        {{i.newstitle}}
      </p>
      <p>{{i.source}}<v-chip
  color="blue"
>{{i.category}}</v-chip></p>
      <div class="text--primary">
        {{i.content}}
      </div>
    </v-card-text>
    <v-card-actions>
      <v-btn
        text
        color="teal accent-4"
        v-bind:href=i.url
      >
        Learn More
      </v-btn>
      <v-btn  
      @click = "addfavourites(i.id)"
      raised
        rounded >
      <v-icon v-if="i.favourite.find(id=> id == userdetail.userid)">mdi-bookmark-check</v-icon>
      <v-icon v-else>mdi-bookmark-outline</v-icon>
      
      </v-btn>
    </v-card-actions>
    </v-card>
    <br>

</div>
<div>
 
  <br><br><br><br><br><br>
</div>
<v-footer fixed>
 
    <v-col
      class="text-center"
      cols="13"
      rows="13"
    >
    
        <v-select
          :items="items"
          label="Categories"
          v-model="secat"
    

        ></v-select>
         
    <v-btn :to = "{ name:'home' }" color="primary" rounded elevation="24"><v-icon>mdi-home</v-icon></v-btn>
      <v-btn :to = "{ name:'savednews' }" rounded> <v-icon>mdi-bookmark-multiple</v-icon></v-btn>

    </v-col>
  </v-footer>
</v-app>
</template>

<script>
import { getAPI } from '../api/axios-base'
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
        userdetail:[],
        news:[],
        savenews:[],
        new : {
          url:'',
          content:'',
          newstitle:'',
          source:'',
          category:''
        },
        newsidsave:null,
        userid:'',
        newsid:'',
        alert:true,
        cntsave:'',
        items: [
        'politics' ,'buisness','tech','sports','army'
      ],
        secat:'',
      offset: true,
      }
    },
    computed: {
      filterProductsByCategory: function(){
                
                return this.news.filter(
                  product => !product.category.indexOf(this.secat))
            },
    }, // get APIData from store.state.
    
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
          setTimeout(()=>{
      this.alert=false
    },5000),
          this.getNews()
          this.addfavourites()
    },
    methods:{
      getNews() {
        getAPI.get("/api/news", { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } }).then(response => {
        //console.log(response)
        this.news = response.data
        
      })
      .catch(error => {
        console.log(error)
        this.errored = true
      })
      .finally(() => this.loading = false)
      },

      addfavourites(saveid) {
        this.alert = true
        axiosBase.post('/favourite/', {
         newsid:saveid,
         userid:this.userdetail.userid
        })
          .then(res => {
            console.log(res)
            this.getNews()
          })
      }
      
}

      
      
    
}
</script>