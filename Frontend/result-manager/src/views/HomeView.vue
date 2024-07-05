<template>
  <div class="home">
    <div class="card w-50 m-5 card1">
      <div class="card-body">
        <h5 class="card-title">Teacher</h5>
        <p class="card-text">Login as Course Teacher</p>
        <router-link class="btn btn-primary b1" @click="togglemod2" to="/tlogin"
          >Login</router-link
        >
      </div>
    </div>
    <div class="card w-50 m-5 card2">
      <div class="card-body">
        <h5 class="card-title">Student</h5>
        <p class="card-text">Login as Student</p>

        <router-link
          class="btn btn-primary b2"
          @click="togglemod2"
          to="/stlogin"
          >Login</router-link
        >
      </div>
    </div>
  </div>
</template>

<script>
import studentlogin from "./components/studentlogin.vue";
import teacherlogin from "./components/teacherlogin.vue";
// @ is an alias to /src

export default {
  name: "home",
  components: { studentlogin, teacherlogin },
  data() {
    return {
      showmodal1: false,
      showmodal2: false,
    };
  },
  methods: {
    togglemod1() {
      this.showmodal1 = !this.showmodal1;
    },
    togglemod2() {
      this.showmodal2 = !this.showmodal2;
    },
  },
};
</script>
<style>
.home
{
  display:flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>



