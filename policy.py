class Policy:
    def __init__(self):
        self.matrix = []

    """
    Get the states and actions from the policy
    """
    def get_state_action(self, index):
        if index < len(self.matrix):
            return self.matrix[index][0], self.matrix[index][1], self.matrix[index][2]
        else:
            print("Out of bounds when looking for a particular policy")
            return

    """
    insert a unique action in the policy
    """
    def insert_action(self, index, action, value):
        if index < len(self.matrix):
            policytuple = self.matrix[index]
            policytuple[1] = action
            policytuple[2] = value
            self.matrix[index] = policytuple
        else:
            print("Out of bounds when inserting an action in policy")
            return

    """
    insert a unique state in the policy    
    """
    def insert_state(self, index, state, value):
        if index < len(self.matrix):
            policytuple = self.matrix[index]
            policytuple[0] = state
            policytuple[2] = value
            self.matrix[index] = policytuple
        else:
            print("Out of bounds when inserting a state in policy")
            return

    """
    insert both a state and a action at a same index in the policy
    """
    def insert_state_action(self, index, state, action, value):
        if index < len(self.matrix):
            policytuple = self.matrix[index]
            policytuple[0] = state
            policytuple[1] = action
            policytuple[2] = value
            self.matrix[index] = policytuple
        else:
            print("Out of bounds when inserting a state and action in policy")
            return

    """
    initialize the policy as an array of 3 dimensionnal arrays filled with 0
    """
    def init_policy(self, length):
        self.matrix = [[0, 0, 0] for i in range(length)]
