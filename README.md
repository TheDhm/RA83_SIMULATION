# Ricart and Agrawala 1983 (RA83) SIMULATION
## About
A simulation of RA83 with 10 containers (running a simple django server) as 10 nodes, and a watchdog server to watch the evolution of the algorithm.
## Requirements
* Docker
* Django
## Getting Started
1. Build the 'ra83-server' image using dockerfile 'RA83D/Dockerfile'
2. in /ra83_watchdog : migrate and create a superuser 
3. Run the Django server 'ra83_watchdog' on port 8000
4. create 10 worker instances using django admin
5. Deploy the containers: run 'RA83D/start_servers.py'
6. visit http://localhost:8000 , refresh to load changes