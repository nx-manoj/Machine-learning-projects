# Machine Learning Projects

A collection of end-to-end data-science projects — each one takes a raw dataset through cleaning, exploratory analysis and modelling, and reports where the result can and cannot be trusted.

## Projects

| Project | Task | What's inside |
|---|---|---|
| **|d[Ia-Agro-Power-Water-Nexus](./India-Agro-Power-Water-Nexus)** | Econometric & ML | Econometric & Machine Learning Analysis of Crop Yields, Irrigation Electrification, and Aquifer Sustainability Across 20 Indian States, 2004–2025 — Panel OLS, Ridge FE, Random Forest, Gradient Boosting & K-Means Policy Clustering |
| **[Bengaluru-Housing-Prices](Bengaluru-Housing-Prices/)** | Regression | 13,320 Bengaluru property listings. Cleaning rules with counts, EDA, five models compared on 5-fold CV, held-out evaluation at ₹27.6 L MAE. Notebook + 6-page report + 11-slide deck. |
| **[BullDozer](BullDozer/)** | Regression | Bulldozer sale-price prediction. |
| **[Heart Disease Analysis](notebooks/Heart%20Disease%20Analysis.ipynb)** | Classification | Exploratory analysis on the heart-disease dataset in [`data/`](data/). |

## The Bengaluru case study

The most complete project in this repo. Short version:

- **Built-up area** is the strongest driver of asking price (r = 0.74).
- **Locality** sets the rate — the same square foot costs **₹2,885** in Attibele and **₹13,719** in Rajaji Nagar, a **4.8×** spread.
- A **3BHK** asks 51% more than a 2BHK in the same locality but offers only 37% more floor area — about 10% is configuration premium.
- A gradient-boosted model prices a held-out listing to a **17.7%** median error, and **systematically under-predicts above ₹150 lakh**.

Start here: [`Bengaluru-Housing-Prices/README.md`](Bengaluru-Housing-Prices/README.md)

## Conventions

Every project folder carries its own README, requirements and reproducible notebook. Data is either committed alongside the project or linked in that project's README. Random seeds are fixed so results regenerate exactly.

## Setup

```bash
git clone https://github.com/nx-manoj/Machine-learning-projects.git
cd Machine-learning-projects/<project-folder>
pip install -r requirements.txt
jupyter notebook
```
