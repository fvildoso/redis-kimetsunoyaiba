# redis-kimetsunoyaiba

Este proyecto llamado `redis-kimetsunoyaiba` es una aplicación de ejemplo que utiliza Python 3.10 para conectarse a una
instancia de Redis y realizar operaciones básicas de lectura y escritura de variables.

## Requisitos previos

Asegúrate de tener instalado lo siguiente:

- Python 3.10 (puedes descargarlo desde <code>aquí</code>)
- Otros paquetes y dependencias especificados en el archivo <code>requirements.txt</code>

Además, para trabajar de manera más rápida y sencilla con una instancia de Redis, se recomienda utilizar Docker. Docker
es una plataforma de contenedores que permite crear y ejecutar aplicaciones en entornos aislados.

Para instalar Redis utilizando Docker, sigue los siguientes pasos:

1. Instala Docker en tu sistema operativo siguiendo las instrucciones correspondientes a tu plataforma: Windows, macOS o
   Linux. Puedes encontrar las instrucciones de instalación en el sitio web oficial de Docker.

2. Una vez que Docker esté instalado, abre una terminal o línea de comandos y ejecuta el siguiente comando para
   descargar y ejecutar una instancia de Redis:

Sin persistencia de datos.

   ```bash
   docker run -d --name redis-container -p 6379:6379 redis:latest redis-server --appendonly no --save ""
   ```

Con persistencia de datos.

   ```bash
   docker run --name redis-container -p 6379:6379 -d redis
   ```

## Configuración

Antes de ejecutar la aplicación, asegúrate de configurar correctamente los siguientes parámetros en el archivo <code>
.env</code>:

```
REDIS_HOST = 'localhost'      # Dirección IP o nombre de host de la instancia de Redis.
REDIS_PORT = 6379             # Puerto de la instancia de Redis.
REDIS_PASSWORD =          # Contraseña de autenticación de la instancia de Redis (si es necesario).
```

Si tu instancia de Redis tiene una contraseña de autenticación, asegúrate de proporcionarla en la variable <code>
REDIS_PASSWORD</code>. De lo contrario, déjala en blanco.

## Uso

Una vez que hayas configurado los parámetros adecuados, puedes ejecutar la aplicación utilizando el siguiente comando:

<code>python main.py</code>

La aplicación se conectará a la instancia de Redis y realizará las siguientes operaciones:

1. Escribir una variable en Redis.
2. Leer el valor de la variable escrita.
3. Escribir un JSON en Redis.
4. Leer el JSON de Redis.
5. Parsear el JSON a un diccionario en Python.

Los resultados de cada operación se mostrarán en la consola.

## Contribución

Si deseas contribuir a este proyecto, siéntete libre de hacer un fork y enviar tus pull requests. Agradezco cualquier
mejora o corrección de errores que puedas proporcionar.

## Licencia

Este proyecto se distribuye bajo la licencia <code>MIT</code>. Si utilizas el código de este proyecto, asegúrate de
cumplir con los términos de la licencia.

---

Espero que este README sea útil para comprender cómo utilizar <code>redis-kimetsunoyaiba</code> y realizar operaciones
básicas de lectura y escritura en Redis desde Python 3.10. Si tienes alguna pregunta o problema, no dudes en abrir un
issue en el repositorio del proyecto. ¡Disfruta usando Redis con Kimetsu no Yaiba!
