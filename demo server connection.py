import warnings

warnings.filterwarnings('ignore', message='Unverified HTTPS request')
import base64
import requests

Base_url = "https://python.local/wp-json"
media_url =f'{Base_url}/wp/v2/media'
post_url =f'{Base_url}/wp/v2/post'
user = "imran"
password = "FjZF Fdkl kvAr j1VZ vC2V nszw"
credential = f'{user}:{password}'
token = base64.b64encode(credential.encode())
header = {'Authorization':f'Basic {token.decode("utf-8")}'}

def wp_post(post_url, data):
    res = requests.post(post_url,json=data, headers= header, verify=False )
    print( res.status_code)


def wp_h2(text):
    code = f' <!-- wp:heading --><h2 class="wp-block-heading">{text}</h2><!-- /wp:heading -->'
    return code

content = wp_h2('this is wordpress title')
data = {"title": "this is wordpress title",
        "content": content,
        "status":"publish",
       }
wp_post(post_url,data)
