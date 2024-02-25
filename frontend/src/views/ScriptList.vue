<template>
  <div>
    <div v-if="forMobile">
      <center>
        <button type="button" class="btn btn-block bg-gradient-warning mb-3 mt-5" data-bs-toggle="modal" data-bs-target="#modal-notification">Device Error, Click Here.</button>
      </center>
      <!-- Modal -->
      <div class="col-md-4">
        <div class="modal fade" id="modal-notification" tabindex="-1" role="dialog" aria-labelledby="modal-notification" aria-hidden="true">
          <div class="modal-dialog modal-danger modal-dialog-centered modal-" role="document">
            <div class="modal-content">
              <div class="modal-header">
                <h6 class="modal-title" id="modal-title-notification">Your attention is required</h6>
                
              </div>
              <div class="modal-body">
                <div class="py-3 text-center">
                  <i class="ni ni-bell-55 ni-3x"></i>
                  <h4 class="text-gradient text-danger mt-4">Device Error !!!</h4>
                  <p>The features of this platform isn't appropriate for mobile devices, to know the purpose of this site<a
                href="https://www.canva.com/design/DAE7Do2LYAA/QliiS2jwlVsfbWTFvg0K4g/view?utm_content=DAE7Do2LYAA&utm_campaign=designshare&utm_medium=link&utm_source=publishpresent"
                target="_blank"
                > Click Here.</a
              >
              </p>
                </div>
              </div>
              <div class="modal-footer">
                <a
                href="https://www.canva.com/design/DAE7Do2LYAA/QliiS2jwlVsfbWTFvg0K4g/view?utm_content=DAE7Do2LYAA&utm_campaign=designshare&utm_medium=link&utm_source=publishpresent"
                target="_blank"
                >
                  <button type="button" class="btn btn-white">Ok, Got it</button>
                </a>
                <!-- <button type="button" class="btn btn-link text-black ml-auto" data-bs-dismiss="modal">Close</button> -->
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="row removable mb-4" v-else>
      <div class="row removable mb-4">
        <div
          class="input-group col-4 m-auto"
          style="width: 270px; margin-left: 12px"
        >
          <span class="input-group-text text-body"
            ><i class="fas fa-search" aria-hidden="true"></i
          ></span>
          <input
            type="text"
            id="mysearch"
            class="form-control col-4 m-auto"
            :placeholder="
              this.$store.state.isRTL ? 'أكتب هنا...' : 'Type here...'
            "
            v-on:keyup="mySearchFunction"
          />
        </div>

        <div class="col-8 m-auto">
          <p style="display: inline; margin-right: 5px; font-weight: bold">
            Switch to:
          </p>
          <img
            style="margin-left: 16px; cursor: pointer"
            src="../assets/img/icons/windows.png"
            v-if="myos != 'Windows'"
            v-on:click="osWiseScript('Windows')"
            width="35"
          />
          <img
            style="margin-left: 16px; cursor: pointer"
            src="../assets/img/icons/linux.png"
            v-if="myos != 'Linux'"
            v-on:click="osWiseScript('Linux')"
            width="35"
          />
          <img
            style="margin-left: 16px; cursor: pointer"
            src="../assets/img/icons/mac.png"
            v-if="myos != 'Mac'"
            v-on:click="osWiseScript('Mac')"
            width="35"
          />
        </div>
      </div>

      <div class="col-12">
        <div class="mb-4">
          <div class="pb-0 p-0">
            <!-- <h6 class="mb-1">Task Store</h6> -->
            <div class="flex">
              <button
                class="btn btn-sm btn-outline-info mx-3 mt-3"
                v-on:click="getScriptList"
              >
                Explore
              </button>
              <button
                class="btn btn-sm btn-outline-info mx-3 mt-3"
                v-on:click="topTrending"
              >
                Top Trending
              </button>
              <button
                class="btn btn-sm btn-outline-info mx-3 mt-3"
                v-on:click="reverseAllScript"
              >
                New
              </button>
              <button
                class="btn btn-sm btn-outline-info mx-3 mt-3"
                v-on:click="free"
              >
                Free
              </button>
              <button
                class="btn btn-sm btn-outline-info mx-3 mt-3"
                v-on:click="premium"
              >
                Premium
              </button>
              
              <!-- <router-link to="/Paytm">
                <button
                  class="btn btn-sm btn-outline-info mx-3 mt-3"
                >
                  Paytm
                </button>
              </router-link> -->
              
            </div>
          </div>
          <div class="body p-3 pt-1">
            <div class="row">
              <div
                class="col-xl-3 col-md-6 mb-5 mx-4 mycard nameScript"
                v-for="i in this.scriptData"
                :key="i.id"
                style="background-color: white"
                id="scriptSearchId"
              >
                <div class="card card-blog card-plain mycard mt-4">
                  <!-- Start -->
                  <div class="d-flex">
                    <div class="avatar avatar-xl bg-gradient-dark">
                      <img :src="i['scriptIco']" class="avatar avatar-xl" />
                    </div>
                    <div class="ms-3 my-auto">
                      <router-link
                        :to="'/script-details-us?id=' + i.id + '&install=ins'"
                        v-if="i.isInstall == 'NotExist'"
                      >
                        <h6>
                          {{ i.title }}
                        </h6>
                      </router-link>
                      <router-link
                        :to="'/script-details-us?id=' + i.id + '&install=uns'"
                        v-else-if="i.isInstall == 'Exist'"
                      >
                        <h6>
                          {{ i.title }}
                        </h6>
                      </router-link>
                      <router-link
                        :to="'/script-details-us?id=' + i.id + '&install=not'"
                        v-else
                      >
                        <h6>
                          {{ i.title }}
                        </h6>
                      </router-link>
                      <div class="avatar-group">
                        <p class="text-sm d-flex-left" autocomplete="off">
                          {{ i["author"] }}
                        </p>
                      </div>
                    </div>
                    <!-- <div class="ms-auto">
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
                            <router-link class="dropdown-item border-radius-md" :to="'/script-details-us?id=' + i.id">
                              View Details
                            </router-link>
                          </li>
                          <li>
                            <p style="font-size: 15px; padding-left: 15px;"
                              class="text-warning dropdown-item border-radius-md"
                              @click="sendToSetting(i['id'])">
                              Install
                            </p>
                          </li>
                        </ul>
                      </div>
                    </div> -->
                  </div>

                  <hr class="horizontal dark" />
                  <div class="row">
                    <div class="col-5">
                      <p
                        class="
                          text-secondary text-sm
                          font-weight-bold
                          mt-2
                          px-2
                        "
                      >
                        {{ i["installed"] }} Installs
                      </p>
                    </div>
                    <div class="col-7 text-end">
                      <button
                        type="button"
                        class="mb-0 btn btn-outline-light btn-sm py-2"
                        style="color: grey"
                        @click="sendToSetting(i['id'], i['price'])"
                        v-if="i.isInstall == 'NotExist' && ( i['price'] <= 0 || i['price'] == '$0' )"
                      >
                        Install
                      </button>
                      <button
                        type="button"
                        class="mb-0 btn btn-outline-light btn-sm py-2"
                        style="color: grey"
                        @click="sendToSetting(i['id'], i['price'])"
                        v-else-if="i.isInstall == 'NotExist' && (i['price'] > 0 )"
                      >
                        Purchase
                      </button>
                      <button
                        type="button"
                        class="mb-0 btn btn-outline-light btn-sm py-2"
                        style="color: red;"
                        @click="uninstallThisScript(i['id'])"
                        v-else-if="i.isInstall == 'Exist'"
                      >
                        Uninstall
                      </button>
                      <button
                        type="button"
                        class="mb-0 btn btn-outline-light btn-sm py-2 disabled"
                        style="color: grey"
                        v-else
                      >
                        Can't Install
                      </button>
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

