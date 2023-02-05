'''
Graph Miner Program

Caroline Canfield, Theresa Rumoro, and Emily Walden
Professor Kim
Intro to AI
18 October, 2022

This program takes in a file of edges that show which nodes connect to each other. It hen uses a fitness function
to determine how fit a solution is, which then allows the top paths to breed with each other. The goal of this
program is for the computer to find an optimal solution, which would be the best path between the user's
inputted nodes.

https://appdividend.com/2021/06/21/how-to-read-file-into-list-in-python/#:~:text=To%20read%20a%20file%20into,text%20file%20into%20a%20list
    This source was used to help us read from the file and append the information into a list.


https://igraph.org/python/versions/latest/tutorials/quickstart/quickstart.html
https://www.cs.rhul.ac.uk/home/tamas/development/igraph/tutorial/tutorial.html
    These two sources helps us create the graph and highlight specific paths.

IMPORTANT: Please change the name of the file in parse_graph() if another file name wants to be read, or name
            the file downloaded graph_data.txt. Thank you!

Assumptions:
    -User manually inputs the file name in parse_graph()
    -The first two lines in the file are comments
'''

# Import needed libraries
from cgi import test
from turtle import color
import igraph as graph
import matplotlib.pyplot as plot
import math
import random

# Create needed global variables
test_nodes = []
node_graph = graph.Graph()
nodes = []
user_nodes = []
population = []
generation_counter = 1


'''
parse_graph takes in the wanted file, reads it, splits up the informaiton into a list of lists.
'''
def parse_graph():
    # Call global nodes
    global nodes
    # Open the file
    open_file = open("graph_data.txt", "r")
    # nodes holds all the ndoes once the file is read
    nodes = []
    # Keeps track while traversing in the while loop
    tracker = 0
    # Skips the first two lines because they are comments
    open_file.readline()
    open_file.readline()
    # Use while loop to traverse through the file and check for True statement to exit
    while True:
        # Holds each node at each line
        node_index = []
        # Read each line in the file
        line = open_file.readline()
        # If the line is empty, break
        if (line == ''):
            break
        # If the first vertex is a single digit number
        if (line[1] == ' ' ):
            # If the second vertex on the line is a single digit number
            if (line[3] == ' '):
                # Create the nodes out of the correct indexes, change them to be integers and append them to node_index
                node1 = line[0]
                node2 = line[2]
                node_1 = int(node1)
                node_2 = int(node2)
                node_index.append(node_1)
                node_index.append(node_2)
            # Else the second vertex on the line is a double digit number
            else:
                # Create the nodes out of the correct indexes, change them to be integers and append them to node_index
                node1 = line[0]
                node2 = line[2] + line[3]
                node_1 = int(node1)
                node_2 = int(node2)
                node_index.append(node_1)
                node_index.append(node_2)
        # If the first number is a double digit number and the second number is single digit number
        elif (line[4] == ''):
            # Create the nodes out of the correct indexes, change them to be integers and append them to node_index
            node1 = line[0] + line [1]
            node2 = line[3]
            node_1 = int(node1)
            node_2 = int(node2)
            node_index.append(node_1)
            node_index.append(node_2)
        # If the first and second number are double digits
        else:
            # Create the nodes out of the correct indexes, change them to be integers and append them to node_index
            node1 = line[0] + line [1]
            node2 = line[3] + line[4]
            node_1 = int(node1)
            node_2 = int(node2)
            node_index.append(node_1)
            node_index.append(node_2)
        # Append node_index to the nodes
        nodes.append(node_index)
        # Increment tracker
        tracker += 1
        # If there is no line of information, break
        if not line:
            break
    # Close file
    open_file.close()


