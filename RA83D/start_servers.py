import docker

client = docker.from_env()
server_name = "worker_"
port = 8100

for i in range(10):
    print(server_name+str(i+1))
    client.containers.run(image="ra83-server",
                          detach=True,
                          ports={'8000/tcp': port},
                          name=server_name+str(i+1),
                          environment=[f"WORKER_NAME={i+1}"])
    port += 1
