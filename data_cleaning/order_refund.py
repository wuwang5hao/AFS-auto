# 售后订单
# 产品表现
import requests


def get_lingxing_pe_data():
    url = "https://gw.lingxingerp.com/amz-order/api/afterSalesOrder/orderList"
    headers = {
        "X-AK-Company-Id": "90144120400547840",
        "X-AK-Version": "3.5.2.3.0.022",
        "X-AK-Uid": "10490028",
        "auth-token": "16a5DU8cZWB8q581vrnV5Fh/piANFlEOhLYTs98783orUBAEZEwxIWbrpRuH+JktmZINapyIHx1UaKNJ6KolGFcoAiYGaLKUSOmrgRLg7sIi+u3I6JlMW93vAZ6CRHxPjwvWIUVGyiFlcC7s4AkhUrQ9bZMITkMZ",
        "X-AK-Request-Id": "87147cbf-64bc-4243-b876-cffbbc1123cb",
        "X-AK-Request-Source": "erp",
        "X-AK-Lanugage": "zh",
        "X-AK-Zid": "143570",
        "X-AK-PLATFORM": "2",
        "AK-Client-Type": "web",
        "AK-Origin": "https://erp.lingxing.com",
        "X-AK-ENV-KEY": "SAAS-47",
        "User-Agent": "Apifox/1.0.0 (https://apifox.com)",
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "*/*",
        "Host": "gw.lingxingerp.com",
        "Connection": "keep-alive",
    }

    params ={
      "searchFieldTime": "1",
      "afterType": "1",
      "deliveryType": "1",
      "searchField": "amazonOrderId",
      "intervalLogicalOperator": "greater",
      "intervalDays": "",
      "startDate": "2025-08-01",
      "endDate": "2025-08-31",
      "searchValue": "",
      "multiple": False,
      "pageNo": 1,
      "pageSize": 100,
      "req_time_sequence": "/amz-order/api/afterSalesOrder/orderList$$63"
}
    res = requests.post(url, json=params, headers=headers)
    data = res.json().get("data")
    print(res.json())


get_lingxing_pe_data()
