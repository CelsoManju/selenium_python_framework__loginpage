import json
from utilities.custom_logger import customLogger as cl

class json_hanler():
    
    def __init__(self):
        #todo move the template file and result file name to a config file
        self.json_template_file = "test_result_template.json"
        self.json_result_file = "test_result.json"
    
    def read_json(self,file):
        try:
            filename = self.json_template_file            
            with open(filename, 'r') as file:
                data = json.load(file)
                file.close()
                return data
        except Exception as e :
            #todo add custom log
            print ("exception")
            return False
    
    def write_json(self,file,data):
        try:
            filename = self.json_result_file
            with open(self.json_file, 'w') as file:
                json.dump(data, file, indent=4)
                file.close()
            return True
        except Exception as e :
            #todo add custom log
            print ("exception")
            return False
            
    
    