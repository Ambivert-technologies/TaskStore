<template>
  <nav
    class="shadow-none navbar navbar-main navbar-expand-lg border-radius-xl"
    v-bind="$attrs"
    id="navbarBlur"
    data-scroll="true"
  >
    <div class="px-3 py-1 container-fluid">
      <breadcrumbs :currentPage="currentRouteName" :textWhite="textWhite" />
      <div
        class="mt-2 collapse navbar-collapse mt-sm-0 me-md-0 me-sm-4"
        :class="this.$store.state.isRTL ? 'px-0' : 'me-sm-4'"
        id="navbar"
      >
        <div
          class="pe-md-3 d-flex align-items-center"
          :class="this.$store.state.isRTL ? 'me-md-auto' : 'ms-md-auto'"
        >
          
        </div>
        <ul class="navbar-nav justify-content-end">

          <li class="nav-item dropdown d-flex align-items-center ps-4 pe-2" v-if="loggedIn">
            <a
              href="javascript:;"
              id="dropdownMenuProfile"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              <div class="d-flex align-items-center">
                <img
                  src="https://demos.creative-tim.com/soft-ui-dashboard/assets/img/team-3.jpg"
                  class="avatar avatar-xs"
                />
                <p class="text-sm ms-2 mb-0">{{username}}</p>
              </div> </a
            ><a> </a>
            <ul
              class="
                dropdown-menu dropdown-menu-end
                px-2
                py-3
                me-sm-n4
                position-sm-relative position-absolute
                bg-white
              "
              aria-labelledby="dropdownMenuProfile"
            >
              <a> </a>
              <!-- <li class="mb-2">
                <a> </a
                ><a class="dropdown-item border-radius-md" href="javascript:;">
                  <i class="fa fa-user" aria-hidden="true"></i>
                  <span class="ms-2">My profile</span>
                </a>
              </li> -->
              <router-link to="/change-pwd">
                <li class="mb-2">
                  <a class="dropdown-item border-radius-md" href="javascript:;">
                    <i class="fa fa-tools" aria-hidden="true"></i>
                    <span class="ms-2">Settings</span>
                  </a>
                </li>
              </router-link>
              <!-- <li class="mb-2">
                <a class="dropdown-item border-radius-md" href="javascript:;">
                  <i class="fa fa-calendar" aria-hidden="true"></i>
                  <span class="ms-2">Activity</span>
                </a>
              </li> -->
              <hr class="horizontal dark" />
              <li @click="signout">
                <a class="dropdown-item border-radius-md" href="javascript:;">
                  <i class="fa fa-sign-out-alt" aria-hidden="true"></i>
                  <span class="ms-2">Logout</span>
                </a>
              </li>
            </ul>
          </li>

          <li
            class="nav-item d-flex align-items-center cursor-pointer mx-3"
            @click="signout"
            v-if="!loggedIn"
          >
            <i
              class="fa fa-user cursor-pointer"
              :class="this.$store.state.isRTL ? 'ms-sm-2' : 'me-sm-1'"
            ></i>
            <!-- <span v-if="this.$store.state.isRTL" class="d-sm-inline d-none"
                >يسجل دخول</span
              > -->
            <!-- <span v-if="loggedIn" class="d-sm-inline d-none">Sign Out</span> -->

            <span class="d-sm-inline d-none">Sign In</span>
          </li>
          <li
            class="nav-item d-flex align-items-center cursor-pointer"
            @click="signup"
            v-if="!loggedIn"
          >
            <i
              class="fa fa-user cursor-pointer"
              :class="this.$store.state.isRTL ? 'ms-sm-2' : 'me-sm-1'"
            ></i>
            <!-- <span v-if="this.$store.state.isRTL" class="d-sm-inline d-none"
                >يسجل دخول</span
              > -->
            <!-- <span v-if="loggedIn" class="d-sm-inline d-none">Sign Out</span> -->

            <span class="d-sm-inline d-none">Sign Up</span>
          </li>
          <!-- <li class="nav-item d-xl-none ps-3 d-flex align-items-center">
            <a
              href="#"
              @click="toggleSidebar"
              class="p-0 nav-link text-body"
              id="iconNavbarSidenav"
            >
              <div class="sidenav-toggler-inner">
                <i class="sidenav-toggler-line"></i>
                <i class="sidenav-toggler-line"></i>
                <i class="sidenav-toggler-line"></i>
              </div>
            </a>
          </li>
          <li class="px-3 nav-item d-flex align-items-center">
            <a
              class="p-0 nav-link"
              @click="toggleConfigurator"
              :class="textWhite ? textWhite : 'text-body'"
            >
              <i class="cursor-pointer fa fa-cog fixed-plugin-button-nav"></i>
            </a>
          </li> -->
        </ul>
      </div>
    </div>
  </nav>
</template>
<script>
import Breadcrumbs from "../Breadcrumbs.vue";
import { mapMutations, mapActions } from "vuex";

// FOR AXIOS API
import { createApp } from "vue";
import App from "../../App.vue";
const appInstance = createApp(App);
import VueAxios from "vue-axios";
import axios from "axios";
appInstance.use(VueAxios, axios);

export default {
  name: "navbar",
  data() {
    return {
      showMenu: false,
      loggedIn: false,
      username: "",
    };
  },
  props: ["minNav", "textWhite"],
  created() {
    this.minNav;
  },
  beforeMount() {
    this.loggedIn = localStorage.getItem("loggedIn");
    if (this.loggedIn === "true") {
      this.loggedIn = true;
    }
    this.getUserNameFun();
  },
  methods: {
    ...mapMutations(["navbarMinimize", "toggleConfigurator"]),
    ...mapActions(["toggleSidebarColor"]),

    toggleSidebar() {
      this.toggleSidebarColor("bg-white");
      this.navbarMinimize();
    },

    signout() {
      localStorage.clear();
      this.$router.push("/sign-in");
    },

    signup() {
      localStorage.clear();
      this.$router.push("/sign-up");
    },

    async getUserNameFun() {
      var userId = localStorage.getItem("uid");
      var role = localStorage.getItem("role");
      await appInstance.axios
        .get("https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/getUserName/" + userId + "/" + role)
        // .get("http://127.0.0.1:8000/app/v1/users/getUserName/" + userId + "/" + role)
        .then((res) => {
          this.username = res.data["msg"];
        });
    },
  },
  components: {
    Breadcrumbs,
  },
  computed: {
    currentRouteName() {
      return this.$route.name;
    },
  },
  updated() {
    const navbar = document.getElementById("navbarBlur");
    window.addEventListener("scroll", () => {
      if (window.scrollY > 10 && this.$store.state.isNavFixed) {
        navbar.classList.add("blur");
        navbar.classList.add("position-sticky");
        navbar.classList.add("shadow-blur");
      } else {
        navbar.classList.remove("blur");
        navbar.classList.remove("position-sticky");
        navbar.classList.remove("shadow-blur");
      }
    });
  },
};
</script>
