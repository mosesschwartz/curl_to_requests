'''Converts a cURL command to code for Python Requests'''

from curl_to_requests import curl_to_requests

curl_cmd = '''curl 'https://github.com/mosesschwartz/curl_to_requests' -H 'Accept-Encoding: gzip, deflate, sdch' -H 'Accept-Language: en-US,en;q=0.8' -H 'CSP: active' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36' -H 'Accept: text/html, */*; q=0.01' -H 'Referer: https://github.com/mosesschwartz/curl_to_requests' -H 'Connection: keep-alive' --compressed'''

print curl_cmd
print
print '--> curl_to_requests --> '
print
print curl_to_requests.curl_to_requests(curl_cmd)

