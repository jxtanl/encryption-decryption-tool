class FileOperation:
    def __init__(self, filename, operation, execution_time):
        self.filename = filename
        self.operation = operation
        self.execution_time = execution_time

    def __str__(self):
        return f"File: {self.filename}, Operation: {self.operation}, Execution Time: {self.execution_time} seconds"
