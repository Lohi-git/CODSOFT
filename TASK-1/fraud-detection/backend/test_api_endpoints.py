import urllib.request
import urllib.error
import json

BASE_URL = 'http://127.0.0.1:5000'

LEGIT_SAMPLE = [
    -1.3598071336738, -0.0727811733098497, 2.53634673796914, 1.37815522427443, -0.338320769942518, 
    0.462387777762292, 0.239598554061257, 0.0986979012610507, 0.363786969611213, 0.0907941719789316, 
    -0.551599533260813, -0.617800855762348, -0.991389847235408, -0.311169353699879, 1.46817697209427, 
    -0.470400525259478, 0.207971241929242, 0.0257905801985591, 0.403992960255733, 0.251412098239705, 
    -0.018306777944153, 0.277837575558899, -0.110473910188767, 0.0669280749146731, 0.128539358273528, 
    -0.189114843888824, 0.133558376740387, -0.0210530534538215, 149.62
]

FRAUD_SAMPLE = [
    -2.3122265423263, 1.95199201064158, -1.60985073229769, 3.9979055875468, -0.522187864667764, 
    -1.42654531920595, -2.53738730624579, 1.39165724829804, -2.77008927719433, -2.77227214465915, 
    3.20203320709635, -2.89990738849473, -0.595221881324605, -4.28925378244217, 0.389724120274487, 
    -1.14074717980657, -2.83005567450437, -0.0168224681808257, 0.416955705037907, 0.126910559061474, 
    0.517232370861764, -0.0350493686052974, -0.465211076182388, 0.320198198514526, 0.0445191674731724, 
    0.177839798284401, 0.261145002567677, -0.143275874698919, 0.0
]

def make_request(path, method='GET', payload=None):
    url = f"{BASE_URL}{path}"
    headers = {}
    data = None
    if payload is not None:
        data = json.dumps(payload).encode('utf-8')
        headers = {'Content-Type': 'application/json'}
    
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as response:
            status = response.status
            body = response.read().decode('utf-8')
            return status, json.loads(body)
    except urllib.error.HTTPError as e:
        status = e.code
        body = e.read().decode('utf-8')
        try:
            return status, json.loads(body)
        except:
            return status, body
    except Exception as e:
        return 0, str(e)

def test_root():
    print("\n--- Testing Root Endpoint (/) ---")
    status, response = make_request('/')
    print(f"Status: {status}")
    print(f"Response: {response}")
    assert status == 200
    print("PASS")

def test_health():
    print("\n--- Testing Health Endpoint (/health) ---")
    status, response = make_request('/health')
    print(f"Status: {status}")
    print(f"Response: {response}")
    assert status == 200
    assert response['status'] == 'ok'
    assert response['model_loaded'] is True
    print("PASS")

def test_predict_legit():
    print("\n--- Testing Predict Endpoint (/predict) - Legit Sample ---")
    payload = {"features": LEGIT_SAMPLE}
    status, response = make_request('/predict', method='POST', payload=payload)
    print(f"Status: {status}")
    print(f"Response: {response}")
    assert status == 200
    assert response['label'] == 'LEGIT'
    assert response['prediction'] == 0
    print("PASS")

def test_predict_fraud():
    print("\n--- Testing Predict Endpoint (/predict) - Fraud Sample ---")
    payload = {"features": FRAUD_SAMPLE}
    status, response = make_request('/predict', method='POST', payload=payload)
    print(f"Status: {status}")
    print(f"Response: {response}")
    assert status == 200
    assert response['label'] == 'FRAUD'
    assert response['prediction'] == 1
    print("PASS")

def test_predict_invalid_features():
    print("\n--- Testing Predict Endpoint (/predict) - Invalid Features (28 columns instead of 29) ---")
    payload = {"features": LEGIT_SAMPLE[:-1]} # drop Amount
    status, response = make_request('/predict', method='POST', payload=payload)
    print(f"Status: {status}")
    print(f"Response: {response}")
    assert status == 400
    assert "expected 29 features" in response['error']
    print("PASS")

def test_predict_empty_payload():
    print("\n--- Testing Predict Endpoint (/predict) - Empty Payload ---")
    status, response = make_request('/predict', method='POST', payload={})
    print(f"Status: {status}")
    print(f"Response: {response}")
    assert status == 400
    assert "missing features" in response['error']
    print("PASS")

if __name__ == "__main__":
    test_root()
    test_health()
    test_predict_legit()
    test_predict_fraud()
    test_predict_invalid_features()
    test_predict_empty_payload()
