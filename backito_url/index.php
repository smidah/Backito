<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title> - Backito</title>
  <!-- Bootstrap -->
  <link href="css/bootstrap.min.css" rel="stylesheet">
  <!-- Custom CSS -->
  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css">
  <link href='https://fonts.googleapis.com/css?family=Raleway' rel='stylesheet' type='text/css'>
  <link href='https://fonts.googleapis.com/css?family=Caesar+Dressing' rel='stylesheet' type='text/css'>
  <!-- Favicon -->
  <link rel="icon" href="../favicon.png" />
  <!-- Loading -->
  <script src="js/pace.min.js"></script>
</head>
<body>
  <div class="container-fluid">
    <div class="row" style="background-color: #96281B">
      <div class="col-md-12 entete">
        <h1 style="text-align:center;"><i class="fa fa-cogs"></i> Backito</h1>
      </div>
    </div>
  </div>
  <div class="container">
    <div class="row">
      <div class="col-md-6 insta">
        <h3 style="text-align: center;"><i class="fa fa-gg-circle"></i> Backito</h3><hr style="width: 60%; border-color: #333">
        <div style="overflow-y: scroll; height: 300px; padding: 15px; background-color: #333; color: white; border: none; border-left: 15px solid #7f1e1c; border-radius: 1px;" class="instainv">
          <?php
          $file = fopen("/home/student/backup/.backito","r");

          while(! feof($file))
          {
            echo fgets($file). "<br />";
          }

          fclose($file);
          ?>
        </div>
        <br>
      </div>
      <div class="col-md-offset-1 col-md-5 insta">
        <h3 style="text-align: center;"><i class="fa fa-archive"></i> Backup Files</h3><hr style="width: 60%; border-color: #333">
        <h5 class="col-md-10 col-md-offset-1" style="font-weight: bold;"><?php echo "<i class='fa fa-folder-open-o'></i> backup/" ?></h5>
        <div class="col-md-10 col-md-offset-1 instainv" style="border: none; border-left: 15px solid #7f1e1c; border-radius: 1px; background-color: #333">
          <br>
          <?php
          foreach (scandir("/home/student/backup/") as $key) {
            if ($key == ".." || $key == ".")
              continue;
            else if (is_dir("/home/student/backup/" . $key))
              echo '<a><i class="fa fa-folder-o"></i> ' . $key . "</a><br>";
            else
              echo '<i class="fa fa-file"></i> <span style="color: white; font-weight: bold">' . $key . "</span><br>";
          }
          ?>
          <br>
        </div>
        <br>
      </div>
      <div class="col-md-12 insta">
       <h3 style="text-align: center;"><i class="fa fa-calendar-o"></i> Last Backup : </h3><hr style="width: 60%; border-color: #333">
       <div class="col-md-10 col-md-offset-1 instainv" style="border: none; border-left: 15px solid #7f1e1c; border-radius: 1px; background-color: #333">
        <br>
        <h1 style="color: white"> 
          <?php
          $file = "/home/student/backup/.backito";
          $data = file($file);
          $line = $data[count($data)-1]; 
          echo substr($line, 0, 23)
          ?>
        </h1>
        <br>
      </div>
      <br>
    </div>
  </div>
</div>
</div>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<script src="js/bootstrap.min.js"></script>
</body>
</html>
