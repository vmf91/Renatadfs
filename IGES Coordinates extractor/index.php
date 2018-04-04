<?php
if($_SERVER["REQUEST_METHOD"] == "POST"){
	$target_dir = "uploads/";
	$filename = "input.igs";
	$target_file = $target_dir . $filename;
	$uploadOk = 1;
	$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));

	// Check file size
	if ($_FILES["dataset"]["size"] > 500000) {
	    echo "Sorry, your file is too large.";
	    $uploadOk = 0;
	}
	// Allow certain file formats
	if($imageFileType != "igs" && $imageFileType != "iges") {
	    echo "Sorry, only .IGS and .IGES files are allowed.";
	    $uploadOk = 0;
	}
	// Check if $uploadOk is set to 0 by an error
	if ($uploadOk == 0) {
	    echo "Sorry, your file was not uploaded.";
	// if everything is ok, try to upload file
	} else {
		// Remove previous files
		if(file_exists($target_file)){
			unlink($target_file);
		}
		if(file_exists('uploads/out.csv')){
			unlink('uploads/out.csv');
		}
		
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
<title>IGES Coordinates extractor</title>
<body>
	<h2>IGES Coordinates extractor</h2>
	<form method="POST" action="" enctype="multipart/form-data">
		<input type="file" name="dataset" accept=".igs,.iges" />
		<button type="submit">Submit</button>
	</form>
</body>
</html>