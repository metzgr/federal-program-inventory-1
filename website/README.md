# Federal Program Inventory (FPI) website

## Building the website
The FPI website is generated using data from SAM.gov and USASpending.gov. This repository contains all of the information used to build the current FPI website.

The website is built using [Jekyll](https://github.com/jekyll/jekyll), a widely-used open-source static site generator, as well as the [U.S. Web Design System](https://github.com/uswds/uswds). The site is generated inside of an isolated Docker container. This container builds the website using Jekyll and packages the resulting files into an [nginx-unprivileged](https://github.com/nginxinc/docker-nginx-unprivileged) image for deployment.

## Preview locally with data (recommended)
This runs the full stack (Elasticsearch, API, indexer, website) via Docker Compose so the site is populated with data.

Prerequisites:
- Docker Desktop

If you are behind a corporate proxy (e.g., Zscaler):
- Export your proxy/root CA as PEM (.crt) and place it in `website/certs/` (this folder is gitignored). The Docker build will trust any `*.crt` in that directory.

Steps (from the repository root):

1. Start Elasticsearch and API
   - `docker compose up -d --build elasticsearch`
   - `docker compose up -d --build api`
2. Load data into Elasticsearch (one-time per session)
   - `docker compose run --rm indexer`
   - Optional: verify documents exist → `curl http://localhost:9200/programs/_count`
3. Start the website
   - `docker compose up -d --build website`
   - Open http://localhost:8080

Notes:
- For local development, the frontend is configured to call the API on `http://localhost:8000`. If you change API host/port, update the value in `website/_includes/_footer-search.html` (`apiBaseUrl`).
- To stop the stack: `docker compose down`

## Quick static preview (no live data)
This runs only the static website container (useful for layout/HTML/CSS checks). The program list and search features will appear empty without the API.

From `/website/`:
1. `docker build -t fpi-website .`
2. `docker run -p 4000:8080 --rm --name fpiweb fpi-website`
3. Open http://localhost:4000

## Data extraction
To learn more about the data that powers the FPI website and how to update it, navigate to the [data_extraction](data_extract/README.md) sub-directory.

## Deploying the website

### Github Actions
When a new commit is made to the `release` branch, Github Actions will automatically trigger a build of the website using the process described above. Once completed, this will create a new deployable package on Github Packages.