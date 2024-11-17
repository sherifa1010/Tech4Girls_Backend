class Employee:
    def __init__ (self, name, position):
        
        self.name = name
        self.position = position
        
        def get_details(self):
            
            return f"name: {self.name}, position: {self.position}"
        
        class manager(Employee):
            def __init__(self, name, position, department):
                
                super().__init__(name, position)
                self.department = department
                def get_details(self):
                    return f"name: {self.name}, position: {self.position}, department: {self.department}"
                
                if __name__ == "__main__":
                    employee1 =Employee("ama puni", "graphic designer")
                    print(employee1.get_details(self))
                    manager1 = manager("williams tetteh", "project manager", "development")
                    print(manager1.get_details(self))
        