import Swal from "sweetalert2";


export default {
  name: "ScriptList",
  beforeMount() {
    // var loggedIn = localStorage.getItem("loggedIn");
    var isMobile = window.orientation > -1;
    // isMobile = true;
    if (isMobile === true) {
      this.forMobile = true;
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

      backupAllScriptList: [],

      myos: "",

      forMobile: false,

      alreadyInstall: false
    };
  },

  methods: {
    paytm() {
      var config = {
        "root": "",
        "flow": "DEFAULT",
        "data": {
        "orderId": "DJDN_DDFJSS", /* update order id */
        "token": "AD_12A", /* update token value */
        "tokenType": "TXN_TOKEN",
        "amount": "20" /* update amount */
        },
        "handler": {
          "notifyMerchant": function(eventName,data){
            console.log("notifyMerchant handler function called");
            console.log("eventName => ",eventName);
            console.log("data => ",data);
          } 
        }
      }

      if(window.Paytm && window.Paytm.CheckoutJS){
          window.Paytm.CheckoutJS.onLoad(function excecuteAfterCompleteLoad() {
              // initialze configuration using init method 
              window.Paytm.CheckoutJS.init(config).then(function onSuccess() {
                  // after successfully updating configuration, invoke JS Checkout
                  window.Paytm.CheckoutJS.invoke();
              }).catch(function onError(error){
                  console.log("error => ",error);
              });
          });
      }
    },

    reverseAllScript() {
      this.scriptData = {};
      var count = 0;
      for (
        let i = Object.keys(this.backupAllScriptList).length - 1;
        i >= 0;
        i--
      ) {
        const element = this.backupAllScriptList[i];
        this.scriptData[count] = {
          id: element["_id"],
          title: element["ScriptName"],
          author: element["AuthorName"],
          scriptIco: String(element["ScriptIcon"]),
          installed: String(element["installed"]),
          isInstall: String(element["exist"]),
        };
        count = count + 1;
      }
    },

    premium() {
      this.scriptData = {};
      var count = 0;
      for (let i = 0; i < Object.keys(this.backupAllScriptList).length; i++) {
        const element = this.backupAllScriptList[i];
        if (String(element["price"]) != "$0") {
          this.scriptData[count] = {
            id: element["_id"],
            title: element["ScriptName"],
            author: element["AuthorName"],
            scriptIco: String(element["ScriptIcon"]),
            installed: String(element["installed"]),
            isInstall: String(element["exist"]),
          };
          count = count + 1;
        }
      }
    },

    free() {
      this.scriptData = {};
      var count = 0;
      for (let i = 0; i < Object.keys(this.backupAllScriptList).length; i++) {
        const element = this.backupAllScriptList[i];
        if (String(element["price"]) == "$0") {
          this.scriptData[count] = {
            id: element["_id"],
            title: element["ScriptName"],
            author: element["AuthorName"],
            scriptIco: String(element["ScriptIcon"]),
            installed: String(element["installed"]),
            isInstall: String(element["exist"]),
          };
          count = count + 1;
        }
      }
    },

    topTrending() {
      this.scriptData = {};
      var count = 0;
      for (let i = 0; i < Object.keys(this.backupAllScriptList).length; i++) {
        const element = this.backupAllScriptList[i];
        if (String(element["installed"]) >= 2) {
          this.scriptData[count] = {
            id: element["_id"],
            title: element["ScriptName"],
            author: element["AuthorName"],
            scriptIco: String(element["ScriptIcon"]),
            installed: String(element["installed"]),
            isInstall: String(element["exist"]),
          };
          count = count + 1;
        }
      }
    },

    async getScriptList() {
      var OSName = "Unknown";
      if (window.navigator.userAgent.indexOf("Windows NT 10.0") != -1)
        OSName = "Windows";
      if (window.navigator.userAgent.indexOf("Windows NT 6.3") != -1)
        OSName = "Windows";
      if (window.navigator.userAgent.indexOf("Windows NT 6.2") != -1)
        OSName = "Windows";
      if (window.navigator.userAgent.indexOf("Windows NT 6.1") != -1)
        OSName = "Windows";
      if (window.navigator.userAgent.indexOf("Windows NT 6.0") != -1)
        OSName = "Windows";
      if (window.navigator.userAgent.indexOf("Windows NT 5.1") != -1)
        OSName = "Windows";
      if (window.navigator.userAgent.indexOf("Windows NT 5.0") != -1)
        OSName = "Windows";
      if (window.navigator.userAgent.indexOf("Mac") != -1) OSName = "Mac";
      if (window.navigator.userAgent.indexOf("X11") != -1) OSName = "UNIX";
      if (window.navigator.userAgent.indexOf("Linux") != -1) OSName = "Linux";

      this.myos = OSName;

      const data = new FormData();
      data.append("os", OSName);
      data.append("uid", localStorage.getItem("uid"));
      await appInstance.axios
        .post(
          "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/scriptListWithAll",
          data,
          { headers: { "Content-Type": "application/json" } }
        )
        // .post("http://127.0.0.1:8000/app/v1/users/scriptListWithAll",data, { headers: { "Content-Type": "application/json" } })
        .then((res) => {
          var allScirptList = res.data["msg"];
          this.backupAllScriptList = allScirptList;
          this.scriptData = {};
          for (let i = 0; i < allScirptList.length; i++) {
            const element = allScirptList[i];
            this.scriptData[i] = {
              id: element["_id"],
              title: element["ScriptName"],
              author: element["AuthorName"],
              price: element["price"],
              scriptIco: String(element["ScriptIcon"]),
              installed: String(element["installed"]),
              isInstall: String(element["exist"]),
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

    async osWiseScript(OSName) {
      const data = new FormData();
      data.append("os", OSName);
      data.append("uid", localStorage.getItem("uid"));
      await appInstance.axios
        // .post(
        //   "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/scriptList",
        //   data,
        //   { headers: { "Content-Type": "application/json" } }
        // )
        .post("http://127.0.0.1:8000/app/v1/users/scriptList",data, { headers: { "Content-Type": "application/json" } })
        .then((res) => {
          var allScirptList = res.data["msg"];
          this.backupAllScriptList = allScirptList;
          this.scriptData = {};
          for (let i = 0; i < allScirptList.length; i++) {
            const element = allScirptList[i];
            // scrID = element["_id"];
            this.scriptData[i] = {
              id: element["_id"],
              title: element["ScriptName"],
              author: element["AuthorName"],
              scriptIco: String(element["ScriptIcon"]),
              installed: String(element["installed"]),
              isInstall: "Can't Install",
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
    },

    sendToSetting2(scrptId) {
      var loggedIn = localStorage.getItem("loggedIn");
      if (loggedIn != "true") {
        this.$router.push("/sign-in");
      } else {
        var url =
          "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/sendToSetting";
        // var url="http://127.0.0.1:8000/app/v1/users/sendToSetting";
        const data = new FormData();
        data.append("sId", scrptId);
        data.append("uid", localStorage.getItem("uid"));
        appInstance.axios
          .post(url, data, { headers: { "Content-Type": "application/json" } })
          .then((res) => {
            if (res.data["msg"] === "done") {
              // Swall Added Msg
              // Swal.fire(
              //   "Script Added !!!",
              //   "A new script succesfully added...",
              //   "success"
              // );
              this.getScriptList();
              // this.getScriptList();  // If required we can put it later, basically update the installation number in real time
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
      }
    }, // End of sendToSetting()

    async makePayment(scrptId, price, number) {
      var url =
          "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/makePayment";
        // var url="http://127.0.0.1:8000/app/v1/users/makePayment";
        const data = new FormData();
        data.append("sId", scrptId);
        data.append("price", price);
        data.append("number", number);
        data.append("uid", localStorage.getItem("uid"));
        appInstance.axios
          .post(url, data, { headers: { "Content-Type": "application/json" } })
          .then((res) => {
            if (res.data["msg"] === "done") {
              var link = res.data['link'];
              localStorage.removeItem("pSid");
              localStorage.setItem("pSid", scrptId);
              window.open(link, '_blank');
            }else{
              Swal.fire({
                icon: "error",
                title: "Oops...",
                text: "Can't generate the payment link at this moment, try later...",
              });
            }
          });
    },

    sendToSetting(scrptId, price) {
      
      var loggedIn = localStorage.getItem("loggedIn");
      if (loggedIn != "true") {
        this.$router.push("/sign-in");
      } else {
        if(price == "$0" || price == "₹0" || price.toLowerCase() == "free" || price == "0"){
          this.sendToSetting2(scrptId);
        }else{
          let number = prompt("Please enter your phone number", "9132000000");
          if (number != null) {
            if(number === "9132000000"){
              alert("Invalid number...")
            }else{
              this.makePayment(scrptId, price, number);
            }
          }else{
            alert("Invalid input...")
          }
        }
      }
    }, // End of sendToSetting() For payment gateway checking

    mySearchFunction() {
      var input, filter, li, a, i, txtValue;
      input = document.getElementById("mysearch");
      filter = input.value.toUpperCase();
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

    uninstallThisScript(scrId){
      event.preventDefault();
      var uid = localStorage.getItem("uid");
      const formData = new FormData();
      formData.append("sId", scrId);
      formData.append("uid", uid);

      appInstance.axios
        .post("https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/delScript", formData, {
        // .post("http://127.0.0.1:8000/app/v1/users/delScript", formData, {
          headers: { "Content-Type": "application/json" },
        })
        .then((res) => {
          if (res.data["msg"] === "done") {
            // Swal
            // Swal.fire('Script Uninstall Successfully !!!');
            this.getScriptList();
          } else {
            Swal.fire({
                icon: "error",
                title: "Oops...",
                text: "You don't have any script...",
            });
          }
        });
    }
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
