import redis
import time

# Configuración de la conexión
redis_url = 'tu_redis_url'
redis_password = 'tu_redis_password'

client = redis.StrictRedis.from_url(redis_url, password=redis_password)

# Publicar mensajes en un canal
channel = 'mi_canal'

while True:
    message = input("Introduce el mensaje a publicar: ")
    client.publish(channel, message)
    print(f"Mensaje publicado: {message}")
    time.sleep(1)
