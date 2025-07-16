from feature_extractor import extract_features

# Test some sample URLs
test_urls = [
    "https://secure-login.bankofamerica.com",
    "http://192.168.0.1/evil",
    "https://google.com",
    "http://example.com/login?user=admin"
]

for url in test_urls:
    features = extract_features(url)
    print(f"URL: {url}\nFeatures: {features}\n")
