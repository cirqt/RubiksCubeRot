from colorama import Fore, Style

class RubiksCube:
    def __init__(self):
        # Initialize a solved Rubik's Cube
        self.cube = [
            [['W' for _ in range(3)] for _ in range(3)],  # Top face (White)
            [['R' for _ in range(3)] for _ in range(3)],  # Front face (Red)
            [['B' for _ in range(3)] for _ in range(3)],  # Right face (Blue)
            [['O' for _ in range(3)] for _ in range(3)],  # Back face (Orange)
            [['G' for _ in range(3)] for _ in range(3)],  # Left face (Green)
            [['Y' for _ in range(3)] for _ in range(3)]   # Bottom face (Yellow)
        ]

    def rotate_face_clockwise(self, face):
        # Rotate a face of the cube clockwise
        self.cube[face] = [list(row) for row in zip(*self.cube[face][::-1])]
        
        # Rotate the adjacent edges
        if face == 0:  # Top face
            self.cube[1][0], self.cube[2][0], self.cube[3][0], self.cube[4][0] = \
                self.cube[2][0], self.cube[3][0], self.cube[4][0], self.cube[1][0]
        elif face == 1:  # Front face
            self.cube[0][2], self.cube[2][:, 0], self.cube[5][0], self.cube[4][:, 2] = \
                self.cube[4][:, 2], self.cube[0][2], self.cube[2][:, 0], self.cube[5][0]
        elif face == 2:  # Right face
            self.cube[0][:, 2], self.cube[3][:, 0], self.cube[5][:, 2], self.cube[1][:, 2] = \
                self.cube[3][:, 0], self.cube[5][:, 2], self.cube[1][:, 2], self.cube[0][:, 2]
        elif face == 3:  # Back face
            self.cube[0][0], self.cube[4][:, 0], self.cube[5][2], self.cube[2][:, 2] = \
                self.cube[4][:, 0], self.cube[5][2], self.cube[2][:, 2], self.cube[0][0]
        elif face == 4:  # Left face
            self.cube[0][:, 0], self.cube[1][:, 0], self.cube[5][:, 0], self.cube[3][:, 2] = \
                self.cube[1][:, 0], self.cube[5][:, 0], self.cube[3][:, 2], self.cube[0][:, 0]
        elif face == 5:  # Bottom face
            self.cube[1][2], self.cube[4][2], self.cube[3][2], self.cube[2][2] = \
                self.cube[4][2], self.cube[3][2], self.cube[2][2], self.cube[1][2]

    def rotate_face_counterclockwise(self, face):
        # Rotate a face of the cube counterclockwise
        self.cube[face] = [list(row) for row in zip(*self.cube[face])][::-1]

    def display(self):
        # Display the cube in a more readable format with colors

        color_map = {
            'W': Fore.WHITE,
            'R': Fore.RED,
            'B': Fore.BLUE,
            'O': Fore.MAGENTA,  # Magenta can be used to represent Orange
            'G': Fore.GREEN,
            'Y': Fore.YELLOW
        }

        faces = ['Orange', 'Green', 'White', 'Blue', 'Yellow', 'Red']
        face_order = [3, 4, 0, 2, 5, 1]  # Order to display faces

        for i, face in enumerate(face_order):
            print(f"{faces[i]} face:")
            for row in self.cube[face]:
                print(' '.join(color_map[color] + color + Style.RESET_ALL for color in row))
            print()

# Example usage
if __name__ == "__main__":
    cube = RubiksCube()
    cube.display()
    cube.rotate_face_clockwise(0)
    cube.display()