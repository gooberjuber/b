from abc import ABC, abstractmethod
from typing import Any, Dict
import configparser


class AbstractClass(ABC):

    @abstractmethod
    def on_start(self):
        """Initialize or start execution."""
        pass

    @abstractmethod
    def validate_input_data(self, data: Dict[str, Any]) -> bool:
        """Validate the input data for correctness and completeness."""
        pass

    @abstractmethod
    def preprocess_input_data(self, file: Dict[str, Any]) -> str:
        """Specific to preprocessing"""
        pass

    @abstractmethod
    def store_user_preprocess_info(self, user_data: Dict[str, Any]) -> bool:
        """Store user's dataset information into the database."""
        pass

    @abstractmethod
    def user_component(self, connection: Any, inputval: Dict[str, Any]) -> bool:
        """To copy the user defined components to databse"""
        pass

    @abstractmethod
    def connection_db(self, db_type: str, db_config: dict) -> Any:
        """Connect to a specified database (Azure Blob, PostgreSQL, MySQL, MongoDB, DynamoDB)."""
        pass
    
    @abstractmethod
    def connection_validation(self, db_type: str, connection_string: str) -> str:
        """Validate if a connection to the specified database is possible."""
        pass

    @abstractmethod
    def check_data_availability(self, db_type: str, data_identifier: Any) -> bool:
        """Check the availability of data in the specified database."""
        pass

    @abstractmethod
    def copy_data(self, local_file_path: str, container_name: str, connect_str:str, data_identifier: Any) -> bool:
        """Copy data from one database to another."""
        pass

    @abstractmethod
    def load_config(self, config: str) -> configparser.ConfigParser:
        """Method to load the configuration details from the config file stored in DB"""
        pass

    @abstractmethod
    def get_json(self, file: str) -> dict:
        """Reading json file."""
        pass

    @abstractmethod
    def execute(self) -> Dict[str, Any]:
        """Execute the strategy."""
        pass

    @abstractmethod
    def on_error(self, errordata: Dict[str, Any]):
        """Handle any error in execution and return appropriate response."""
        pass
    
    @abstractmethod
    def alert_system(self, alert_message: str, severity: str) -> None:
        """Trigger alerts based on the system's performance, security, or other events."""
        pass

    @abstractmethod
    def on_finish(self, data : Any):
        """Handle post-execution tasks like cleanup."""
        pass

    @abstractmethod
    def explainability_monitor(self) -> Dict[str, Any]:
        """Track and provide explainability for the results generated."""
        pass
    
    @abstractmethod
    def monitor_performance(self) -> None:
        """Monitor the performance metrics like execution time, resource usage."""
        pass

    @abstractmethod
    def log_feedback(self, feedback: str) -> None:
        """Log feedback for the execution."""
        pass

    @abstractmethod
    def adaptive_adjustments(self) -> None:
        """Automatically adapt based on feedback and environmental conditions."""
        pass

    @abstractmethod
    def log_processing_data(self, data: Dict[str, Any], result: Dict[str, Any]) -> None:
        """Log input data and results for future analysis ."""
        pass