'''
create_graph creates the graph with the vertices and edges and highlights paths.
'''
def create_graph(path_nodes):
    # Call global nodes, node_graph, and generation_counter
    global nodes
    global node_graph
    global generation_counter
    # Set counter equal to 0
    counter = 0
    # Create an empty list called test_nodes
    test_nodes = []
    # While counter is less than path_nodes, append the counter index path_nodes to test_nodes and increment counter
    while (counter < len(path_nodes)):
        test_nodes.append(path_nodes[counter])
        counter += 1
    # Find the length of the nodes list
    length = len(nodes)
    # Divide the length by 2 because we are only focused on the lines and not the amount of data
    length /= 2
    # Round down for the length
    length = math.floor(length)
    # Create the edges using the global nodes, which includes the pathways between the nodes
    edges = nodes
    # Create a graph using igraph with the length and edges as parameters
    node_graph = graph.Graph(length, edges)
    # Set empty list called name to label the nodes
    name = []
    # Set counter equal to zero
    counter = 0
    # While the counter is less than or equal to the length, append the counter value to name and increment counter
    while (counter <= len(nodes)):
        # Append the counter
        name.append(counter)
        #Increment the counter
        counter += 1
    # Using the vertex sequence property, name each node using the name list
    node_graph.vs["Node Labels"] = name
    # Create the variable path to be an empty list
    path = []
    # Set node counter equal to 0
    node_counter = 0
    # While loop that confirms that the node_counter is less than or equal to the length of the nodes list
    while (node_counter <= len(nodes)):
        # If the length of the test_nodes is 0
        if (len(test_nodes) == 0):
            # While the node_counter is less than or equal to the length of the name list
            while (node_counter <= len(name)):
                # Append 0 and increment node_counter
                path.append(0)
                node_counter += 1
        # If the test_nodes at index 0 equals 1
        elif (test_nodes[0] == 1):
            # Append the nodes value to path, pop the first value from test_nodes, and increment node_counter
            path.append(nodes[node_counter])
            test_nodes.pop(0)
            node_counter += 1
        # If the test_nodes at index 0 equals 0
        elif (test_nodes[0] == 0):
            # Append the nodes value to path, pop the first value from test_nodes, and increment node_counter
            path.append(0)
            test_nodes.pop(0)
            node_counter += 1
        # Else, append 0 and increment node_counter
        else:
            path.append(0)
            node_counter += 1
    # Using the edge sequence property, assign the value of the edge using the path list
    node_graph.es["Edge Color"] = path
    # Sort the user_nodes list
    user_nodes.sort()
    # Copy the user_nodes list to wanted_nodes
    wanted_nodes = user_nodes.copy()
    # Create the variable user_node_path to be an empty list
    user_node_path = []
    # Set node_counter equal to 0
    node_counter = 0
    # Set the test_counter equal to 0
    test_counter = 0
    # While loop that confirms that the node_counter is less than or equal to the length of the nodes list
    while (node_counter <= len(nodes)):
        # If length of wanted_nodes is 0
        if (len(wanted_nodes) == 0):
            # While the node_counter is less than or equal to the length of the name list
            while (node_counter <= len(name)):
                # Append 0 and increment node_counter
                user_node_path.append(0)
                node_counter += 1
        # If the value in the name node_counter index equals the value in the wanted_nodes test_counter index
        elif (name[node_counter] == wanted_nodes[test_counter]):
            # Append 1 to the user_node_path, pop the first value from wanted_nodes, and increment node_counter
            user_node_path.append(1)
            wanted_nodes.pop(0)
            node_counter += 1
        # If the value in the name node_counter index is not equal to the value in the wanted_nodes test_counter index
        elif (name[node_counter] != wanted_nodes[test_counter]):
            # Append 0 to the user_node_path and increment node_counter
            user_node_path.append(0)
            node_counter += 1
        # Else, append 0 to user_node_path and increment node_counter
        else:
            user_node_path.append(0)
            node_counter += 1
    # Using the vertex sequence property, assign the value of the vertex using the user_node_path list
    node_graph.vs["Vertex Color"] = user_node_path
    # Use the matplotlib library to create the graph and set the size of the new window to 8 by 8
    graph_visual, size = plot.subplots(figsize=(8,8))
    # Use matplotlib library to make the graph unique
    graph.plot(
        # Call node_graph
        node_graph,
        # Set the target to size, which shows where the graph should be drawn
        target = size,
        # Make the vertex size equal to 0.2
        vertex_size = 0.2,
        # Create the color of the vertex to be purple or yellow if it is one of the user's nodes
        vertex_color = ["#C576F6" if user_node_path == 0 else "#FDDA0D" for user_node_path in node_graph.vs["Vertex Color"]],
        # Create the outline of the vertex to be purple or yellow if it is one of the user's nodes
        vertex_frame_color = ["#C576F6" if user_node_path == 0 else "#FDDA0D" for user_node_path in node_graph.vs["Vertex Color"]],
        # Label each node
        vertex_label = node_graph.vs["Node Labels"],
        # Create the size of the label to be 13
        vertex_label_size = 13.0,
        # Create the edge color to be purple or yellow if it is one of the connections to create the path
        edge_color = ["#C576F6" if path == 0 else "#FDDA0D" for path in node_graph.es["Edge Color"]]
    )
    # Print the graph for the user
    plot.show()
    # Change the generation_counter into a string
    generation_counter = str(generation_counter)
    # Save the graph as a pdf with each labeled generation
    graph_visual.savefig("Generation_" + generation_counter + ".pdf")


