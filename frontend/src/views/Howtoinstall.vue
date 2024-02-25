<template>
  <div class="card">
    <div class="card-body">
      <div class="container-fluid pt-3">
        <div class="row removable">
          <div class="col-12 mb-4">
            <h2
              class="display-5 text-center font-weight-bold"
              spellcheck="false"
            ></h2>
            <p class="text-center"></p>
            <div class="card mb-4">
              <div class="card-body p-3">
                <div class="row">
                  <div class="col-lg-6">
                    <div class="d-flex flex-column h-100">
                      <p class="mb-1 pt-2 text-bold">How does it work ?</p>
                      <h5 class="font-weight-bolder">Getting Started</h5>
                      <p class="mb-5" spellcheck="false" autocomplete="off">
                        Download the panel according to your OS and
                        install it to get started...
                      </p>
                      <div class="row">
                      <div class="col-lg-4 text-center d-flex flex-column">
                        <div class="card mb-4">
                          <a href="https://gitlab.com/tasks29/taskstore/-/raw/main/TaskStore.exe?inline=false">
                            <div class="card-body">
                              <img
                                src="../assets/img/icons/windows.png"
                                height="48"
                              />
                              <p class="mb-0 text-sm">Windows</p>
                            </div>
                          </a>
                        </div>
                      </div>
                      <div class="col-lg-4 text-center d-flex flex-column">
                        <div class="card mb-4">
                          <a href="#">
                            <div class="card-body">
                              <img src="../assets/img/icons/mac.png" />
                              <p class="mb-0 text-sm">Coming Soon</p>
                            </div>
                          </a>
                        </div>
                      </div>
                      <div class="col-lg-4 text-center d-flex flex-column">
                        <div class="card mb-4">
                          <a href="javascript:;">
                            <div class="card-body">
                              <img src="../assets/img/icons/linux.png" />
                              <p class="mb-0 text-sm">Coming Soon</p>
                            </div>
                          </a>
                        </div>
                        </div>
                      </div>
                      <a
                        class="
                          text-body text-sm
                          font-weight-bold
                          mb-0
                          icon-move-right
                          mt-auto
                        "
                        href="https://www.youtube.com/watch?v=vjZCUrC_tfU"
                        target="_blank"
                        >Watch&nbsp;<i
                          class="fas fa-arrow-right text-sm ms-1"
                          aria-hidden="true"
                        ></i>
                      </a>
                    </div>
                  </div>
                  <div class="col-lg-5 ms-auto text-center mt-5 mt-lg-0">
                    <div class="bg-gradient-warning border-radius-lg h-100">
                      <div
                        class="
                          position-relative
                          d-flex
                          align-items-center
                          justify-content-center
                          h-100
                        "
                      >
                        <iframe class="w-100 h-100 position-relative border-radius-lg"
                          src="https://www.youtube.com/embed/vjZCUrC_tfU?autoplay=1&mute=1">
                        </iframe>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-12"></div>
        </div>
        <div class="row removable">
          <div class="col-xl-3 col-sm-6">
            <div class="card mb-4">
              <div class="card-body p-3">
                <div class="row">
                  <div class="col-8">
                    <div class="numbers">
                      <p class="text-sm mb-0 text-capitalize font-weight-bold">
                        Tasks
                      </p>
                      <h5 class="font-weight-bolder mb-0">{{task}}</h5>
                    </div>
                  </div>
                  <div class="col-4 text-end">
                    <div
                      class="
                        icon icon-shape
                        shadow
                        text-center
                        border-radius-md
                        bg-gradient-warning
                      "
                    >
                      <i
                        class="
                          ni ni-money-coins
                          text-lg
                          opacity-10
                          text-default
                        "
                        aria-hidden="true"
                      ></i>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-xl-3 col-sm-6">
            <div class="card mb-4">
              <div class="card-body p-3">
                <div class="row">
                  <div class="col-8">
                    <div class="numbers">
                      <p class="text-sm mb-0 text-capitalize font-weight-bold">
                        Time Saved
                      </p>
                      <h5 class="font-weight-bolder mb-0">∞</h5>
                    </div>
                  </div>
                  <div class="col-4 text-end">
                    <div
                      class="
                        icon icon-shape
                        shadow
                        text-center
                        border-radius-md
                        bg-gradient-warning
                      "
                    >
                      <i
                        class="ni ni-world text-lg opacity-10"
                        aria-hidden="true"
                      ></i>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-xl-3 col-sm-6">
            <div class="card mb-4">
              <div class="card-body p-3">
                <div class="row">
                  <div class="col-8">
                    <div class="numbers">
                      <p class="text-sm mb-0 text-capitalize font-weight-bold">
                        Users
                      </p>
                      <h5 class="font-weight-bolder mb-0">{{user}}</h5>
                    </div>
                  </div>
                  <div class="col-4 text-end">
                    <div
                      class="
                        icon icon-shape
                        shadow
                        text-center
                        border-radius-md
                        bg-gradient-warning
                      "
                    >
                      <i
                        class="ni ni-paper-diploma text-lg opacity-10"
                        aria-hidden="true"
                      ></i>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-xl-3 col-sm-6">
            <div class="card mb-4">
              <div class="card-body p-3">
                <div class="row">
                  <div class="col-8">
                    <div class="numbers">
                      <p class="text-sm mb-0 text-capitalize font-weight-bold">
                        Installed
                      </p>
                      <h5 class="font-weight-bolder mb-0">{{installed}}</h5>
                    </div>
                  </div>
                  <div class="col-4 text-end">
                    <div
                      class="
                        icon icon-shape
                        shadow
                        text-center
                        border-radius-md
                        bg-gradient-warning
                      "
                    >
                      <i
                        class="ni ni-cart text-lg opacity-10"
                        aria-hidden="true"
                      ></i>
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
import App from "../App.vue";
const appInstance = createApp(App);
import VueAxios from "vue-axios";
import axios from "axios";
appInstance.use(VueAxios, axios);


export default {
  name: "Howtoinstall",

  data() {
    return{
      task: "",
      user: "",
      installed: ""
    }
  },

  mounted() {
      appInstance.axios
      .get("https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/howtoinstall", {
      // .get("http://127.0.0.1:8000/app/v1/users/howtoinstall", {
        headers: { "Content-Type": "application/json" },
      })
      .then((res) => {
        if (res.data["msg"] === true) {
          this.user = res.data['data']['users']
          this.task = res.data['data']['script']
          this.installed = res.data['data']['installed_script']
        }
      });
  }
};
</script>