<template>
  <div class="row removable mb-4">
    <div class="col-12">
      <div class="mb-4">
        <div class="pb-0 p-3">
          <div class="input-group" style="width: 270px; margin-left: 12px;">
            <span class="input-group-text text-body"
              ><i class="fas fa-search" aria-hidden="true"></i
            ></span>
            <input
              type="text"
              id="mysearch"
              class="form-control"
              :placeholder="
                this.$store.state.isRTL ? 'أكتب هنا...' : 'Type here...'
              "
              v-on:keyup="mySearchFunction"
            />
          </div>
        </div>
        <div class="body pt-4">
          <div class="row">
            <div
              class="col-xl-3 col-md-6 mb-5 mx-4 mycard nameScript"
              v-for="i in this.scriptData"
              :key="i.id"
              style="background-color: white;"
            >
              <div class="card card-blog card-plain mycard  mt-4">
                <!-- Menu Start -->
                <div class="d-flex">
                  <div class="avatar avatar-xl bg-gradient-dark">
                    <img :src="i['scriptIco']" class="avatar avatar-xl"/>
                  </div>
                  <div class="ms-3 my-auto">
                    <router-link :to="'/script-details?id=' + i.id">
                    <h6>
                      {{ i.title }}
                    </h6>
                    </router-link>
                    <div class="avatar-group">
                      <p class="text-sm d-flex-left" autocomplete="off">
                        Author: {{ i["author"] }}
                      </p>
                    </div>
                  </div>
                  <div class="ms-auto">
                    <div class="dropdown">
                      <a
                        class="cursor-pointer"
                        id="dropdownTable"
                        data-bs-toggle="dropdown"
                        aria-expanded="false"
                        style="margin-left: -15px;"
                      >
                        <i
                          class="fa fa-ellipsis-v text-secondary"
                          aria-hidden="true"
                        ></i>
                      </a>
                      <ul
                        class="dropdown-menu px-2 py-3 ms-sm-n4 ms-n5"
                        aria-labelledby="dropdownTable"
                      >
                        <li>
                          <router-link class="dropdown-item border-radius-md" :to="'/script-details?id=' + i.id">
                              View Details
                          </router-link>
                        </li>
                        <li>
                          <router-link class="dropdown-item border-radius-md" :to="'/script-edit?id=' + i.id">
                              Edit
                          </router-link>
                        </li>
                        <li>
                          <p
                            style="font-size: 15px; padding-left: 15px;"
                            class="text-warning dropdown-item border-radius-md"
                            @click="changeStatus(i['id'])"
                            v-if="i.status == 'Activate'">
                            {{ i.status }}
                          </p>
                          <p
                            style="font-size: 15px; padding-left: 15px;"
                            class="text-danger dropdown-item border-radius-md"
                            @click="changeStatus(i['id'])"
                            v-if="i.status == 'Deactivate'">
                            {{ i.status }}
                          </p>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
                <hr class="horizontal dark" />
                <div class="row">
                  <div class="col-5">
                    <p
                      class="text-secondary text-sm font-weight-bold mt-2 px-2"
                    >
                      {{i['installed']}} Installs
                    </p>
                  </div>
                  <div class="col-7 text-end">
                    <button
                      type="button"
                      class="mb-0 btn btn-outline-light font-weight-bold btn-sm text-warning"
                      @click="changeStatus(i['id'])"
                      v-if="i.status == 'Activate'"
                    >
                      {{ i.status }}
                    </button>
                    <button
                      type="button"
                      class="mb-0 btn btn-outline-light font-weight-bold btn-sm text-danger"
                      @click="changeStatus(i['id'])"
                      v-if="i.status == 'Deactivate'"
                    >
                      {{ i.status }}
                    </button>
                  </div>
                </div>
                <!-- Menu End -->
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
  name: "ReqScript",
  components: {
    // ProjectsCard,
  },

  beforeMount() {
    var loggedIn = localStorage.getItem("loggedIn");
    if (loggedIn != "true") {
      this.$router.push("/");
    } else {
      this.getScriptList();
    }
  },
  data() {
    return {
      // For Script Rating Purpose
      starRate: [1, 2, 3, 4],

      // Script Lists
      scriptData: {},
      scriptListDataCheck: false,
      scriptLen: 0,
      categories: ["Automation", "Hacking"],
      // End Script List
    };
  },

  methods: {
    mySearchFunction() {
      var input, filter, li, a, i, txtValue;
      input = document.getElementById("mysearch");
      filter = input.value.toUpperCase();
      // ul = document.getElementById("scriptSearchId");
      li = document.getElementsByClassName("nameScript");
      for (i = 0; i < li.length; i++) {
          a = li[i].getElementsByTagName("h6")[0];
          txtValue = a.textContent || a.innerText;
          if (txtValue.toUpperCase().indexOf(filter) > -1) {
              li[i].style.display = "";
          } else {
              li[i].style.display = "none";
          }
      }
    },

    async getScriptList() {
      await appInstance.axios
        .get(
          "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/reqScript"
        )
        // .get("http://127.0.0.1:8000/app/v1/users/reqScript")
        .then((res) => {
          var allScirptList = res.data["msg"];
          console.log(allScirptList);
          for (let i = 0; i < allScirptList.length; i++) {
            const element = allScirptList[i];
            // scrID = element["_id"];
            this.scriptData[i] = {
              id: element["_id"],
              title: element["ScriptName"],
              author: element["AuthorName"],
              status: element["status"],
              scriptIco: String(element["ScriptIcon"]),
              installed: String(element["installed"]),
            };
          }
          this.scriptLen = allScirptList.length;
        });
      // Update The Text
      if (this.scriptLen > 0) {
        this.scriptListDataCheck = true;
      } else {
        this.scriptListDataCheck = false;
      }
    }, // End Of Function

    changeStatus(scrptId) {
      var url =
        "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/changeStatus";
      // var url="http://127.0.0.1:8000/app/v1/users/changeStatus";
      const data = new FormData();
      data.append("sId", scrptId);
      appInstance.axios
        .post(url, data, { headers: { "Content-Type": "application/json" } })
        .then((res) => {
          if (res.data["msg"] === "done") {
            // Swall Added Msg
            Swal.fire(
              "Done !!!",
              "Current status successfully changed...",
              "success"
            );
            this.getScriptList();
          } else if (res.data["msg"] === "error") {
            Swal.fire({
              icon: "error",
              title: "Oops...",
              text: "Something went wrong, try again!!!",
            });
          } else {
            Swal.fire({
              icon: "error",
              title: "Already Exist...",
              text: "This script is already exist.",
            });
          }
        });
    }, // End of sendToSetting()
  },
};
</script>

<style scoped>
.mycard {
  padding-bottom: 5px;
  box-shadow: 3px 3px 3px 3px rgba(235, 233, 233, 0.2);
  transition: 0.3s;
  border-radius: 20px;
}
.author {
  color: grey;
  margin-top: -14px;
  font-size: 14px;
  margin-bottom: 5px;
}
.scrIc {
  height: 150px;
  width: 100%;
}
</style>

