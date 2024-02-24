<template>
  <div
    class="w-auto h-auto collapse navbar-collapse max-height-vh-100 h-100"
    id="sidenav-collapse-main"
  >
    <ul class="navbar-nav">
      <li class="mt-0 nav-item">
        <!-- <router-link :to="{ name: 'Profile' }"> -->
        <div class="d-flex align-items-center justify-content-cente ms-4 ps-2">
          <img
            src="https://www.w3schools.com/w3css/img_avatar3.png"
            class="avatar avatar-sm"
          />
          <div class="ms-2">
            <h6 class="text-sm mb-0">{{ username }}</h6>
            <p class="text-xs font-weight-bold mb-0" v-if="admin">Admin</p>
            <p class="text-xs font-weight-bold mb-0" v-if="dev">Developer</p>
            <p class="text-xs font-weight-bold mb-0" v-if="user">User</p>
            <p class="text-xs font-weight-bold mb-0" v-if="emp">Employee</p>
            <p class="text-xs font-weight-bold mb-0" v-if="org">Organization</p>
          </div>
        </div>
        <!-- </router-link> -->
      </li>

      <hr class="horizontal dark mt-3" />

      <li class="mt-3 nav-item">
        <h6
          class="text-xs ps-4 text-uppercase font-weight-bolder opacity-6"
          :class="this.$store.state.isRTL ? 'me-4' : 'ms-2'"
          v-if="tu"
        >
          Refresh Me
        </h6>
      </li>
      <li class="nav-item" v-if="tu" @click="refreshTestUser">
        <sidenav-collapse navText="Refresh" :to="{ name: '/' }">
          <template v-slot:icon> ⟳ </template>
        </sidenav-collapse>
      </li>

      <li class="mt-3 nav-item">
        <h6
          class="text-xs ps-4 text-uppercase font-weight-bolder opacity-6"
          :class="this.$store.state.isRTL ? 'me-4' : 'ms-2'"
          v-if="admin"
        >
          TaskStore Users
        </h6>
      </li>
      <li class="nav-item" v-if="admin">
        <sidenav-collapse navText="All Users" :to="{ name: 'All Users' }">
          <template v-slot:icon> 👥 </template>
        </sidenav-collapse>
      </li>

      <li class="mt-3 nav-item">
        <h6
          class="text-xs ps-4 text-uppercase font-weight-bolder opacity-6"
          :class="this.$store.state.isRTL ? 'me-4' : 'ms-2'"
        >
          How to use?
        </h6>
      </li>
      <li class="nav-item mb-2">
        <sidenav-collapse
          navText="Get Started"
          :to="{ name: 'how-to-install' }"
        >
          <template v-slot:icon>
            <icon name="virtual-reality" />
          </template>
        </sidenav-collapse>
      </li>

      <li class="mt-1 nav-item">
        <h6
          class="text-xs ps-4 text-uppercase font-weight-bolder opacity-6"
          :class="this.$store.state.isRTL ? 'me-4' : 'ms-2'"
        >
          Dashboard Option
        </h6>
      </li>
      <li class="nav-item" v-if="admin">
        <sidenav-collapse navText="Dashboard" :to="{ name: 'Dashboard' }">
          <template v-slot:icon>
            <icon name="dashboard" />
          </template>
        </sidenav-collapse>
      </li>
      <li class="nav-item" v-if="admin">
        <sidenav-collapse
          navText="Add Category"
          :to="{ name: 'Script Category' }"
        >
          <template v-slot:icon>
            <!-- <icon name="dashboard" /> -->
            📝
          </template>
        </sidenav-collapse>
      </li>
      <li class="nav-item" v-if="admin">
        <sidenav-collapse
          navText="Add Language"
          :to="{ name: 'Script Language' }"
        >
          <template v-slot:icon>
            <!-- <icon name="dashboard" /> -->
            📝
          </template>
        </sidenav-collapse>
      </li>
      <li class="nav-item" v-if="!admin">
        <sidenav-collapse navText="Tasks Store" :to="{ name: 'Task Store' }">
          <template v-slot:icon>
            <icon name="virtual-reality" />
          </template>
        </sidenav-collapse>
      </li>
      <li class="nav-item" v-if="admin">
        <sidenav-collapse
          navText="Requests Store"
          :to="{ name: 'Requests Store' }"
        >
          <template v-slot:icon>
            <icon name="dashboard" />
          </template>
        </sidenav-collapse>
      </li>
      <li class="nav-item" v-if="isLoggedIn">
        <sidenav-collapse
          navText="Installed Task"
          :to="{ name: 'SavedScripts' }"
        >
          <template v-slot:icon>
            <icon name="billing" />
          </template>
        </sidenav-collapse>
      </li>
      <li class="nav-item" v-if="dev || admin">
        <sidenav-collapse navText="Upload Here" :to="{ name: 'UploadScript' }">
          <template v-slot:icon> 📁 </template>
        </sidenav-collapse>
      </li>

      <!-- <li class="nav-item">
        <sidenav-collapse navText="Timesheet" :to="{ name: 'def' }">
          <template v-slot:icon> ⏳ </template>
        </sidenav-collapse>
      </li> -->

      <li class="mt-3 nav-item">
        <h6
          class="text-xs ps-4 text-uppercase font-weight-bolder opacity-6"
          :class="this.$store.state.isRTL ? 'me-4' : 'ms-2'"
        >
          Requested Scripts
        </h6>
      </li>
      <li class="nav-item">
        <sidenav-collapse
          navText="Posts"
          :to="{ name: 'postrequest' }"
        >
          <template v-slot:icon>
            <icon name="virtual-reality" />
          </template>
        </sidenav-collapse>
      </li>


      
      <li class="mt-3 nav-item">
        <h6
          class="text-xs ps-4 text-uppercase font-weight-bolder opacity-6"
          :class="this.$store.state.isRTL ? 'me-4' : 'ms-2'"
        >
          Privacy & Policy
        </h6>
      </li>
      <li class="nav-item">
        <sidenav-collapse
          navText="Privacy & Policy"
          :to="{ name: 'Privacy & Policy' }"
        >
          <template v-slot:icon>
            <icon name="virtual-reality" />
          </template>
        </sidenav-collapse>
      </li>
      <li class="nav-item">
        <sidenav-collapse navText="Terms & Condition" :to="{ name: 'T&C' }">
          <template v-slot:icon>
            <icon name="rtl-page" />
          </template>
        </sidenav-collapse>
      </li>
    </ul>
  </div>
