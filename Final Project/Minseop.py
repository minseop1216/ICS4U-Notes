from snake import Snake
import random

class Minseop(Snake):
    def __init__(self):
        start_x, start_y = (5, 1)

        color = (20,100,150)
        name = "Minseop"
        
        length = 150
        attack = 10
        hp = 40

        super().__init__(start_x, start_y, color, name, length, attack, hp)

        self.directions = [
            [-1, 0],  
            [1, 0],   
            [0, -1],  
            [0, 1]   
        ]
    
    def _getPosition(self) -> tuple[int, int]:
        x, y, _ = self.body_positions[0]
        return (x, y)
    
    def _checkCollision(self, direction : list[int, int]) -> bool:
        x, y = self._getPosition()
        nx = x + direction[0]
        ny = y + direction[1]

        max_x, max_y = self.matrix_size()

        return (nx < 0 or nx >= max_x) or (ny < 0 or ny >= max_y)
    
    def move(self) -> list[int, int]:
        
        if not self._checkCollision([0, 1]):
            direction = [0, 1]
        if not self._checkCollision([1, 0]):
            direction = [1, 0]
        if not self._checkCollision([0, -1]):
            direction = [0, -1]
        
        direction = [-1, 0]
    
        return super().move(direction)
    
    def detect(self, map):
        pass
