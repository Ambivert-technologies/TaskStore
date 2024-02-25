<template>
  <div class="container top-0 position-sticky z-index-sticky">
    
  </div>
  <main class="mt-0 main-content main-content-bg">
    <section>
        <div class="container">
            <div class="center">
                <p>Loading data...</p>
                <div class="d-flex justify-content-center text-align-items-center">
                    <div class="spinner-grow text-primary" role="status">
                    <span class="sr-only">Loading...</span>
                    </div>
                    <div class="spinner-grow text-secondary" role="status">
                    <span class="sr-only">Loading...</span>
                    </div>
                    <div class="spinner-grow text-success" role="status">
                    <span class="sr-only">Loading...</span>
                    </div>
                    <div class="spinner-grow text-danger" role="status">
                    <span class="sr-only">Loading...</span>
                    </div>
                    <div class="spinner-grow text-warning" role="status">
                    <span class="sr-only">Loading...</span>
                    </div>
                    <div class="spinner-grow text-info" role="status">
                    <span class="sr-only">Loading...</span>
                    </div>
                    <div class="spinner-grow text-light" role="status">
                    <span class="sr-only">Loading...</span>
                    </div>
                    <div class="spinner-grow text-dark" role="status">
                    <span class="sr-only">Loading...</span>
                    </div>
                </div>
            </div>
        </div>
    </section>
  </main>
</template>

<script>
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
  name: "AfterPayment",
  components: {
  },

  data(){
    return{
      
    }
  },

  mounted() {
    var oId = this.$route.query.order_id;
    var oTok = this.$route.query.order_token;
    // localStorage.removeItem("pSid");
    var paySid = localStorage.getItem("pSid");
    var url =
          "https://yh3aetiwp1.execute-api.ap-south-1.amazonaws.com/dev/app/v1/users/checkPayment";
    // var url="http://127.0.0.1:8000/app/v1/users/checkPayment";
    const data = new FormData();
    data.append("oId", oId);
    data.append("oTok", oTok);
    data.append("paySid", paySid);
    data.append("uid", localStorage.getItem("uid"));
    appInstance.axios
      .post(url, data, { headers: { "Content-Type": "application/json" } })
      .then((res) => {
        if (res.data["msg"] === "done") {
          this.$router.push("/script-list");
        }else if(res.data["msg"] === "notdone"){
          alert("Your payment succesfull, but script not added, please contact us via mail...");
        }else{
          Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Can't generate the payment link at this moment, try later...",
          });
        }
      });
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

<style>
.container { 
  height: 200px;
  position: relative;
}

.center {
  margin: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}
</style>
