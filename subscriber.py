import redis

# Configuración de la conexión
redis_url = 'tu_redis_url'
redis_password = 'tu_redis_password'

client = redis.StrictRedis.from_url(redis_url, password=redis_password)

# Suscribirse a un canal
channel = 'mi_canal'
pubsub = client.pubsub()
pubsub.subscribe(channel)

print(f"Suscrito al canal: {channel}")

# Procesar mensajes
for message in pubsub.listen():
    if message['type'] == 'message':
        print(f"Mensaje recibido: {message['data'].decode('utf-8')}")
