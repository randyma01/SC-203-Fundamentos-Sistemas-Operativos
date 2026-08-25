import socket
from flask import Flask

app = Flask(__name__)

@app.route('/')


def hello():
    hostname = socket.gethostname()
    return f"""
    <div style='font-family: Arial, sans-serif; text-align: center; margin-top: 50px;'>
        <h1 style='color: #2b5797;'>🚀 Proyecto SC-203: Docker Swarm</h1>
        
        <h2>Respuesta servida por el Contenedor/Nodo: 
            <span style='color: #e74c3c;'>{hostname}</span>
        </h2>
        
        <p>¡El tráfico web está siendo balanceado entre las réplicas del clúster!</p>
    </div>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)