<?php

echo "<h1>Teste de autenticação</h1>";

/* gerar token */

$urlAuth = "http://idealsoftexportaweb.eastus.cloudapp.azure.com:60500/auth/?serie=HIEAPA-600759-ROCT&codfilial=1";

echo "<h4>Url de Autenticação - $urlAuth</h4>";

$user_agent = "Teste PHP"; //O USER AGENT PRECISA SER O MESMO EM TODAS AS REQUISIÇÕES

$curl_token = curl_init();

curl_setopt_array($curl_token, array(
  CURLOPT_URL => $urlAuth,
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_USERAGENT => $user_agent,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "GET",
));

$response = curl_exec($curl_token);
$json = json_decode($response, true);

curl_close($curl_token);

//print_r($json);

$statusCode = $json['statusCode'];

if ($statusCode != "200")
{
	echo "<p>Erro ao gerar token!</p>";
	
	exit;
} 
else 
{
	$token = $json['dados']['token'];

	echo "<p>Token $token</p>";

	$timestamp = time();
	$method = "get";
	$body = ""; //preencher quando houver

	$valoresConcatenados = "$method$timestamp$body";

	$hash = hash_hmac("sha256", "$valoresConcatenados", "senha");
	$bytes = hex2bin($hash);
		
	$signature = base64_encode($bytes);
	
	echo "<p>Timestamp $timestamp</p>";

	echo "<p>Signature $signature</p>";

	$curlConsulta = curl_init();

	$urlConsulta = "http://idealsoftexportaweb.eastus.cloudapp.azure.com:60500/aux/cores";

	echo "<h4>Url de Consulta - $urlConsulta</h4>";

	curl_setopt_array($curlConsulta, array(
	  CURLOPT_URL => $urlConsulta,
	  CURLOPT_RETURNTRANSFER => true,
	  CURLOPT_ENCODING => "",
	  CURLOPT_MAXREDIRS => 10,
	  CURLOPT_TIMEOUT => 0,
	  CURLOPT_USERAGENT => $user_agent,
	  CURLOPT_FOLLOWLOCATION => true,
	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
	  CURLOPT_CUSTOMREQUEST => "GET",
	  CURLOPT_HTTPHEADER => array(
		"CodFilial: 1",
		"Content-Type: application/json",
		"Timestamp: $timestamp",
		"Signature: $signature",
		"Authorization: Token $token"
	  ),
	));

	$response = curl_exec($curlConsulta);

	curl_close($curlConsulta);
	echo "<p> Resultado - $response</p>";	
}

?>
