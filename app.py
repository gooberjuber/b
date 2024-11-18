import llm_hit
import bert_scoring
import dataset_reader
from abstract import AbstractClass
from typing import Dict, Any
import configparser
from validate_input import validate_input_data

d = {
  "Pipeline ID": "12345",
  "Workspace ID": "abc-xyz-001",
  "Process ID": "67890",
  "Subcomponent ID": "sub-001",
  "Component ID": "comp-001",
  "azure_blob": {
        "connection_string": "",
        "container_name": "databricks-storage-container"
    },
  "data":{
    "question": "What is color?",
    "model_endpoint": "text-embedding-3-small",  
    "llm_provider": "openai"  
  }
}


class ConcreteClassBertEval(AbstractClass):

    def on_start(self, data : dict[Any, Any]):
        """Initialize or start execution."""
        self.pipeline_id = data.get("Pipeline ID")
        self.workspace_id = data.get("Workspace ID")
        self.process_id = data.get("Process ID")
        self.subcomponent_id = data.get("Subcomponent ID")
        self.component_id = data.get("Component ID")
        self.azure_blob = data.get("azure_blob")
        self.data = data.get("data")
    
    def validate_input_data(self, data: Dict[str, Any]) -> bool:
        """Validate the input data for correctness and completeness."""
        return validate_input_data(data)
    
    def execute(self) -> Dict[str, Any]:
        """Execute the strategy."""
        pass

    def on_error(self, errordata: Dict[str, Any]):
        """Handle any error in execution and return appropriate response."""
        return_data = {
            "execution_status" : "failure",
            "Pipeline ID" : self.pipeline_id,
            "Workspace ID" : self.workspace_id,
            "Process ID" : self.process_id,
            "Subcomponent ID" : self.subcomponent_id,
            "Component ID" : self.component_id,
            "data" : errordata
        }
        return return_data

    def on_finish(self, data):
        """Handle post-execution tasks like cleanup."""
        return_data = {
            "execution_status" : "failure",
            "Pipeline ID" : self.pipeline_id,
            "Workspace ID" : self.workspace_id,
            "Process ID" : self.process_id,
            "Subcomponent ID" : self.subcomponent_id,
            "Component ID" : self.component_id,
            "data" : data
        }
        return return_data

    def preprocess_input_data(self, file: Dict[str, Any]) -> str:
        """Specific to preprocessing"""
        pass

    def store_user_preprocess_info(self, user_data: Dict[str, Any]) -> bool:
        """Store user's dataset information into the database."""
        pass

    def user_component(self, connection: Any, inputval: Dict[str, Any]) -> bool:
        """To copy the user defined components to databse"""
        pass

    def connection_db(self, db_type: str, db_config: dict) -> Any:
        """Connect to a specified database (Azure Blob, PostgreSQL, MySQL, MongoDB, DynamoDB)."""
        pass
    
    def connection_validation(self, db_type: str, connection_string: str) -> str:
        """Validate if a connection to the specified database is possible."""
        pass

    def check_data_availability(self, db_type: str, data_identifier: Any) -> bool:
        """Check the availability of data in the specified database."""
        pass

    def copy_data(self, local_file_path: str, container_name: str, connect_str:str, data_identifier: Any) -> bool:
        """Copy data from one database to another."""
        pass

    def load_config(self, config: str) -> configparser.ConfigParser:
        """Method to load the configuration details from the config file stored in DB"""
        pass

    def get_json(self, file: str) -> dict:
        """Reading json file."""
        pass

    def alert_system(self, alert_message: str, severity: str) -> None:
        """Trigger alerts based on the system's performance, security, or other events."""
        pass
    
    def explainability_monitor(self) -> Dict[str, Any]:
        """Track and provide explainability for the results generated."""
        pass
    
    def monitor_performance(self) -> None:
        """Monitor the performance metrics like execution time, resource usage."""
        pass

    def log_feedback(self, feedback: str) -> None:
        """Log feedback for the execution."""
        pass

    def adaptive_adjustments(self) -> None:
        """Automatically adapt based on feedback and environmental conditions."""
        pass

    def log_processing_data(self, data: Dict[str, Any], result: Dict[str, Any]) -> None:
        """Log input data and results for future analysis ."""
        pass


def score():
    # loads data from blob storage to dataframe
    dataset = dataset_reader.load_df("qa.csv")
    if dataset['success']:
        dataframe = dataset['data']
    print(dataframe)
    
    # loads dataset into rows
    rows = dataset_reader.get_rows_df(dataframe, "query", "answer")
    if rows['success']:
        rows = rows['data']
    
    # loading the reference sentences from dataset
    reference_sentences = [row['answer'] for row in rows]

    # creating candidate sentences from dataset queries by sending to llm
    candidate_sentences = []
    queries = [row['query'] for row in rows]
    for query in queries:
        llm_response = llm_hit.generate_single_answer(query)
        if llm_response['success'] == False:
            return {
                "success" : False,
                "error" : f"could not generate answer for query {llm_response['error']}",
                "data" : None
            }
        else:
            candidate_sentences.append(llm_response['data'])
    
    # computing bert scores
    bert_scores = bert_scoring.score('en', 'distilroberta-base', candidate_sentences, reference_sentences)

    return bert_scores
    
obj = ConcreteClassBertEval()

obj.on_start(d)
print(obj.validate_input_data(d))


    
