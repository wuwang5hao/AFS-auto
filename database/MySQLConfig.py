# 创建数据表完全可配置

# 日产品表现
productExpressionDay_table_config = {
    "name": "amz_sum_day_order",
    "comment": "日产品表现",
    "primary_key": "ID",  # 主键字段名
    "fields": [
        {
            "name": "ID",
            "type": "INT",
            "constraints": ["AUTO_INCREMENT", "NOT NULL"],
            "comment": "主键，自增ID",
        },
        {
            "name": "OrderDate",
            "type": "DATE",
            "constraints": ["NOT NULL"],
            "comment": "统计日期，对应【日期】联合主键之一",
        },
        {
            "name": "StoreName",
            "type": "VARCHAR(50)",
            "constraints": ["NOT NULL"],
            "comment": "店铺名称",
        },
        {
            "name": "MSKU",
            "type": "VARCHAR(50)",
            "constraints": ["NOT NULL"],
            "comment": "领星口径的MSKU，实际为SKU，需要在亚马逊后台填写与ASIN建立映射关系，同时与SKU建立映射关系关联采购单。",
        },
        {
            "name": "SKU",
            "type": "VARCHAR(50)",
            "constraints": [],
            "comment": "领星口径的SKU，实际为产品的采购编码。产品立项通过后产生该编码",
        },
        {
            "name": "ASIN",
            "type": "VARCHAR(20)",
            "constraints": ["NOT NULL"],
            "comment": "亚马逊平台的产品唯一标识码，由亚马逊分配。一般为10位，以B0开头，少数为11位和12位。",
        },
        {
            "name": "ParentASIN",
            "type": "VARCHAR(20)",
            "constraints": ["NOT NULL"],
            "comment": "父ASIN，同一个变体的父ASIN相同，由亚马逊分配。",
        },
        {
            "name": "ProductName",
            "type": "VARCHAR(100)",
            "constraints": [],
            "comment": "产品名称",
        },
        {
            "name": "PriceSell",
            "type": "DECIMAL(10,2)",
            "constraints": ["NOT NULL"],
            "comment": "售价，对应【售价(总价)】",
        },
        {
            "name": "PriceSellNet",
            "type": "DECIMAL(10,2)",
            "constraints": ["NOT NULL"],
            "comment": "平均售价，对应【销售均价】",
        },
        {
            "name": "UnitsSell",
            "type": "INT",
            "constraints": ["NOT NULL"],
            "comment": "产品销量，对应【销量】",
        },
        {
            "name": "OrdersSell",
            "type": "INT",
            "constraints": ["NOT NULL"],
            "comment": "产品销售订单量，对应【订单量】",
        },
        {
            "name": "RevenueSell",
            "type": "DECIMAL(10,2)",
            "constraints": ["NOT NULL"],
            "comment": "产品销售额，对应【销售额】",
        },
        {
            "name": "RevenueSellNet",
            "type": "DECIMAL(10,2)",
            "constraints": ["NOT NULL"],
            "comment": "产品净销售额，对应【净销售额】。【净销售额】 = 【销售额】-【促销折扣】",
        },
        {
            "name": "UnitsPromotion",
            "type": "INT",
            "constraints": ["NOT NULL"],
            "comment": "促销销量，对应【促销销量】",
        },
        {
            "name": "OrdersPromotion",
            "type": "INT",
            "constraints": ["NOT NULL"],
            "comment": "促销订单量，对应【促销订单量】",
        },
        {
            "name": "RevenuePromotion",
            "type": "DECIMAL(10,2)",
            "constraints": ["NOT NULL"],
            "comment": "促销销售额，对应【促销销售额】",
        },
        {
            "name": "Discount",
            "type": "FLOAT(5,4)",
            "constraints": ["NOT NULL"],
            "comment": "促销折扣，对应【促销折扣】",
        },
        {
            "name": "UnitsRefund",
            "type": "INT",
            "constraints": ["NOT NULL"],
            "comment": "退款数量",
        },
        {
            "name": "RevenueRefund",
            "type": "DECIMAL(10,2)",
            "constraints": ["NOT NULL"],
            "comment": "退款金额",
        },
        {
            "name": "CategoryName",
            "type": "VARCHAR(100)",
            "constraints": [],
            "comment": "大类名称",
        },
        {
            "name": "CategoryRank",
            "type": "INT",
            "constraints": ["NOT NULL"],
            "comment": "大类排名",
        },
        {
            "name": "SubcategoryName",
            "type": "VARCHAR(100)",
            "constraints": [],
            "comment": "小类名称",
        },
        {
            "name": "SubcategoryRank",
            "type": "INT",
            "constraints": ["NOT NULL"],
            "comment": "小类排名",
        },
        {
            "name": "Rating",
            "type": "FLOAT(3,1)",
            "constraints": ["NOT NULL"],
            "comment": "产品星级，对应【评分】,样例为4.3。",
        },
        {
            "name": "RatingNum",
            "type": "INT",
            "constraints": ["NOT NULL"],
            "comment": "Rating数量，对应【评论数】",
        },
        {
            "name": "Buybox",
            "type": "FLOAT(6,4)",
            "constraints": ["NOT NULL"],
            "comment": "Buybox，对应【Buybox赢得率】",
        },
        {
            "name": "RatingRate",
            "type": "FLOAT(4,2)",
            "constraints": ["NOT NULL"],
            "comment": "留评率，对应【留评率】",
        },
        {
            "name": "GrossProfit",
            "type": "DECIMAL(10,2)",
            "constraints": ["NOT NULL"],
            "comment": "订单毛利，对应【订单毛利润】",
        },
        {
            "name": "GrossProfitRate",
            "type": "FLOAT(6,4)",
            "constraints": ["NOT NULL"],
            "comment": "订单毛利率，对应【订单毛利率】",
        },
        {
            "name": "ROI",
            "type": "FLOAT(8,4)",
            "constraints": ["NOT NULL"],
            "comment": "投入产出比，对应【ROI】",
        },
        {
            "name": "InventoryFBMAvailable",
            "type": "INT",
            "constraints": ["NOT NULL"],
            "comment": "FBM库存-可售",
        },
        {
            "name": "InventoryFBAavailable",
            "type": "INT",
            "constraints": ["NOT NULL"],
            "comment": "FBA库存-可售",
        },
        {
            "name": "InventoryFBAIn",
            "type": "INT",
            "constraints": ["NOT NULL"],
            "comment": "FBA库存-入库中",
        },
        {
            "name": "SessionsTotal",
            "type": "INT",
            "constraints": ["NOT NULL"],
            "comment": "总Sessions，对应【Sessions-Total】",
        },
        {
            "name": "SessionsMobile",
            "type": "INT",
            "constraints": ["NOT NULL"],
            "comment": "移动端Sessions，对应【Sessions-Mobile】",
        },
        {
            "name": "SessionsBrowser",
            "type": "INT",
            "constraints": ["NOT NULL"],
            "comment": "PC端Sessions，对应【Sessions-Browser】",
        },
        {
            "name": "PVTotal",
            "type": "INT",
            "constraints": ["NOT NULL"],
            "comment": "总PageView数，对应【PV-Total】",
        },
        {
            "name": "PVMobile",
            "type": "INT",
            "constraints": ["NOT NULL"],
            "comment": "移动端PageView数，对应【PV-Mobile】",
        },
        {
            "name": "PVBrowser",
            "type": "INT",
            "constraints": ["NOT NULL"],
            "comment": "PC端PageView数，对应【PV-Browser】",
        },
        {
            "name": "CVRTotal",
            "type": "FLOAT(6,4)",
            "constraints": ["NOT NULL"],
            "comment": "订单转换率(含自然和广告)，对应【CVR】",
        },
        {
            "name": "CVRUnitTotal",
            "type": "FLOAT(6,4)",
            "constraints": ["NOT NULL"],
            "comment": "销量转换率(含自然和广告)，对应【销量CVR】",
        },
        {
            "name": "UnitsAdvert",
            "type": "INT",
            "constraints": ["NOT NULL"],
            "comment": "广告销量，对应【直接成交销量】",
        },
        {
            "name": "OrdersAdvert",
            "type": "INT",
            "constraints": ["NOT NULL"],
            "comment": "广告直接订单量，对应【直接成交订单量】",
        },
        {
            "name": "RevenueAdvert",
            "type": "DECIMAL(10,2)",
            "constraints": ["NOT NULL"],
            "comment": "广告直接销售额，对应【直接成交销售额】",
        },
        {
            "name": "UnitsAdvertTotal",
            "type": "INT",
            "constraints": ["NOT NULL"],
            "comment": "广告总销量，含其他产品的销量。对应【广告销量】",
        },
        {
            "name": "OrdersAdvertTotal",
            "type": "INT",
            "constraints": ["NOT NULL"],
            "comment": "广告总订单量，含其他产品的订单量。对应【广告订单量】",
        },
        {
            "name": "RevenueAdvertTotal",
            "type": "DECIMAL(10,2)",
            "constraints": ["NOT NULL"],
            "comment": "广告总销售额，含其他产品的销售额。对应【广告销售额】。",
        },
        {
            "name": "ImpressionsAdvert",
            "type": "INT",
            "constraints": ["NOT NULL"],
            "comment": "广告展现，对应【展示】",
        },
        {
            "name": "ClickAdvert",
            "type": "INT",
            "constraints": ["NOT NULL"],
            "comment": "广告点击，对应【点击】",
        },
        {
            "name": "CTRAdvert",
            "type": "FLOAT(8,6)",
            "constraints": ["NOT NULL"],
            "comment": "广告点击率，对应【CTR】。公式为：100 * ClickAdvert / ImpressionsAdvert",
        },
        {
            "name": "SpendAdvert",
            "type": "DECIMAL(10,2)",
            "constraints": ["NOT NULL"],
            "comment": "广告花费【广告花费】",
        },
        {
            "name": "CPCAdvert",
            "type": "DECIMAL(10,2)",
            "constraints": ["NOT NULL"],
            "comment": "平均每次广告点击花费，对应【CPC】；公式为：SpendAdvert / ClickAdvert",
        },
        {
            "name": "CPMAdvert",
            "type": "DECIMAL(10,2)",
            "constraints": ["NOT NULL"],
            "comment": "平均每千次展现的广告花费，对应【CPM】",
        },
        {
            "name": "ROASAdvert",
            "type": "FLOAT(6,2)",
            "constraints": ["NOT NULL"],
            "comment": "对应【ROAS】",
        },
        {
            "name": "ACOSAdvert",
            "type": "FLOAT(6,4)",
            "constraints": ["NOT NULL"],
            "comment": "对应【ACOS】",
        },
        {
            "name": "ASoASAdvert",
            "type": "FLOAT(6,4)",
            "constraints": ["NOT NULL"],
            "comment": "对应【ASoAS】",
        },
        {
            "name": "CPOAdvert",
            "type": "DECIMAL(10,2)",
            "constraints": ["NOT NULL"],
            "comment": "对应【CPO】",
        },
        {
            "name": "CPUAdvert",
            "type": "DECIMAL(10,2)",
            "constraints": ["NOT NULL"],
            "comment": "对应【CPU】",
        },
        {
            "name": "ClickNature",
            "type": "INT",
            "constraints": ["NOT NULL"],
            "comment": "自然点击，对应【自然点击量】",
        },
        {
            "name": "OrdersNature",
            "type": "INT",
            "constraints": ["NOT NULL"],
            "comment": "自然订单数量，对应【自然订单量】",
        },
        {
            "name": "CVRNature",
            "type": "FLOAT(6,4)",
            "constraints": ["NOT NULL"],
            "comment": "自然订单转化率，对应【自然CVR】",
        },
    ],

}

