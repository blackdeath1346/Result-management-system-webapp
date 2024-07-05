<template>
  <div>
    <div class="container">
      <div class="card w-100 mb-3 c1">
        <div class="card-body">
            <h4>Course:</h4>
          <h5 class="card-title">{{ getname }}</h5>
          <p class="card-text">
            Bachelor of Computer Science and Engineering, Jadavpur University
          </p>
          <button @click="getEnrollments" class="btn btn-primary">
            Toggle Show Students
          </button>

          <ul v-if="showStudent">
            <li v-for="enrollment in st_enrollments" :key="enrollment.student" class="c2">
              <div class="c3">
                <p class="card-text" v-if="students[enrollment.student]">{{ students[enrollment.student].roll_no }}</p>
                <p class="card-text" v-else>Student data loading...</p>
              </div>
              <div class="c3">
                <p class="card-text" v-if="students[enrollment.student]">{{ students[enrollment.student].name }}</p>
                <p class="card-text" v-else>Student data loading...</p>
              </div>
              <div class="c3">
                <label class="card-text" >marks:</label>
                <input type="number" v-model="enrollment.marks"/>
              </div>
              <div class="c3">
                    <button class="btn btn-primary" @click="updateMarks(enrollment)">Update</button>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import api from "./services/api.js";
import Vue from 'vue';
export default {
  data() {
    return {
      id: this.$route.params.id,
      name: " ",
      enrollments: [],
      students: {},
      st_enrollments:[],
      marks: -1,
      showStudent:false
    };
  },
  methods: {
    getEnrollments() {
        this.showStudent=!this.showStudent;
      api.getEnrollment().then((response) => {
        this.enrollments = response.data;
       // console.log(this.enrollments);
        
        this.filterstudents2();
        this.fetchStudentDetails();
      });
    },
    filterstudents2()
    {
        this.st_enrollments = this.enrollments
        .filter((enrollment) => enrollment.course=== this.id)
       
    },
    fetchStudentDetails() {
      const studentPromises = this.st_enrollments.map((enrollment) => {
        return api.getItem(enrollment.student).then((response) => {
          this.students[enrollment.student] = response.data;
        });
      });
      console.log(this.students);
      return Promise.all(studentPromises);
    },
    updateMarks(enrollment)
    {
        console.log("updateMarks called")
        const enrollmentId = enrollment.url.split('/').slice(-2, -1)[0]; // Extract id from URL
        console.log(enrollment);
        console.log(enrollmentId);
        //console.log(enrollment.id);
        api.updateEnrollment(enrollmentId,enrollment.student,enrollment.course,enrollment.marks)
        .catch(error => {
          console.error("Error updating marks: ", error);
        });
        
    }

  },
  computed: {
    getname() {
      api.getCourse(this.id).then((response) => {
        this.name = response.data.name;
      });
      return this.name;
    },
  },
  created() {
    this.getEnrollments();
    //this.getname();
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
  justify-content: center;
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
</style>