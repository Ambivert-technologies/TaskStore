<template>
  <!-- <navbar btnBackground="bg-gradient-primary" /> -->
  <div
    class="
      pt-5
      m-3
      page-header
      align-items-start
      min-vh-50
      pb-11
      border-radius-lg
    "
    :style="{
      backgroundImage:
        'url(' + require('@/assets/img/curved-images/curved6.jpg') + ')',
    }"
  >
    <span class="mask bg-gradient-dark opacity-6"></span>
    <div class="container">
      <div class="row justify-content-center">
        <div class="mx-auto text-center col-lg-5">
          <h1 class="mt-5 mb-2 text-white">Welcome!</h1>
          <p class="text-white text-lead">
            Enter your email and password to sign in
          </p>
        </div>
      </div>
    </div>
  </div>
  <div class="container">
    <div class="row mt-lg-n10 mt-md-n11 mt-n10 justify-content-center">
      <div class="mx-auto col-xl-5 col-lg-5 col-md-7">
        <div class="card z-index-0">
          <div class="pt-4 text-center card-header">
            <h5>Sign-in</h5>
          </div>
          <div class="card-body">
            <div class="card card-plain">
                
                <div class="card-body">
                  <form @submit="formSubmit" role="form" class="text-start">
                    <label>I'm a</label>
                    <div class="mb-3">
                      <select class="form-control form-control-lg" id="role">
                        <option value="">--Select--</option>
                        <option value="user">User</option>
                        <option value="dev">Developer</option>
                        <option value="organization">Organization</option>
                        <option value="employee">Employee</option>
                      </select>
                    </div>
                    <label>Email</label>
                    <vsud-input
                      type="email"
                      placeholder="Email"
                      name="email"
                    />
                    <label>Password</label>
                    <vsud-input
                      v-model="pwd"
                      type="password"
                      placeholder="Password"
                      name="password"
                    />
                    <!-- <vsud-switch id="rememberMe">
                      Remember me
                    </vsud-switch> -->
                    <div class="text-center" style="display: inline;">
                      <vsud-button
                        class="my-4 mb-0"
                        variant="gradient"
                        color="info"
                        full-width
                        type="submit"
                        style="display: inline;"
                        >Sign in 
                        &nbsp;&nbsp;<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true" v-if="pleaseWait"></span>
                      </vsud-button>

                      <router-link to="/forgot-pwd" class="text-warning text-gradient font-weight-bold">
                        <p class="mx-auto mb-4 text-sm" style="display: inline;">
                          Forgot Password ?
                        </p>
                      </router-link>
                    </div>
                  </form>
                </div>
                <div class="px-1 pt-0 text-center card-footer px-lg-2">
                  <p class="mx-auto mb-4 text-sm">
                    Don't have an account?
                    <router-link to="/sign-up" class="text-info text-gradient font-weight-bold">
                      Sign Up
                    </router-link>
                  </p>
                </div>
              </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- <app-footer /> -->
</template>


<script>
// import Navbar from "@/examples/PageLayout/Navbar.vue";
// import AppFooter from "@/examples/PageLayout/Footer.vue";
import VsudInput from "@/components/VsudInput.vue";
// import VsudSwitch from "@/components/VsudSwitch.vue";
import VsudButton from "@/components/VsudButton.vue";
const body = document.getElementsByTagName("body")[0];

// FOR AXIOS API
import { createApp } from "vue";
import App from "../App.vue";
const appInstance = createApp(App);
import VueAxios from "vue-axios";
import axios from "axios";
appInstance.use(VueAxios, axios);


import Swal from 'sweetalert2';

export default {
  name: "signin",
  components: {
    // Navbar,
    // AppFooter,
    VsudInput,
    // VsudSwitch,
    VsudButton,
  },

  data(){
    return{
      lib: [1, 2, 3],
      pleaseWait: false
    }
  },

  methods: {
    formSubmit(event){
      this.pleaseWait = true;
      event.preventDefault();
      var email = document.getElementsByName("email")[0].value;
      var pwd = document.getElementsByName("password")[0].value;
      var role = document.getElementById("role").value;
      var formData = new FormData();
      formData.append("email", email);
      formData.append("pwd", pwd);
      formData.append("role", role);

      if(email.trim() != "" && pwd.trim() != "" && role.trim() != ""){
        appInstance.axios
        .post("https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/login", formData, {
          headers: { "Content-Type": "application/json" },
        })
        // appInstance.axios
        // .post("http://127.0.0.1:8000/app/v1/users/login", formData, {
        //   headers: { "Content-Type": "application/json" },
        // })
        .then((res) => {
          if (res.data["msg"] === true) {
            // console.log(res.data["allData"]);
            localStorage.clear();
            localStorage.setItem("uid", res.data["uid"]);
            localStorage.setItem("role", res.data["role"]);
            localStorage.setItem("loggedIn", "true");
            this.pleaseWait = false;
            // Swal.fire('Authenticate!', 'Welcome to Task Store', 'success');
            if(res.data["role"] === "admin"){
              this.$router.push("/dashboard");
            }else{
              this.$router.push("/script-list");
            }
          } else {
            this.pleaseWait = false;
            Swal.fire({icon: 'error',title: 'Oops...',text: 'Invalid Credential !!!'})
          }
        });
      }else{
        this.pleaseWait = false;
        Swal.fire({
          icon: 'error',
          title: 'Oops...',
          text: 'Please provide required credentials...'
        })
      }
    }
  },

  beforeMount() {
    this.$store.state.hideConfigButton = true;
    this.$store.state.showNavbar = false;
    this.$store.state.showSidenav = false;
    this.$store.state.showFooter = false;
    body.classList.remove("bg-gray-100");
  },
  beforeUnmount() {
    this.$store.state.hideConfigButton = false;
    this.$store.state.showNavbar = true;
    this.$store.state.showSidenav = true;
    this.$store.state.showFooter = true;
    body.classList.add("bg-gray-100");
  },
};
</script>