# 退款
refund_table_config = {
    "name": "amz_refund_detail",
    "comment": "亚马逊用户退款表",
    "primary_key": "RefundID",  # 主键字段名
    "fields": [
        {
            "name": "RefundID",
            "type": "INT",
            "constraints": ["AUTO_INCREMENT", "NOT NULL"],
            "comment": "主键，自增ID",
        },
        {
            "name": "PurchaseOrderID",
            "type": "VARCHAR(30)",
            "constraints": ["NOT NULL"],
            "comment": "亚马逊订单号，联合主键之一。亚马逊订单号一般为19位，格式为XXX-XXXXXXX-XXXXXXX",
        },
        {
            "name": "MSKU",
            "type": "VARCHAR(30)",
            "constraints": ["NOT NULL"],
            "comment": "领星口径的MSKU，实际为SKU，需要在亚马逊后台填写与ASIN建立映射关系，同时与SKU建立映射关系关联采购单",
        },
        {
            "name": "StoreName",
            "type": "VARCHAR(50)",
            "constraints": ["NOT NULL"],
            "comment": "店铺名称",
        },
        {
            "name": "ASIN",
            "type": "VARCHAR(30)",
            "constraints": ["NOT NULL"],
            "comment": "亚马逊平台的产品唯一标识码，由亚马逊分配。一般为10位，以" "B0" "开头，少数为11位和12位",
        },
        {
            "name": "Fulfillment",
            "type": "VARCHAR(30)",
            "constraints": ["NOT NULL"],
            "comment": "尾程配送方式：FBA和FBM",
        },
        {
            "name": "PurchaseTime",
            "type": "DATETIME",
            "constraints": [],
            "comment": "订购时间",
        },
        {
            "name": "RefundTime",
            "type": "DATETIME",
            "constraints": ["NOT NULL"],
            "comment": "退款时间",
        },
        {
            "name": "UnitRefund",
            "type": "INT",
            "constraints": ["NOT NULL"],
            "comment": "退款数量",
        },
        {
            "name": "RevenueSell",
            "type": "DECIMAL(10,2)",
            "constraints": ["NOT NULL"],
            "comment": "订单金额",
        },
        {
            "name": "RevenueRefund",
            "type": "DECIMAL(10,2)",
            "constraints": ["NOT NULL"],
            "comment": "退款金额",
        },
        {
            "name": "CostRefund",
            "type": "DECIMAL(10,2)",
            "constraints": ["NOT NULL"],
            "comment": "退款费用",
        },
    ],
}

