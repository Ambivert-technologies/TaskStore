<template>
  <div class="card">
    <div class="card-body">
      <h5 class="card-title mb-3">Provide Script Details</h5>
      <form>
        <div class="row">
          <div class="col-md-4">
            <div v-if="entercurpwd">
              <form @submit="checkCurPwd" role="form" class="text-start">
                <div class="form-group">
                  <label for="otpemail">Current password</label>
                  <input
                    type="password"
                    id="otpemail"
                    class="form-control"
                    v-model="currpwd"
                    placeholder="Type your current password"
                    required
                  />
                </div>
                <button
                  type="submit"
                  class="btn btn-sm btn-outline-primary mb-3"
                  style="display: inline"
                >
                  Verify
                </button>
              </form>
            </div>

            <div v-if="enterEditEmailPwd">
              <form @submit="resetPass" role="form" class="text-start">
                <div class="form-group">
                  <label for="pass">Email</label>
                  <input
                    type="email"
                    id="pass"
                    class="form-control"
                    v-model="responseEmail"
                    placeholder="Email"
                    required
                  />
                </div>
                <div class="form-group">
                  <label for="cpass">Password</label>
                  <input
                    type="text"
                    id="cpass"
                    class="form-control"
                    v-model="responsePwd"
                    placeholder="Password"
                    minlength="8"
                    required
                  />
                </div>
                <button type="submit" class="btn bg-gradient-warning btn-lg">
                  Submit &nbsp;&nbsp;<span
                    class="spinner-border spinner-border-sm"
                    role="status"
                    aria-hidden="true"
                    v-if="pleaseWait"
                  ></span>
                </button>
              </form>
            </div>
          </div>
        </div>
      </form>
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
  name: "EditScript",
  data() {
    return {
      entercurpwd: true,
      enterEditEmailPwd: false,
      currpwd: "",
      pleaseWait: false,
      responseEmail: "",
      responsePwd: "",
      userId: "",
    };
  },

  methods: {
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

    checkCurPwd(event) {
      event.preventDefault();
      if (this.currpwd.trim() != "") {
        var formData = new FormData();
        formData.append("currpwd", this.currpwd);
        formData.append("uid", localStorage.getItem("uid"));
        appInstance.axios
          .post(
            "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/checkCurPwd",
            // "http://127.0.0.1:8000/app/v1/users/checkCurPwd",
            formData,
            {
              headers: { "Content-Type": "application/json" },
            }
          )
          .then((res) => {
            if (res.data["msg"] === true) {
              Swal.fire({
                icon: "success",
                title: "Verified !!!",
                text: "You can change your credentials...",
              });
              (this.responseEmail = res.data["data"]["email"]),
                (this.responsePwd = res.data["data"]["pwd"]),
                (this.entercurpwd = false);
              this.enterEditEmailPwd = true;
            } else {
              Swal.fire({
                icon: "error",
                title: "Wrong Input !!!",
                text: "Unauthorized access...",
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
      var str = this.responsePwd.toString();
      if (this.checkForSpecialChar(str)) {
        Swal.fire({
          icon: "error",
          title: "Weak Password !!!",
          text: "Your password should be combination of Special Chars and uppercase letter.",
        });
      } else {
        if (this.responseEmail.trim() != "" && this.responsePwd.trim() != "") {
          var formData = new FormData();
          formData.append("pwd", this.responsePwd);
          formData.append("email", this.responseEmail);
          formData.append("uid", localStorage.getItem("uid"));
          appInstance.axios
            .post(
              "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/resetPass",
              // "http://127.0.0.1:8000/app/v1/users/resetPass",
              formData,
              {
                headers: { "Content-Type": "application/json" },
              }
            )
            .then((res) => {
              if (res.data["msg"] === true) {
                Swal.fire({
                  icon: "success",
                  title: "Credentials Changed !!!",
                  text: "Credentials Successfully Changed",
                });
                localStorage.clear();
                this.$router.push("/sign-in");
              } else {
                Swal.fire({
                  icon: "error",
                  title: "Oooops!!!",
                  text: "Something went wrong, try again!!!",
                });
              }
            });
        } else {
          Swal.fire({
            icon: "error",
            title: "Error !!!",
            text: "Please fill required fields...",
          });
        }
      }
    },
  },
};
</script>
