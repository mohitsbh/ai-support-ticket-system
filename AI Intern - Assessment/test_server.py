import subprocess, sys, os, time, requests
os.chdir(r'C:\Users\msbho\Downloads\AI Intern - Assessment')
proc = subprocess.Popen([sys.executable, '-m', 'uvicorn', 'main:app', '--host', '0.0.0.0', '--port', '8080'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(5)
try:
    r = requests.get('http://localhost:8080/')
    print('Root status:', r.status_code, 'Length:', len(r.text))
    r = requests.get('http://localhost:8080/api/health')
    print('Health:', r.json()['status'])
    r = requests.post('http://localhost:8080/api/query', json={'question': 'How many tickets are open?'})
    print('Query:', r.json()['answer'])
    r = requests.get('http://localhost:8080/api/anomalies?days=30')
    a = r.json()
    print('Anomalies:', a['summary']['total_anomalies'])
    print('\nALL WORKING!')
except Exception as e:
    print('Error:', e)
finally:
    proc.kill()