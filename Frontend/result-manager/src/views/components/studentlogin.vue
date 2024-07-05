<template>
    <div class="container">
      <form class="form1" @submit.prevent="test">
        <label ><b>Student Login</b></label>
        <label>Roll:</label><input type="text" v-model="id"> <label>Password</label
        ><input type="password" v-model="entpassword"/>
        <button class="b3" type="submit">Login</button>
        
       
      </form>
    </div>
    
</template>
<script>
import api from './services/api.js';
export default{
  data(){
    return{
      id:'',
      name:'',
      password:'.',
      entpassword:'',
      student:[]
    }
  },
  methods:{
    test()
    {
      api.getItem(this.id).then(response=>{this.password=response.data.password
      if(this.password==this.entpassword)
      {
        this.$router.push(`/stlogin/${this.id}`)
      }
      else
      {
        alert("Invalid Password")
      }}).catch(error=>{alert("Something went wrong")})
    }

  }
}
</script>

<style scoped>

.form1 {
  width: 40%;
  height: 35%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: antiquewhite;
  border-radius: 15px;
}
.container {
    top:0px;
    left:0px;
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;

}
.b3
{
    margin: 15px;
    background-color: rgb(62, 62, 153);
    color:aliceblue;
}
</style>