import requests
import hashlib
import  sys
def request_api_data(quary_char):
    url = 'https://api.pwnedpasswords.com/range/' + quary_char
    # response data
    res = requests.get(url)
    if res.status_code!=200:
     raise RuntimeError(f'Error fetchingL: {res.status_code},check error')
    return res
def get_password_leak(hashes,hash_to_check):
    hashes =(line.split(':') for line in hashes.text.splitlines())
    for h,count in hashes:
      if h == hash_to_check:
          return count
    return 0

def pwned_api_check(password):
    sha1password =hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char,tail =sha1password[:5] ,sha1password[5:]
    response =request_api_data(first5_char)
    return get_password_leak(response ,tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)

        if count:
            print(f'{password} was hacked {count} times.You should change your password!!!')
        else:
            print(f'{password} was not found. Carry on. Good Luck!')
    return  'done'

if __name__ =='__main__':
 main(sys.argv[1:])

# pwned_api_check('123')
# request_api_data('1234545BJFB JFBFJNFKJBFKFBFKBFKFKFBFKBFK')