# 退货
return_table_config = {
    "name": "amz_return_detail",
    "comment": "退货表",
    "primary_key": "ReturnID",  # 主键字段名
    "fields": [
        {
            "name": "ReturnID",
            "type": "INT",
            "constraints": ["AUTO_INCREMENT", "NOT NULL"],
            "comment": "主键，自增ID",
        },
        {
            "name": "PurchaseOrderID",
            "type": "VARCHAR(30)",
            "constraints": ["NOT NULL"],
            "comment": "亚马逊订单号，联合主键之一。亚马逊订单号一般为19位，格式为XXX-XXXXXXX-XXXXXXX",
        },
        {
            "name": "MSKU",
            "type": "VARCHAR(30)",
            "constraints": ["NOT NULL"],
            "comment": "领星口径的MSKU，实际为SKU，需要在亚马逊后台填写与ASIN建立映射关系，同时与SKU建立映射关系关联采购单",
        },
        {
            "name": "StoreName",
            "type": "VARCHAR(50)",
            "constraints": ["NOT NULL"],
            "comment": "店铺名称",
        },
        {
            "name": "ASIN",
            "type": "VARCHAR(30)",
            "constraints": ["NOT NULL"],
            "comment": "亚马逊平台的产品唯一标识码，由亚马逊分配。一般为10位，以" "B0" "开头，少数为11位和12位",
        },
        {
            "name": "Fulfillment",
            "type": "VARCHAR(30)",
            "constraints": ["NOT NULL"],
            "comment": "尾程配送方式：FBA和FBM",
        },
        {
            "name": "PurchaseTime",
            "type": "DATETIME",
            "constraints": [],
            "comment": "订购时间",
        },
        {
            "name": "RetrunDate",
            "type": "DATE",
            "constraints": ["NOT NULL"],
            "comment": "退款时间",
        },
        {
            "name": "UnitReturn",
            "type": "INT",
            "constraints": ["NOT NULL"],
            "comment": "退款数量",
        },
        {
            "name": "RevenueSell",
            "type": "DECIMAL(10,2)",
            "constraints": ["NOT NULL"],
            "comment": "订单金额",
        },
        {
            "name": "RevenueRefund",
            "type": "DECIMAL(10,2)",
            "constraints": ["NOT NULL"],
            "comment": "退款金额",
        },
        {
            "name": "CostRefund",
            "type": "DECIMAL(10,2)",
            "constraints": ["NOT NULL"],
            "comment": "退款费用",
        },
        {
            "name": "ReturnReason",
            "type": "VARCHAR(255)",
            "constraints": ["NOT NULL"],
            "comment": "退货原因",
        },
        {
            "name": "ReturnState",
            "type": "VARCHAR(255)",
            "constraints": [],
            "comment": "退货状态",
        },
        {
            "name": "InventoryAttributes",
            "type": "VARCHAR(255)",
            "constraints": [],
            "comment": "库存属性",
        },
        {
            "name": "LPNCode",
            "type": "VARCHAR(255)",
            "constraints": [],
            "comment": "顾客退货的物流编码：LPN编号。",
        },
        {
            "name": "CustomerMessage",
            "type": "TEXT",
            "constraints": [],
            "comment": "买家留言",
        },
        {
            "name": "CustomerMessageCH",
            "type": "TEXT",
            "constraints": [],
            "comment": "买家留言中文",
        },
    ],
}

