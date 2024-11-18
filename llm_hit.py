import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_single_answer(query : str):
    try:
        # this dummy data shall be replaced by an api call to an llm by passing the query to that api and receiving a response for that query
        dummy_data = {
            "q1" : "a1",
            "q2" : "a2",
            "q3" : "a3"
        }

        return {
            "success" : True,
            "data" : dummy_data[query],
            "error" : None
        }
    
    except Exception as e:
        logger.error(f"generate_single_answer {str(e)}")
        return {
            "success" : False,
            "data" : None,
            "error" : str(e)
        }


