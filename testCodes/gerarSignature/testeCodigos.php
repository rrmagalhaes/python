<?php

$key = "senha";

$dataPed = '{"CpfCnpj": "02733105345", "CodigoOperacao": "500", "Data": "2022-02-10T15:00:00", "Produtos": [{"Codigo": "1", "CodigoCor": null, "CodigoTamanho": null, "Quantidade": 1.0000, "PrecoUnitario": 100.34, "DescontoUnitario": 0.00}], "Recebimentos": [{"ValorParcelas": 100.34, "Tipo": "CR"}], "DadosEntrega": {"Valor": 10.00, "NaoSomarFreteTotalNota": true, "OutroEndereco": {"Cep": "82600380", "Endereco": "Rua Nunia", "Numero": "11", "Complemento": null, "Bairro": "Teste", "Cidade": "Curitiba", "Uf": "PR"}}}';

$customer = [
		  "CpfCnpj" => "16025717087",
		  "CodigoOperacao" => "500",
		  "CodigoCaixa" => "1",
		  "Data" => "2019-02-19T00:00:00-03:00",
		  "Produtos" => [
		    [
		      "Codigo" => "1",
		      "CodigoCor" => 1,
		      "CodigoTamanho" => 1,
		      "Quantidade" => 1.0000,
		      "PrecoUnitario" => 576.34,
		      "DescontoUnitario" => 100.00
		    ]
		  ],
		  "Recebimentos" => [
		    [
		      "ValorParcelas" => 476.34,
		      "CodigoAdministradora" => 1,
		      "Vencimento" => "2021-02-19T00:00:00-03:00",
		      "Nsu" => "995544",
		      "QuantidadeParcelas" => 1,
		      "NumeroCartao" => "2344",
		      "Tipo" => "C"
		    ]
		  ],
		  "DadosEntrega" => [
		    "Valor" => 10.00,
		    "OpcoesFretePagoPor" => "O",
		    "PesoBruto" => 0.0,
		    "PesoLiquido" => 0.0,
		    "Volume" => 0.0,
		    "DataEntrega" =>  "2021-02-19T00:00:00-03:00",
		    "CnpjTransportadora" => "24165926000103",
		    "NaoSomarFreteTotalNota" => true,
		    "OutroEndereco" => [
		      "Cep" => "82600380",
		      "Endereco" => "RUa nunia",
		      "Numero" => "dfjs 11",
		      "Complemento" => "",
		      "Bairro" => "Teste",
		      "Cidade" => "Curitiba",
		      "Uf" => "PR"
		    ]
		  ]
		];

		//$data_string = json_encode($dataPed);
		//echo "<p>$data_string</p>";	
		$metodo    = "post"; //método em minúsculo
		$timestamp = 1645295482;
		$body      = base64_encode($dataPed);
		echo "--- BODY ---";
		echo "<p>$body</p>";	
		$concatenados = "$metodo$timestamp$body";
        echo "--- Concatenados ---";
		echo "<p>$concatenados</p>";

		$hash = hash_hmac("sha256", utf8_encode($concatenados), utf8_encode($key));
		echo "--- Hash ---";
		echo "<p>$hash</p>";

        $bytes = hex2bin($hash); //gera array de bytes do hash
		echo "--- Bytes ---";
		echo "<p>$bytes</p>";

        $signature = base64_encode($bytes);
		echo "--- Signature ---";
		echo "<p>$signature</p>";
		
?>		