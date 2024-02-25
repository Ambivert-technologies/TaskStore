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
                <form>
                  <div class="row">
                    <div v-if="enterMail">
                      <form @submit="formSubmit" role="form" class="text-start">
                        <div class="form-group">
                          <label for="mail">Email Address</label>
                          <input
                            type="text"
                            id="mail"
                            class="form-control"
                            v-model="regMail"
                            placeholder="Enter your registered email address"
                            required
                          />
                        </div>
                        <button
                          type="submit"
                          class="btn btn-sm btn-outline-info mb-3"
                          style="display: inline"
                        >
                          Submit
                        </button>
                      </form>
                    </div>

                    <div v-if="securityQuestionArea">
                      <form @submit="resetPass" role="form" class="text-start">
                        <div class="form-group">
                          <label for="sq">Security Questions</label>
                          <input
                            type="text"
                            id="sq"
                            class="form-control"
                            v-model="sq"
                            placeholder="Security Question"
                            required
                          />
                        </div>
                        <div class="form-group">
                          <label for="sqa">Write the answer</label>
                          <input
                            type="text"
                            id="sqa"
                            class="form-control"
                            v-model="enter_sqa"
                            placeholder="Type here..."
                            required
                          />
                        </div>
                        <button
                          type="submit"
                          class="btn bg-gradient-warning btn-lg"
                        >
                          Submit &nbsp;&nbsp;<span
                            class="spinner-border spinner-border-sm"
                            role="status"
                            aria-hidden="true"
                            v-if="pleaseWait"
                          ></span>
                        </button>
                      </form>
                    </div>

                    <div v-if="passwordArea">
                      <form @submit="changePwd" role="form" class="text-start">
                        <div class="form-group">
                          <label for="pwd">New Password</label>
                          <input
                            type="text"
                            id="pwd"
                            class="form-control"
                            v-model="new_pwd"
                            placeholder="Enter a new password"
                            required
                          />
                        </div>
                        <button
                          type="submit"
                          class="btn btn-sm btn-outline-info mb-3"
                          style="display: inline"
                        >
                          Submit
                        </button>
                      </form>
                    </div>
                  </div>
                </form>
              </div>
              <div class="px-1 pt-0 text-center card-footer px-lg-2">
                <p class="mx-auto mb-4 text-sm">
                  Don't have an account?
                  <router-link
                    to="/sign-up"
                    class="text-info text-gradient font-weight-bold"
                  >
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
const body = document.getElementsByTagName("body")[0];

// FOR AXIOS API
import { createApp } from "vue";
import App from "../App.vue";
const appInstance = createApp(App);
import VueAxios from "vue-axios";
import axios from "axios";
appInstance.use(VueAxios, axios);

import Swal from "sweetalert2";

export default {
  name: "ForgotPwd",
  components: {
    // Navbar,
    // AppFooter,
  },

  data() {
    return {
      enterMail: true,
      pleaseWait: false,

      sq: "",
      sqa: "",
      enter_sqa: "",
      regMail: "",
      new_pwd: "",

      securityQuestionArea: false,
      passwordArea: false,
    };
  },

  methods: {
    checkForSpecialChar(string) {
      var specialChars =
        "1234567890<>@!#$%^&*()_+[]{}?:;|'\"\\,./~`-=ABCDEFGHIJKLMNOPQRSTUVWXYZ";
      for (var i = 0; i < specialChars.length; i++) {
        if (string.indexOf(specialChars[i]) > -1) {
          return true;
        }
      }
      return false;
    },

    formSubmit(event) {
      event.preventDefault();
      if (this.regMail.trim() != "") {
        var formData = new FormData();
        formData.append("mail", this.regMail);
        appInstance.axios
          .post(
            "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/getSecQue",
            // "http://127.0.0.1:8000/app/v1/users/getSecQue",
            formData,
            {
              headers: { "Content-Type": "application/json" },
            }
          )
          .then((res) => {
            if (res.data["msg"] === true) {
              this.sq = res.data["data"]["sq"],
              this.sqa = res.data["data"]["sqa"],
              this.securityQuestionArea = true;
              this.enterMail = false;
            } else {
              Swal.fire({
                icon: "error",
                title: "Invalid Email !!!",
                text: "Dont't have any account associated to this email...",
              });
            }
          });
      } else {
        Swal.fire({
          icon: "error",
          title: "Error !!!",
          text: "Please fill the required field",
        });
      }
    },

    resetPass(event) {
      event.preventDefault();
      if((this.enter_sqa).toLowerCase() === this.sqa){
        Swal.fire({
          icon: "success",
          title: "Verified !!!",
          text: "You can change your credentials...",
        });
        this.enterMail = false;
        this.securityQuestionArea = false;
        this.passwordArea = true;
      }else{
        Swal.fire({
          icon: "error",
          title: "Error !!!",
          text: "Wrong answer...",
        });
      }
    },

    changePwd(event){
      event.preventDefault();
      if (this.new_pwd.trim() != "") {
        if(this.checkForSpecialChar(this.new_pwd.toString())){
          var formData = new FormData();
          formData.append("mail", this.regMail);
          formData.append("pwd", this.new_pwd);
          appInstance.axios
            .post(
              "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/forgotPwd",
              // "http://127.0.0.1:8000/app/v1/users/forgotPwd",
              formData,
              {
                headers: { "Content-Type": "application/json" },
              }
            )
            .then((res) => {
              if (res.data["msg"] === true) {
                Swal.fire({
                  icon: "success",
                  title: "Password Changed !!!",
                  text: "New password successfully updated...",
                });
                localStorage.clear();
                this.$router.push("/sign-in");
              } else {
                Swal.fire({
                  icon: "error",
                  title: "Invalid Email !!!",
                  text: "Dont't have any account associated to this email...",
                });
              }
            });
        }else{
          Swal.fire({
            icon: "error",
            title: "Weak Password !!!",
            text: "Please enter a strong password...",
          });
        }
      }else{
        Swal.fire({
          icon: "error",
          title: "Empty field!!!",
          text: "Password field can't be empty...",
        });
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
