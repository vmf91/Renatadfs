<?php
if($_SERVER["REQUEST_METHOD"] == "POST"){
	$target_dir = "uploads/";
	$filename = "data.csv";
	$target_file = $target_dir . $filename;
	$uploadOk = 1;
	$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));

	// Check file size
	if ($_FILES["dataset"]["size"] > 500000) {
	    echo "Sorry, your file is too large.";
	    $uploadOk = 0;
	}
	// Allow certain file formats
	if($imageFileType != "csv") {
	    echo "Sorry, only .CSV files are allowed.";
	    $uploadOk = 0;
	}
	// Check if $uploadOk is set to 0 by an error
	if ($uploadOk == 0) {
	    echo "Sorry, your file was not uploaded.";
	// if everything is ok, try to upload file
	} else {
	    if (move_uploaded_file($_FILES["dataset"]["tmp_name"], $target_file)) {
	        echo "The file ". basename( $_FILES["dataset"]["name"]). " has been uploaded.";

	        exec('python process.py');
			sleep(1);
			header("Location: uploads/out.csv"); /* Redirect browser */
			exit();
	    } else {
	        echo "Sorry, there was an error uploading your file.";
	    }
	}
}
?>

<!DOCTYPE html>
<html>
<title>Teeth position on digital models</title>
<body>
	<h2>Teeth position on digital models</h2>
	<form method="POST" action="" enctype="multipart/form-data">
		<input type="file" name="dataset" accept=".csv" />
		<button type="submit">Submit</button>
	</form>

	<p><a href="template.csv">Click here</a> to download a template</p>
</body>
</html>