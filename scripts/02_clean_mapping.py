"""Clean 02_entity_mapping_raw.csv -> processed CSV.

- English column names
- English mappings for industry_sector and ownership
- City romanization
"""
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw" / "02_entity_mapping_raw.csv"
OUT = ROOT / "data" / "processed" / "02_entity_city_mapping.csv"

INDUSTRY_EN = {
    "软件/信息技术服务": "Software / IT Services",
    "传媒/文化/文旅": "Media / Culture / Tourism",
    "金融": "Finance",
    "制造/硬件电子": "Manufacturing / Hardware Electronics",
    "教育": "Education",
    "互联网平台": "Internet Platform",
    "医药健康": "Healthcare / Pharma",
    "汽车/交通物流": "Automotive / Transport / Logistics",
    "科研机构/实验室": "Research Institution / Lab",
    "能源/电力/资源": "Energy / Power / Resources",
    "政务/公共管理": "Government / Public Administration",
    "零售/消费/贸易": "Retail / Consumer / Trade",
    "人力资源/专业服务": "HR / Professional Services",
    "电信运营商": "Telecom Operator",
    "建筑/地产": "Construction / Real Estate",
    "其他/未归类": "Other / Unclassified",
}

OWNERSHIP_EN = {
    "民营企业及其他": "Private",
    "国有企业": "SOE",
    "外资": "Foreign",
    "高校/科研院所": "University / Research",
    "政府机关": "Government",
}


def main():
    df = pd.read_csv(RAW)
    df = df.rename(columns={
        "单位": "entity_cn",
        "属地（省级）": "province_cn",
        "城市(地级市)": "city_cn",
        "法人登记类型": "entity_legal_type_cn",
        "登记全称/说明": "reg_full_name",
        "业务属性": "business_nature",
        "市场主体形态": "market_entity_form_cn",
        "所有制背景": "ownership_cn",
        "行业赛道": "industry_sector_cn",
        "科技细分": "tech_subsector_cn",
        "备案/登记侧": "filing_side_cn",
        "条目数": "entity_count",
        "涉及模型/应用名称": "linked_names_cn",
        "法人类型核实依据": "legal_type_source",
    })
    df["industry_sector_en"] = df["industry_sector_cn"].map(INDUSTRY_EN)
    df["ownership_en"] = df["ownership_cn"].map(OWNERSHIP_EN)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT, index=False, encoding="utf-8-sig")
    print(f"[02] {len(df)} rows -> {OUT}")


if __name__ == "__main__":
    main()
