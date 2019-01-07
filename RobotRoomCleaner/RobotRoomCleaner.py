# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
                
        """ 
        """up right down left"""
        self.directions = [(-1,0),(0,-1),(1,0),(0,1)]
        self.dfs(robot, 0, 0, 0, set())
        
        
    def dfs(self, robot, loc_row, loc_col, curDirection, visited):
        if (loc_row, loc_col) in visited:
            return

        visited.add((loc_row, loc_col))
        robot.clean()
        
        for i in range(0,4):
            
            #go in each 4 directions
            
            new_direction = (curDirection + i) % 4
            neighbor_row = loc_row + self.directions[new_direction][0]
            neighbor_col = loc_col + self.directions[new_direction][1]
            #print('new direction {}'.format(new_direction))
            #print('passed in direction {}'.format(curDirection))
  
            if (neighbor_row, neighbor_col) not in visited and robot.move():
                self.dfs(robot, neighbor_row, neighbor_col, new_direction, visited)
            
                self.go_back(robot)
            
            robot.turnLeft()    

            
    def go_back(self, robot):
        """ moves back to the tile the robot was on previously before the next dfs call
            simply an additional 'pop' stack cleaning to do. Additionally, the robot is reset to the 
            direction it was pointing before
        """
        robot.turnLeft()
        robot.turnLeft()
        robot.move()
        robot.turnLeft()
        robot.turnLeft()