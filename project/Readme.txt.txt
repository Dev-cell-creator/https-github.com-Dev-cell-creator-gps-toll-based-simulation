This project simulates an automated toll collection system using 
GPS and vehicle detection. Key features include vehicle detection
with OpenCV, GPS-based distance calculation with Geopy,
toll computation based on vehicle type and distance, 
and a simulated payment gateway for automatic toll deduction. 
Built with Flask, it provides a web interface for dynamic toll 
calculation and payment simulation.

Steps to be followed:

	Clone the Repository:

		git clone https://github.com/your-repo/gps-toll-simulation.git
		cd gps-toll-simulation
	
	Create and Activate a Virtual Environment:

		python -m venv venv
		On Windows: venv\Scripts\activate
		On macOS/Linux: source venv/bin/activate
	
	Install Required Packages:

		pip install Flask opencv-python geopy

	Run the program:
	
		python app.py