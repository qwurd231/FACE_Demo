<template>
  <div
    class="container"
    style="position: absolute; top: 40%; left: 50%; transform: translate(-50%, -50%)"
  >
    <div class="row justify-content-center">
      <div class="col-md-6">
        <form>
          <div class="form-group">
            <label for="exampleFormControlTextarea">Enter Your Text</label>
            <textarea
              class="form-control"
              id="exampleFormControlTextarea"
              rows="8"
              style=""
            ></textarea>
          </div>
          <button
            type="submit"
            class="btn btn-primary"
            id="submit"
            style="position: relative; left: 100%; transform: translateX(-100%)"
          >
            Submit
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup></script>
