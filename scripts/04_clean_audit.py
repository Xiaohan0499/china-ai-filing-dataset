"""Clean 04_app_audit_log_raw.csv -> processed CSV."""
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw" / "04_app_audit_log_raw.csv"
OUT = ROOT / "data" / "processed" / "04_app_audit_log.csv"


def main():
    df = pd.read_csv(RAW)
    df = df.rename(columns={
        "app": "app_cn",
        "entity": "entity_cn",
        "app_city": "app_city_cn",
        "status": "audit_status_cn",
        "edge_count": "edge_count",
        "models_found": "models_found_cn",
        "note": "note_cn",
        "evidence": "evidence",
        "信息来源": "source",
        "filing_no(应用)": "app_filing_no",
    })
    OUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT, index=False, encoding="utf-8-sig")
    print(f"[04] {len(df)} rows -> {OUT}")


if __name__ == "__main__":
    main()
