<template>
  <div class="card">
    <div class="card-body">
      <h5 class="card-title mb-3">Provide Script Details</h5>
      <form @submit="formSubmit">
        <div class="row">
          <div class="col-md-4">
            <div class="form-group">
              <label for="scNm">Script Name</label>
              <input
                type="text"
                class="form-control"
                id="scNm"
                v-model="scriptDetails['name']"
                placeholder="Enter your script name"
                required
              />
            </div>
          </div>
           <div class="col-md-4">
            <div class="form-group">
              <label for="price">Price (INR)</label>
              <input
                type="text"
                class="form-control"
                id="price"
                v-model="scriptDetails['price']"
                placeholder="Example:- 4"
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
                v-model="scriptDetails['author']"
                placeholder="Type author name"
                required
              />
            </div>
          </div>

          <div class="col-md-4">
            <div class="form-group">
              <label for="cat">Select Category</label>
              <select class="form-control form-control-lg" id="cat" required>
                <option :value="scriptDetails['cat']" disabled selected>{{scriptDetails['cat']}}</option>
                <option v-for="item in catList" :key="item.id" :value="item">{{item}}</option>
              </select>
            </div>
          </div>
          <div class="col-md-4">
            <div class="form-group">
              <label for="lang">Developing Language</label>
              <select class="form-control form-control-lg" id="lang" required>
                <option :value="scriptDetails['lang']" disabled selected>{{scriptDetails['lang']}}</option>
                <option v-for="item in langList" :key="item.id" :value="item">{{item}}</option>
              </select>
            </div>
          </div>
          <div class="col-md-4">
            <div class="form-group">
              <label for="os">Select OS</label>
              <select class="form-control form-control-lg" id="os" required>
                <option :value="scriptDetails['os']" disabled selected>{{scriptDetails['os']}}</option>
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
              <label for="scFl">Upload Script &nbsp;&nbsp;&nbsp;&nbsp;
                <a target="_blank" style="font-size: 16px; font-weight: bold; color: black;" :href="`https://scriptstore-fastapi.s3.ap-south-1.amazonaws.com/All_Script/ScriptID_`+this.routeId+`/Script/`+scriptDetails['file']"><i class="fa fa-eye"></i></a>
              </label>
              <input type="file" class="form-control" id="scFl"/>
            </div>
          </div>
          <div class="col-md-6">
            <div class="form-group">
              <label for="scIc">Upload Script Icon &nbsp;&nbsp;&nbsp;&nbsp;
                <a target="_blank" style="font-size: 16px; font-weight: bold; color: black;" :href="`https://scriptstore-fastapi.s3.ap-south-1.amazonaws.com/All_Script/ScriptID_`+this.routeId+`/ScriptIcon/`+scriptDetails['icon']"><i class="fa fa-eye"></i></a>
              </label>
              <input type="file" class="form-control" id="scIc" />
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-md-6">
            <div class="form-group">
              <label for="scDp">Upload Dependency &nbsp;&nbsp;&nbsp;&nbsp; 
                <a target="_blank" style="font-size: 16px; font-weight: bold; color: black;" :href="`https://scriptstore-fastapi.s3.ap-south-1.amazonaws.com/All_Script/ScriptID_`+this.routeId+`/Dependency/`+scriptDetails['dep']"><i class="fa fa-eye"></i></a>
              </label>
              <input type="file" class="form-control" id="scDp" :value="scriptDetails['Dependency']"/>
            </div>
          </div>
          <div class="col-md-6">
            <div class="form-group">
              <label for="youtubelink">Youtube Link</label>
              <input type="text" v-model="scriptDetails['youtubelink']" class="form-control" id="youtubelink" required />
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
  name: "EditScript",
  data() {
    return {
      catList: [],
      langList: [],
      scriptDetails: {
          "name": "",
          "author": "",
          "cat": "",
          "os": "",
          "lang": "",
          "desc": "",
          "script": "",
          "icon": "",
          "youtubelink": "",
          "price": "",
          "dep": "",
      },
      userId: "",
      pleaseWait: false,
      routeId: "",
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

        // DO FROM HERE, ABOVE FOR SELECT TAG
        var form_data = new FormData();
        form_data.append("id", this.$route.query.id);
        this.routeId = this.$route.query.id;
        appInstance.axios
        .post("https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/scriptDetailsForEdit", form_data, {
        // .post("http://127.0.0.1:8000/app/v1/users/scriptDetailsForEdit", form_data, {
          headers: { "Content-Type": "application/json" },
        })
          .then((res) => {
            if (res.data["msg"] === true) {
              var jsonData = res.data["data"];
              console.log(jsonData);

              this.scriptDetails['name'] = jsonData['ScriptName'];
              this.scriptDetails['author'] = jsonData['AuthorName'];
              this.scriptDetails['cat'] = jsonData['cat'];
              this.scriptDetails['os'] = jsonData['os'];
              this.scriptDetails['lang'] = jsonData['lang'];
              this.scriptDetails['desc'] = jsonData['Description'];
              document.getElementById("scDs").value = this.scriptDetails['desc'];
              this.scriptDetails['script'] = jsonData['ScriptFileName'];
              this.scriptDetails['icon'] = jsonData['ScriptIcon'];
              this.scriptDetails['youtubelink'] = jsonData['youtubelink'];
              this.scriptDetails['price'] = jsonData['price'];
              this.scriptDetails['dep'] = jsonData['Dependency'];
              this.scriptDetails['icon'] = jsonData['ScriptIcon'];
              this.scriptDetails['file'] = jsonData['ScriptFileName'];
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

      var checkPrice = parseFloat(document.getElementById("price").value);
      // alert(checkPrice)
      // var isNumber = /^\d+\.\d+$/.test(checkPrice);
      if(isNaN(checkPrice) === false){
        this.pleaseWait = true;
        const form_data = new FormData();

        form_data.append("sid", this.$route.query.id);

        var price = document.getElementById("price").value;
        form_data.append("price", price);

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

        var youtube = document.getElementById("youtubelink").value;
        form_data.append("youtubelink", youtube);

        var scriptFile = document.getElementById("scFl").files[0];
        if (scriptFile != undefined){
          form_data.append("scriptFile", scriptFile);
        }

        var scriptIcon = document.getElementById("scIc").files[0];
        if (scriptIcon != undefined){
          form_data.append("scriptIcon", scriptIcon);
        }

        var upldDep = document.getElementById("scDp").files[0];
        if(upldDep != undefined){
          form_data.append("upldDep", upldDep);
        }

        form_data.append("userId", this.userId);

        appInstance.axios
          .post("https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/edit_script_upload", form_data, {
          // .post("http://127.0.0.1:8000/app/v1/users/edit_script_upload", form_data, {
            headers: { "Content-Type": "application/json" },
          })
          .then((res) => {
            if (res.data["msg"] === true) {
              this.pleaseWait = false;
              Swal.fire(
                "Successfully Updated !!!",
                "Your script successfully updated...",
                "success"
              );
              this.$router.push("/reqscript");
            } else {
              this.pleaseWait = false;
              Swal.fire({
                icon: "error",
                title: "Invalid Price !!!",
                text: "Price can be only numbers",
              });
            }
          });
      }else{
        Swal.fire({
          icon: "error",
          title: "Oops...",
          text: "Price is invalid...",
        });
      }
    },
  },
};
</script>
