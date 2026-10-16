"""Clean 01_filing_registry_raw.csv -> processed CSV.

- English column names
- Parse filing_date into datetime, derive filing_year/month
- Keep Chinese names as _cn columns for traceability
"""
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw" / "01_filing_registry_raw.csv"
OUT = ROOT / "data" / "processed" / "01_filing_registry.csv"

# City romanization for major prefecture-level cities
CITY_EN = {
    "北京市": "Beijing", "上海市": "Shanghai", "天津市": "Tianjin", "重庆市": "Chongqing",
    "广州市": "Guangzhou", "深圳市": "Shenzhen", "杭州市": "Hangzhou", "南京市": "Nanjing",
    "苏州市": "Suzhou", "成都市": "Chengdu", "武汉市": "Wuhan", "西安市": "Xi'an",
    "长沙市": "Changsha", "郑州市": "Zhengzhou", "合肥市": "Hefei", "济南市": "Jinan",
    "青岛市": "Qingdao", "沈阳市": "Shenyang", "哈尔滨市": "Harbin", "昆明市": "Kunming",
    "大连市": "Dalian", "宁波市": "Ningbo", "无锡市": "Wuxi", "佛山市": "Foshan",
    "东莞市": "Dongguan", "珠海市": "Zhuhai", "福州市": "Fuzhou", "厦门市": "Xiamen",
    "太原市": "Taiyuan", "石家庄市": "Shijiazhuang", "长春市": "Changchun", "南昌市": "Nanchang",
    "南宁市": "Nanning", "贵阳市": "Guiyang", "兰州市": "Lanzhou", "乌鲁木齐市": "Urumqi",
    "呼和浩特市": "Hohhot", "银川市": "Yinchuan", "西宁市": "Xining", "拉萨市": "Lhasa",
    "海口市": "Haikou", "三亚市": "Sanya", "温州市": "Wenzhou", "绍兴市": "Shaoxing",
    "嘉兴市": "Jiaxing", "金华市": "Jinhua", "台州市": "Taizhou", "常州市": "Changzhou",
    "徐州市": "Xuzhou", "南通市": "Nantong", "扬州市": "Yangzhou", "盐城市": "Yancheng",
    "唐山市": "Tangshan", "保定市": "Baoding", "廊坊市": "Langfang", "洛阳市": "Luoyang",
    "南阳市": "Nanyang", "宜宾市": "Yibin", "绵阳市": "Mianyang", "遵义市": "Zunyi",
    "曲靖市": "Qujing", "大庆市": "Daqing", "鞍山市": "Anshan", "吉林市": "Jilin",
    "邯郸市": "Handan", "邢台市": "Xingtai", "沧州市": "Cangzhou", "芜湖市": "Wuhu",
    "泉州市": "Quanzhou", "漳州市": "Zhangzhou", "惠州市": "Huizhou", "中山市": "Zhongshan",
    "柳州市": "Liuzhou", "桂林市": "Guilin", "乐山市": "Leshan", "湖州市": "Huzhou",
}


def main():
    df = pd.read_csv(RAW)
    # Rename to English
    df = df.rename(columns={
        "type": "record_type",
        "category": "category_cn",
        "entity": "entity_cn",
        "name": "name_cn",
        "注册地(地级市)": "city_cn",
        "AI备案属地/province": "province_cn",
        "filing_date": "filing_date",
        "filing_year": "filing_year",
        "filing_month": "filing_month",
        "filing_no": "filing_no",
    })
    # Romanize city
    df["city_en"] = df["city_cn"].map(CITY_EN).fillna(df["city_cn"])
    # Normalize record_type: service=model filing, app=service registration
    df["record_type"] = df["record_type"].map({"service": "model_filing", "app": "service_registration"})
    OUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT, index=False, encoding="utf-8-sig")
    print(f"[01] {len(df)} rows -> {OUT}")


if __name__ == "__main__":
    main()
