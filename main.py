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
            for i in range(3):
                self.cube[1][0][i], self.cube[2][0][i], self.cube[3][0][i], self.cube[4][0][i] = \
                    self.cube[4][0][i], self.cube[1][0][i], self.cube[2][0][i], self.cube[3][0][i]
        elif face == 1:  # Front face
            for i in range(3):
                self.cube[2][i][0], self.cube[0][2][i], self.cube[4][i][2], self.cube[5][0][i] = \
                    self.cube[0][2][i], self.cube[4][i][2], self.cube[5][0][i], self.cube[2][i][0]
        elif face == 2:  # Right face
            for i in range(3):
                self.cube[0][i][2], self.cube[1][i][2], self.cube[5][i][2], self.cube[3][2-i][0] = \
                    self.cube[3][2-i][0], self.cube[0][i][2], self.cube[1][i][2], self.cube[5][i][2]
        elif face == 3:  # Back face
            for i in range(3):
                self.cube[0][0][i], self.cube[4][i][0], self.cube[5][2][i], self.cube[2][i][2] = \
                    self.cube[2][i][2], self.cube[0][0][i], self.cube[4][i][0], self.cube[5][2][i]
        elif face == 4:  # Left face
            for i in range(3):
                self.cube[0][i][0], self.cube[1][i][0], self.cube[5][i][0], self.cube[3][i][2] = \
                    self.cube[3][i][2], self.cube[0][i][0], self.cube[1][i][0], self.cube[5][i][0]
        elif face == 5:  # Bottom face
            for i in range(3):
                self.cube[1][2][i], self.cube[2][2][i], self.cube[3][2][i], self.cube[4][2][i] = \
                    self.cube[2][2][i], self.cube[3][2][i], self.cube[4][2][i], self.cube[1][2][i]
                
                
    
    def rotate_face_counterclockwise(self, face):
        # Rotate a face of the cube counterclockwise
        self.cube[face] = [list(row) for row in zip(*self.cube[face])][::-1]
        
        # Rotate the adjacent edges
        if face == 0:  # Top face
            self.cube[2][0], self.cube[1][0], self.cube[4][0], self.cube[3][0] = \
                self.cube[1][0], self.cube[4][0], self.cube[3][0], self.cube[2][0]
        elif face == 1:  # Front face
            for i in range(3):  
                self.cube[0][2][i], self.cube[4][i][2], self.cube[5][0][i], self.cube[2][i][0] = \
                    self.cube[2][i][0], self.cube[0][2][i], self.cube[4][i][2], self.cube[5][0][i]
        elif face == 2:  # Right face
            for i in range(3):
                self.cube[3][2-i][0], self.cube[0][i][2], self.cube[1][i][2], self.cube[5][i][2] = \
                    self.cube[0][i][2], self.cube[1][i][2], self.cube[5][i][2], self.cube[3][2-i][0]
        elif face == 3:  # Back face
            temp = [row[0] for row in self.cube[2]]
            for i in range(3):
                self.cube[2][i][2], self.cube[0][0][i], self.cube[4][i][0], self.cube[5][2][i] = \
                    self.cube[0][0][i], self.cube[4][i][0], self.cube[5][2][i], self.cube[2][i][2]
        elif face == 4:  # Left face
            for i in range(3):
                self.cube[3][i][2], self.cube[0][i][0], self.cube[1][i][0], self.cube[5][i][0] = \
                    self.cube[0][i][0], self.cube[1][i][0], self.cube[5][i][0], self.cube[3][i][2]
        elif face == 5:  # Bottom face
            self.cube[4][2], self.cube[3][2], self.cube[2][2], self.cube[1][2] = \
                self.cube[1][2], self.cube[4][2], self.cube[3][2], self.cube[2][2]

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
    actions = input("Enter the actions to perform on the cube (e.g., R B' G): ").split()
    face_map = {'W': 0, 'R': 1, 'B': 2, 'O': 3, 'G': 4, 'Y': 5}

    for action in actions:
        face = face_map[action[0]]
        if len(action) > 1 and action[1] == "'":
            cube.rotate_face_counterclockwise(face)
        else:
            cube.rotate_face_clockwise(face)

    cube.display()