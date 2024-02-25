<template>
  <div class="row removable mb-4">
    <div class="col-12">
      <div class="card mb-4">
        <div class="card-header pb-0">
          <h6 class="mb-1">TaskStore User List</h6>
          <p class="text-sm">Total User: {{ totalUser }}</p>
        </div>

        <div class="row removable mb-4 mt-2">
          <div class="input-group col-4 m-auto" style="width: 270px; margin-left: 12px;">
            <span class="input-group-text text-body"
              ><i class="fas fa-search" aria-hidden="true"></i
            ></span>
            <input
              type="text"
              id="mysearch"
              class="form-control col-4 m-auto"
              :placeholder="
                this.$store.state.isRTL ? 'أكتب هنا...' : 'Search by name...'
              "
              v-on:keyup="mySearchFunction"
            />
          </div>
          <div class="flex col-8 m-auto">
              <button class="btn btn-sm btn-outline-info mx-3 mt-3" v-on:click="activeUser">Active User</button>
              <button class="btn btn-sm btn-outline-info mx-3 mt-3" v-on:click="deactiveUser">Deactive User</button>
              <button class="btn btn-sm btn-outline-info mx-3 mt-3" v-on:click="users">Users</button>
              <button class="btn btn-sm btn-outline-info mx-3 mt-3" v-on:click="developers">Developers</button>
          </div>
        </div>
        <div class="card-body py-0">
          <div class="row">
            <!-- Dialog Box -->
            <div class="col-md-4">
              <div
                class="modal fade"
                id="modal-default"
                tabindex="-1"
                role="dialog"
                aria-labelledby="modal-default"
                aria-hidden="true"
              >
                <div
                  class="modal-dialog modal- modal-dialog-centered modal-"
                  role="document"
                >
                  <div class="modal-content">
                    <div class="modal-header">
                      <h6 class="modal-title" id="modal-title-default">
                        Edit User Role
                      </h6>
                      <button
                        type="button"
                        class="btn-close"
                        data-bs-dismiss="modal"
                        aria-label="Close"
                      >
                        <span aria-hidden="true">×</span>
                      </button>
                    </div>
                    <div class="modal-body">
                      <!-- Editing Form -->
                      <form @submit="editRoleFormSubmit">
                        <div class="row">
                          <div class="col-md-6">
                            <div class="form-group">
                              <label for="role">Role</label>
                              <select class="form-control form-control-lg" id="role">
                                <option value="">-- Select --</option>
                                <option value="user">User</option>
                                <option value="dev">Developer</option>
                                <option value="admin">Admin</option>
                                <option value="tu">Test User</option>
                              </select>
                            </div>
                          </div>
                        </div>
                        <button
                          type="submit"
                          class="btn bg-gradient-warning btn-lg"
                        >
                          Save Changes
                        </button>
                      </form>
                      <!-- End Editing Forms -->
                    </div>
                    <div class="modal-footer">
                      <button
                        type="button"
                        class="btn btn-outline-warning"
                        data-bs-dismiss="modal"
                      >
                        Close
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!-- End Dialog -->

            <div class="col-xl-12 col-md-12 mb-4">
              <div class="card col-md-12 card-blog card-plain mycard">
                <div class="px-1 pb-0 card-body">
                  <div class="table-responsive p-0">
                    <table class="table mb-0">
                      <thead>
                        <tr>
                          <th
                            class="
                              text-uppercase text-secondary text-xs
                              font-weight-bolder
                              heading
                            "
                          >
                            Name
                          </th>
                          <th
                            class="
                              text-uppercase text-secondary text-xs
                              font-weight-bolder
                              heading
                            "
                          >
                            Email
                          </th>
                          <th
                            class="
                              text-uppercase text-secondary text-xs
                              font-weight-bolder
                              heading
                            "
                          >
                            Role
                          </th>
                          <th
                            class="
                              text-uppercase text-secondary text-xs
                              font-weight-bolder
                              heading
                            "
                          >
                            Status
                          </th>
                          <th
                            class="
                              text-center text-uppercase text-secondary text-xs
                              font-weight-bolder
                              heading
                            "
                            colspan="2"
                          >
                            Action
                          </th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr class="userList" v-for="item in userItem" :key="item.id">
                          <td class="align-middle">
                            <p class="text-xs font-weight-bold mb-0 slNo">
                              {{ item["name"] }}
                            </p>
                          </td>
                          <td class="align-middle">
                            <p class="text-xs font-weight-bold mb-0 slNo">
                              {{ item["email"] }}
                            </p>
                          </td>
                          <td class="align-middle">
                            <p class="text-xs font-weight-bold mb-0 slNo"
                              data-bs-toggle="modal"
                              data-bs-target="#modal-default"
                            >
                              <a href="javascript:;" @click="saveUserId(item['_id'])">{{ item["role"] }}</a>
                            </p>
                          </td>
                          <td class="align-middle">
                            <p
                              class="text-xs font-weight-bold mb-0 slNo"
                              style="color: green"
                              v-if="item['status'] == 'Activate'"
                            >
                              {{ item["status"] }} ✅
                            </p>
                            <p
                              class="text-xs font-weight-bold mb-0 slNo"
                              style="color: red"
                              v-else
                            >
                              {{ item["status"] }} ❌
                            </p>
                          </td>
                          <td class="align-middle text-center cursor-pointer">
                            <button
                              type="button"
                              class="btn btn-outline-success"
                              data-bs-dismiss="modal"
                              v-if="item['status'] != 'Activate'"
                              @click="userStatusChange(item['_id'], 'Activate')"
                            >
                              Activate
                            </button>
                            <button
                              type="button"
                              class="btn btn-outline-danger"
                              data-bs-dismiss="modal"
                              v-else
                              @click="
                                userStatusChange(item['_id'], 'Deactivate')
                              "
                            >
                              Deactivate
                            </button>
                          </td>
                          <td class="align-middle text-center cursor-pointer">
                            <button
                              type="button"
                              class="btn btn-danger"
                              data-bs-dismiss="modal"
                              @click="userDelete(item['_id'])"
                            >
                              Delete
                            </button>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// FOR AXIOS API
