<template>
  <div>
    <div class="row removable mb-4">
      <!-- MODAL START FROM HERE -->
      <div class="col-md-4">
        <!-- <button type="button" class="btn btn-block bg-gradient-dark mb-3" data-bs-toggle="modal" data-bs-target="#modal-default">X</button> -->
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
                  Script Details
                </h6>
                <button
                  type="button"
                  class="btn-close mb-3"
                  data-bs-dismiss="modal"
                  aria-label="Close"
                >
                  <span style="color: black" class="font-weight-bold">X</span>
                </button>
              </div>
              <div class="modal-body">
                <!-- Editing Form -->
                <form @submit="makeAScriptReq">
                  <!-- <div class="row">
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
                </div> -->
                  <div class="row">
                    <div class="form-group">
                      <label for="scTit">Script Title</label>
                      <input
                        id="scTit"
                        type="text"
                        class="form-control"
                        placeholder="Type a appropriate title"
                        required
                      />
                    </div>
                  </div>
                  <div class="row">
                    <div class="form-group">
                      <label for="scDesc">Description</label>
                      <textarea
                        class="form-control"
                        required
                        id="scDesc"
                      ></textarea>
                    </div>
                  </div>
                  <button type="submit" class="btn bg-gradient-warning btn-lg">
                    Submit
                  </button>
                </form>
                <!-- End Editing Forms -->
              </div>
              <div class="modal-footer">
                <!-- <button type="button" class="btn bg-gradient-primary">Save changes</button> -->
                <!-- <button type="button" class="btn bg-gradient-warning" data-bs-dismiss="modal">Close</button> -->
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- <div class="row removable mb-4">
        <h1>SAYED IS HERE</h1>
      </div> -->

      <div class="col-12">
        <div class="container-fluid pt-3">
          <div class="row removable">
            <div class="col-lg-4">
              <button
                class="btn mb-4 bg-gradient-warning"
                data-bs-toggle="modal"
                data-bs-target="#modal-default"
              >
                Make a post
              </button>
            </div>
            <div class="col-lg-8">
              <!-- <input class="form-control mb-4" placeholder="Type your requirements..." /> -->
            </div>
          </div>
          <div class="row mt-4 removable">
            <div class="col-lg-8 col-md-6">
              <div class="card mb-4">
                <div class="card-header pb-0">
                  <div class="row">
                    <div class="col-lg-6 col-7">
                      <h6>Previous posts</h6>
                      <p class="text-sm mb-0">
                        <i
                          class="fa fa-hashtag text-info"
                          aria-hidden="true"
                        ></i>
                        <span class="font-weight-bold ms-1"
                          >Total Post: {{ dbData.length }}</span
                        >
                      </p>
                    </div>
                    <!-- <div class="col-lg-6 col-5 my-auto text-end">
                      <div class="dropdown float-lg-end pe-4">
                        <a
                          class="cursor-pointer"
                          id="dropdownTable"
                          data-bs-toggle="dropdown"
                          aria-expanded="false"
                        >
                          <i
                            class="fa fa-ellipsis-v text-secondary"
                            aria-hidden="true"
                          ></i>
                        </a>
                        <ul
                          class="dropdown-menu px-2 py-3 ms-sm-n4 ms-n5"
                          aria-labelledby="dropdownTable"
                          style="
                            position: absolute;
                            inset: 0px auto auto 0px;
                            margin: 0px;
                            transform: translate3d(0px, 25.5px, 0px);
                          "
                          data-popper-placement="bottom-start"
                        >
                          <li>
                            <a
                              class="dropdown-item border-radius-md"
                              href="javascript:;"
                              >Action</a
                            >
                          </li>
                          <li>
                            <a
                              class="dropdown-item border-radius-md"
                              href="javascript:;"
                              >Another action</a
                            >
                          </li>
                          <li>
                            <a
                              class="dropdown-item border-radius-md"
                              href="javascript:;"
                              >Something else here</a
                            >
                          </li>
                        </ul>
                      </div>
                    </div> -->
                  </div>
                </div>
                <div class="card-body px-0 pb-2">
                  <div class="table-responsive">
                    <table class="table align-items-center mb-0">
                      <thead>
                        <tr>
                          <th
                            class="
                              text-uppercase text-secondary text-xxs
                              font-weight-bolder
                              opacity-7
                            "
                            autocomplete="off"
                            spellcheck="false"
                          >
                            Requested Script
                          </th>
                          <th
                            class="
                              text-uppercase text-secondary text-xxs
                              font-weight-bolder
                              opacity-7
                              ps-2
                            "
                          >
                            Upvote
                          </th>
                          <th
                            v-if="myRole == 'admin'"
                            class="
                              text-center text-uppercase text-secondary text-xxs
                              font-weight-bolder
                              opacity-7
                            "
                          >
                            Action
                          </th>
                          <th
                            class="
                              text-center text-uppercase text-secondary text-xxs
                              font-weight-bolder
                              opacity-7
                            "
                          >
                            Completion
                          </th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="singleData in dbData" :key="singleData.id">
                          <td spellcheck="false">
                            <div class="d-flex px-2 py-1">
                              <div
                                class="
                                  d-flex
                                  flex-column
                                  justify-content-centers
                                "
                              >
                                <h6 class="mb-0 text-sm">
                                  {{ singleData["title"] }}
                                </h6>
                              </div>
                            </div>
                          </td>
                          <td>
                            <span class="text-xs font-weight-bold">
                              <p
                                class="text-sm mb-0"
                                @click="
                                  updateUpvote(
                                    singleData['upvote'],
                                    singleData['_id']
                                  )
                                "
                              >
                                {{ singleData["upvote"] }}+ &nbsp;&nbsp;
                                <i
                                  class="fa fa-chevron-up"
                                  aria-hidden="true"
                                  style="cursor: pointer; color: orange"
                                ></i>
                              </p>
                            </span>
                          </td>
                          <td
                            v-if="myRole == 'admin'"
                            class="align-middle text-center text-sm"
                          >
                            <span
                              v-if="myRole == 'admin'"
                              class="text-xs font-weight-bold"
                            >
                              <select
                                v-model="selectedVal"
                                @change="updateScriptStatus(singleData['_id'])"
                                class="form-control form-control-sm"
                              >
                                <option value="err_ss">-- Select --</option>
                                <option value="10">10%</option>
                                <!-- Initiated -->
                                <option value="25">25%</option>
                                <!-- Checked -->
                                <option value="50">50%</option>
                                <!-- Working -->
                                <option value="70">70%</option>
                                <!-- On hold -->
                                <option value="100">100%</option>
                                <!-- Finished -->
                              </select>
                            </span>
                          </td>
                          <td class="align-middle">
                            <!-- For 10% -->
                            <div
                              v-if="singleData['workingStatus'] == 10"
                              class="progress-wrapper w-75 mx-auto"
                            >
                              <div class="progress-secondary">
                                <div class="progress-percentage">
                                  <span class="text-xs font-weight-bold"
                                    >10%</span
                                  >
                                </div>
                              </div>
                              <div class="progress">
                                <div
                                  class="
                                    progress-bar
                                    bg-gradient-secondary
                                    w-10
                                  "
                                  role="progressbar"
                                  aria-valuenow="10"
                                  aria-valuemin="0"
                                  aria-valuemax="100"
                                ></div>
                              </div>
                            </div>
                            <!-- For 25% -->
                            <div
                              v-if="singleData['workingStatus'] == 25"
                              class="progress-wrapper w-75 mx-auto"
                            >
                              <div class="progress-primary">
                                <div class="progress-percentage">
                                  <span class="text-xs font-weight-bold"
                                    >25%</span
                                  >
                                </div>
                              </div>
                              <div class="progress">
                                <div
                                  class="progress-bar bg-gradient-primary w-25"
                                  role="progressbar"
                                  aria-valuenow="25"
                                  aria-valuemin="0"
                                  aria-valuemax="100"
                                ></div>
                              </div>
                            </div>
                            <!-- For 50% -->
                            <div
                              v-if="singleData['workingStatus'] == 50"
                              class="progress-wrapper w-75 mx-auto"
                            >
                              <div class="progress-info">
                                <div class="progress-percentage">
                                  <span class="text-xs font-weight-bold"
                                    >50%</span
                                  >
                                </div>
                              </div>
                              <div class="progress">
                                <div
                                  class="progress-bar bg-gradient-info w-50"
                                  role="progressbar"
                                  aria-valuenow="50"
                                  aria-valuemin="0"
                                  aria-valuemax="100"
                                ></div>
                              </div>
                            </div>
                            <!-- For 70% -->
                            <div
                              v-if="singleData['workingStatus'] == 70"
                              class="progress-wrapper w-75 mx-auto"
                            >
                              <div class="progress-warning">
                                <div class="progress-percentage">
                                  <span class="text-xs font-weight-bold"
                                    >70%</span
                                  >
                                </div>
                              </div>
                              <div class="progress">
                                <div
                                  class="progress-bar bg-gradient-warning w-70"
                                  role="progressbar"
                                  aria-valuenow="70"
                                  aria-valuemin="0"
                                  aria-valuemax="100"
                                ></div>
                              </div>
                            </div>
                            <!-- For 100% -->
                            <div
                              v-if="singleData['workingStatus'] == 100"
                              class="progress-wrapper w-75 mx-auto"
                            >
                              <div class="progress-success">
                                <div class="progress-percentage">
                                  <span class="text-xs font-weight-bold"
                                    >100%</span
                                  >
                                </div>
                              </div>
                              <div class="progress">
                                <div
                                  class="progress-bar bg-gradient-success w-100"
                                  role="progressbar"
                                  aria-valuenow="100"
                                  aria-valuemin="0"
                                  aria-valuemax="100"
                                ></div>
                              </div>
                            </div>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-lg-4 col-md-6">
              <div class="card mb-4 h-100">
                <div class="card-header pb-0">
                  <h6>Post Milestone Overview</h6>
                  <!-- <p class="text-sm">
                    <i
                      class="fa fa-arrow-up text-success"
                      aria-hidden="true"
                    ></i>
                    <span class="font-weight-bold">24%</span> this month
                  </p> -->
                </div>
                <div class="card-body p-3">
                  <div class="timeline timeline-one-side">
                    <div class="timeline-block mb-3">
                      <span class="timeline-step">
                        <i class="fa fa-arrow-up text-dark text-gradient"></i>
                      </span>
                      <div class="timeline-content">
                        <p class="text-sm">
                          <!-- <i
                            class="fa fa-arrow-up text-success"
                            aria-hidden="true"
                          ></i> -->
                          <span class="font-weight-bold">10%</span> Initiated
                        </p>
                      </div>
                    </div>
                    <div class="timeline-block mb-3">
                      <span class="timeline-step">
                        <i class="fa fa-arrow-up text-primary text-gradient"></i>
                      </span>
                      <div class="timeline-content">
                        <p class="text-sm">
                          <!-- <i
                            class="fa fa-arrow-up text-success"
                            aria-hidden="true"
                          ></i> -->
                          <span class="font-weight-bold">25%</span> We checked
                        </p>
                      </div>
                    </div>
                    <div class="timeline-block mb-3">
                      <span class="timeline-step">
                        <i class="fa fa-arrow-up text-info text-gradient"></i>
                      </span>
                      <div class="timeline-content">
                        <p class="text-sm">
                          <!-- <i
                            class="fa fa-arrow-up text-success"
                            aria-hidden="true"
                          ></i> -->
                          <span class="font-weight-bold">50%</span> Working in progress
                        </p>
                      </div>
                    </div>
                    <div class="timeline-block mb-3">
                      <span class="timeline-step">
                        <i class="fa fa-arrow-up text-warning text-gradient"></i>
                      </span>
                      <div class="timeline-content">
                        <p class="text-sm">
                          <!-- <i
                            class="fa fa-arrow-up text-success"
                            aria-hidden="true"
                          ></i> -->
                          <span class="font-weight-bold">70%</span> Facing Issues
                        </p>
                      </div>
                    </div>
                    <div class="timeline-block mb-3">
                      <span class="timeline-step">
                        <i class="fa fa-arrow-up text-success text-gradient"></i>
                      </span>
                      <div class="timeline-content">
                        <p class="text-sm">
                          <!-- <i
                            class="fa fa-arrow-up text-success"
                            aria-hidden="true"
                          ></i> -->
                          <span class="font-weight-bold">100%</span> Finished
                        </p>
                      </div>
                    </div>
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
import App from "../../App.vue";
const appInstance = createApp(App);
import VueAxios from "vue-axios";
import axios from "axios";
appInstance.use(VueAxios, axios);
import Swal from "sweetalert2";

