# Machine Learning, Web Scraping and FastAPI Projects

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)

Machine learning notebooks, four web scrapers and a FastAPI product API in one repository.

| Folder | What's inside |
|---|---|
| [`machine learning/`](machine%20learning) | Regression, classification, model tuning, ensemble and clustering notebooks, plus a heart disease prediction app |
| [`web scrapping/`](web%20scrapping) | Scrapers for Amazon, an Apple Store page, Booking.com and Worldometers |
| [`fast-api ecommerce peoject/`](fast-api%20ecommerce%20peoject) | Product management REST API with validated product data |

## Machine learning

Jupyter notebooks built with pandas, scikit-learn, Matplotlib and Seaborn. Each project goes from EDA and cleaning to a trained, evaluated model.

| Topic | Notebooks | What they cover |
|---|---|---|
| EDA and preprocessing | `part 1/heart_project`, `part 1/insurance_project` | Exploring, cleaning, encoding and scaling the heart disease and insurance datasets, and feature engineering |
| Regression | `part 2/car price predict`, `part 2/insurance project` | Car price prediction on Ford data (one-hot vs label encoding) and insurance charges prediction with linear regression, evaluated with R² and adjusted R² |
| Classification | `part 3/logistic regression`, `knn`, `naive bayes`, `decision tree`, `svm` | Titanic survival prediction with five algorithms, compared with accuracy, F1 score and classification reports |
| Heart disease app | `part 3/final project` | Compares five classifiers, saves the best model (logistic regression) and serves it in a Streamlit app |
| Model tuning | `part 4/cross validation`, `grid search sv`, `random search cv` | Cross-validation on Titanic, and grid and random search for SVM hyperparameters on Iris |
| Ensemble learning | `part 4/ensemble learning` | Stacking, bagging (random forest) and boosting (AdaBoost, gradient boosting, XGBoost) on Iris |
| Unsupervised learning | `part 4/unsupervised learning` | K-means, DBSCAN vs K-means on non-linear clusters, and PCA dimensionality reduction |

Run the heart disease prediction app:

```bash
cd "machine learning/part 3/final project"
pip install streamlit pandas scikit-learn joblib
streamlit run app.py
```

Enter the patient's details (age, sex, chest pain type, blood pressure, cholesterol and more) and the app predicts the risk of heart disease.

## Web scrapers

Built with Requests, BeautifulSoup and pandas. Each one saves its results to a CSV file.

| Scraper | File | What it collects |
|---|---|---|
| Amazon product | `p1_amazon product/app.py` | Title, price, rating, bullet points and customer reviews from a product page |
| Apple Store page | `p2_apple store/scrap_store.py` | Page header, menu items, and each product's name, price, quantity, rating and estimated shipping, from a saved HTML page |
| Booking.com hotels | `p3_bookings/scrape_bookings.py` | Paste a Booking.com search results link and a file name; it saves each hotel's name, location, price, rating, score, reviews and link |
| World population | `p4_scrape_tables/table_scraping.ipynb` | Population tables from Worldometers |

```bash
cd "web scrapping/p3_bookings"
pip install requests beautifulsoup4 pandas
python scrape_bookings.py
```

## FastAPI product API

A REST API over 100 sample products stored in `products.json`. Pydantic models validate every product, including UUIDs, seller emails and website URLs, and positive dimensions.

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | List products. Filter by `name`, and page through results with `limit` (default 10) and `offset` |
| `GET` | `/{product_id}` | Get one product |
| `POST` | `/` | Add a product (returns `201`) |
| `PUT` | `/{product_id}` | Update a product |
| `DELETE` | `/{product_id}` | Delete a product |

```bash
cd "fast-api ecommerce peoject"
pip install fastapi uvicorn "pydantic[email]" python-dotenv
uvicorn main:app --reload
```

Interactive docs are at http://127.0.0.1:8000/docs.

## Author

**Hassan Khursheed** · [github.com/hassankhursheed](https://github.com/hassankhursheed)
