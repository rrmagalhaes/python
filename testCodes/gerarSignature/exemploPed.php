<?php
	public function addOrder($data =[]) {
			$this->init();

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

			$data_string = json_encode($customer);
			$teste2      = http_build_query($customer);	
			$metodo    = "post"; //método em minúsculo
			$timestamp = time();
			$body      = base64_encode($data_string);
			
			$hash = hash_hmac("sha256", utf8_encode("$metodo$timestamp$body"), utf8_encode($this->password));

			$bytes = hex2bin($hash); //gera array de bytes do hash

			$signature = base64_encode($bytes);

			$token = $this->session->data['teste']['token'];

			$contentlength = strlen ( $data_string );
?>
