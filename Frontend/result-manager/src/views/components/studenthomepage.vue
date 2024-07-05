<template>
  <div>
    <div class="container">
      <div class="card w-75 mb-3 c1">
        <div class="card-body">
          <h5 class="card-title">{{ getname }}</h5>
          <p class="card-text">
            Jadavpur University, Department of Computer Science and Engineering
          </p>
          <a href="#" class="btn btn-primary" @click="toggleshow"
            >Show Courses</a
          >
          <div v-if="show">
            <p class="p1">
              *MARKS THAT HAVEN'T BEEN UPDATED YET ARE DEPICTED IN NEGATIVE
            </p>
            <table class="table table-striped">
              <tbody>
                <tr v-for="enrollment in st_enrollments"
              :key="enrollment.couse">
                  <td><p class="card-text" v-if="courses[enrollment.course]">
                  {{ courses[enrollment.course].name }}:
                </p>
                <p class="card-text" v-else>Student data loading...</p></td>
                  <td>{{ enrollment.marks }}</td>

                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      <div><img src="./unnamed.jpg" alt="" class="img1" /></div>
    </div>
  </div>
</template>

<script>
import api from "./services/api.js";
export default {
  data() {
    return {
      id: this.$route.params.id,
      name: " ",
      name2: "",
      show: false,
      enrollments: [],
      courses: {},
      st_enrollments: [],
    };
  },
  methods: {
    toggleshow() {
      this.show = !this.show;
      this.getEnrollments();
    },
    getEnrollments() {
      //this.showStudent=!this.showStudent;
      api.getEnrollment().then((response) => {
        this.enrollments = response.data;
        // console.log(this.enrollments);

        this.filterstudents2();
        this.fetchStudentDetails();
        //console.log(this.students);
      });
    },
    filterstudents2() {
      this.st_enrollments = this.enrollments.filter(
        (enrollment) => enrollment.student === this.id
      );
    },
    fetchStudentDetails() {
      const studentPromises = this.st_enrollments.map((enrollment) => {
        return api.getCourse(enrollment.course).then((response) => {
          this.courses[enrollment.course] = response.data;
        });
      });
      console.log(this.courses);
      return Promise.all(studentPromises);
    },
  },
  computed: {
    getname() {
      api.getItem(this.id).then((response) => {
        this.name = response.data.name;
      });
      return this.name;
    },
  },
};
</script>

<style scoped>
.c1 {
  margin: 20px;
}
.container {
  display: flex;
  flex-direction: row;
}
.img1 {
  margin: 20px;
}
.c2 {
  display: flex;
  flex-direction: row;
  justify-content: center;
}
.c3 {
  margin: 5%;
}
.p1 {
  color: red;
  margin: 7px;
}
</style>