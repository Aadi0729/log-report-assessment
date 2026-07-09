There is an Apache-style access log located at /app/access.log.

Analyze the log and write a JSON report to:

/app/report.json

Your report must satisfy all of the following:

1. Include the total number of requests as `total_requests`.
2. Include the number of unique client IP addresses as `unique_ips`.
3. Include the most frequently requested path as `top_path`.
4. Write valid JSON to the exact output path `/app/report.json`.
