<?php 
function skit($samples,$targets,$predict,$debug=false){
	 
	if($debug){
		echo "<pre>";
		var_dump("samples",$samples,"targets",$targets,"predict",$predict);
		echo "</pre>";
	}
	$json_encode=json_encode($samples);
	$json_encode=urlencode($json_encode);

	$targets=json_encode($targets);
	$targets=urlencode($targets);

	
	$predict=json_encode($predict);
	$predict=urlencode($predict);
 
	$url="http://fillwithyourip:8080/?x={$json_encode}&y={$targets}&predict={$predict}"; 
	$terserah=file_get_contents($url);

	$isi=explode("[[",$terserah)[1];
	$isi=explode("]]",$isi)[0];
	$isi=(float)$isi;
	
	if($debug){
		echo "<pre>";
		var_dump($isi);
		echo "</pre>";
	}
	return $isi;
}

//call the function here
$samples = [[13.4,13.4,36.2,30.1,60.3,60.3]];
$targets = [[10.7]];
$predict = [[13.6,13.6,37.6,30.5,61.9,61.9]];
$prediction=skit($samples1,$targets1,[$predict[$i]]);
echo "Your prediction is: " . $prediction;
?>
