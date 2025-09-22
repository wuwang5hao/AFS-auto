# 产品表现
import requests


def get_lingxing_pe_data():
    url = "https://gw.lingxingerp.com/bd/productPerformance/asinLists"
    headers = {
        "X-AK-Company-Id": "90144120400547840",
        "X-AK-Version": "3.5.2.3.0.022",
        "X-AK-Uid": "10490028",
        "auth-token": "168cveu/SXPmge2CFoMxpXVpcm+c9eYqVlRm5GOgSmyDTzoa9h1UNOxaAyFAhqmx8ni82QyahvdzImWPuVfexN1w2mewV10d4WTGeVG9XsrjXTwMO6uhgdRjD70fLuItnLTpkB/4NaPji9fGLD4Pl2qeioeD7iNE",
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

    params = {
        "ad_cost_type": "",
        "attr_value_ids": [],
        "auto_tags": [],
        "bids": [],
        "cids": [],
        "currency_code": "",
        "delivery_methods": [],
        "developers": [],
        "extend_search": [],
        "gtag_ids": [],
        "mids": [],
        "order_types": [],
        "owner_uids": [],
        "principal_uids": [],
        "product_states": [],
        "promotions": [],
        "regions": [],
        "sids": [],
        "search_value": [],
        "date_range_type": 0,
        "date_type": "purchase",
        "end_date": "2025-09-18",
        "only_query_today": True,
        "start_date": "2025-09-18",
        "today_hour": "02",
        "length": 20,
        "offset": 0,
        "sort_field": "volume",
        "sort_type": "desc",
        "is_recently_enum": True,
        "is_resale": "",
        "purchase_status": 0,
        "query_order_profit": True,
        "search_field": "asin",
        "summary_field": "asin",
        "summary_field_level1": "",
        "summary_field_level2": "",
        "turn_on_summary": 0,
        "req_time_sequence": "/bd/productPerformance/asinLists$$7",
    }
    res = requests.post(url, json=params, headers=headers)
    data = res.json().get("data")
    print(res.json())


get_lingxing_pe_data()
