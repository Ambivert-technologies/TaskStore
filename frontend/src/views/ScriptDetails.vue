<template>
  <div class="container-fluid pt-3">
    <div class="row removable" v-for="i in this.scriptData" :key="i.id">
      <div class="col-lg-8">
        <div class="row removable">
          <div class="col-xl-7"></div>

          <div class="col-xl-5"></div>
        </div>
        <div class="card mb-4">
          <div class="card-body p-3">
            <div class="row">
              <div class="col-lg-6">
                <div class="bg-gradient-primary border-radius-lg h-100">
                  <img
                    src="https://demos.creative-tim.com/soft-ui-dashboard/assets/img/shapes/waves-white.svg"
                    class="position-absolute h-100 w-50 top-0 d-lg-block d-none"
                    alt="waves"
                  />
                  <div
                    class="
                      position-relative
                      d-flex
                      align-items-center
                      justify-content-center
                      h-100
                    "
                  >
                    <img
                      class="
                        w-100
                        h-100
                        position-relative
                        z-index-2
                        border-radius-lg
                      "
                      :src="i.scriptIco"
                    />
                  </div>
                </div>
              </div>
              <div class="col-lg-5 ms-auto mt-5 mt-lg-0">
                <div class="d-flex flex-column h-100">
                  <h5 class="font-weight-bolder">{{ i.title }}</h5>
                  <p class="mb-5">
                    {{ i.Description }}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="row removable mb-4">
          <div class="col-12">
            <div class="card mb-4">
              <center>
                <div style="width: 553px; height: 350px; text-align: center">
                  <iframe class="w-100 h-100 position-relative py-4"
                    :src="i.video"
                    >
                  </iframe> 
                </div>
              </center>
              <div class="card-header pb-0 p-3">
                <h6 class="mb-1">Screenshots</h6>
              </div>
              <div class="card-body p-3">
                <div class="row">
                  <div class="col-xl-9 col-md-6 mb-4">
                    <ScreenShot/>
                  </div>
                  <div class="col-xl-3 col-md-6 mb-4">
                    <div class="card h-100 card-plain border">
                      <div
                        class="
                          card-body
                          d-flex
                          flex-column
                          justify-content-center
                          text-center
                        "
                      >
                        <a href="javascript:;">
                          <i
                            class="fa fa-plus text-secondary mb-3"
                            aria-hidden="true"
                          ></i>
                          <h5 class="text-secondary">New project</h5>
                        </a>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-lg-4">
        <div class="card mb-5 pb-4">
          <div class="card-header p-3 pb-0">
            <div class="row">
              <div class="col-8 d-flex">
                <div>
                  <img
                    src="https://www.w3schools.com/w3css/img_avatar3.png"
                    class="avatar avatar-sm me-2"
                    alt="avatar image"
                  />
                </div>
                <div class="d-flex flex-column justify-content-center">
                  <h6 class="mb-0 text-sm">{{ i.author }}</h6>
                  <p class="text-xs">
                    <b>{{ i.dev_email }}</b
                    >&nbsp;
                  </p>
                  <!-- <div>Posted 2h ago</div> -->
                  <p></p>
                </div>
              </div>
              <div class="col-4">
                <span id="htblast" class="heart bg-gradient-info ms-auto float-end" v-on:click="blast"></span>
              </div>
            </div>
          </div>
          <div class="card-body p-3 pt-1">
            <!-- <p class="text-sm">
              {{i.Description}}
            </p> -->
            <div class="d-flex bg-gray-100 border-radius-lg p-3">
              <h4 class="my-auto">
                {{ i.price }}
              </h4>
              <a href="javascript:;" class="btn btn-outline-dark mb-0 ms-auto"
                >Install</a
              >
            </div>
          </div>
        </div>
        <div class="card mb-4">
          <div class="card-header pb-0 p-3">
            <div class="d-flex align-items-center">
              <h6 class="mb-0">More Details</h6>
            </div>
          </div>
          <div class="card-body p-3">
            <div class="d-flex align-items-center mt-0">
              <i class="fa fa-tags" aria-hidden="true"></i>
              <div class="ms-3">
                <h6 class="mb-0">Category</h6>
                <span class="text-xs mb-0 text-primary">{{ i.cat }}</span>
              </div>
            </div>

            <div class="d-flex align-items-center mt-4">
              <i class="fa fa-code" aria-hidden="true"></i>
              <div class="ms-3">
                <h6 class="mb-0">Language</h6>
                <span class="text-xs mb-0 text-primary">{{ i.lang }}</span>
              </div>
            </div>

            <div class="d-flex align-items-center mt-4">
              <i class="fa fa-calendar" aria-hidden="true"></i>
              <div class="ms-3">
                <h6 class="mb-0">Date</h6>
                <span class="text-xs mb-0 text-primary">{{ i.date }} </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ScreenShot from "./ScreenShot.vue"

