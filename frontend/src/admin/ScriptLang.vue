<template>
  <div class="row removable mb-4">
    <div class="col-12">
      <div class="card mb-4">
        <div class="card-header pb-0">
          <h6 class="mb-1">Add Here</h6>
          <p class="text-sm">Task Language</p>
        </div>
        <div class="card-body py-0">
          <div class="row">
            <!-- Dialog For Script Details -->
            <div class="col-md-4">
              <!-- <button type="button" class="btn btn-block bg-gradient-primary mb-3" data-bs-toggle="modal" data-bs-target="#modal-default">Default</button> -->
              <div
                class="modal fade"
                id="modal-default"
                tabindex="-1"
                role="dialog"
                aria-labelledby="modal-default"
                aria-hidden="true"
              >
                <div
                  class="modal-dialog modal- modal-dialog-centered modal-"
                  role="document"
                >
                  <div class="modal-content">
                    <div class="modal-header">
                      <h6 class="modal-title" id="modal-title-default">
                        Edit Language
                      </h6>
                      <button
                        type="button"
                        class="btn-close"
                        data-bs-dismiss="modal"
                        aria-label="Close"
                      >
                        <span aria-hidden="true">×</span>
                      </button>
                    </div>
                    <div class="modal-body">
                      <!-- Editing Form -->
                      <form @submit="editCatFormSubmit">
                        <div class="row">
                          <div class="col-md-6">
                            <div class="form-group">
                              <label for="cat">Language</label>
                              <input
                                type="text"
                                class="form-control"
                                v-model="elang"
                                placeholder="Edit here..."
                                required
                              />
                            </div>
                          </div>
                        </div>
                        <button
                          type="submit"
                          class="btn bg-gradient-warning btn-lg"
                        >
                          Save Changes
                        </button>
                      </form>
                      <!-- End Editing Forms -->
                    </div>
                    <div class="modal-footer">
                      <button
                        type="button"
                        class="btn btn-outline-warning"
                        data-bs-dismiss="modal"
                      >
                        Close
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!-- End Dialog -->

            <div class="col-xl-12 col-md-12 mb-4">
              <div class="card col-md-6 card-blog card-plain mycard">
                <div class="px-1 pb-0 card-body">
                  <form @submit="formSubmit">
                    <div class="row">
                      <div class="col-md-6">
                        <div class="form-group">
                          <label for="lang">Language Name</label>
                          <input
                            type="text"
                            class="form-control"
                            id="lang"
                            placeholder="Enter the new language..."
                            required
                          />
                        </div>
                      </div>
                    </div>
                    <button
                      type="submit"
                      class="btn bg-gradient-warning btn-lg"
                    >
                      Submit
                    </button>
                  </form>
                </div>
              </div>

              <div class="card col-md-6 card-blog card-plain mycard">
                <div class="px-1 pb-0 card-body">
                  <div class="table-responsive p-0">
                    <table class="table mb-0">
                      <thead>
                        <tr>
                          <th
                            class="
                              text-uppercase text-secondary text-xs
                              font-weight-bolder
                              heading
                            "
                          >
                            Languages
                          </th>
                          <th
                            class="
                              text-center text-uppercase text-secondary text-xs
                              font-weight-bolder
                              heading
                            "
                            colspan="2"
                          >
                            Action
                          </th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="item in langItems" :key="item.id">
                          <td class="align-middle">
                            <p class="text-xs font-weight-bold mb-0 slNo">
                              {{ item["lang"] }}
                            </p>
                          </td>
                          <td class="align-middle text-center cursor-pointer">
                            <p
                              class="font-weight-bold mb-0 slNo"
                              data-bs-toggle="modal"
                              data-bs-target="#modal-default"
                              @click="editCat(item['_id'], item['lang'])"
                            >
                              ✏️
                            </p>
                          </td>
                          <td class="align-middle text-center cursor-pointer">
                            <p
                              class="font-weight-bold mb-0 slNo"
                              @click="delCat(item['_id'])"
                            >
                              🗑️
                            </p>
                          </td>
                        </tr>
                      </tbody>
                    </table>
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
  name: "ScriptLang",
  data() {
    return {
      langItems: [],
      elang: "",
      elangId: ""
    };
  },
  mounted() {
    var loggedIn = localStorage.getItem("loggedIn");
    var role = localStorage.getItem("role");
    if (loggedIn != "true") {
      this.$router.push("/");
    } else {
      if (role != "admin") {
        this.$router.push("/");
      } else {
        appInstance.axios
          .get(
            "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/getLang",
            // "http://127.0.0.1:8000/app/v1/users/getLang",
            {
              headers: { "Content-Type": "application/json" },
            }
          )
          .then((res) => {
            if (res.data["msg"] === true) {
              this.langItems = res.data["data"];
            } else {
              Swal.fire({
                icon: "error",
                title: "Oops...",
                text: "Won't be able to fetch existing category!!!",
              });
            }
          });
      }
    }
  },

  methods: {
    formSubmit(event) {
      event.preventDefault();

      var lang = document.getElementById("lang").value;
      var formData = new FormData();
      formData.append("lang", lang);

      if (lang.trim() != "") {
        appInstance.axios
          .post(
            "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/newScriptlang",
            // "http://127.0.0.1:8000/app/v1/users/newScriptlang",
            formData,
            {
              headers: { "Content-Type": "application/json" },
            }
          )
          .then((res) => {
            if (res.data["msg"] === true) {
              Swal.fire(
                "Successfully added !!!",
                "A new script category successfully added...",
                "success"
              );
              this.mountedAlter();
            } else {
              Swal.fire({
                icon: "error",
                title: "Oops...",
                text: "Something went wrong!!!",
              });
            }
          });
      } else {
        Swal.fire({
          icon: "error",
          title: "Oops...",
          text: "Empty field not allowed...",
        });
      }
    },

    editCat(langId, lang) {
      this.elang = lang;
      this.elangId = langId;
    },

    editCatFormSubmit(event){
      event.preventDefault();
      var formData = new FormData();
      formData.append("elang", this.elang);
      formData.append("elangId", this.elangId);
      appInstance.axios
        .post("https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/editLang", formData, {
        // .post("http://127.0.0.1:8000/app/v1/users/editLang", formData, {
          headers: { "Content-Type": "application/json" },
        })
        .then((res) => {
          if (res.data["msg"] === true) {
            // Swal
            Swal.fire("Successfully Updated !!!",
                "Changes are saved...",
                "success");
            this.mountedAlter();
          } else {
            Swal.fire({
              icon: "error",
              title: "Oops...",
              text: "Can't delete at this moment, try later...",
            });
          }
        });
    },

    delCat(catId) {
      event.preventDefault();
      const formData = new FormData();
      formData.append("langId", catId);

      appInstance.axios
        .post("https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/delLang", formData, {
        // .post("http://127.0.0.1:8000/app/v1/users/delLang", formData, {
          headers: { "Content-Type": "application/json" },
        })
        .then((res) => {
          if (res.data["msg"] === true) {
            // Swal
            Swal.fire("Deleted Successfully!");
            this.mountedAlter();
          } else {
            Swal.fire({
              icon: "error",
              title: "Oops...",
              text: "Can't delete at this moment, try later...",
            });
          }
        });
    },

    mountedAlter() {
      var loggedIn = localStorage.getItem("loggedIn");
      var role = localStorage.getItem("role");
      if (loggedIn != "true") {
        this.$router.push("/");
      } else {
        if (role != "admin") {
          this.$router.push("/");
        } else {
          appInstance.axios
            .get(
              "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/getLang",
              // "http://127.0.0.1:8000/app/v1/users/getLang",
              {
                headers: { "Content-Type": "application/json" },
              }
            )
            .then((res) => {
              if (res.data["msg"] === true) {
                this.langItems = [];
                this.langItems = res.data["data"];
              } else {
                Swal.fire({
                  icon: "error",
                  title: "Oops...",
                  text: "Won't be able to fetch existing category!!!",
                });
              }
            });
        }
      }
    },
  },
};
</script>

<style scoped>
.mycard {
  display: inline-flex;
}
.slNo {
  margin-left: 16px;
}
</style>
