from typing import Dict, Any
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_input_data(data: Dict[str, Any]) -> bool:
    """Validate the input data for correctness and completeness."""

    needed_params = ["Pipeline ID", "Workspace ID", "Process ID", "Subcomponent ID", "Component ID", "data", "azure_blob"]

    for param in needed_params:
        if param not in data:
            logger.error(f"needed param {param} not present in input data")
            return {"success" : True, "data" : False, "error" : None}
    if "connection_string" not in data['azure_blob'] or "container_name" not in data['azure_blob']:
        logger.error(f"needed param container_name or connection_string not present in azure_blob")
        return {"success" : True, "data" : False, "error" : None}
    
    return {"success" : True, "data" : True, "error" : None}


