# 📊 Armenian Business Registry Pipeline & Data Extractor

An automated, high-throughput asynchronous data pipeline engineered to extract, normalize, clean, and structure corporate entity datasets directly from the official Government Registry of the Republic of Armenia (`e-register.am`).

---

## ⚡ Core Architecture & Engineering Impact

* **High-Throughput Ingestion Pipeline:** Architected an end-to-end extraction pipeline capable of parsing and processing mass datasets containing over **23,000+ corporate records**.
* **Deterministic Lifecycle Filtering:** Built a logical data-cleaning layer that automatically detects and strips inactive or liquidated entities, isolating a clean, operational matrix of **13,000+ active businesses**.
* **Chronological Ingestion Sorting:** Developed a timestamp-sorting mechanism that indexes entities based on their official registration dates, prioritizing the freshest business leads for immediate downstream consumption.

---

## 🛠️ Technical Stack & Implementation Details

* **Asynchronous Networking (`Python 3.12` / `asyncio` + `httpx`):** Implemented non-blocking I/O event loops to orchestrate highly concurrent HTTP requests, slashing total extraction latency and pulling large-scale registry assets within seconds without degrading system performance.
* **Semantic HTML Parsing (`BeautifulSoup4`):** Engineered robust DOM selectors to deconstruct complex raw HTML payloads, reliably extracting specific data points such as Legal Entity Names, Operational Addresses, and Incorporation Statuses.
* **Storage Optimization (`JSON` / `JSONL`):** Streamlined storage throughput by writing datasets into structured JSON Lines (`.jsonl`) format, allowing memory-efficient, line-by-line streaming of massive files without loading the entire payload into RAM.
* **Data Sanitization & Regex Guards (`Regular Expressions`):** Deployed precise tokenization and pattern-matching logic to eliminate raw string anomalies, structural noise, and corrupted records during the transformation stage.
