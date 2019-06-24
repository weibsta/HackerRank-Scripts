# Lock users
import requests
import json

apiToken = '' #replace with relevant api key
lockList = [] # Add list of users w/ firstname lastname  [WIP] email is better, parsing first/last is hard and doesn't work 100%
hrURL = 'https://www.hackerrank.com/x/api/v3/users'
deleteArr = []
totalUsers;
limit_count = 100

# Get list of all users
def getUsers(offset):
    offset = offset
    r = requests.get(url=hrURL+'?limit=%d&offset=%d' % (limit_count,offset), headers={'Authorization':apiToken})
    res = r.json()

    for y in lockList:
        firstname = y.split(' ', 1)[0]
        lastname = y.split(' ', 1)[1]
        for x in res['data']:
            if x['firstname'] == firstname and x['lastname'] == lastname and x['status'] != 'locked':
                deleteArr.append(x['id'])

def lockUsers():
    for x in deleteArr:
        r = requests.delete(url='https://www.hackerrank.com/x/api/v3/users/'+x, headers={'Authorization':apiToken})
        print(str(r.status_code) + ' locking user: ' + x)

def getTotalUsers():
    r = requests.get(url=hrURL+'?limit=%d&offset=%d' % (limit_count,offset), headers={'Authorization':apiToken})
    res = r.json()
    totalUsers = res['total']

getTotalUsers()

for x in range(0, totalUsers, limit_count):
    getUsers(x)

lockUsers()
