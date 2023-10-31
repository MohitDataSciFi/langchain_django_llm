from django.shortcuts import render
from django.http import JsonResponse
from . import langchain_helper
import logging
import os

# # Set the base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Set up logging
log_filename = os.path.join(BASE_DIR, 'chatbot.log')
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def chat(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        chain = langchain_helper.get_qa_chain()

        try:
            # Process the chat and get the response
            response = chain(message)

            # Log the message and response
            logger.info(f'Message: {message}')
            logger.info(f'Response: {response["result"]}')

            # Return the response
            return JsonResponse({'message': message, 'response': response['result']})
        
        except Exception as e:
            # Log the error
            logger.error(str(e))

            # Handle the error and return an appropriate response
            return JsonResponse({'error': str(e)})
    
    return render(request, 'chatbot.html')