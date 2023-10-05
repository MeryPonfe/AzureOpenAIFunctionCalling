# AzureOpenAIFunctionCalling
PoC Azure OpenAI Function calling

Hotel Search Chatbot
 
Este proyecto implementa un chatbot de búsqueda de hoteles utilizando la API de OpenAI y Gradio. El chatbot puede procesar solicitudes de búsqueda de hoteles en función de la ubicación, el precio máximo y las características deseadas.

Requisitos
 
Para ejecutar este proyecto, asegúrate de tener instaladas las siguientes librerías:
os
openai
json
gradio
python-dotenv


Puedes instalar estas librerías utilizando pip:
pip install openai json gradio python-dotenv  
 

Configuración
 
Antes de ejecutar el script, crea un archivo .env con las credenciales de la API de OpenAI. El archivo debe tener el siguiente formato:
OPENAI_API_TYPE="your_api_type"  
OPENAI_API_KEY_ALL="your_api_key"  
OPENAI_API_BASE_ALL="your_api_base"  
OPENAI_API_VERSION_ALL="your_api_version"  
 
Reemplaza los valores con tus credenciales de API.


Ejecución
Para ejecutar el chatbot, simplemente ejecuta el script:
python search-hotels.py  
 

Una vez que el chatbot se esté ejecutando, se lanzará una interfaz de Gradio en el navegador web. Puedes chatear con el bot escribiendo mensajes en el cuadro de texto y presionando Enter.

El chatbot procesará los mensajes y devolverá información de hoteles relevantes basada en las solicitudes de búsqueda cuando el usuario lo solicite.

Funciones
El archivo hotel.py contiene las siguientes funciones:
search_hotels(): Busca hoteles en función de los parámetros proporcionados, como ubicación, precio máximo y características deseadas.
format_hotel_info(): Devuelve el resultado de los hoteles encontrados en formato texto para poder mostrar en el chatbot la información legible.
