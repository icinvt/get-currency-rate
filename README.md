# 事前準備

###  環境変数の設定

以下の環境変数を設定する。

S3_BUCKET = <出力先のS3バケット名>  
S3_FILE = <出力するCSVファイル名>  

### Layerの設定

以下のpythonバージョン別のリストから、「requests」、「pandas」のARNを選択して登録する。  
https://github.com/keithrozario/Klayers?tab=readme-ov-file#list-of-arns

### 適切なIAMロール、ポリシーの設定

以下のURLの内容に従って、適切なIAMロール、ポリシーを設定する。  
https://aws.amazon.com/jp/builders-flash/202309/learn-lambda-iam-policies/