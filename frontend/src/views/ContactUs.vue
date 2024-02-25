<template>
  <div class="card">
    <div class="card-body">
      <div class="container-fluid pt-3">
        <div class="row removable">
          <div class="col-lg-5 d-flex">
            <div class="bg-gradient-dark my-lg-3 border-radius-md">
              <img
                src="https://demos.creative-tim.com/soft-ui-design-system-pro/assets/img/shapes/waves-white.svg"
                alt="pattern-lines"
                class="position-absolute start-0 top-0 h-100 opacity-6"
              />
              <div class="card-body p-5 position-relative">
                <h3 class="text-white">Task Store</h3>
                <p class="text-white opacity-8 mb-4">
                  Fill up the form and our Team will get back to you within 24
                  hours.
                </p>
                <!-- <div class="d-flex p-2 text-white">
                  <div>
                    <i class="fas fa-phone text-sm" aria-hidden="true"></i>
                  </div>
                  <div class="ps-3">
                    <span class="text-sm opacity-8">+91 9960160016</span>
                  </div>
                </div> -->
                <div class="d-flex p-2 text-white">
                  <div>
                    <i class="fas fa-envelope text-sm" aria-hidden="true"></i>
                  </div>
                  <div class="ps-3">
                    <span class="text-sm opacity-8">hello@taskstore.in</span>
                  </div>
                </div>
                <div class="d-flex p-2 text-white">
                  <div>
                    <i
                      class="fas fa-map-marker-alt text-sm"
                      aria-hidden="true"
                    ></i>
                  </div>
                  <div class="ps-3">
                    <span class="text-sm opacity-8">India<br /> </span>
                  </div>
                </div>
                <div class="mt-4">
                  <button
                    type="button"
                    class="btn btn-icon-only btn-link text-white btn-lg mb-0"
                    data-toggle="tooltip"
                    data-placement="bottom"
                    data-original-title="Log in with Facebook"
                  >
                    <i class="fab fa-facebook" aria-hidden="true"></i>
                  </button>
                  <button
                    type="button"
                    class="btn btn-icon-only btn-link text-white btn-lg mb-0"
                    data-toggle="tooltip"
                    data-placement="bottom"
                    data-original-title="Log in with Twitter"
                  >
                    <i class="fab fa-twitter" aria-hidden="true"></i>
                  </button>
                  <button
                    type="button"
                    class="btn btn-icon-only btn-link text-white btn-lg mb-0"
                    data-toggle="tooltip"
                    data-placement="bottom"
                    data-original-title="Log in with Dribbble"
                  >
                    <i class="fab fa-dribbble" aria-hidden="true"></i>
                  </button>
                  <button
                    type="button"
                    class="btn btn-icon-only btn-link text-white btn-lg mb-0"
                    data-toggle="tooltip"
                    data-placement="bottom"
                    data-original-title="Log in with Instagram"
                  >
                    <i class="fab fa-instagram" aria-hidden="true"></i>
                  </button>
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-7">
            <form
              id="contact-form"
              class="mb-4"
              method="post"
              autocomplete="off"
            >
              <div class="card-body position-relative p-3 ps-0">
                <div class="row mt-4">
                  <div class="col-md-6">
                    <label>First name</label>
                    <div class="input-group mb-4">
                      <input
                        class="form-control"
                        placeholder="Enter your first name"
                        aria-label="First Name..."
                        type="text"
                      />
                    </div>
                  </div>
                  <div class="col-md-6 ps-2">
                    <label>Last name</label>
                    <div class="input-group mb-4">
                      <input
                        type="text"
                        class="form-control"
                        placeholder="Enter your last name"
                        aria-label="Last Name..."
                      />
                    </div>
                  </div>
                </div>
                <div>
                  <label>Email address</label>
                  <div class="input-group mb-4">
                    <input
                      type="email"
                      class="form-control"
                      placeholder="Enter your email address"
                    />
                  </div>
                </div>
                <!-- <label>What are you interested on?</label>
                            <div class="d-flex">
                                <div>
                                    <div class="form-check me-3">
                                        <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1" checked="">
                                        <label class="form-check-label" for="flexRadioDefault1">
                                            Design
                                        </label>
                                    </div>
                                </div>
                                <div>
                                    <div class="form-check me-3">
                                        <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2">
                                        <label class="form-check-label" for="flexRadioDefault2">
                                            Development
                                        </label>
                                    </div>
                                </div>
                                <div>
                                    <div class="form-check me-3">
                                        <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault3">
                                        <label class="form-check-label" for="flexRadioDefault3">
                                            Support
                                        </label>
                                    </div>
                                </div>
                                <div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault4">
                                        <label class="form-check-label" for="flexRadioDefault4">
                                            Other
                                        </label>
                                    </div>
                                </div>
                            </div> -->
                <div class="form-group mt-4">
                  <label>Your message</label>
                  <textarea
                    name="message"
                    class="form-control"
                    id="message"
                    rows="3"
                  ></textarea>
                </div>
                <div class="text-end">
                  <button type="button" class="btn bg-gradient-dark mb-0">
                    Send message
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ContactUs",
};
</script>