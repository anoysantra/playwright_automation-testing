# Step 1: Start with the official Microsoft Playwright Python base image
FROM ://microsoft.com
# Step 2: Set the folder inside the container where your code will live
WORKDIR /app
# Step 3: Copy only the dependencies file first (optimizes Docker caching)
COPY requirements.txt .

# Step 4: Install your Python testing libraries (pytest, requests, etc.)
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of your local automation test code into the container
COPY . .

# Create the reports folder so pytest can write the results into it
RUN mkdir -p reports

# Set the environment variable so Python can find your root modules (pages, utils)
ENV PYTHONPATH=/app

# Command to run ALL tests inside the 'tests' folder and output the HTML report
CMD ["pytest", "tests", "-v", "--html=playwright-report/report.html", "--self-contained-html"]