import { createApp } from "vue";
import App from "../App.vue";
const appInstance = createApp(App);
import VueAxios from "vue-axios";
import axios from "axios";
appInstance.use(VueAxios, axios);
import Swal from "sweetalert2";

export default {
  name: "All_users",
  data() {
    return {
      totalUser: 0,
      userItem: [],
      editUserid: 0,
      elang: "",
      elangId: "",
    };
  },
  mounted() {
    var loggedIn = localStorage.getItem("loggedIn");
    var role = localStorage.getItem("role");
    if (loggedIn != "true") {
      this.$router.push("/");
    } else {
      if (role != "admin") {
        this.$router.push("/");
      } else {
        appInstance.axios
          .get(
            "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/getUser",
            // "http://127.0.0.1:8000/app/v1/users/getUser",
            {
              headers: { "Content-Type": "application/json" },
            }
          )
          .then((res) => {
            if (res.data["msg"] === true) {
              this.userItem = res.data["data"];
              this.totalUser = res.data["totalUser"];
            } else {
              Swal.fire({
                icon: "error",
                title: "Oops...",
                text: "Won't be able to fetch existing category!!!",
              });
            }
          });
      }
    }
  },

  methods: {
    userStatusChange(uid, status_to) {
      var formData = new FormData();
      formData.append("uid", uid);
      formData.append("status_to", status_to);
      appInstance.axios
        .post(
          "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/userStatusChange",
          // "http://127.0.0.1:8000/app/v1/users/userStatusChange",
          formData,
          {
            headers: { "Content-Type": "application/json" },
          }
        )
        .then((res) => {
          if (res.data["msg"] === true) {
            Swal.fire(
              "Successfully Updated !!!",
              "User status changed successfully...",
              "success"
            );
            this.mountedAlter();
          } else {
            Swal.fire({
              icon: "error",
              title: "Oops...",
              text: "Something went wrong!!!",
            });
          }
        });
    },

    userDelete(uid) {
      var del_conf = confirm("Are you sure ?");
      if(del_conf === true){
        var formData = new FormData();
        formData.append("uid", uid);
        appInstance.axios
          .post(
            "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/userDelete",
            // "http://127.0.0.1:8000/app/v1/users/userDelete",
            formData,
            {
              headers: { "Content-Type": "application/json" },
            }
          )
          .then((res) => {
            if (res.data["msg"] === true) {
              Swal.fire(
                "Successfully Deleted !!!",
                "User deleted successfully...",
                "success"
              );
              this.mountedAlter();
            } else {
              Swal.fire({
                icon: "error",
                title: "Oops...",
                text: "Something went wrong!!!",
              });
            }
          });
      }
    },


    saveUserId(val){
      this.editUserid = val;
    },

    editRoleFormSubmit(event) {
      event.preventDefault();
      var formData = new FormData();
      formData.append("role", document.getElementById('role').value);
      formData.append("userId", this.editUserid);
      appInstance.axios
        .post(
          "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/editUserRole",
          // "http://127.0.0.1:8000/app/v1/users/editUserRole",
          formData,
          {
            headers: { "Content-Type": "application/json" },
          }
        )
        .then((res) => {
          if (res.data["msg"] === true) {
            // Swal
            Swal.fire(
              "Successfully Updated !!!",
              "Changes are saved...",
              "success"
            );
            this.mountedAlter();
          } else {
            Swal.fire({
              icon: "error",
              title: "Oops...",
              text: "Can't perform at this moment, try later...",
            });
          }
        });
    },

    mountedAlter() {
      var loggedIn = localStorage.getItem("loggedIn");
      var role = localStorage.getItem("role");
      if (loggedIn != "true") {
        this.$router.push("/");
      } else {
        if (role != "admin") {
          this.$router.push("/");
        } else {
          appInstance.axios
            .get(
              "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/getUser",
              // "http://127.0.0.1:8000/app/v1/users/getUser",
              {
                headers: { "Content-Type": "application/json" },
              }
            )
            .then((res) => {
              if (res.data["msg"] === true) {
                this.userItem = res.data["data"];
                this.totalUser = res.data["totalUser"];
              } else {
                Swal.fire({
                  icon: "error",
                  title: "Oops...",
                  text: "Won't be able to fetch existing category!!!",
                });
              }
            });
        }
      }
    },

    activeUser() {
      var formData = new FormData();
      formData.append("col", "status");
      formData.append("desired", "Activate");
      appInstance.axios
        .post(
          "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/filterUser",
          // "http://127.0.0.1:8000/app/v1/users/filterUser",
          formData,
          {
            headers: { "Content-Type": "application/json" },
          }
        )
        .then((res) => {
          if (res.data["msg"] === true) {
            this.userItem = res.data["data"];
            this.totalUser = res.data["totalUser"];
          } else {
            Swal.fire({
              icon: "error",
              title: "Oops...",
              text: "Can't perform at this moment, try later...",
            });
          }
        });
    },

    deactiveUser(){
      var formData = new FormData();
      formData.append("col", "status");
      formData.append("desired", "Deactivate");
      appInstance.axios
        .post(
          "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/filterUser",
          // "http://127.0.0.1:8000/app/v1/users/filterUser",
          formData,
          {
            headers: { "Content-Type": "application/json" },
          }
        )
        .then((res) => {
          if (res.data["msg"] === true) {
            this.userItem = res.data["data"];
            this.totalUser = res.data["totalUser"];
          } else {
            Swal.fire({
              icon: "error",
              title: "Oops...",
              text: "Can't perform at this moment, try later...",
            });
          }
      });
    },


    users(){
      var formData = new FormData();
      formData.append("col", "role");
      formData.append("desired", "user");
      appInstance.axios
        .post(
          "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/filterUser",
          // "http://127.0.0.1:8000/app/v1/users/filterUser",
          formData,
          {
            headers: { "Content-Type": "application/json" },
          }
        )
        .then((res) => {
          if (res.data["msg"] === true) {
            this.userItem = res.data["data"];
            this.totalUser = res.data["totalUser"];
          } else {
            Swal.fire({
              icon: "error",
              title: "Oops...",
              text: "Can't perform at this moment, try later...",
            });
          }
      });
    },

    developers(){
      var formData = new FormData();
      formData.append("col", "role");
      formData.append("desired", "dev");
      appInstance.axios
        .post(
          "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/filterUser",
          // "http://127.0.0.1:8000/app/v1/users/filterUser",
          formData,
          {
            headers: { "Content-Type": "application/json" },
          }
        )
        .then((res) => {
          if (res.data["msg"] === true) {
            this.userItem = res.data["data"];
            this.totalUser = res.data["totalUser"];
          } else {
            Swal.fire({
              icon: "error",
              title: "Oops...",
              text: "Can't perform at this moment, try later...",
            });
          }
      });
    },

    mySearchFunction() {
      var input, filter, li, a, i, txtValue;
      input = document.getElementById("mysearch");
      filter = input.value.toUpperCase();
      li = document.getElementsByClassName("userList");
      for (i = 0; i < li.length; i++) {
          a = li[i].getElementsByTagName("td")[0];
          txtValue = a.textContent || a.innerText;
          if (txtValue.toUpperCase().indexOf(filter) > -1) {
              li[i].style.display = "";
          } else {
              li[i].style.display = "none";
          }
      }
    }
  },
};
</script>

<style scoped>
.mycard {
  display: inline-flex;
}
.slNo {
  margin-left: 16px;
}
</style>
