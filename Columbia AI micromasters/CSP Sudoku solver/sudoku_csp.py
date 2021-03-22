#Contraing Satisfaction Program assigment for CSMM.101x: Artificial Intelligence (AI) course
#Solves a sudoku using AC-3 and Backtracking.
#Print solution and saveds it in a created text file called solution.txt
#Needs to be executed from command line as follow: python3 sudoku_sudy.py <input_string>
#List of unsolved sudoku are in sudoku_start.txt 
#ex. 000260701680070090190004500820100040004602900050003028009300074040050036703018000


import itertools
import sys
import argparse
import numpy as np

characters = 'ABCDEFGHI'
numbers = '123456789'

#creates the Sudoku
class Sudoku:

    def __init__(self, board):
        self.variables = list()
        self.domains = dict()
        self.constraints = list()
        self.neighbors = dict()
        self.pruned = dict()
        self.prepare(board)


    def prepare(self, board):

        game = list(board)

        self.variables = self.combine(characters, numbers)

        self.domains = {v: list(range(1, 10)) if game[i] == '0' else [int(game[i])] for i, v in enumerate(self.variables)}

        self.pruned = {v: list() if game[i] == '0' else [int(game[i])] for i, v in enumerate(self.variables)}

        self.build_constraints()

        self.build_neighbors()

    def build_constraints(self):

        blocks = (
                [self.combine(characters, number) for number in numbers] +
                [self.combine(character, numbers) for character in characters] +
                [self.combine(character, number) for character in ('ABC', 'DEF', 'GHI') for number in
                 ('123', '456', '789')]
        )

        for block in blocks:
            combinations = self.permutate(block)
            for combination in combinations:
                if [combination[0], combination[1]] not in self.constraints:
                    self.constraints.append([combination[0], combination[1]])

    def build_neighbors(self):

        for x in self.variables:
            self.neighbors[x] = list()
            for c in self.constraints:
                if x == c[0]:
                    self.neighbors[x].append(c[1])

    def solved(self):

        for v in self.variables:
            if len(self.domains[v]) > 1:
                return False

        return True

    def complete(self, assignment):

        for x in self.variables:
            if len(self.domains[x]) > 1 and x not in assignment:
                return False

        return True

    def consistent(self, assignment, var, value):

        consistent = True

        for key, val in assignment.iteritems():
            if val == value and key in self.neighbors[var]:
                consistent = False

        return consistent

    def assign(self, var, value, assignment):

        assignment[var] = value

        self.forward_check(var, value, assignment)

    def unassign(self, var, assignment):

        if var in assignment:

            for (D, v) in self.pruned[var]:
                self.domains[D].append(v)

            self.pruned[var] = []

            del assignment[var]

    def forward_check(self, var, value, assignment):

        for neighbor in self.neighbors[var]:
            if neighbor not in assignment:
                if value in self.domains[neighbor]:
                    self.domains[neighbor].remove(value)
                    self.pruned[var].append((neighbor, value))

    @staticmethod
    def constraint(xi, xj):
        return xi != xj

    @staticmethod
    def combine(alpha, beta):
        return [a + b for a in alpha for b in beta]

    @staticmethod
    def permutate(iterable):
        result = list()

        for L in range(0, len(iterable) + 1):
            if L == 2:
                for subset in itertools.permutations(iterable, L):
                    result.append(subset)

        return result

    @staticmethod
    def conflicts(sudoku, var, val):

        count = 0

        for n in sudoku.neighbors[var]:
            if len(sudoku.domains[n]) > 1 and val in sudoku.domains[n]:
                count += 1

        return count

    def out(self, mode):

        if mode == 'console':

            for var in self.variables:
                sys.stdout.write(str(self.domains[var][0]))

        elif mode == 'file':
            return
# Arc Consistency Algorithm algorithm 
def ac3(sudoku):

    queue = list(sudoku.constraints)

    while queue:

        xi, xj = queue.pop(0)

        if revise(sudoku, xi, xj):

            if len(sudoku.domains[xi]) == 0:
                return False

            for xk in sudoku.neighbors[xi]:
                if xk != xi:
                    queue.append([xk, xi])

    return True

def revise(sudoku, xi, xj):

    revised = False

    for x in sudoku.domains[xi]:
        if not any([sudoku.constraint(x, y) for y in sudoku.domains[xj]]):
            sudoku.domains[xi].remove(x)
            revised = True

    return revised

#Back track algorithm
def backtrack(assignment, sudoku):

    if len(assignment) == len(sudoku.variables):
        return assignment

    var = select_unassigned_variable(assignment, sudoku)

    for value in order_domain_values(sudoku, var):

        if sudoku.consistent(assignment, var, value):

            sudoku.assign(var, value, assignment)

            result = backtrack(assignment, sudoku)
            if result:
                return result

            sudoku.unassign(var, assignment)

    return False

    # Most Constrained Variable heuristic
    # Pick the unassigned variable that has fewest legal values remaining.
def select_unassigned_variable(assignment, sudoku):
    unassigned = [v for v in sudoku.variables if v not in assignment]
    return min(unassigned, key=lambda var: len(sudoku.domains[var]))

    # Least Constraining Value heuristic
    # Prefers the value that rules out the fewest choices for the neighboring variables in the constraint graph.
def order_domain_values(sudoku, var):
    if len(sudoku.domains[var]) == 1:
        return sudoku.domains[var]

    return sorted(sudoku.domains[var], key=lambda val: sudoku.conflicts(sudoku, var, val))

def main():

    sud= sys.argv[1]
    if len(sud)!=81:
        print("Not a valid sudoku puzzle. It needs 81 numbers")
    else:
        parser = argparse.ArgumentParser()
        parser.add_argument('board')
        args = parser.parse_args()
        print(str(args))


        sudoku = Sudoku(args.board)

        if ac3(sudoku):

            if sudoku.solved():
                solution=[]
                output = open('solution.txt', 'w')
        

                for var in sudoku.variables:
                    output.write(str(sudoku.domains[var][0]))
                    solution.append((sudoku.domains[var][0]))
                output.close()

                n=np.array(solution).reshape(9,9)
                print("\n")
                print("Solution:")
                print(n)
                print("\n")
                

            else:

                assignment = {}

                for x in sudoku.variables:
                    if len(sudoku.domains[x]) == 1:
                        assignment[x] = sudoku.domains[x][0]

                assignment = backtrack(assignment, sudoku)

                for d in sudoku.domains:
                    sudoku.domains[d] = assignment[d] if len(d) > 1 else sudoku.domains[d]

                if assignment:

                    output = open('solution.txt', 'w')
                    for var in sudoku.variables:
                        output.write(str(sudoku.domains[var]))
                        solution.append((sudoku.domains[var][0]))
                    output.close()
                    n=np.array(solution).reshape(9,9)
                    print("\n")
                    print("Solution:")
                    print(n)
                    print("\n")
                   

                else:
                    print ("No solution exists")
                    

if __name__ == '__main__':
    main()
