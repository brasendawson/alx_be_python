from polymorphism_demo import Rectangle, Circle

def main():
    # Create instances of Rectangle and Circle
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    # Demonstrating polymorphism by calling area() on different shapes
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
