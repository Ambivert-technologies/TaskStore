<template>
  <div class="card mb-4">
    <div class="card-header pb-0">
      <h6>Local Scripts</h6>
    </div>
    <div class="card-body px-0 pt-0 pb-2">
      <div class="table-responsive p-0">
        <table class="table align-items-center mb-0">
          <thead>
            <tr>
              <th
                class="text-uppercase text-secondary text-xs font-weight-bolder"
              >
                Sl. No.
              </th>
              <th
                class="text-uppercase text-secondary text-xs font-weight-bolder"
              >
                Script Name
              </th>
              <th
                class="text-uppercase text-secondary text-xs font-weight-bolder"
              >
                Author Name
              </th>
              <th
                class="
                  text-center text-uppercase text-secondary text-xs
                  font-weight-bolder
                "
                colspan="2"
              >
                Action
              </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in items" :key="item.id">
              <td
                class="text-uppercase text-secondary text-xs font-weight-bolder"
              >
                <p class="text-xs font-weight-bold mb-0 slNo">
                  {{ item + 1 }}.
                </p>
              </td>
              <td class="align-middle">
                <p class="text-xs font-weight-bold mb-0 slNo">
                  {{ scriptNameAndAuthor["scriptName"][item] }}
                </p>
              </td>
              <td class="align-middle">
                <p class="text-xs font-weight-bold mb-0 slNo">
                  {{ scriptNameAndAuthor["authorName"][item] }}
                </p>
              </td>
              <td
                class="align-middle text-center cursor-pointer"
                @click="viewDetails(scriptNameAndAuthor['scriptId'][item])"
              >
                <p class="font-weight-bold mb-0 slNo" data-bs-toggle="modal" data-bs-target="#modal-default">👁️</p>
              </td>
              <td
                class="align-middle text-center cursor-pointer"
                @click="delScript(scriptNameAndAuthor['scriptId'][item])"
              >
                <p class="font-weight-bold mb-0 slNo">🗑️</p>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>


    <!-- Dialog For Script Details -->
    <div class="col-md-4">
      <!-- <button type="button" class="btn btn-block bg-gradient-primary mb-3" data-bs-toggle="modal" data-bs-target="#modal-default">Default</button> -->
      <div class="modal fade" id="modal-default" tabindex="-1" role="dialog" aria-labelledby="modal-default" aria-hidden="true">
        <div class="modal-dialog modal- modal-dialog-centered modal-" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h6 class="modal-title" id="modal-title-default">Script Details</h6>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">×</span>
              </button>
            </div>
            <div class="modal-body">
              <table class="table align-items-center mb-0">
                    <img :src=scriptIcon alt="..." width="90" height="80"/>
                    <tbody>
                      
                      <tr>
                        <td>Script ID:</td>
                        <td>{{scriptId}}</td>
                      </tr>
                      <tr>
                        <td>Script Name:</td>
                        <td class="wrapcon">{{scriptName}}</td>
                      </tr>
                      <tr>
                        <td>Description:</td>
                        <td class="wrapcon">{{scriptDesc}}</td>
                      </tr>
                      <tr>
                        <td>Author Name:</td>
                        <td class="wrapcon">{{scriptAuthor}}</td>
                      </tr>
                    </tbody>
                </table>
            </div>
            <div class="modal-footer">
              <!-- <button type="button" class="btn bg-gradient-primary">Save changes</button> -->
              <button type="button" class="btn bg-gradient-warning" data-bs-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- End Dialog -->
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

import Swal from 'sweetalert2';

export default {
  name: "SavedScripts",
  data() {
    return {
      items: [],
      scriptNameAndAuthor: [],

      // Script Details
      scriptId: "",
      scriptName: "",
      scriptDesc: "",
      scriptIcorn: "",
      scriptAuthor: "",
      // End Script Details

      // For Dialog
      dialog: false,
      // End Of Dialog
    };
  },
  mounted() {
    var loggedIn = localStorage.getItem("loggedIn");
    if (loggedIn != "true") {
      this.$router.push("/");
    } else {
      var uid = localStorage.getItem("uid");
      const data = new FormData();
      data.append("uid", uid);

      appInstance.axios
        .post("https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/getScirptForSetting", data, {
        // .post("http://127.0.0.1:8000/app/v1/users/getScirptForSetting", data, {
          headers: { "Content-Type": "application/json" },
        })
        .then((res) => {
          if (res.data["msg"] === "empty") {
            alert("You don't have any script, please add something.");
          } else {
            if (res.data["msg"] === true) {
              var resp_data = res.data["data"];
              this.scriptNameAndAuthor = resp_data;
              for (let i = 0; i < resp_data["authorName"].length; i++) {
                this.items.push(i);
              }
            }
          }
        });
    }
  },
  methods: {
    mountedAlter() {
      var loggedIn = localStorage.getItem("loggedIn");
      if (loggedIn != "true") {
        this.$router.push("/login");
      } else {
        var uid = localStorage.getItem("uid");
        const data = new FormData();
        data.append("uid", uid);

        appInstance.axios
          .post("https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/getScirptForSetting", data, {
          // .post("http://127.0.0.1:8000/app/v1/users/getScirptForSetting", data, {
            headers: { "Content-Type": "application/json" },
          })
          .then((res) => {
            this.scriptNameAndAuthor = [];
            this.items = [];
            if (res.data["msg"] === "empty") {
              alert("You don't have any script, please add something.");
            } else {
              if (res.data["msg"] === true) {
                var resp_data = res.data["data"];
                this.scriptNameAndAuthor = resp_data;
                for (let i = 0; i < resp_data["authorName"].length; i++) {
                  this.items.push(i);
                }
              }
            }
          });
      }
    },
    viewDetails(sId) {
      this.dialog = true;
      const formData = new FormData();
      formData.append("sId", sId);

      appInstance.axios
        .post("https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/getScriptDetails", formData, {
        // .post("http://127.0.0.1:8000/app/v1/users/getScriptDetails", formData, {
          headers: { "Content-Type": "application/json" },
        })
        .then((res) => {
          if (res.data["msg"] === true) {
            var respData = res.data["data"];
            this.scriptId = respData["id"];
            this.scriptName = respData["ScriptName"];
            this.scriptDesc = respData["Description"];
            this.scriptIcon = respData["ScriptIcon"];
            this.scriptAuthor = respData["AuthorName"];
          } else {
            alert("Something went wrong !");
          }
        });
    },

    delScript(sId) {
      event.preventDefault();
      var uid = localStorage.getItem("uid");
      const formData = new FormData();
      formData.append("sId", sId);
      formData.append("uid", uid);

      appInstance.axios
        .post("https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/delScript", formData, {
        // .post("http://127.0.0.1:8000/app/v1/users/delScript", formData, {
          headers: { "Content-Type": "application/json" },
        })
        .then((res) => {
          if (res.data["msg"] === "done") {
            // Swal
            // Swal.fire('Deleted Successfully!')
            this.mountedAlter();
          } else {
            Swal.fire({
                icon: "error",
                title: "Oops...",
                text: "You don't have any script...",
            });
          }
        });
    },
  },
};
</script>


<style scoped>
.slNo {
  margin-left: 16px;
}
.wrapcon{
  word-wrap: break-word;   
  white-space: normal;
}
</style>