// FOR AXIOS API
import { createApp } from "vue";
import App from "../App.vue";
const appInstance = createApp(App);
import VueAxios from "vue-axios";
import axios from "axios";
appInstance.use(VueAxios, axios);

// import Swal from "sweetalert2";

export default {
  name: "ScriptDetails",
  components: {
    ScreenShot
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
      // Script Lists
      scriptData: {},
      scriptListDataCheck: false,
      scriptLen: 0,
      // End Script List

      imageArray: [
        "https://cdn.pixabay.com/photo/2015/12/12/15/24/amsterdam-1089646_1280.jpg",
        "https://cdn.pixabay.com/photo/2016/02/17/23/03/usa-1206240_1280.jpg",
        "https://cdn.pixabay.com/photo/2015/05/15/14/27/eiffel-tower-768501_1280.jpg",
        "https://cdn.pixabay.com/photo/2016/12/04/19/30/berlin-cathedral-1882397_1280.jpg",
      ],
    };
  },

  methods: {
    blast(){
      var result = document.getElementById("htblast").classList.toggle("heart-blast");
      var url = "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/fav_script";
      // var url="http://127.0.0.1:8000/app/v1/users/fav_script";
      const data = new FormData();
      data.append("sId", this.$route.query.id);
      data.append("like", result);
      appInstance.axios
      .post(url, data, { headers: { "Content-Type": "application/json" } })
      .then((res) => {
        if (res.data["msg"] === "done") {
          console.log("Done Fav");
        }  
      });
    },
    async getScriptList() {
      await appInstance.axios
        .get(
          "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/reqScriptDetail/" +
            this.$route.query.id
        )
        // .get("http://127.0.0.1:8000/app/v1/users/reqScriptDetail/"+this.$route.query.id)
        .then((res) => {
          var allScirptList = res.data["msg"];
          for (let i = 0; i < allScirptList.length; i++) {
            const element = allScirptList[i];
            this.scriptData[i] = {
              id: element["_id"],
              title: element["ScriptName"],
              author: element["AuthorName"],
              status: element["status"],
              scriptIco: String(element["ScriptIcon"]),
              price: String(element["price"]),

              ScriptFileName: String(element["ScriptFileName"]),
              Description: String(element["Description"]),
              Dependency: String(element["Dependency"]),
              cat: String(element["cat"]),
              lang: String(element["lang"]),
              date: String(element["date"]),
              video: String(element["video"]),

              dev_email: String(element["dev_email"]),
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
  },
};
</script>

<style scoped>
.mycard {
  padding-bottom: 5px;
  border: 1px solid rgb(197, 195, 195);
}
.author {
  color: rgb(228, 228, 228);
  margin-top: -14px;
  font-size: 14px;
  margin-bottom: 5px;
}
.scrIc {
  height: 150px;
  width: 100%;
}

.heart {
  width: 70px;
  height: 70px;
  transform: translate(-50%, -50%);
  background: url(http://imagizer.imageshack.com/img923/4545/XdJDuY.png) no-repeat;  
  cursor: pointer;
  
}
.heart-blast {
  background-position: -2800px 0;
  transition: background 1s steps(28);
}
</style>
