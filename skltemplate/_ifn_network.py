import math

class Node:
    def __init__(self, index):
        self.index = index


class RootNode(Node):
    def __init__(self):
        super().__init__(0)
        self.first_layer = None

    def set_layer(self, layer):
        self.first_layer = layer


class ClassNode(Node):
    def __init__(self, index):
        super().__init__(index)


class AttributeNode(Node):
    def __init__(self, index, inner_index, prev_node, layer, partial_x, partial_y, is_terminal=False):
        super().__init__(index)
        self.inner_index = inner_index
        self.prev_node = prev_node
        self.layer = layer
        self.is_terminal = is_terminal
        self.weight_probability_pair = {}
        self.partial_x = partial_x
        self.partial_y = partial_y

    def set_terminal(self):
        self.is_terminal = True

    def set_weight_probability_pair(self, weight_probability_pair):
        if self.is_terminal:
            self.weight_probability_pair = weight_probability_pair


class HiddenLayer:
    def __init__(self, index):
        self.index = index
        self.next_layer = None
        self.nodes = None
        self.is_continuous = False

    def set_nodes(self, nodes):
        self.nodes = nodes


    def get_node(self, index):
        for node in self.nodes:
            if node.index == index:
                return node
        return None


class IfnNetwork:
    def __init__(self):
        self.target_layer = []
        self.root_node = RootNode

    def build_target_layer(self, num_of_classes):
        if len(num_of_classes) != 0:
            for i in num_of_classes:
                self.target_layer.append(ClassNode(i))

    def create_network_structure_file(self):
        f = open("network_structure_py.txt", "w+")
        f.write("Network Structure:" + "\n\n")

        curr_layer = self.root_node.first_layer
        first_line = "0"
        for node in curr_layer.nodes:
            first_line = first_line + " " + str(node.index)
        f.write(first_line + "\n")
        while curr_layer.next_layer is not None:
            for curr_node in curr_layer.nodes:
                curr_line = str(curr_node.index)
                for next_node in curr_layer.next_layer.nodes:
                    if next_node.prev_node == curr_node.index:
                        curr_line = curr_line + " " + str(next_node.index)
                if ' ' in curr_line:
                    f.write(curr_line + "\n")
            curr_layer = curr_layer.next_layer
        f.close()

