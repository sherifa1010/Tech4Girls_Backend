class Rectangle:
    def __init__(self, length, width):
        """initialize the rectangle with length and width"""
        self.lenth = length
        self.width = width
        
        @property
        def area(self):
            """calculate the area of the rectangle."""
            return self.length * self.width
        def perimeter(self):
            """return the string representation of the rectangle"""
            return 2 * (self.length + self.width)
        def __str__(self):
            return f"rectangle(length(length: {self.lenth}, width: {self.width})"
        def __eq__(self, other):
            """check if two rectangles have equal areas."""
            if isinstances(other, rectangle):
                return self.area == other.area
            return NotImplemented
        
        if __name__ == "__main__":
            rec1 = rectangle(6, 3)
            rec2 = rectangle(12, 8)
            
            print(rec1)
            print(f"area of rec1: {rec1.area}")
            print(f"perimeter of rec1: {rec1.perimeter}")
            
            print(rec2)
            print(f"area of rec2: {rec2.area}")
            print(f"perimeter of rec1: {rec2.perimeter}")
            
            if rec1 == rec2:
                print("rec1 and rec2 have equal areas.")
            else:
                print("rec1 and rec2 do not have equal areas.")
            
        