<template>
<div>
  <nav class="navbar navbar-expand-lg bg-body-tertiary bg-dark">
    <div>
      <router-link class="navbar-brand" to="/home">DashBoard</router-link>
      <router-link class="navbar-brand" to="/about">About</router-link>
       
    </div>
   
  </nav>
    
<router-view />
</div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #e9eef4;
}

nav a.router-link-exact-active {
  color: #42b983;
}
.card2
{
  background-color:rgb(92, 220, 115);
  color: white;
  border-radius: 20px;
}
.b2
{
  background-color: rgb(25, 56, 28);
  color: rgb(255, 255, 255);
  
  
}
.card1
{
  background-color:rgb(173, 102, 170);
  color: white;
  border-radius: 20px;
}
.b1
{
  background-color: rgb(57, 21, 51);
  color: rgb(255, 255, 255);
  
  
}
</style>
