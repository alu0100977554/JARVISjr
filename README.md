# JARVIS-Jr

Asistente virtual JARVIS-Jr para la asignatura Sistemas Inteligentes de la Universidad Politécnica de Madrid.


## Usage


JARVIS-Jr funciona completamente por comandos de voz. Los comandos reconocidos son:
- Jarvis: diciendo una oración con esta palabra, entra en modo asistente, que permitirá realizar un tarea según uno de los siguientes comandos:
	- Reproduce: un vídeo en YouTube.
	- Busca: información en Google.
	- Qué es o quién: busca un artículo de Wikipedia.
	- Hora: dice la hora actual. 
	- Chiste: cuenta un chiste de informáticxs.
	- Entra en modo sin barreras: para establecer la conexión con GPT-3.
	- Apágate: cierre del programa.
- Si se le habla sin decir la palabra Jarvis, se entiende que se quiere establecer una conversación y entrará en modo chatbot. Dependiendo de lo que se diga, asignará la frase a una categoría y ofrecerá una respuesta acorde a dicha categoría. La categorías reconocidas son:
	- Bienvenida. Hola, ey, buenos días...
	- Despedida. Adiós, hasta pronto...
	- Información. Qué eres...
	- Creadores. Quién te creó...
	- Funcionalidades. Qué puedes hacer...

## Posibles problemas

- Es probable que el bot no entienda a la primera lo que se le dice. Es importante seguir el orden de ejecución de los comandos.
- El modo experimental no funciona correctamente porque GPT-3 no reconoce el español a través de la conexión establecida. Se espera una respuesta en inglés sobre algo que no se ha pedido si se le pregunta cualquier cosa.
- La conexión con GPT-3 se establece a gracias a una clave privada. En caso de fallo, se debe a que dicha clave ha caducado. He creado una nueva clave a la hora de subir los ficheros a GitHub. Si vuelve a fallar, pónganse en contacto conmigo.
