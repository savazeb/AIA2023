class State:
    OPEN = 0
    WALL = 1
    BEGIN = 2
    END = 3
    FLOW_N = 4
    FLOW_E = 5
    FLOW_S = 6
    FLOW_W = 7
    ROUTE_N = 8
    ROUTE_E = 9
    ROUTE_S = 10
    ROUTE_W = 11

    def is_flow(self, state):
        """
        Args:
            state (int)

        Returns:
            bool: true if state is a FLOW state
        """
        return state >= 4 and state <= 7

    def is_route(self, state):
        """
        Args:
            state (int):

        Returns:
            bool: true if state is a ROUTE state
        """
        return state >= 8 and state <= 11

    def find(f, states):
        """
        Args:
            f (function)
            states (list)

        Returns:
            int: position where predicate f returns true
        """
        for i in range(len(states)):
            if f(states[i]):
                return i
        return -1

    def find_begin(self, states):
        """
        Args:
            states (list)

        Returns:
            int: position of the first BEGIN, or -1
        """
        return self.find(lambda x: x == self.BEGIN, states)

    def find_end(self, states):
        """
        Args:
            states (list)

        Returns:
            int: position of the first END, or -1
        """
        return self.find(lambda x: x == self.END, states)

    def find_flow(self, states):
        """
        Args:
            states (int)

        Returns:
            int: position of the first FLOW state, or -1
        """
        return self.find(self.is_flow(), states)

    def points_at_me(self, state, relation):
        """
        Args:
            state (int)
            relation (int): (0=north, 1=east, 2=south, 3=west)

        Returns:
            bool: true if state points in given direction
        """
        return (state % 4) == ((relation + 2) % 4)

    def next(self, state, states):
        """
        Args:
            state (int)
            states (list)

        Returns:
            int: the next state given neighbors neighbors
        """
        begin = State.find_begin(states)
        end = State.find_end(states)
        flow = begin if begin >= 0 else self.find_flow(states)
        route = state.find_route(states)

        match state:
            case self.OPEN:
                if flow >= 0:
                    return 4 + flow
                else:
                    return state

            case self.FLOW_N | self.FLOW_E | self.FLOW_S | self.FLOW_W:
                if route >= 0 and self.points_at_me(states[route], route):
                    return state + 4
                else:
                    return state

            case self.END:
                if flow >= 0:
                    return flow + 8
                else:
                    return state

            case self.BEGIN:
                if route >= 0:
                    return states[route]
                else:
                    return state

            case _:
                return state