'''
prompt_user prompts the user for a list of nodes and takes into account any user error.
The user must enter d or D to represent done to start the rest of the program.
'''
def prompt_user():
    # Call global user_nodes
    global user_nodes
    # Prompt user for node input
    user_input = input("Please enter one node and click enter (enter 'd' or 'D' when done): ")
    # If the user put in a letter and the letter is not d or D
    if (user_input.isdigit() == False and user_input != "d" and user_input != "D"):
        # Prompt the user to input a valid number and return prompt_user()
        print("Please enter a valid number.")
        return prompt_user()
    # If the user inputs a d or a D and the length of the user_nodes is only 1
    elif (len(user_nodes) == 1 and (user_input == "d" or user_input == "D")):
        # Prompt the user to input at least 2 values and return prompt_user()
        print("Please enter at least 2 values.")
        return prompt_user()
    # If the length of the user_nodes is greater than 2 and the user inputted a d or a D, return
    elif (len(user_nodes) >= 2 and (user_input == "d" or user_input == "D")):
        return
    # Else, the user inputted a potential node
    else:
        # Turn the user input into an int
        user_input = int(user_input)
        # Find the length of the nodes and divide by 2 to find the node length
        length = (len(nodes)/2)
        # Round down to find the length of the nodes
        length = math.floor(length)
        # If the user_input is greater than the length of the node list options
        if (user_input > length):
            # Prompt the user to enter a value in range and return prompt_user()
            print("Please enter a value in range of 0 to ", (length))
            return prompt_user()
        # If the length of the user_nodes is 0
        elif (len(user_nodes) == 0):
            # Append the input to the user_nodes list and return prompt_user()
            user_nodes.append(user_input)
            return prompt_user()
        # If the length of the user_nodes is not 0
        elif (len(user_nodes) != 0):
            # Set counter to 0
            counter = 0
            # While loop to iterate through the user_nodes list
            while (counter < len(user_nodes)):
                # If the user_input is the same as the user_nodes at the index of counter
                if user_nodes[counter] == user_input:
                    # Prompt the user to input a different value, increment counter, and return prompt_user()
                    print("Please input a different value.")
                    counter += 1
                    return prompt_user()
                # Else, the values are not equal, increment counter
                else:
                    counter += 1
            # Append the user input to the user_nodes
            user_nodes.append(user_input)
            # Sort user_nodes
            user_nodes.sort()
            # Return prompt_user()
            return prompt_user()


'''
initial_population creates all of the solutions needed to find the optimal solution.
'''
def initial_population():
    # Call global population
    global population
    # Set tracker equal to 0
    tracker = 0
    #generates 1000 individuals
    while (tracker < 1000):
        # Create list to store new individuals
        individual = []
        # Set tracker_2 to 0
        tracker_2 = 0
        # Iterate through individual and assigns 0 or 1 to each index,
        # we want individual to be the same size of nodes because it represents
        # if the edges are present in the solution
        while (tracker_2 < len(nodes)):
            # For each index of individual assign 0 or 1 by calling coin_toss and increment tracker_2
            individual.append(coin_toss())
            tracker_2+=1
        # Once inidvidual has been iterated through the proper amount,
        # append that list to the proper index of population,
        # and increment tracker
        population.append(individual)
        tracker+=1
    # Return population
    return population


'''
Randomly generates a 0 or a 1 and returns the value
'''
def coin_toss():
    # Find a random 0 or 1 and return that value
     coin = random.randint(0,1)
     return coin


