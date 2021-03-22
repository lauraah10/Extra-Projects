#Puzzle solver with Tree search alg assigment for CSMM.101x: Artificial Intelligence (AI) course
#Solves a puzzle using A star with, bfs and dfs.
#Print steps to solve and saves on a file the time to solve, the depth of nodes, the cost and ram used
#Needs to be executed from command line as follow: python3 driver2.py <Search method> <puzzle as a string>
#example: python3 driver.py bfs 0,8,7,6,5,4,3,2,1



import queue
from collections import deque
import time
import resource
import sys
import heapq
import math
import os

start_time = time.process_time()



## The Class that Represents the Puzzle

ACTION_UP = '0 '
ACTION_DOWN = '1 '
ACTION_LEFT = '2 '
ACTION_RIGHT = '3 '

ACTION_TO_STRING = {
    ACTION_UP: "Up",
    ACTION_DOWN: "Down",
    ACTION_LEFT: "Left",
    ACTION_RIGHT: "Right"
}


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


class PuzzleState(object):
    """docstring for PuzzleState"""

    def __init__(self, config, n, parent=None, actionList="", cost=0):
        if n * n != len(config) or n < 2:
            raise Exception("the length of config is not correct!")

        self.n = n
        self.cost = cost
        self.parent = parent
        self.actionList = actionList

        self.dimension = n
        self.config = config
        self.children = []

        for i, item in enumerate(self.config):
            if item == 0:
                self.blank_row = i // self.n
                self.blank_col = i % self.n
                break

    def display(self):
        for i in range(self.n):
            line = []
            offset = i * self.n

            for j in range(self.n):
                line.append(self.config[offset + j])

            print(line)

    def move_left(self):
        if self.blank_col == 0:
            return None
        else:
            blank_index = self.blank_row * self.n + self.blank_col
            target = blank_index - 1
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, actionList=self.actionList + ACTION_LEFT,
                               cost=self.cost + 1)

    def move_right(self):
        if self.blank_col == self.n - 1:
            return None

        else:
            blank_index = self.blank_row * self.n + self.blank_col
            target = blank_index + 1
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, actionList=self.actionList + ACTION_RIGHT,
                               cost=self.cost + 1)

    def move_up(self):
        if self.blank_row == 0:
            return None

        else:
            blank_index = self.blank_row * self.n + self.blank_col
            target = blank_index - self.n
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, actionList=self.actionList + ACTION_UP,
                               cost=self.cost + 1)

    def move_down(self):
        if self.blank_row == self.n - 1:
            return None

        else:
            blank_index = self.blank_row * self.n + self.blank_col
            target = blank_index + self.n
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, actionList=self.actionList + ACTION_DOWN,
                               cost=self.cost + 1)

    # gives you a list of list where you have all the posible states by moving the 0 up/down/left/right
    def expand(self):

        """expand the node"""

        # add child nodes in order of UDLR

        if len(self.children) == 0:
            up_child = self.move_up()

            if up_child is not None:
                self.children.append(up_child)

            down_child = self.move_down()

            if down_child is not None:
                self.children.append(down_child)

            left_child = self.move_left()

            if left_child is not None:
                self.children.append(left_child)

            right_child = self.move_right()

            if right_child is not None:
                self.children.append(right_child)

        return self.children


def bfs_search(initial_state, goal):
    # Tracks all kids explored and created
    explored = []

    # creating the queue
    entire = queue.Queue()
    # adding the parent state to queue
    entire.put(initial_state)
    explored.append(initial_state.config)

    # initial state doesn't count
    opened = -1
    depth = 0

    while entire.empty() != True:
        # get item out of the queue and save it
        current = entire.get()

        # increase the opened states
        opened = opened + 1

        # check if the states matches the goal
        if goal == current.config:
            # max_depth=max(current.cost for cost in entire.queue)
            actionlist = current.actionList
            time1 = time.process_time() - start_time
            writeOutput(current, actionlist, opened, depth, time1)
            return True

        # call the funciton that returns the list of list that has all the possible states
        children = current.expand()

        # add them to the queue only if it hasn't been explored or is not in the list (no duplicates wanted)
        for kid in children:
            if kid.config not in explored:
                if depth < kid.cost:
                    depth = kid.cost
                explored.append(kid.config)
                entire.put(kid)

    return False


