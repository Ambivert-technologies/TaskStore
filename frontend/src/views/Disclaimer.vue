<template>
  <div class="card">
    <div class="card-header pb-0 px-3">
      <h4 class="mb-0 mx-4">Disclaimer for Task Store</h4>
    </div>
    <div class="card-body">
      <ul class="list-group">
        <li
          class="
            list-group-item
            border-0
            d-flex
            mb-2
            bg-gray-100
            border-radius-lg
          "
        >
          <div class="d-flex flex-column">
            <p>
              If you require any more information or have any questions about
              our site's disclaimer, please feel free to contact us by email at
              hello@taskstore.in.
            </p>

            <h6>Disclaimers for TaskStore.in</h6>

            <p>
              All the information on this website - http://www.taskstore.in/ -
              is published in good faith and for general information purpose
              only. TaskStore.in does not make any warranties about the
              completeness, reliability and accuracy of this information. Any
              action you take upon the information you find on this website
              (TaskStore.in), is strictly at your own risk. TaskStore.in will
              not be liable for any losses and/or damages in connection with the
              use of our website.
            </p>

            <p>
              From our website, you can visit other websites by following
              hyperlinks to such external sites. While we strive to provide only
              quality links to useful and ethical websites, we have no control
              over the content and nature of these sites. These links to other
              websites do not imply a recommendation for all the content found
              on these sites. Site owners and content may change without notice
              and may occur before we have the opportunity to remove a link
              which may have gone 'bad'.
            </p>

            <p>
              Please be also aware that when you leave our website, other sites
              may have different privacy policies and terms which are beyond our
              control. Please be sure to check the Privacy Policies of these
              sites as well as their "Terms of Service" before engaging in any
              business or uploading any information.
            </p>

            <h6>Consent</h6>

            <p>
              By using our website, you hereby consent to our disclaimer and
              agree to its terms.
            </p>

            <h6>Update</h6>

            <p>
              Should we update, amend or make any changes to this document,
              those changes will be prominently posted here.
            </p>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "Disclaimer",
  mounted() {
    this.role = localStorage.getItem("role");
  },
};
</script>
