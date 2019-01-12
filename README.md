# curl_to_requests
curl_to_requests is a Python module that converts cURL commands into equivalent Python code using the requests library. Many cURL features are unsupported (it's a very complex piece of software), but curl_to_requests is far more complete than any of the other cURL converting utilities I've found.

Example:
```Python
from curl_to_requests import curl_to_requests

curl_cmd = '''curl 'https://github.com/mosesschwartz/curl_to_requests' \\
    -H 'Accept-Encoding: gzip, deflate, sdch' \\
    -H 'Accept-Language: en-US,en;q=0.8' \\
    -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36' \\
    -H 'Accept: text/html, */*; q=0.01' \\
    -H 'Referer: https://github.com/mosesschwartz/curl_to_requests' \\
    -H 'Connection: keep-alive' --compressed'''

print curl_to_requests(curl_cmd)
```
