import { createRouter, createWebHistory } from "vue-router";
import Dashboard from "@/views/Dashboard.vue";
import Tables from "@/views/Tables.vue";
import Billing from "@/views/Billing.vue";
import VirtualReality from "@/views/VirtualReality.vue";
import Profile from "@/views/Profile.vue";
import Rtl from "@/views/Rtl.vue";
import SignIn from "@/views/SignIn.vue";
import SignUp from "@/views/SignUp.vue";
import ScriptDetailsUserSide from "@/views/ScriptDetailsUserSide.vue";
import Pnp from "@/views/Pnp.vue";
import Tnc from "@/views/Tnc.vue";
import Howtoinstall from "@/views/Howtoinstall.vue";
import ContactUs from "@/views/ContactUs.vue";
import Changepwd from "@/views/Changepwd.vue";

// My Added
import ScriptList from "@/views/ScriptList.vue";
import SavedScripts from "@/views/SavedScripts.vue";
import UploadScript from "@/views/UploadScript.vue";
import ReqScript from "@/views/ReqScript.vue";
import ScriptDetails from "@/views/ScriptDetails.vue";
import EditScript from "@/views/EditScript.vue";
import ScriptCat from "@/admin/ScriptCat.vue";
import ScriptLang from "@/admin/ScriptLang.vue";
import All_users from "@/admin/All_users.vue";
import ForgotPwd from "@/views/ForgotPwd.vue";
import Disclaimer from "@/views/Disclaimer.vue";
import RefPol from "@/views/RefPol.vue";

import Paytm from "@/views/Paytm.vue";
import ErrorPaytm from "@/views/ErrorPaytm.vue";
import AfterPayment from "@/views/AfterPayment.vue";
import checkUI from "@/views/checkUI.vue";
import PostComments from "@/views/Comments/PostComments.vue";

const routes = [
  {
    path: "/",
    name: "/",
    redirect: "/script-list",
  },
  {
    path: "/Paytm",
    name: "Paytm",
    component: Paytm,
  },
  {
    path: "/checkUI",
    name: "checkUI",
    component: checkUI,
  },
  {
    path: "/AfterPayment",
    name: "AfterPayment",
    component: AfterPayment,
  },
  {
    path: "/ErrorPaytm",
    name: "ErrorPaytm",
    component: ErrorPaytm,
  },
  {
    path: "/all_users",
    name: "All Users",
    component: All_users,
  },
  {
    path: "/how-to-install",
    name: "how-to-install",
    component: Howtoinstall,
  },
  {
    path: "/forgot-pwd",
    name: "Forgot-Password",
    component: ForgotPwd,
  },
  {
    path: "/contact-us",
    name: "contact-us",
    component: ContactUs,
  },
  {
    path: "/Disclaimer",
    name: "Disclaimer",
    component: Disclaimer,
  },
  {
    path: "/RefPol",
    name: "RefPol",
    component: RefPol,
  },
  {
    path: "/change-pwd",
    name: "change-pwd",
    component: Changepwd,
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: Dashboard,
  },
  {
    path: "/script-list",
    name: "Task Store",
    component: ScriptList,
  },
  {
    path: "/script-edit",
    name: "Edit Script",
    component: EditScript,
  },
  {
    path: "/reqscript",
    name: "Requests Store",
    component: ReqScript,
  },
  {
    path: "/script-details",
    name: "TaskDetails",
    component: ScriptDetails,
  },
  {
    path: "/script-details-us",
    name: "Task Details",
    component: ScriptDetailsUserSide,
  },
  {
    path: "/pnp",
    name: "Privacy & Policy",
    component: Pnp,
  },
  {
    path: "/tnc",
    name: "T&C",
    component: Tnc,
  },
  {
    path: "/saved-sc",
    name: "SavedScripts",
    component: SavedScripts,
  },
  {
    path: "/script-cat",
    name: "Script Category",
    component: ScriptCat,
  },
  {
    path: "/script-lang",
    name: "Script Language",
    component: ScriptLang,
  },
  {
    path: "/tables",
    name: "Tables",
    component: Tables,
  },
  {
    path: "/billing",
    name: "Billing",
    component: Billing,
  },
  {
    path: "/virtual-reality",
    name: "Virtual Reality",
    component: VirtualReality,
  },
  {
    path: "/profile",
    name: "Profile",
    component: Profile,
  },
  {
    path: "/rtl-page",
    name: "Rtl",
    component: Rtl,
  },
  {
    path: "/sign-in",
    name: "Sign In",
    component: SignIn,
  },
  {
    path: "/sign-up",
    name: "Sign Up",
    component: SignUp,
  },
  // Not Done yet below
  {
    path: "/upload-script",
    name: "UploadScript",
    component: UploadScript,
  },
  {
    path: "/def",
    name: "def",
    component: SignUp,
  },
  {
    path: "/postrequest",
    name: "postrequest",
    component: PostComments,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  linkActiveClass: "active",
});

export default router;
