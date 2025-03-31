import joblib 
from sentence_transformers import SentenceTransformer

model_embedding = SentenceTransformer('all-MiniLM-L6-v2')
model = joblib.load(r'E:\Projects\Log classification\model\log_classifier.joblib')

def classify_log_message(log_message):

    embedding = model_embedding.encode(log_message )

    # Check if the maximum probability is less than 0.5
    # If so, return "Unknown" or any other label you prefer
    probability = model.predict_proba([embedding])[0]
    if max(probability)< 0.5:
        return "Unknown"

    # Predict the label using the loaded model
    predicted_label = model.predict([embedding])[0]

    return predicted_label


if __name__ == "__main__":
    logs = [
        "alpha.osapi_compute.wsgi.server - 12.10.11.1 - API returned 404 not found error",
        "GET /v2/3454/servers/detail HTTP/1.1 RCODE   404 len: 1583 time: 0.1878400",
        "System crashed due to drivers errors when restarting the server",
        "Hey bro, chill ya!",
        "Multiple login failures occurred on user 6454 account",
        "Server A790 was restarted unexpectedly during the process of data transfer"
    ]
    for log in logs:
        label = classify_log_message(log)
        print(log, "->", label)