<template>
  <nav
    class="navbar navbar-dark bg-dark fixed-top"
    style="display: flex; margin-top: 0; margin-left: 0"
  >
    <div class="container-fluid" style="display: flex">
      <a class="navbar-brand" href="#">FACE Demo</a>
      <form class="d-flex" role="search" style="padding-left: 50%">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" />
        <button class="btn btn-success" type="submit">Search</button>
      </form>
      <div>
        <RouterLink to="/settings">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="36"
            height="36"
            color="white"
            fill="currentColor"
            class="bi bi-gear-wide-connected"
            viewBox="-4 -4 24 24"
            preserveAspectRatio="xMidYMid meet"
          >
            <path
              d="M7.068.727c.243-.97 1.62-.97 1.864 0l.071.286a.96.96 0 0 0 1.622.434l.205-.211c.695-.719 1.888-.03 1.613.931l-.08.284a.96.96 0 0 0 1.187 1.187l.283-.081c.96-.275 1.65.918.931 1.613l-.211.205a.96.96 0 0 0 .434 1.622l.286.071c.97.243.97 1.62 0 1.864l-.286.071a.96.96 0 0 0-.434 1.622l.211.205c.719.695.03 1.888-.931 1.613l-.284-.08a.96.96 0 0 0-1.187 1.187l.081.283c.275.96-.918 1.65-1.613.931l-.205-.211a.96.96 0 0 0-1.622.434l-.071.286c-.243.97-1.62.97-1.864 0l-.071-.286a.96.96 0 0 0-1.622-.434l-.205.211c-.695.719-1.888.03-1.613-.931l.08-.284a.96.96 0 0 0-1.186-1.187l-.284.081c-.96.275-1.65-.918-.931-1.613l.211-.205a.96.96 0 0 0-.434-1.622l-.286-.071c-.97-.243-.97-1.62 0-1.864l.286-.071a.96.96 0 0 0 .434-1.622l-.211-.205c-.719-.695-.03-1.888.931-1.613l.284.08a.96.96 0 0 0 1.187-1.186l-.081-.284c-.275-.96.918-1.65 1.613-.931l.205.211a.96.96 0 0 0 1.622-.434zM12.973 8.5H8.25l-2.834 3.779A4.998 4.998 0 0 0 12.973 8.5m0-1a4.998 4.998 0 0 0-7.557-3.779l2.834 3.78zM5.048 3.967l-.087.065zm-.431.355A4.98 4.98 0 0 0 3.002 8c0 1.455.622 2.765 1.615 3.678L7.375 8zm.344 7.646.087.065z"
            />
          </svg>
        </RouterLink>
      </div>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="offcanvas"
        data-bs-target="#offcanvasDarkNavbar"
        aria-controls="offcanvasDarkNavbar"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div
        class="offcanvas offcanvas-end text-bg-dark"
        tabindex="-1"
        id="offcanvasDarkNavbar"
        aria-labelledby="offcanvasDarkNavbarLabel"
      >
        <div class="offcanvas-header" style="margin-left: 1.5rem; margin-top: 1rem">
          <button
            type="button"
            class="btn-close btn-close-white"
            data-bs-dismiss="offcanvas"
            aria-label="Close"
          ></button>
        </div>
        <div class="offcanvas-body">
          <ul
            class="navbar-nav justify-content-end flex-grow-1 pe-3"
            style="display: flex; margin-left: 1.5rem"
          >
            <li style="display: flex; justify-content: center; align-items: center; height: 200px">
              <img
                src="https://www.w3schools.com/howto/img_avatar.png"
                alt="Avatar"
                class="nav-item"
                style="height: 200px; width: 200px; margin-right: 10%; border-radius: 150px"
              />
            </li>
          </ul>
          <div
            class="list-group"
            style="
              margin-top: 10%;
              margin-bottom: 15%;
              display: flex;
              flex-direction: column;
              justify-content: center;
              align-items: center;
            "
          >
            <RouterLink
              to="/"
              class="list-group-item list-group-item-action list-group-item-secondary"
              >Home</RouterLink
            >
            <RouterLink
              to="/history"
              class="list-group-item list-group-item-action list-group-item-secondary"
              >History</RouterLink
            >
            <RouterLink
              to="/settings"
              class="list-group-item list-group-item-action list-group-item-secondary"
              >Settings</RouterLink
            >
          </div>
          <hr />

          <button
            type="button"
            class="btn btn-danger"
            style="
              width: 70%;
              display: flex;
              justify-content: center;
              align-items: center;
              margin-left: 15%;
              margin-top: 10%;
              height: 10%;
            "
          >
            <RouterLink to="/logout" style="color: white; font-size: 1.5rem">Logout</RouterLink>
          </button>
        </div>
      </div>
    </div>
  </nav>
</template>

<script lang="ts">
declare module '@/components/header/TopBar.vue' {}
</script>

<style scoped>
.list-group-item-secondary {
  outline-color: azure;
  color: antiquewhite;
  background-color: #343a40;
  width: 90%;
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: sans-serif;
  font-size: 1.5rem;
  border-radius: 10px;
  margin-bottom: 5%;
}

.list-group-item-secondary:hover {
  background-color: #1b2a38;
  color: aliceblue;
}
</style>
