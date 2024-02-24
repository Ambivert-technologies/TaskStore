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
            Create a new account for free, and make your life easy with awesome scripts.
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
            <h5>Register</h5>
          </div>
          <div class="card-body">
            <form @submit="formSubmit" role="form" v-if="myrole=='' || myrole=='err' || myrole=='user' || myrole=='dev'">
              <div class="mb-3">
                <select v-on:change="changeMyRole()" class="form-control form-control-lg" id="role">
                  <option value="err">I'm a</option>
                  <option value="user">User</option>
                  <option value="dev">Developer</option>
                  <option value="organization">Organization</option>
                  <option value="employee">Employee</option>
                </select>
              </div>
              <div class="mb-3">
                <vsud-input
                  id="name"
                  type="text"
                  placeholder="Name"
                  aria-label="Name"
                />
              </div>
              <div class="mb-3">
                <vsud-input
                  id="email"
                  type="email"
                  placeholder="Email"
                  aria-label="Email"
                />
              </div>
              <div class="form-group">
                <input
                  id="sq"
                  type="text"
                  placeholder="Security Question(e.g. What is my pet name?)"
                  aria-label="Password"
                  class="form-control"
                  v-model="sq"
                  v-on:keyup="chkLen"
                  required
                />
              </div>
              <div class="form-group" v-if="sqaCon">
                <input
                  id="sqa"
                  type="text"
                  placeholder="Type your answer..."
                  aria-label="Password"
                  class="form-control"
                  v-model="sqa"
                  required
                />
              </div>
              <div class="form-group">
                <input
                  id="pwd"
                  type="password"
                  placeholder="Password"
                  aria-label="Password"
                  minlength="8"
                  class="form-control"
                  required
                />
              </div>
              <vsud-checkbox id="flexCheckDefault" checked>
                I agree the
                <router-link :to="{ name: 'T&C' }">Terms and Conditions</router-link>
              </vsud-checkbox>

              <div class="text-center">
                <vsud-button
                  color="dark"
                  type="submit"
                  fullWidth
                  variant="gradient"
                  class="my-4 mb-2"
                >
                  Sign up &nbsp;&nbsp;<span
                    class="spinner-border spinner-border-sm"
                    role="status"
                    aria-hidden="true"
                    v-if="pleaseWait"
                  ></span>
                </vsud-button>
              </div>
              <p class="text-sm mt-3 mb-0">
                Already have an account?
                <router-link
                  to="/sign-in"
                  class="text-dark text-gradient font-weight-bold"
                >
                  Sign in
                </router-link>
              </p>
            </form>

            <form @submit="formSubmit" role="form" v-if="myrole=='organization'">
              <div class="mb-3">
                <select v-on:change="changeMyRole()" class="form-control form-control-lg" id="role">
                  <option value="err">I'm a</option>
                  <option value="user">User</option>
                  <option value="dev">Developer</option>
                  <option value="organization" selected>Organization</option>
                  <option value="employee">Employee</option>
                </select>
              </div>
              <div class="mb-3">
                <vsud-input
                  id="name"
                  type="text"
                  placeholder="Organization Name"
                  aria-label="Name"
                />
              </div>
              <div class="mb-3">
                <vsud-input
                  id="email"
                  type="email"
                  placeholder="Enter Organization Email"
                  aria-label="Email"
                />
                <p v-if="validOrgEmail" style="font-size: 14px; color: red;">
                [!] Enter valid Organization Email ID or you may <router-link target="_blank" to="contact-us" style="color: blue;"><u>Contact us.</u></router-link>
                </p>
              </div>
              <div class="mb-3">
                <vsud-input
                  id="tmSize"
                  type="number"
                  placeholder="Number of employee"
                  aria-label="Size"
                />
              </div>
              <div class="mb-3">
                <vsud-input
                  id="industry"
                  type="text"
                  placeholder="Industry Name"
                  aria-label="Industry"
                />
              </div>
              <div class="form-group">
                <input
                  id="sq"
                  type="text"
                  placeholder="Security Question(e.g. What is my pet name?)"
                  aria-label="Password"
                  class="form-control"
                  v-model="sq"
                  v-on:keyup="chkLen"
                  required
                />
              </div>
              <div class="form-group" v-if="sqaCon">
                <input
                  id="sqa"
                  type="text"
                  placeholder="Type your answer..."
                  aria-label="Password"
                  class="form-control"
                  v-model="sqa"
                  required
                />
              </div>
              <div class="form-group">
                <input
                  id="pwd"
                  type="password"
                  placeholder="Password"
                  aria-label="Password"
                  minlength="8"
                  class="form-control"
                  required
                />
              </div>
              <vsud-checkbox id="flexCheckDefault" checked>
                I agree the
                <router-link :to="{ name: 'T&C' }">Terms and Conditions</router-link>
              </vsud-checkbox>

              <div class="text-center">
                <vsud-button
                  color="dark"
                  type="submit"
                  fullWidth
                  variant="gradient"
                  class="my-4 mb-2"
                >
                  Sign up &nbsp;&nbsp;<span
                    class="spinner-border spinner-border-sm"
                    role="status"
                    aria-hidden="true"
                    v-if="pleaseWait"
                  ></span>
                </vsud-button>
              </div>
              <p class="text-sm mt-3 mb-0">
                Already have an account?
                <router-link
                  to="/sign-in"
                  class="text-dark text-gradient font-weight-bold"
                >
                  Sign in
                </router-link>
              </p>
            </form>

            <form @submit="formSubmit" role="form" v-if="myrole=='employee'">
              <div class="mb-3">
                <select v-on:change="changeMyRole()" class="form-control form-control-lg" id="role">
                  <option value=" ">I'm a</option>
                  <option value="user">User</option>
                  <option value="dev">Developer</option>
                  <option value="organization">Organization</option>
                  <option value="employee" selected>Employee</option>
                </select>
              </div>
              <div class="mb-3">
                <vsud-input
                  id="name"
                  type="text"
                  placeholder="Your Name"
                  aria-label="Name"
                />
              </div>
              <!-- <div class="mb-3">
                <select class="form-control form-control-lg" id="orge">
                  <option value="" selected>-- Organization --</option>
                  <option value="user" v-for="i in this.allOrg" :key="i.id">{{i}}</option>
                </select>
              </div> -->
              <!-- <div class="mb-3">
                <vsud-input
                  id="email"
                  type="email"
                  placeholder="Enter Organization Email"
                  aria-label="Email"
                />
              </div> -->
              <div class="mb-3">
                <vsud-input
                  id="emp_email"
                  type="email"
                  placeholder="Employee Email"
                  aria-label="Email"
                />
              </div>
              <div class="form-group">
                <input
                  id="sq"
                  type="text"
                  placeholder="Security Question(e.g. What is my pet name?)"
                  aria-label="Password"
                  class="form-control"
                  v-model="sq"
                  v-on:keyup="chkLen"
                  required
                />
              </div>
              <div class="form-group" v-if="sqaCon">
                <input
                  id="sqa"
                  type="text"
                  placeholder="Type your answer..."
                  aria-label="Password"
                  class="form-control"
                  v-model="sqa"
                  required
                />
              </div>
              <div class="form-group">
                <input
                  id="pwd"
                  type="password"
                  placeholder="Password"
                  aria-label="Password"
                  minlength="8"
                  class="form-control"
                  required
                />
              </div>
              <vsud-checkbox id="flexCheckDefault" checked>
                I agree the
                <router-link :to="{ name: 'T&C' }">Terms and Conditions</router-link>
              </vsud-checkbox>

              <div class="text-center">
                <vsud-button
                  color="dark"
                  type="submit"
                  fullWidth
                  variant="gradient"
                  class="my-4 mb-2"
                >
                  Sign up &nbsp;&nbsp;<span
                    class="spinner-border spinner-border-sm"
                    role="status"
                    aria-hidden="true"
                    v-if="pleaseWait"
                  ></span>
                </vsud-button>
              </div>
              <p class="text-sm mt-3 mb-0">
                Already have an account?
                <router-link
                  to="/sign-in"
                  class="text-dark text-gradient font-weight-bold"
                >
                  Sign in
                </router-link>
              </p>
            </form>
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
import VsudCheckbox from "@/components/VsudCheckbox.vue";
import VsudButton from "@/components/VsudButton.vue";

