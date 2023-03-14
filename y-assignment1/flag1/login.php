<!doctype html>
<html lang="en">

<?php

require("head-include.php");
echo_head("Login");

?>

      <div class="sidebar-wrapper">
        <ul class="nav">
          <li class="nav-item active  ">
            <a class="nav-link" href="#">
              <i class="material-icons">lock</i>
              <p>Login</p>
            </a>
          </li>
          <!-- your sidebar here -->
        </ul>
      </div>
    </div>
    <div class="main-panel">
      <!-- Navbar -->
      <nav class="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top ">
        <div class="container-fluid">
          <div class="navbar-wrapper">
            <a class="navbar-brand" href="javascript:;">Login</a>
          </div>
          <button class="navbar-toggler" type="button" data-toggle="collapse" aria-controls="navigation-index" aria-expanded="false" aria-label="Toggle navigation">
            <span class="sr-only">Toggle navigation</span>
            <span class="navbar-toggler-icon icon-bar"></span>
            <span class="navbar-toggler-icon icon-bar"></span>
            <span class="navbar-toggler-icon icon-bar"></span>
          </button>
        </div>
      </nav>
      <!-- End Navbar -->
      <div class="content">
        <div class="container-fluid">
          <form class="navbar-form" action="auth.php" method="post">
            <div class="input-group no-border">
              <input type="text" class="form-control" placeholder="Username" name="user">
              <br/>
              <input type="password" class="form-control" placeholder="Password" name="pass">
              <button type="submit" class="btn btn-white btn-round btn-just-icon">
                <i class="material-icons">lock</i>
                <div class="ripple-container"></div>
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</body>

</html>