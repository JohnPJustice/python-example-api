Install Prequisites

## For local development
pip install --user pipenv

## For Container development
docker build -t {your-image-name}
docker run -d -p 3000:3000 {your-image-name}


Basic starting point for a containerized python API using tornado.