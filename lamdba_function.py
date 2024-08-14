import json
import requests
import boto3
import os
import pandas as pd
import io

bucket = os.environ.get('S3_BUCKET')
outfile = os.environ.get('S3_FILE')

def lambda_handler(event, context):
    url = 'https://www.mizuhobank.co.jp/market/quote.csv'
    response = requests.get(url)
    if response.status_code == 200:
        response.encoding = response.apparent_encoding
        df = pd.read_csv(io.StringIO(response.text), index_col=0)
        df.rename(columns ={'Unnamed: 1':'USD','Unnamed: 2':'GBP','Unnamed: 3':'EUR','Unnamed: 4':'CAD','Unnamed: 5':'CHF','Unnamed: 6':'SEK','Unnamed: 7':'DKK','Unnamed: 8':'NOK','Unnamed: 9':'AUD','Unnamed: 10':'NZD','Unnamed: 11':'ZAR','Unnamed: 12':'BHD','Unnamed: 13':'IDR(100)','Unnamed: 14':'CNY(100)','Unnamed: 15':'HKD','Unnamed: 16':'INR','Unnamed: 17':'MYR(100)','Unnamed: 18':'PHP','Unnamed: 19':'SGD','Unnamed: 20':'KRW(100)','Unnamed: 21':'THB','Unnamed: 22':'KWD','Unnamed: 23':'SAR','Unnamed: 24':'AED','Unnamed: 25':'MXN','Unnamed: 26':'PGK','Unnamed: 27':'HUF','Unnamed: 28':'CZK','Unnamed: 29':'PLN','Unnamed: 30':'TRY','Unnamed: 31':'','Unnamed: 32':'IDR','Unnamed: 33':'CNY','Unnamed: 34':'MYR','Unnamed: 35':'KRW','Unnamed: 36':'TWD','Unnamed: 37':'RUB'}, inplace = True)
        df.rename(columns ={'参考相場':'IDR'}, inplace=True)
        dff = df[2:].stack()
        dff.to_csv('/tmp/tmp.csv')
        '''
        with open('/tmp/tmp.csv', mode='w') as file:
            file.write(response.text)
            file.close()
        '''
        s3 = boto3.resource('s3')
        use_bucket = s3.Bucket(bucket)
        use_bucket.upload_file('/tmp/tmp.csv', outfile)
        os.remove('/tmp/tmp.csv')
    return {
        'statusCode': response.status_code,
        'body': json.dumps('Hello from Lambda!')
    }
