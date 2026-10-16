"""Clean 03_app_model_edges_raw.csv -> processed CSV.

- English column names
- Remove dirty nodes containing '—'
- Keep self-loops flagged (users can filter them for network analysis)
"""
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw" / "03_app_model_edges_raw.csv"
OUT = ROOT / "data" / "processed" / "03_app_model_edges.csv"


def main():
    df = pd.read_csv(RAW)
    df = df.rename(columns={
        "app": "app_cn",
        "app_city": "app_city_cn",
        "model": "model_cn",
        "model_city": "model_city_cn",
        "entity": "entity_cn",
        "provider": "provider_cn",
        "evidence": "evidence",
        "note": "note_cn",
        "edge_type": "edge_type_cn",
        "信息来源": "source",
        "filing_no(应用)": "app_filing_no",
        "model_filing_no(模型备案号)": "model_filing_no",
    })
    # Remove dirty rows where either city contains '—'
    before = len(df)
    df = df[~df["app_city_cn"].astype(str).str.contains("—", na=False)]
    df = df[~df["model_city_cn"].astype(str).str.contains("—", na=False)]
    after = len(df)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT, index=False, encoding="utf-8-sig")
    print(f"[03] {before} -> {after} rows (removed {before-after} dirty) -> {OUT}")


if __name__ == "__main__":
    main()