// FOR AXIOS API
import { createApp } from "vue";
import App from "../App.vue";
const appInstance = createApp(App);
import VueAxios from "vue-axios";
import axios from "axios";
appInstance.use(VueAxios, axios);

import Swal from "sweetalert2";

export default {
  name: "sign-up",
  data() {
    return {
      pleaseWait: false,
      sq: "",
      sqaCon: false,
      sqa: "",

      myrole: "",
      allOrg: [],
      validOrgEmail: false,
    };
  },
  components: {
    // Navbar,
    // AppFooter,
    VsudInput,
    VsudCheckbox,
    VsudButton,
  },

  methods: {
    chkLen(){
      if(this.sq.trim().length > 4){
        this.sqaCon = true;
      }else{
        this.sqaCon = false;
      }
    },

    changeMyRole(){
      this.myrole = document.getElementById("role").value;
      // if(this.myrole === "employee"){
      //   appInstance.axios
      //   .get(
      //     // "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/getAllOrg",
      //     "http://127.0.0.1:8000/app/v1/users/getAllOrg",
      //     {
      //       headers: { "Content-Type": "application/json" },
      //     }
      //   )
      //   .then((res) => {
      //     if (res.data["msg"] === "done") {
      //       this.allOrg = res.data["data"];
            
      //     } else {
      //       Swal.fire({
      //         icon: "error",
      //         title: "Oops...",
      //         text: res.data["err_msg"],
      //       });
      //     }
      //   });
      // }
    },

    checkForSpecialChar(string) {
      var specialChars =
        "1234567890<>@!#$%^&*()_+[]{}?:;|'\"\\,./~`-=ABCDEFGHIJKLMNOPQRSTUVWXYZ";
      for (var i = 0; i < specialChars.length; i++) {
        if (string.indexOf(specialChars[i]) > -1) {
          return false;
        }
      }
      return true;
    },

    formSubmit(e) {
      e.preventDefault();
      var str = document.getElementById("pwd").value;
      var role = document.getElementById("role").value;
      var formData = new FormData();

      if (this.checkForSpecialChar(str)) {
        Swal.fire({
          icon: "error",
          title: "Weak Password !!!",
          text: "Your password should be combination of Special Chars and uppercase letter or numbers.",
        });
      } else {
        this.pleaseWait = true;
        if (role != "employee"){
          var email = document.getElementById("email").value;
        }
        var pwd = document.getElementById("pwd").value;
        var name = document.getElementById("name").value;
        
        // var role = "user";

        if (role != "employee"){
          formData.append("email", email);
        }else{
          formData.append("email", "not applicable")
        }


        var goahead = false;
        if(role === "organization"){
          var indexOfAt = email.indexOf("@");
          var result = email.slice(indexOfAt+1); 
          if(
            result.toLowerCase() === "hotmail.com" || 
            result.toLowerCase() === "outlook.com" || 
            result.toLowerCase() === "gmail.com" || 
            result.toLowerCase() === "inbox.com" || 
            result.toLowerCase() === "yahoo.com" || 
            result.toLowerCase() === "zohomail.in" || 
            result.toLowerCase() === "mail.com" || 
            result.toLowerCase() === "protonmail.com" || 
            result.toLowerCase() === "icloud.com")
            {
              goahead = false;
              this.pleaseWait = false;
              this.validOrgEmail = true;
            }else{
              goahead = true;
              this.validOrgEmail = false;
            }
        }else{
          goahead = true;
          this.validOrgEmail = false;
        }
        
        if(goahead === true){
            formData.append("pwd", pwd);
            formData.append("name", name);
            formData.append("sq", this.sq);
            formData.append("sqa", this.sqa);
            formData.append("role", role);

            // API Call From here
            if (
              pwd.trim() != "" &&
              name.trim() != "" &&
              role != "" && 
              this.sqa.trim() != ""
            ) {
              if (role === "employee"){
                var emp_email = document.getElementById("emp_email").value;
                formData.append("emp_email", emp_email);
                appInstance.axios
                  .post(
                    "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/emp_register",
                    // "http://127.0.0.1:8000/app/v1/users/emp_register",
                    formData,
                    {
                      headers: { "Content-Type": "application/json" },
                    }
                  )
                  .then((res) => {
                    if (res.data["msg"] === "done") {
                      localStorage.clear();
                      this.pleaseWait = false;
                      Swal.fire(
                        "Congratulation!",
                        "Registration Succesfull...",
                        "success"
                      );
                      this.$router.push("/sign-in");
                    } else {
                      this.pleaseWait = false;
                      Swal.fire({
                        icon: "error",
                        title: "Oops...",
                        text: res.data["err_msg"],
                      });
                    }
                  });

              }else if(role === "organization"){
                var tmSize = document.getElementById("tmSize").value;
                formData.append("tmSize", tmSize);
                var industry = document.getElementById("industry").value;
                formData.append("industry", industry);
                appInstance.axios
                  .post(
                    "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/org_register",
                    // "http://127.0.0.1:8000/app/v1/users/org_register",
                    formData,
                    {
                      headers: { "Content-Type": "application/json" },
                    }
                  )
                  .then((res) => {
                    if (res.data["msg"] === "done") {
                      localStorage.clear();
                      this.pleaseWait = false;
                      Swal.fire(
                        "Congratulation!",
                        "Registration Succesfull...",
                        "success"
                      );
                      this.$router.push("/sign-in");
                    } else {
                      this.pleaseWait = false;
                      Swal.fire({
                        icon: "error",
                        title: "Oops...",
                        text: res.data["err_msg"],
                      });
                    }
                  });

              }else{
                appInstance.axios
                  .post(
                    "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/register",
                    // "http://127.0.0.1:8000/app/v1/users/register",
                    formData,
                    {
                      headers: { "Content-Type": "application/json" },
                    }
                  )
                  .then((res) => {
                    if (res.data["msg"] === "done") {
                      localStorage.clear();
                      this.pleaseWait = false;
                      Swal.fire(
                        "Congratulation!",
                        "Registration Succesfull...",
                        "success"
                      );
                      this.$router.push("/sign-in");
                    } else {
                      this.pleaseWait = false;
                      if (res.data["msg"] === "EmailExist") {
                        Swal.fire({
                          icon: "error",
                          title: "Email Exist !",
                          text: "You already have an account, please sign in.",
                        });
                      }else{
                        Swal.fire({
                          icon: "error",
                          title: "Oops...",
                          text: "Something went wrong, try again !!!",
                        });
                      }
                      
                    }
                  });
              }

            } else {
              this.pleaseWait = false;
              Swal.fire({
                icon: "error",
                title: "Oops...",
                text: "Please fill all required field...",
              });
            }
        }
          
      }
      // End Of API Request
    },
  },

  created() {
    this.$store.state.hideConfigButton = true;
    this.$store.state.showNavbar = false;
    this.$store.state.showSidenav = false;
    this.$store.state.showFooter = false;
  },
  beforeUnmount() {
    this.$store.state.hideConfigButton = false;
    this.$store.state.showNavbar = true;
    this.$store.state.showSidenav = true;
    this.$store.state.showFooter = true;
  },
};
</script>