def dfs_search(parent, goal):
    # Stack
    entire = Stack()

    # List of all created and explored states
    explored = {}
    entire.push(parent)
    explored[parent.config] = True
    depth = 0
    opened = -1

    while not entire.isEmpty():
        current = entire.pop()

        opened = opened + 1
        if goal == current.config:
            time1 = time.process_time()
            print(time1)
            writeOutput(current, current.actionList, opened, depth, time1)
            return True

        new = current.expand()

        while new != []:
            kid = new.pop()
            if kid.config not in explored:
                if depth < kid.cost:
                    depth = kid.cost

                explored[kid.config] = True
                entire.push(kid)

    return False


def A_star_search(initial_state, goal):
    # starts a dictionary
    entire = {}

    # opened
    opened = -1
    # saving the sate of the puzzle along with it's heuristics
    entire[initial_state] = manhattan_dist(initial_state.config)

    # formula for the heuristics h1(heuristics) + total
    # f=h1+g(cost)

    # saving values of the ex
    explored = []
    depth = 0
    # while the dictionary is not empty
    while entire != {}:
        current = (min(entire.items(), key=lambda x: x[1]))[0]

        entire.pop(current)

        explored.append(current.config)
        opened = opened + 1

        if goal == current.config:
            time1 = time.process_time() - start_time
            writeOutput(current, current.actionList, opened, depth, time1)
            return True

        for kid in current.expand():
            if kid not in explored:
                if kid not in entire:
                    # f=manhattan(kid.config)+current.cost
                    entire[kid] = manhattan_dist(kid.config) + kid.cost
                if depth < kid.cost:
                    depth = kid.cost

    return False
    # priority queue


# heuristic that gets the total nuumber of wrong tiles
def wrongtiles(state, goal):
    h1 = 0
    # counts the numbers in the incorect location
    for num in range(len(state)):
        if goal[num] != state[num]:
            h1 = h1 + 1
    return (h1)


# calculates the manhattan distance to get the heuristics for A*
def manhattan_dist(puz):
    manh = 0
    i = 0
    # saves the goal locations of where the numbers are supposed to be at, example 0 at (0,0)
    gdict = {}
    for x in range(3):
        for y in range(3):
            gdict[i] = [x, y]
            i = i + 1

    # calculates the Manhattan Distance
    # keeps track of the location of the puzzle
    i = 0
    for x in range(3):
        for y in range(3):
            # tells the locaiton of where that number is supposed to be at
            goalx = gdict[puz[i]][0]
            goaly = gdict[puz[i]][1]
            # calculates
            manh = manh + abs(x - goalx) + abs(y - goaly)
            i = i + 1
    return (manh)


# write results to a document
def writeOutput(current, actionlist, opened, depth, time1):
    ram = (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) / 1000
    list1 = actionlist[:-1].split(" ")

    steps = [ACTION_TO_STRING[action + " "] for action in list1]
    print(steps)

    file = open("output.txt", "w")
    file.write("path_to_goal: %s\r\n" % (steps))
    file.write("cost_of_path: %d\r\n" % (current.cost))
    file.write("nodes_expanded: %d\r\n" % (opened))
    file.write("search_depth: %d\r\n" % (current.cost))
    file.write("max_search_depth: %d\r\n" % (depth))
    file.write("running_time: %f\r\n" % (time1))
    file.write("max_ram_usage: %d\r\n" % (ram))
    file.close()


# Main Function that reads in Input and Runs corresponding Algorithm

def main():
    # Running the program on the command line. It wil will have this structure:python3 driver.py bfs 1,2,5,3,4,0,6,7,8

    # so we lower case for incostancies
    searchmethod = sys.argv[1].lower()

    # make a list out of the initial puzzle state
    initial_state = sys.argv[2].split(",")

    # make it into a tuple since tupples are immutable
    initial_state = tuple(map(int, initial_state))

    size = int(math.sqrt(len(initial_state)))

    # make it into a puzzle
    puzzle = PuzzleState(initial_state, size)

    # set the goal state
    goal = tuple([0, 1, 2, 3, 4, 5, 6, 7, 8])

    # call the method according to the search method
    if searchmethod == "bfs":
        bfs_search(puzzle, goal)

    elif searchmethod == "dfs":

        dfs_search(puzzle, goal)

    elif searchmethod == "ast":

        A_star_search(puzzle, goal)

    else:

        print("Enter valid command arguments !")


if __name__ == '__main__':
    main()
