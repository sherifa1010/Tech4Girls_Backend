class Employee:
    def __init__ (self, name, position):
        """initialize the employee name and position"""
        self.name = name
        self.position = position
        
        def get_details(self):
            """display employee details"""
            return f"name: {self.name}, position: {self.position}"
        
        class manager(Employee):
            def __init__(self, name, position, department):
                """initialize the manager's attributes,using super()to initialize inherited attributes."""
                super().__init__(name, position)
                self.department = department
                def get_details(self):
                    return f"name: {self.name}, position: {self.position}, department: {self.department}"
                """override the get_details method to include the department"""
                if __name__ == "__main__":
                    employee1 =Employee("ama puni", "graphic designer")
                    print(employee1.get_details(self))
                    manager1 = manager("williams tetteh", "project manager", "development")
                    print(manager1.get_details(self))
        