</template>
<script>
import Icon from "@/components/Icon.vue";
import SidenavCollapse from "./SidenavCollapse.vue";

// FOR AXIOS API
import { createApp } from "vue";
import App from "../../App.vue";
const appInstance = createApp(App);
import VueAxios from "vue-axios";
import axios from "axios";
appInstance.use(VueAxios, axios);

import Swal from "sweetalert2";

export default {
  name: "SidenavList",
  props: {
    cardBg: String,
  },
  data() {
    return {
      title: "Soft UI Dashboard PRO",
      controls: "dashboardsExamples",
      isActive: "active",
      dev: false,
      user: false,
      admin: false,
      tu: false,
      org: false,
      emp: false,
      username: "",

      isLoggedIn: false,
    };
  },

  mounted() {
    var myrole = localStorage.getItem("role");
    if(myrole != null){
      this.isLoggedIn = true;
    }
    if (myrole === "dev") {
      this.dev = true;
      this.user = false;
    } else if (myrole === "user") {
      this.user = true;
      this.dev = false;
    } else if (myrole === "admin") {
      this.admin = true;
    } else if (myrole === "organization") {
      this.org = true;
    } else if (myrole === "employee") {
      this.emp = true;
    } else if (myrole == "tu") {
      this.tu = true;
    }
    this.getUserNameFun();
  },

  components: {
    Icon,
    SidenavCollapse,
  },
  methods: {
    getRoute() {
      const routeArr = this.$route.path.split("/");
      return routeArr[1];
    },

    async getUserNameFun() {
      var userId = localStorage.getItem("uid");
      var role = localStorage.getItem("role");
      await appInstance.axios
        .get(
          "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/getUserName/" +
            userId +
            "/" +
            role
        )
        // .get("http://127.0.0.1:8000/app/v1/users/getUserName/" + userId + "/" + role)
        .then((res) => {
          this.username = res.data["msg"];
        });
    },

    refreshTestUser() {
      var url = "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/testUserInstall";
      // var url="http://127.0.0.1:8000/app/v1/users/testUserInstall";
      const data = new FormData();
      data.append("uid", localStorage.getItem("uid"));
      appInstance.axios
        .post(url, data, { headers: { "Content-Type": "application/json" } })
        .then((res) => {
          if (res.data["msg"] === "done") {
            // Swall Added Msg
            Swal.fire(
              "Succesfully Updated!!!",
              "New script succesfully added...",
              "success"
            );
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
              text: "All script are already associated to you.",
            });
          }
        });
    },
  },
};
</script>
