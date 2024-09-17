class Rectangle:
   
    all_rectangles = []

    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        Rectangle.all_rectangles.append(self)

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

    @classmethod
    def print_all_rectangles(cls):
        print(f"Total rectangles created: {len(cls.all_rectangles)}")
        for rect in cls.all_rectangles:
            print(f"Rectangle with length={rect.length}, width={rect.width}")
            
if __name__ == "__main__":
    rect1 = Rectangle(10, 5)
    rect2 = Rectangle(7, 3)
    rect3 = Rectangle(15, 8)
    Rectangle.print_all_rectangles()
