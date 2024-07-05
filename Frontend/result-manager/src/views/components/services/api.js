import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000/res_man/v1',
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  },
});

export default {
  getItems() {
    return apiClient.get('/students/');
  },
  getItem(id) {
    return apiClient.get('/students/' + id);
  },
  createItem(data) {
    return apiClient.post('/students/', data);
  },
  updateItem(id, data) {
    return apiClient.put('/students/' + id + '/', data);
  },
  deleteItem(id) {
    return apiClient.delete('/students/' + id);
  },
  getCourse() {
    return apiClient.get('/courses/');
  },
  getCourse(id) {
    return apiClient.get('/courses/' + id);
  },
  createCourse(data) {
    return apiClient.post('/courses/', data);
  },
  updateCourse(id, data) {
    return apiClient.put('/courses/' + id + '/', data);
  },
  deleteCourse(id) {
    return apiClient.delete('/courses/' + id);
  },
  getEnrollment()
  {
    return apiClient.get('/enrollments/');
  },
  /*updateEnrollment(id,data)
  {
    return apiClient.put('/enrollments/' + id + '/',data);
  }*/
  async updateEnrollment(enrollmentId, studentId, courseId, marks) 
  {
    try {
        const response = await apiClient.put(`/enrollments/${enrollmentId}/`, {
            student: studentId,
            course: courseId,
            marks: marks
        }, {
            headers: {
                'Content-Type': 'application/json'
            }
        });
        
        console.log('Enrollment updated successfully:', response.data);
    } catch (error) {
        console.error('Error updating enrollment:', error.response ? error.response.data : error.message);
    }
}
};