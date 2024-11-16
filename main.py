<<<<<<< Updated upstream
#from colorama import Fore, Style
from termcolor import colored

=======
>>>>>>> Stashed changes
class RubiksCube:
    def __init__(self):
        # Initialize a 3x3x6 Rubik's Cube with each face having a unique color
        self.cube = [
<<<<<<< Updated upstream
            [['W' for _ in range(3)] for _ in range(3)],  #0 Top face (White) 
            [['R' for _ in range(3)] for _ in range(3)],  #1 Front face (Red) 
            [['B' for _ in range(3)] for _ in range(3)],  #2 Right face (Blue)
            [['O' for _ in range(3)] for _ in range(3)],  #3 Back face (Orange)
            [['G' for _ in range(3)] for _ in range(3)],  #4 Left face (Green)
            [['Y' for _ in range(3)] for _ in range(3)]   #5 Bottom face (Yellow) 
        ]
        self.adjacent_faces = [
            [4, 1, 2, 3],  # Top face
            [4, 5, 2, 0],  # Front face
            [5, 3, 0, 1],  # Right face
            [4, 0, 2, 5],  # Back face
            [0, 3, 5, 1],  # Left face
            [2, 1, 4, 3]   # Bottom face
=======
            [['W' for _ in range(3)] for _ in range(3)],  # Top face (White)
            [['R' for _ in range(3)] for _ in range(3)],  # Front face (Red)
            [['B' for _ in range(3)] for _ in range(3)],  # Right face (Blue)
            [['O' for _ in range(3)] for _ in range(3)],  # Back face (Orange)
            [['G' for _ in range(3)] for _ in range(3)],  # Left face (Green)
            [['Y' for _ in range(3)] for _ in range(3)]   # Bottom face (Yellow)
>>>>>>> Stashed changes
        ]

    def rotate_face_clockwise(self, face):
        # Rotate a face of the cube clockwise
        self.cube[face] = [list(row) for row in zip(*self.cube[face][::-1])]

        # Rotate the adjacent edges
        if face == 0:  # Top face
<<<<<<< Updated upstream
            temp = [self.cube[4][0][0], self.cube[4][0][1], self.cube[4][0][2]]
            for adjacent_face in self.adjacent_faces[face][:-1]:
                print(self.cube[adjacent_face][0][0])
                self.cube[adjacent_face+1][0], self.cube[adjacent_face+1][1], self.cube[adjacent_face+1][2] = \
                    self.cube[adjacent_face][0], self.cube[adjacent_face][1], self.cube[adjacent_face][2]
            self.cube[3][0][0], self.cube[3][0][1], self.cube[3][0][2] = temp
                
        """
        elif face == 1:  # Front face
            for i in range(3):
                
        elif face == 2:  # Right face
            for i in range(3):
        elif face == 3:  # Back face
            for i in range(3):
        elif face == 4:  # Left face
            for i in range(3):
        elif face == 5:  # Bottom face
            for i in range(3):
        """
                
=======
            self._rotate_edges_clockwise([4, 1, 2, 3], 0)
        elif face == 1:  # Front face
            self._rotate_edges_clockwise([0, 4, 5, 2], 2, reverse=True)
        elif face == 2:  # Right face
            self._rotate_edges_clockwise([0, 1, 5, 3], 2)
        elif face == 3:  # Back face
            self._rotate_edges_clockwise([0, 2, 5, 4], 0, reverse=True)
        elif face == 4:  # Left face
            self._rotate_edges_clockwise([0, 3, 5, 1], 0)
        elif face == 5:  # Bottom face
            self._rotate_edges_clockwise([1, 2, 3, 4], 2)