'''
getTopPerformers uses bubble sort to get the top performers from the population.
'''
def getTopPerformers():
    # Call fitness() and set the returned list to population_scores
    population_scores = fitness()
    # Use the bubble sort method on population_scores and population
    # Use the for loop to iterate through the population scores
    for i in range(len(population_scores)):
        # Use the for loop to iterate through the population scores backwards
        for j in range(0,len(population_scores)-i-1):
            # If the population_scores first index is greater than the population_scores second index
            if population_scores[j]>population_scores[j+1]:
                # Flip both values in the population_scores list
                population_scores[j], population_scores[j+1] = population_scores[j+1], population_scores[j]
                # Flip both values in the population list
                population[j], population[j+1] = population[j+1], population[j]
    # Get the top 20% of the population
    parentsSize = round(.2*len(population), 0)
    # Create the next population parent list only containing top 20% from this generation
    parents = population[:int(parentsSize)]
    # Return parents
    return parents


'''
getTopParents finds the most optimal solution from that generation.
'''
def getTopParent():
    # Call global node_graph
    global node_graph
    # Call getTopPerformers() and set the returned list to parents    
    parents = getTopPerformers()
    # Set the topParent equal to the first index in parents
    topParent = parents[0]
    # Return topParent
    return topParent


'''
crossover with the parameter of ind1 and ind2, which are two parent individuals, and generates a new individual.
'''
def crossover(ind1,ind2):
    # Randomly selects a crossover point using parent 1's length
    crosspoint = int(round(random.random()*len(ind1),0))
    # Takes the first half of the new individual 1's child
    ind1 = ind1[:crosspoint]
    # Takes the second half of the new individual 2's child    
    ind2 = ind2[crosspoint:]
    # Creates the new child by combining the halfs of both individuals
    child = ind1+ind2
    # Return child
    return child


'''
mutate takes the top 20% individuals and creates the next generation by cross mixing between two individuals.
'''
def mutate():
    # Call getTopPerformers to get the next generation parents
    parents = getTopPerformers()
    # Create nextGen to be an empty list
    nextGen=[]
    # While loop to create 1000 new child individuals
    while (len(nextGen) < 1000):
        # Call crossover function to create new random children for our new population
        nextGen.append(crossover(random.choice(parents), random.choice(parents)))
    # Return nextGen
    return nextGen


'''
node_included takes in the individual as a parameter and checks to see if the individual path
contains an edge that connects to any of the user input nodes.
'''
def node_included(individual):
    # Set score equal to 0
    score=0
    # For loop to iterate through the individual
    for i in range(len(individual)):
        # If the specific index in the individual is equal to 1
         if (individual[i] == 1):
            # If the edge contains one of the nodes from the user input
             if (nodes[i][0] in user_nodes) or (nodes[i][1] in user_nodes):
                # If the edge connects 2 of the nodes from the user input, set score equal to value
                 if (nodes[i][0] in user_nodes) and (nodes[i][1] in user_nodes):
                     score+=20000
                # Else, set score equal to value
                 else:
                     score+=10000
    # Return score
    return score


'''
lone_edge takes in the individual as a parameter and checks if the individual path contains a lone edge that 
does not connect to any user input nodes or any other edges.
'''
def lone_edge(individual):
    # Set score equal to 0
    score=0
    # Set edge_list equal to an empty list
    edges_list=[]
    # For loop to iterate through individual path list
    for i in range(len(individual)):
        # If the specific index in individual is equal to 1
        if (individual[i] == 1):
            # Append nodes in edge to edges_list
            edges_list.append(nodes[i][0])
            edges_list.append(nodes[i][1])
    # Set i equal to 0
    i=0
    # While loop to iterate through individual path list
    while (i < len(individual)):
        # If the specific index in individual is equal to 1
        if (individual[i] == 1):
            # Set check_nodes to false if the edge does not connect two of the nodes
            check_nodes = False
            # Set check_edges to false if the edge does not connect to other edges
            check_edges = False
            # If the edge connects at least 1 node
            if (nodes[i][0] in user_nodes) or (nodes[i][1] in user_nodes):
                # Set check_nodes to true 
                check_nodes = True
            # Count how many times the current node appears in the list
            # If the appearance is more than 1, the node connects at least 2 surrounding edges
            if (edges_list.count(nodes[i][0])>1) or (edges_list.count(nodes[i][0])>1):
                # Set check_edges to true
                check_edges = True           
            # If both conditions are still false this is a lone edge, set score with negative value
            if (check_edges==False and check_nodes==False):
                score = -10000
        # Increment i value
        i += 1
    # Return score
    return score


