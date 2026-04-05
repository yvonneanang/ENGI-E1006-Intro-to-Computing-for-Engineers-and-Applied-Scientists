# Take Home 4 
#By Yvonne Anang
import random
import math
from matplotlib import pyplot as plt
import numpy as np

def normpdf(x, mean, sd):
    """
    Return the value of the normal distribution 
    with the specified mean and standard deviation (sd) at
    position x.
    You do not have to understand how this function works exactly. 
    """
    var = float(sd)**2
    denom = (2*math.pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom

def pdeath(x, mean, sd):
    start = x-0.5
    end = x+0.5
    step =0.01    
    integral = 0.0
    while start<=end:
        integral += step * (normpdf(start,mean,sd) + normpdf(start+step,mean,sd)) / 2
        start += step            
    return integral    
    
recovery_time = 9 # recovery time in time-steps
virality = 0.9    # probability that a neighbor cell is infected in 
                  # each time step                                                  

class Cell(object):

    def __init__(self,x, y):
        self.x = x
        self.y = y 
        self.state = "S" # can be "S" (susceptible), "R" (resistant = dead), or 
                         # "I" (infected)
        self.time = 0
    
    def __str__(self):
        return str(self.x) + ', ' + str(self.y)
    
    def infect(self):
        self.time = 0
        self.state = "I"
        
        
    
    def process(self, adjacent_cells):
        self.adjacent_cells = adjacent_cells
        cell_instances = self.adjacent_cells
        random_float = random.random()
        probability_of_death = pdeath(self.time, 6, 3)
        if self.state == "I" and self.time == recovery_time:
            self.state = "S"
        if self.state ==  "I" and random_float <= probability_of_death:
            self.state = "R"
        if self.state == "I" and self.time >= 1:
            for cell_instance in cell_instances:
                if cell_instance.state == "S" and random_float <= virality:
                    cell_instance.infect()
        else:
            self.time += 1
        
        
        
class Map(object):
    
    cells = dict()
    
    def __init__(self):
        self.height = 150
        self.width = 150           
        self.cells = {}

    def add_cell(self, cell):
        self.cell = cell
        key = (cell.x, cell.y)
        self.cells[key] = self.cell
        
    def display(self):
        self.image = np.zeros(shape = (self.width, self.height, 3))
        dictionary_of_cells = self.cells
        for coordinate in dictionary_of_cells:
            x, y = coordinate
            if dictionary_of_cells[coordinate].state == "S":
                self.image[x][y] = [0, 1.0, 0]
            if dictionary_of_cells[coordinate].state == "R":
                self.image[x][y] = [0.5, 0.5, 0.5]
            if dictionary_of_cells[coordinate].state == "I":
                self.image[x][y] = [1.0, 0, 0]
        return plt.imshow(self.image) 
    
    def adjacent_cells(self, x,y):
        self.x = x
        self.y = y
        adjacent_cell_list = []
        self.adjacent_cell_instance_list = []
        
        north_cell = (x, (y + 1))
        south_cell = (x, (y - 1))
        east_cell = ((x + 1), y)
        west_cell = ((x - 1), y)
        
        adjacent_cell_list.append(north_cell)
        adjacent_cell_list.append(south_cell)
        adjacent_cell_list.append(east_cell)
        adjacent_cell_list.append(west_cell)
        
        for adjacent_cell in adjacent_cell_list:
            if adjacent_cell in self.cells:
                self.adjacent_cell_instance_list.append(self.cells[adjacent_cell])
        
        return self.adjacent_cell_instance_list
    
    def time_step(self):
        for cell in self.cells:
            cell_instance = self.cells[cell]
            cell_instance.process(self.adjacent_cells(cell_instance.x, cell_instance.y))
            cell_instance.time += 1
        self.display()
        # Update each cell on the map 
        # display the map.
        
        # ... cell.process(adjacent_cells... )
        

            
def read_map(filename):
    
    m = Map()
    
    f = open(filename,'r')
    
    for line in f:
        coordinates = line.strip().split(',')
        c = Cell(int(coordinates[0]),int(coordinates[1]))
        Map.add_cell(m, c)

    return m

m = read_map("nyc_map.csv")
m.cells[(39,82)].infect()
m.time_step()
