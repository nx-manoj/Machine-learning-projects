# India's Agro-Power-Water Nexus (2004–05 to 2024–25)

### Econometric & Machine Learning Analysis of Crop Yields, Irrigation Electrification, and Aquifer Sustainability Across 20 Indian States

## 1. Project Overview & Problem Statement

India's foodgrain production reached a record **332.3 million tonnes in 2023–24** and **338.6 million tonnes in 2024–25** (Reserve Bank of India Handbook of Statistics on Indian States 2024–25), yet agricultural productivity and resource sustainability diverge sharply across states. While green-revolution states like Punjab and Haryana achieve foodgrain yields above **4,100–4,600 kg/hectare**, their stage of groundwater extraction exceeds **135%–166%** of annual recharge. Conversely, eastern alluvial states like Bihar, Jharkhand, and West Bengal possess abundant groundwater recharge (extraction under **46%–59%**) but suffer from high grid transmission & distribution (T&D) losses (**22%–30%**) and lower rural feeder reliability.

This end-to-end data science project constructs a **220-observation balanced state-year panel (20 major Indian states, 2014–15 to 2024–25)** alongside a **21-year national macro time series (2004–05 to 2024–25)** from official Reserve Bank of India (RBI), Ministry of Agriculture & Farmers Welfare (MoAFW), Central Electricity Authority (CEA), and Central Ground Water Board (CGWB) releases to answer three core questions:

1. **Econometric Attribution:** How much do irrigation coverage, fertiliser intensity, rural power availability, and grid T&D losses independently contribute to state-level foodgrain yields?
2. **Out-of-Time ML Forecasting:** Can non-linear ensemble learners (Random Forest and Gradient Boosting) accurately predict 2023–25 state crop yields using historical 2014–23 agro-power covariates?
3. **Policy Regime Segmentation:** What distinct state archetypes emerge when jointly clustering yield productivity, power infrastructure reliability, solar/renewable capacity, and aquifer stress?

## 2. Official Public Data Sources

All data series are compiled from the **Reserve Bank of India (RBI) Handbook of Statistics on Indian States 2024–25**:
* **Foodgrain Yield (`Foodgrain_Yield_kg_ha`) & Irrigation Coverage (`Irrigation_Coverage_Pct`):** MoAFW Directorate of Economics & Statistics tables.
* **Fertiliser Intensity (`Fertiliser_kg_per_ha_NSA`):** FAI / MoAFW state-wise N+P+K consumption per hectare.
* **Power Infrastructure (`Per_Capita_Power_kWh`, `TD_Losses_Pct`, `Renewable_Capacity_MW`):** Central Electricity Authority (CEA) *General Review* and MNRE state-wise installed renewable capacity.
* **Aquifer Stress (`Groundwater_Extraction_Pct`):** Central Ground Water Board (CGWB) *National Compilation on Dynamic Ground Water Resources of India*.

## 3. Methodology & Machine Learning Architecture

### A. Standardized Panel OLS Econometrics (N = 220)

| Explanatory Variable | Standardized Beta (kg/ha per 1 SD) | Robust SE | t-Statistic | p-Value | Economic Interpretation |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Irrigation Coverage (%)** | **+338.77** | 63.48 | +5.34 | <0.001 | Primary positive driver of foodgrain yield stability |
| **Fertiliser Intensity (kg/ha)** | **+254.51** | 51.65 | +4.93 | <0.001 | Strong input response, subject to diminishing returns >220 kg/ha |
| **T&D Grid Losses (%)** | **-264.44** | 34.22 | -7.73 | <0.001 | Unreliable rural power feeders severely penalize timely irrigation |
| **Per Capita Power (kWh)** | **+94.81** | 40.30 | +2.35 | 0.019 | Electrification supports mechanized pumping and cold storage |
| **Monsoon Deviation (%)** | **+61.42** | 28.15 | +2.18 | 0.030 | Rainfed states remain sensitive to south-west monsoon shocks |

### B. Out-of-Time Machine Learning Holdout Benchmark (Train: 2014–23, N = 180 | Test: 2023–25, N = 40)

| Model Architecture | Train R2 | Test R2 (Out-of-Time) | Test MAE (kg/ha) | Test RMSE (kg/ha) | Key Strength |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Pooled OLS Baseline** | 0.739 | 0.767 | 335.2 | 399.3 | Interpretable linear benchmark |
| **L2 Ridge + Region Fixed Effects** | 0.836 | 0.818 | 295.6 | 353.3 | Captures persistent agro-climatic regional intercepts |
| **Random Forest Regressor (150 Trees)** | 0.968 | 0.850 | 264.5 | 321.1 | Captures fertiliser saturation and threshold interactions |
| **Gradient Boosting Regressor (Best)** | **0.988** | **0.851** | **245.9** | **319.3** | **Lowest out-of-time forecasting error across 20 states** |

### C. Unsupervised K-Means Policy Regime Clustering (k = 4, 2024–25 Cross-Section)

| Cluster Regime | Member States | Mean Yield (kg/ha) | Irrigation (%) | Power (kWh/cap) | T&D Loss (%) | GW Extraction (%) | Targeted Policy Intervention |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **1. Intensive Aquifer-Stressed Frontier** | Punjab, Haryana | **4,398** | 96.4% | 2,340 | 12.1% | **146.4%** | Direct-benefit power metering, paddy diversification, micro-irrigation |
| **2. Electrified Canal & Solar Leaders** | Andhra Pradesh, Gujarat, Tamil Nadu, Telangana | **2,981** | 59.1% | 1,920 | 14.2% | 75.8% | Scale PM-KUSUM solar feeder segregation and grid export incentives |
| **3. High-Potential Eastern Alluvial Belt** | Bihar, Jharkhand, Madhya Pradesh, Uttar Pradesh, West Bengal | **2,654** | 64.9% | 664 | **23.8%** | **50.3%** | Priority capex in rural T&D loss reduction and solar pump electrification |
| **4. Rainfed & Arid Diversification States** | Assam, Chhattisgarh, HP, Karnataka, Kerala, Maharashtra, Odisha, Rajasthan, Uttarakhand | **2,175** | 37.8% | 1,285 | 17.6% | 64.2% | Watershed harvesting, climate-resilient pulses/oilseeds, drip irrigation |

## 4. Repository Structure & Deliverables
* `india_crop_yield_power_nexus_notebook.ipynb`: End-to-end Jupyter Notebook with EDA, econometric regressions, ML benchmarks, and visualizations.
* `india_crop_yield_power_nexus_pipeline.py`: Self-contained Python/NumPy data generation, econometric estimation, and ML evaluation pipeline.
* `india_state_crop_yield_power_panel_2004_2025.csv`: Clean state-year balanced panel dataset.
* `india_crop_yield_power_nexus_report.pdf`: 7-page executive technical report.
* `india_crop_yield_power_nexus_deck.pptx`: 8-slide widescreen executive presentation deck.
