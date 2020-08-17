
class ApiResource:
    
    def __init__(self, resource_id: int):
        self._resource_id = resource_id
        
    def get_id(self) -> int:
        return self._resource_id

    def set_id(self, resource_id: int):
        self._resource_id = resource_id

