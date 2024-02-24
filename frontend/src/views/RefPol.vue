<template>
  <div class="card">
    <div class="card-header pb-0 px-3">
      <h4 class="mb-0 mx-4">Refund and Cancellation Policy</h4>
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
            <p>Our focus is complete customer satisfaction. In the event, if you
            are displeased with the services provided, we will refund back the
            money, provided the reasons are genuine and proved after
            investigation. Please read the fine prints of each deal before
            buying it, it provides all the details about the services or the
            product you purchase. In case of dissatisfaction from our services,
            clients have the liberty to cancel their projects and request a
            refund from us. Our Policy for the cancellation and refund will be
            as follows:</p>
            <h6>Cancellation Policy</h6>
            For Cancellations please contact
            the us via email. Requests received later than 15 business days
            prior to the end of the current service period will be treated as
            cancellation of services for the next service period. 
            <h6 class="mt-3">Refund Policy</h6>
            <p>We will try our best to create the suitable design concepts for our
            clients. In case any client is not completely satisfied with our
            products we can provide a refund. If paid by credit card, refunds
            will be issued to the original credit card provided at the time of
            purchase and in case of payment gateway name payments refund will be
            made to the same account.</p>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "RefPol",
  mounted() {
    this.role = localStorage.getItem("role");
  },
};
</script>
