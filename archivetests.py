import requests
import json

apiToken = #replace with relevant api key
keepTests = [] #list of ids of any tests that shouldn't be archived
testList = []
hrURL = 'https://www.hackerrank.com/x/api/v3/tests'   #HR endpoint

def getTests():
    limit_count = 10
    offset = 0
    try:
        # Make initial request to get the first page
        r = requests.get(url=hrURL+'?limit=%d&offset=%d' % (limit_count,offset), headers={'Authorization':apiToken})
        res = r.json()
        # If total page count is less than limit count, append tests because there is only one page
        if (res['total'] <= limit_count):
            for x in res['data']:
                if x['id'] not in keepTests and x['state'] == 'active':
                    testList.append(x['id'])
                else:
                    print('Not archiving: ' + x['name'])
        else:
            # Else, there are multiple pages so loop until response 'next' value is empty
            while (res['next'] != ""):
                pag = requests.get(url=hrURL+'?limit=%d&offset=%d' % (limit_count,offset), headers={'Authorization':apiToken}).json()
                res['next'] = pag['next']
                # Append test ids as we go through each page
                for x in pag['data']:
                    if x['id'] not in keepTests and x['state'] == 'active':
                        testList.append(x['id'])
                    else:
                        print('Not archiving: ' + x['name'])
                offset += limit_count

        # TODO Appending test logic is repeated in the if/else. Possibly make this into a function?

    except requests.exceptions.HTTPError as err:
        print err
        sys.exit(1)

def cleanTests(testList):
    for x in testList:
        requests.post(url=hrURL + '/' + x + '/archive', headers={'Authorization':apiToken})
        print('Achived test with id: ' + x)

getTests()
cleanTests(testList)
