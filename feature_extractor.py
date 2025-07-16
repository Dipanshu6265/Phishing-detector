def extract_features(url):
    features = []

    # Feature 1: URL Length
    features.append(len(url))

    # Feature 2: Count of '.'
    features.append(url.count('.'))

    # Feature 3: Contains 'https'
    features.append(int('https' in url.lower()))

    # Feature 4: Contains '@'
    features.append(int('@' in url))

    # Feature 5: Contains '//'
    features.append(int('//' in url))

    # Feature 6: Contains '-'
    features.append(int('-' in url))

    # Feature 7: Contains 'login'
    features.append(int('login' in url.lower()))

    return features