# 换货
exchange_table_config = {
    "name": "amz_exchange_detail",
    "comment": "换货表",
    "primary_key": "ReturnID",  # 主键字段名
    "fields": [
        {
            "name": "ReturnID",
            "type": "INT",
            "constraints": ["AUTO_INCREMENT", "NOT NULL"],
            "comment": "主键，自增ID",
        },
        {
            "name": "PurchaseOrderID",
            "type": "VARCHAR(30)",
            "constraints": ["NOT NULL"],
            "comment": "亚马逊订单号，联合主键之一。亚马逊订单号一般为19位，格式为XXX-XXXXXXX-XXXXXXX",
        },
        {
            "name": "MSKU",
            "type": "VARCHAR(30)",
            "constraints": ["NOT NULL"],
            "comment": "领星口径的MSKU，实际为SKU，需要在亚马逊后台填写与ASIN建立映射关系，同时与SKU建立映射关系关联采购单",
        },
        {
            "name": "StoreName",
            "type": "VARCHAR(50)",
            "constraints": ["NOT NULL"],
            "comment": "店铺名称",
        },
        {
            "name": "ASIN",
            "type": "VARCHAR(30)",
            "constraints": ["NOT NULL"],
            "comment": "亚马逊平台的产品唯一标识码，由亚马逊分配。一般为10位，以" "B0" "开头，少数为11位和12位",
        },
        {
            "name": "Fulfillment",
            "type": "VARCHAR(30)",
            "constraints": ["NOT NULL"],
            "comment": "尾程配送方式：FBA和FBM",
        },
        {
            "name": "PurchaseTime",
            "type": "DATETIME",
            "constraints": [],
            "comment": "订购时间",
        },
        {
            "name": "RetrunDate",
            "type": "DATETIME",
            "constraints": ["NOT NULL"],
            "comment": "退款时间",
        },
        {
            "name": "UnitReturn",
            "type": "INT",
            "constraints": ["NOT NULL"],
            "comment": "退款数量",
        },
        {
            "name": "RevenueSell",
            "type": "DECIMAL(10,2)",
            "constraints": ["NOT NULL"],
            "comment": "订单金额",
        },
        {
            "name": "RevenueRefund",
            "type": "DECIMAL(10,2)",
            "constraints": ["NOT NULL"],
            "comment": "退款金额",
        },
        {
            "name": "CostRefund",
            "type": "DECIMAL(10,2)",
            "constraints": ["NOT NULL"],
            "comment": "退款费用",
        },
        {
            "name": "ReturnReason",
            "type": "VARCHAR(255)",
            "constraints": ["NOT NULL"],
            "comment": "退货原因",
        },
        {
            "name": "ChangeOrderID",
            "type": "VARCHAR(30)",
            "constraints": [],
            "comment": "用户换货的亚马逊订单号，联合主键之一。亚马逊订单号一般为19位，格式为 XXX-XXXXXXX-XXXXXXX",
        },
    ],
}


def test():
    lista = [item['name'] for item in productExpressionDay_table_config['fields']]
    print(lista)

test()
# print(len(productExpressionDay_table_config['fields']))