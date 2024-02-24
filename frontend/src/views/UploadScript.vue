<template>
  <div class="card">
    <div class="card-body">
      <h5 class="card-title mb-3">Provide Script Details</h5>
      <form @submit="formSubmit" enctype="multipart/form-data">
        <div class="row">
          <div class="col-md-4">
            <div class="form-group">
              <label for="scNm">Script Name</label>
              <input
                type="text"
                class="form-control"
                id="scNm"
                placeholder="Enter your script name"
                required
              />
            </div>
          </div>
          <div class="col-md-4">
            <div class="form-group">
              <label for="scNm">Price (INR)</label>
              <input
                type="number"
                class="form-control"
                id="price"
                placeholder="Example: 4 (If it free type 0)"
                required
              />
            </div>
          </div>
          <div class="col-md-4">
            <div class="form-group">
              <label for="auNm">Author Name</label>
              <input
                type="text"
                class="form-control"
                id="auNm"
                placeholder="Type author name"
                required
              />
            </div>
          </div>

          <div class="col-md-4">
            <div class="form-group">
              <label for="cat">Select Category</label>
              <select class="form-control form-control-lg" id="cat" required>
                <option value="err">-- Select --</option>
                <option v-for="item in catList" :key="item.id" :value="item">{{item}}</option>
              </select>
            </div>
          </div>
          <div class="col-md-4">
            <div class="form-group">
              <label for="lang">Developing Language</label>
              <select class="form-control form-control-lg" id="lang" required>
                <option value="err">-- Select --</option>
                <option v-for="item in langList" :key="item.id" :value="item">{{item}}</option>
              </select>
            </div>
          </div>
          <div class="col-md-4">
            <div class="form-group">
              <label for="os">Select OS</label>
              <select class="form-control form-control-lg" id="os" required>
                <option value="err" disabled selected>-- Select --</option>
                <option value="Windows">Windows</option>
                <option value="Linux">Linux</option>
                <option value="Mac">Mac</option>
                <option value="All">All</option>
              </select>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-md-12">
            <div class="form-group">
              <label for="scDs">Script Description</label>
              <textarea
                class="form-control"
                id="scDs"
                rows="3"
                required
              ></textarea>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-md-6">
            <div class="form-group">
              <label for="scFl">Upload Script</label>
              <input type="file" class="form-control" id="scFl" required />
            </div>
          </div>
          <div class="col-md-6">
            <div class="form-group">
              <label for="scIc">Upload Script Icon</label>
              <input type="file" class="form-control" id="scIc" required />
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-md-6">
            <div class="form-group">
              <label for="scDp">Upload Dependency</label>
              <input type="file" class="form-control" id="scDp" required />
            </div>
          </div>
          <div class="col-md-6">
            <div class="form-group">
              <label for="youtubelink">Youtube Link</label>
              <input type="text" placeholder="Provide Youtube Link" class="form-control" id="youtubelink" required />
            </div>
          </div>
        </div>
        <button type="submit" class="btn bg-gradient-warning btn-lg">
          Submit
          &nbsp;&nbsp;<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true" v-if="pleaseWait"></span>
        </button>
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
  name: "UploadScript",
  data() {
    return {
      catList: [],
      langList: [],
      userId: "",
      pleaseWait: false
    };
  },

  mounted() {
    var loggedIn = localStorage.getItem("loggedIn");
    var role = localStorage.getItem("role");
    this.userId = localStorage.getItem("uid");
    // alert(this.userId);
    if (loggedIn != "true") {
      this.$router.push("/sign-in");
    } else {
      if (role != "dev" && role != "admin") {
        this.$router.push("/");
      } else {
        appInstance.axios
          .get("https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/getScriptCatList", {
          // .get("http://127.0.0.1:8000/app/v1/users/getScriptCatList", {
            headers: { "Content-Type": "application/json" },
          })
          .then((res) => {
            if (res.data["msg"] === true) {
              this.catList = res.data["data"]
              this.langList = res.data["l_data"];
            } else {
              Swal.fire({
                icon: "error",
                title: "Oops...",
                text: "Script category can't load at this moment.",
              });
            }
          });
      }
    }
  },
  methods: {
    formSubmit(event) {
      event.preventDefault();
      this.pleaseWait = true;

      const form_data = new FormData();

      var cat = document.getElementById("cat").value;
      form_data.append("cat", cat);

      var lang = document.getElementById("lang").value;
      form_data.append("lang", lang);

      var os = document.getElementById("os").value;
      form_data.append("os", os);

      var scriptName = document.getElementById("scNm").value;
      form_data.append("scriptName", scriptName);

      var authorName = document.getElementById("auNm").value;
      form_data.append("authorName", authorName);

      var scriptDesc = document.getElementById("scDs").value;
      form_data.append("scriptDesc", scriptDesc);

      var scriptFile = document.getElementById("scFl").files[0];
      form_data.append("scriptFile", scriptFile)

      var scriptIcon = document.getElementById("scIc").files[0];
      form_data.append("scriptIcon", scriptIcon);

      var upldDep = document.getElementById("scDp").files[0];
      form_data.append("upldDep", upldDep);

      var price = document.getElementById("price").value;
      form_data.append("price", price);

      var youtubelink = document.getElementById("youtubelink").value;
      form_data.append("youtubelink", youtubelink);

      form_data.append("userId", this.userId);

      appInstance.axios
        .post("https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/script_upload", form_data, {
        // .post("http://127.0.0.1:8000/app/v1/users/script_upload", form_data, {
          headers: { "Content-Type": "application/json" },
        })
        .then((res) => {
          if (res.data["msg"] === true) {
            this.pleaseWait = false;
            Swal.fire(
              "Successfully Uploaded!",
              "Your script successfully added...",
              "success"
            );
          } else {
            this.pleaseWait = false;
            Swal.fire({
              icon: "error",
              title: "Oops...",
              text: "Something went wrong !!!",
            });
          }
        });
    },
  },
};
</script>