export default {
  name: "PostComments",
  beforeMount() {
    var loggedIn = localStorage.getItem("loggedIn");
    if (loggedIn != "true") {
      this.$router.push("/");
    }
  },

  data() {
    return {
      dbData: [],
      myRole: "user",
      selectedVal: "-- Select --",
    };
  },

  mounted() {
    this.myRole = localStorage.getItem("role");
    appInstance.axios
      .get(
        "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/fetchCommentScriptReq",
        // "http://127.0.0.1:8000/app/v1/users/fetchCommentScriptReq",
        {
          headers: { "Content-Type": "application/json" },
        }
      )
      .then((res) => {
        if (res.data["msg"] === true) {
          this.dbData = res.data["data"];
        } else {
          console.log("In the else block....");
        }
      });
  },

  methods: {
    mountedAlter() {
      this.myRole = localStorage.getItem("role");
      appInstance.axios
        .get(
          "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/fetchCommentScriptReq",
          // "http://127.0.0.1:8000/app/v1/users/fetchCommentScriptReq",
          {
            headers: { "Content-Type": "application/json" },
          }
        )
        .then((res) => {
          if (res.data["msg"] === true) {
            this.dbData = res.data["data"];
          } else {
            console.log("In the else block....");
          }
        });
    },

    updateScriptStatus(scId) {
      var formData = new FormData();
      formData.append("scId", scId);
      formData.append("value", this.selectedVal);

      appInstance.axios
        .post(
          "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/updateCommentReqSt",
          // "http://127.0.0.1:8000/app/v1/users/updateCommentReqSt",
          formData,
          {
            headers: { "Content-Type": "application/json" },
          }
        )
        .then((res) => {
          if (res.data["msg"] === true) {
            this.dbData = res.data["data"];
            // this.mountedAlter();
          } else {
            Swal.fire({
              icon: "error",
              title: "Oops...",
              text: "Something went wrong!!!",
            });
          }
        });

      this.selectedVal = "-- Select --";
    },

    updateUpvote(upvt, scId) {
      var formData = new FormData();
      formData.append("scId", scId);
      formData.append("value", upvt);
      formData.append("uid", localStorage.getItem("uid"));

      appInstance.axios
        .post(
          "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/updateUpvote",
          // "http://127.0.0.1:8000/app/v1/users/updateUpvote",
          formData,
          {
            headers: { "Content-Type": "application/json" },
          }
        )
        .then((res) => {
          if (res.data["msg"] === true) {
            if (res.data["data"] == "exist") {
              Swal.fire({
                icon: "error",
                title: "Oops...",
                text: "Already voted on this....",
              });
            } else {
              this.dbData = res.data["data"];
            }
          } else {
            Swal.fire({
              icon: "error",
              title: "Oops...",
              text: "Something went wrong!!!",
            });
          }
        });
    },

    makeAScriptReq(event) {
      event.preventDefault();
      var scTit = document.getElementById("scTit").value;
      var scDesc = document.getElementById("scDesc").value;

      var role = localStorage.getItem("role");
      var uid = localStorage.getItem("uid");

      var formData = new FormData();
      formData.append("scTit", scTit);
      formData.append("scDesc", scDesc);
      formData.append("role", role);
      formData.append("uid", uid);

      if (scTit.trim() != "" && scDesc.trim() != "") {
        appInstance.axios
          .post(
            "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/commentScriptReq",
            // "http://127.0.0.1:8000/app/v1/users/commentScriptReq",
            formData,
            {
              headers: { "Content-Type": "application/json" },
            }
          )
          .then((res) => {
            if (res.data["msg"] === true) {
              Swal.fire(
                "Successfully added !!!",
                "A new script category successfully added...",
                "success"
              );
              // this.mountedAlter();
            } else {
              Swal.fire({
                icon: "error",
                title: "Oops...",
                text: "Something went wrong!!!",
              });
            }
          });
      } else {
        Swal.fire({
          icon: "error",
          title: "Oops...",
          text: "Empty field not allowed...",
        });
      }
    },
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