>>>>>>> Stashed changes

    def rotate_face_counterclockwise(self, face):
        # Rotate a face of the cube counterclockwise
        self.cube[face] = [list(row) for row in zip(*self.cube[face])][::-1]

        # Rotate the adjacent edges
        if face == 0:  # Top face
            self._rotate_edges_counterclockwise([4, 1, 2, 3], 0)
        elif face == 1:  # Front face
            self._rotate_edges_counterclockwise([0, 4, 5, 2], 2, reverse=True)
        elif face == 2:  # Right face
            self._rotate_edges_counterclockwise([0, 1, 5, 3], 2)
        elif face == 3:  # Back face
            self._rotate_edges_counterclockwise([0, 2, 5, 4], 0, reverse=True)
        elif face == 4:  # Left face
            self._rotate_edges_counterclockwise([0, 3, 5, 1], 0)
        elif face == 5:  # Bottom face
            self._rotate_edges_counterclockwise([1, 2, 3, 4], 2)

    def _rotate_edges_clockwise(self, faces, row, reverse=False):
        temp = [self.cube[faces[0]][row][i] for i in range(3)]
        for i in range(3):
            self.cube[faces[0]][row][i] = self.cube[faces[3]][row][i] if reverse else self.cube[faces[1]][row][i]
            self.cube[faces[1]][row][i] = self.cube[faces[2]][row][i] if reverse else self.cube[faces[0]][row][i]
            self.cube[faces[2]][row][i] = self.cube[faces[3]][row][i] if reverse else self.cube[faces[1]][row][i]
            self.cube[faces[3]][row][i] = temp[i] if reverse else self.cube[faces[2]][row][i]
        self._swap_edges(faces, row)

    def _rotate_edges_counterclockwise(self, faces, row, reverse=False):
        temp = [self.cube[faces[0]][row][i] for i in range(3)]
        for i in range(3):
            self.cube[faces[0]][row][i] = self.cube[faces[1]][row][i] if reverse else self.cube[faces[3]][row][i]
            self.cube[faces[1]][row][i] = self.cube[faces[2]][row][i] if reverse else self.cube[faces[0]][row][i]
            self.cube[faces[2]][row][i] = self.cube[faces[3]][row][i] if reverse else self.cube[faces[1]][row][i]
            self.cube[faces[3]][row][i] = temp[i] if reverse else self.cube[faces[2]][row][i]
        self._swap_edges(faces, row)

    def _swap_edges(self, faces, row):
        self.cube[faces[0]][row][0], self.cube[faces[0]][row][2] = self.cube[faces[0]][row][2], self.cube[faces[0]][row][0]
        self.cube[faces[1]][row][0], self.cube[faces[1]][row][2] = self.cube[faces[1]][row][2], self.cube[faces[1]][row][0]
        self.cube[faces[2]][row][0], self.cube[faces[2]][row][2] = self.cube[faces[2]][row][2], self.cube[faces[2]][row][0]
        self.cube[faces[3]][row][0], self.cube[faces[3]][row][2] = self.cube[faces[3]][row][2], self.cube[faces[3]][row][0]

    def display(self):
<<<<<<< Updated upstream
        # Display the cube in a more readable format with colors

        """
        color_map = {
            'W': Fore.WHITE,
            'R': Fore.RED,
            'B': Fore.BLUE,
            'O': Fore.MAGENTA,  # Magenta can be used to represent Orange
            'G': Fore.GREEN,
            'Y': Fore.YELLOW
        }
        """
        faces = ['Orange', 'Green', 'White', 'Blue', 'Yellow', 'Red']
        
        
        face_order = [3, 4, 0, 2, 5, 1]  # Order to display faces
        


        
        for i, face in enumerate(face_order):
            print(f"{faces[i]} face:")
            for row in self.cube[face]:
=======
        # Display the cube
        for face in self.cube:
            for row in face:
>>>>>>> Stashed changes
                print(' '.join(row))
            print()
        

# Example usage
if __name__ == "__main__":
    cube = RubiksCube()
    cube.display()
    
    while True:
        command = input("Enter operation (e.g., 'U' for top face clockwise, 'U'' for top face counterclockwise, 'Q' to quit): ").strip().upper()
        if command == 'Q':
            break
        elif command == 'U':
            cube.rotate_face_clockwise(0)
        elif command == 'U\'':
            cube.rotate_face_counterclockwise(0)
        elif command == 'F':
            cube.rotate_face_clockwise(1)
        elif command == 'F\'':
            cube.rotate_face_counterclockwise(1)
        elif command == 'R':
            cube.rotate_face_clockwise(2)
        elif command == 'R\'':
            cube.rotate_face_counterclockwise(2)
        elif command == 'B':
            cube.rotate_face_clockwise(3)
        elif command == 'B\'':
            cube.rotate_face_counterclockwise(3)
        elif command == 'L':
            cube.rotate_face_clockwise(4)
        elif command == 'L\'':
            cube.rotate_face_counterclockwise(4)
        elif command == 'D':
            cube.rotate_face_clockwise(5)
        elif command == 'D\'':
            cube.rotate_face_counterclockwise(5)
        else:
            print("Invalid command. Please try again.")
        
        cube.display()