import requests
import json
import time
from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse
import warnings 

warnings.filterwarnings("ignore")

url = "https://{YOUR-MORPHEUS-APPLIANCE-URL}/api/approvals?max=25&offset=0&sort=name&direction=asc"

headers = {
    "accept": "application/json",
    "authorization": "Bearer {YOUR-MORPHEUS-API-TOKEN-HERE}"  
}

response = requests.get(url, headers=headers, verify=False)
data = response.json()

reconfigureQuery = parse("$.approvals[?(@.requestType[*] =~ 'Instance Reconfigure Approval' & @.status[*] != '1 approved')]")       # only retrieve items that have not been approved and have a requestType of 'Instance Reconfigure Approval'
reconfiguresAwaitingApproval = [match.value for match in reconfigureQuery.find(data)]
# print(json.dumps(reconfiguresAwaitingApproval, indent=2) + '\n')                            

reconfigureApprovalItemIDs = []
for IDs in reconfiguresAwaitingApproval: 
    IDs = IDs['id']
    reconfigureApprovalItemIDs.append(IDs)
# print(f"Reconfigures Pending Approval (item-ids): {reconfigureApprovalItemIDs}" + '\n')

for id in reconfigureApprovalItemIDs: 
    url = f"https://{YOUR-MORPHEUS-APPLIANCE-URL}/api/approval-items/{id}/approve"
    headers = {
        "accept": "application/json",
        "authorization": "Bearer {YOUR-MORPHEUS-API-TOKEN-HERE}"
    }
    response = requests.put(url, headers=headers, verify=False)
    data = response.json()
    print(json.dumps(data, indent=2))
    time.sleep(2)                                      # preventative. look into implementing threads to handle this properly 
