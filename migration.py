import requests
stUrlFrom = 'https://api.treasuredata.com/v3/'
stUrlTo = 'https://api.treasuredata.co.jp/v3/'
stAccountFrom = {'Authorization': 'TD1 xxxxx'}
stAccountTo = {'Authorization': 'TD1 xxxxx'}

def get_database_list(url, account):
    list_return = []
    response = requests.get(url = url+'database/list', headers = account) 
    result = response.json()
    for it in result['databases']:
        
#         default database
        if it['name'] in ['sample_datasets', 'information_schema', 'td_audit_log']:
            continue

#         cdp database
        if it['name'][0:13] == 'cdp_audience_':
            continue
    
        list_return.append(it['name'])
    
    return list_return

def get_table_info_list(url, account, database):
    list_return = []
    response = requests.get(url = url+'table/list/'+database, headers = account) 
    result = response.json()
    return result['tables']
        
def set_table_schema(url, account, database, table_info):
    url_cmd = 'table/update/final/a_test_api?schema='
    response = requests.post(url = url+'table/update/'+database+'/'+table_info['name']
        +'?schema='+table_info['schema'], headers = account) 
    response.json()
    

if __name__ == "__main__":
    list_database = get_database_list(stUrlFrom, stAccountFrom)

    for it_database in list_database:
        list_table_info = get_table_info_list(stUrlFrom, stAccountFrom, it_database)

        for it_table_info in list_table_info:
            set_table_schema(stUrlTo, stAccountTo, it_database, it_table_info)