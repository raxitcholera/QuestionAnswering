<?
set_time_limit(200);
$question = str_replace(' ', '%20',$_REQUEST["uQuestion"]);

$output = array();
$command = "python performances.py ".$question;
//echo $command;
exec($command, $output);

//var_dump( $output);
if(!empty($output))
{
?>
The Question asked :-  '<?=$_REQUEST["uQuestion"]?>' <br/>
The System Answers :-  <?=$output[0]?> <br/>
Was the answer Correct? <br/>
<input type="radio" name="anscorrect" value="Yes" onclick="hidetopfive();" /> Yes  
<input type="radio" name="anscorrect" value="No" onclick="showtopfive();"/> No  
<input type="radio" name="anscorrect" value="Partialy" onclick="showtopfive();"/> Partialy Correct  
<br/>
<div id="topfive" style="display:none;" >
<br/>
<table width="400px" height="180px" border="0" align="center">
	<tr>
		<td>First Ranked</td>
		<td><?=$output[2]?></td>
	</tr>
	<tr>
		<td>Second Ranked</td>
		<td><?=$output[3]?></td>
	</tr>
	<tr>
		<td>Third Ranked</td>
		<td><?=$output[4]?></td>
	</tr>
	<tr>
		<td>Fourth Ranked</td>
		<td><?=$output[5]?></td>
	</tr>
	<tr>
		<td>Fifth Ranked</td>
		<td><?=$output[6]?></td>
	</tr>
</table>
</div>
Time taken for answer :-<?=$output[1]?><br/>
<?
}
else
{
	echo "There seems to be some problem with the question asked please try again.";
}
?>
<script type="text/javascript">
function showtopfive()
{
	document.getElementById("topfive").style.display="block";
}
function hidetopfive()
{
	document.getElementById("topfive").style.display="none";
}
</script>