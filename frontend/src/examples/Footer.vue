<template>
  <footer class="py-3 footer">
    <div class="container-fluid">
      <div class="row align-items-center justify-content-lg-between">
        <div class="mb-4 col-lg-6 mb-lg-0">
          <div
            class="text-sm text-center copyright text-muted"
            :class="this.$store.state.isRTL ? 'text-lg-end' : 'text-lg-start'"
          >
          Copyright © {{ new Date().getFullYear() }} TaskStore
          </div>
        </div>
        <div class="col-lg-6">
          <ul
            class="nav nav-footer justify-content-center justify-content-lg-end"
          >
            <li class="nav-item">
              <a
                href="https://www.canva.com/design/DAE7Do2LYAA/QliiS2jwlVsfbWTFvg0K4g/view?utm_content=DAE7Do2LYAA&utm_campaign=designshare&utm_medium=link&utm_source=publishpresent"
                class="nav-link text-muted"
                target="_blank"
                >About Us</a
              >
            </li>
            <li class="nav-item">
              <router-link class="nav-link text-muted" target="_blank" to="contact-us">Contact Us</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link text-muted" target="_blank" to="Disclaimer">Disclaimer</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link text-muted" target="_blank" to="RefPol">Refund Policy</router-link>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "app-footer",
};
</script>