'''
num_of_edges takes in the individual as a parameter and checks to make sure that there are enough edges in the path to make a solution.
'''
def num_of_edges(individual):
    # If the individual count is greater than the length of the user_nodes, set score equal to value
    if (individual.count(1)>=len(user_nodes)):
        score=1000
    # Else, set score equal to 0
    else:
        score=0
    # Return score
    return score


'''
neighbor_edges takes in the individual as a parameter and finds the adjacent edges of the user nodes.
'''
def neighbor_edges(individual):
    # Get the adjacent edges of the user nodes
    adj_edges = adjacent_edges()
    # Set score equal to 0
    score = 0
    # For loop to traverse through the individual
    for i in range(len(individual)):
        # If individual and adj_edges equal 1, set score equal to value
        if (individual[i]==1 and adj_edges[i]==1):
            score += 10000
    # Return score
    return score


'''
adjacent_edges finds the list of the adjacent edges to each user node.
'''
def adjacent_edges():
    # Call global node_graph and user_nodes
    global node_graph
    global user_nodes
    # Set adj_nodes and adj_edges to an empty list
    adj_nodes = []
    adj_edges = []
    # For loop to traverse through user nodes to get the adjacent edges
    for i in range(len(user_nodes)):
        # Find the adjacent nodes to the specific node
        neighbors = node_graph.neighbors(node_graph.vs[i])
        # For loop to traverse through the neighbors list checking if any of those edges are already
        # in the adjacent edge list
        for i in range(len(neighbors)):
            # If the edges are not already in the list, append neighbors value to adj_nodes
            if (not(neighbors[i] in adj_nodes)):
                adj_nodes.append(neighbors[i])
    # For loop to traverse through the nodes list
    for i in range(len(nodes)):
        # If the first node or second node value is in adj_nodes, append 1
        if (nodes[i][0] in adj_nodes) or (nodes[i][1] in adj_nodes):
            adj_edges.append(1)
        # Else, append 0
        else:
            adj_edges.append(0)
    # Return adj_edges
    return adj_edges


'''
fitness takes in all of the checks for the graph and adds the score from each of those functions.
This determines which path is the best solution out of all of the other paths in the generation.
'''
def fitness():
    # Set tracker and score equal to 0
    tracker = 0
    score = 0
    # Set population_score equal to an empty list
    population_score = []
    # While loop to iterate through the population
    while (tracker < len(population)):
        # Call num_of_edges, lone_edge, node_included, and neighbor_edges to determine the fitness
        # of the specific path
        score += num_of_edges(population[tracker])
        score += lone_edge(population[tracker])
        score += node_included(population[tracker])
        score += neighbor_edges(population[tracker])
        # Append the score to the population_score list
        population_score.append(score)
        # Increment tracker
        tracker += 1
    # Return population_score
    return population_score


'''
main prompts the user for nodes, creates the graphs, and decides
how many generations we want to display.
'''
def main():

    # IMPORTANT: Please change the name of the file on line 49 if another file name wants to be read. Thank you!

    # Call global population, node_graph, and generation_counter
    global population
    global node_graph
    global generation_counter
    # Call parse_graph get the information from the file
    parse_graph()
    # Call prompt_user to get the wanted nodes from the user
    prompt_user()
    # Create an empty path list
    path = []
    # Create a graph with the nodes and with the empty path
    create_graph(path)
    # Create the initial population
    population = initial_population()
    # Set counter equal to 0
    counter = 1
    # While loop to create the amount of generations that we want
    while (counter <= 10):
        # Mutate to create the population
        population = mutate()
        # Create graph to highlight path and send in the list from the getTopParent funciton
        create_graph(getTopParent())
        # Increment counter
        counter += 1
        # Change the generation_counter into an integer
        generation_counter = int(generation_counter)
        # Increment generation_counter
        generation_counter += 1


if __name__ == '__main__':
    main()