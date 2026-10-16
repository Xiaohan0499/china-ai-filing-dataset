# China Generative AI Filing Registry: City-Level Dataset (2023–2025)

Open dataset of China's generative AI filing system, published by the Cyberspace Administration of China (CAC), aggregated to prefecture-level cities.

**DOI**: [10.5281/zenodo.23409615](https://doi.org/10.5281/zenodo.23409615)

## What's in this repo

| Folder | Contents |
|---|---|
| `data/raw/` | Four CSV files as originally collected from CAC announcements (Chinese column names), plus `city_centroids.csv` (297 Chinese prefecture-level city coordinates) |
| `data/processed/` | Cleaned CSV files with English column names and mappings |
| `scripts/` | Cleaning pipeline: run `python scripts/01_clean_registry.py` etc. |
| `notebooks/` | Example analyses: Moran's I spatial diagnostic (I=0.159, p=0.001), city network centrality, k-core decomposition |

## Quick start

```bash
pip install -r requirements.txt
python scripts/01_clean_registry.py
python scripts/02_clean_mapping.py
python scripts/03_clean_edges.py
python scripts/04_clean_audit.py
```

Outputs appear in `data/processed/`.

## Dataset overview

- **1,183 records**: 748 foundation model filings + 435 generative AI service registrations
- **1,028 filing entities** mapped to prefecture-level city, industry, ownership
- **584 app–model invocation edges** (from manual audit of 435 registered services)
- **Coverage**: 297 Chinese prefecture-level cities, Jan 2023 – Dec 2025

## Data sources

- **Filing data**: Public announcements from the Cyberspace Administration of China (CAC), www.cac.gov.cn, manually transcribed.
- **City coordinates**: `data/raw/city_centroids.csv` contains 297 Chinese prefecture-level city administrative center and centroid coordinates. Source: Alibaba Cloud DataV.GeoAtlas administrative boundary dataset (GCJ-02 coordinate system; https://datav.aliyun.com/portal/school/atlas/area_selector). Sansha (297th city) is retained in the coordinate file but excluded from spatial analyses in the example notebook.

## Citation

Shi, X. (2026). *China Generative AI Filing Registry: City-Level Dataset (2023–2025)*. Zenodo. https://doi.org/10.5281/zenodo.23409615

## License

CC-BY 4.0
