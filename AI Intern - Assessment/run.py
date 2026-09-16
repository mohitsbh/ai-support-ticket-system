import uvicorn
from main import app

def main():
	print("Starting AI Support Ticket Analysis System...")
	print("Server running at http://127.0.0.1:8080")
	uvicorn.run(app, host="0.0.0.0", port=8080)


if __name__ == "__main__":
	main()