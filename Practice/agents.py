import numbers
import collections
import collections.abc
from typing import override



class Thing:
    """
        __repr__() dùng xác định cách các đối tượng được biểu diễn 
        dưới dạng chuỗi 
            - Gỡ lỗi, Ghi log, hiểu đầu ra 
        -> Rõ ràng

        __repr__ in Thing return class_name
    """
    def __repr__(self):
        return '<{}>'.format(getattr(self, '__name__', self.__class__.__name__))
    def __init__(self):
        self.alive = False
    def is_alive(self):
        return hasattr(self, 'alive') and self.alive # return alive failse
    def show_state(self):
        print("Some thing I don't ever heared before")
    def display(self, canvas, x, y, width, height):
        pass
class Food(Thing):
    pass
class Water(Thing):
    pass

# Agent là một lớp con của Thing
class Agent(Thing):
    # program is a class
    # this program prameter is a Function
    def __init__(self, program=None ):
        self.alive = True
        self.bump = False
        self.holding = [ ]
        self.performance = 0
        # collections.abc-> Abstract Base Classes for Containers
        if program is None or not isinstance(program, collections.abc.Callable):
            print("Can't find a valid program for {}, falling back to default.".format(self.__class__.__name__))
            # Override func program
            def program(percept):
                # x = 1 
                # eval('x+1') >> 2
                return eval(input('Percept={}; action?'.format(percept)))
        self.program = program
    
    def can_grab(self, thing : Thing):
        return False

#SuperDog kế thừa Agent
class SuperDog(Agent):
    location = 1 
    def movedown(self):
        self.location += 1 

    def eat(self, thing):
        if isinstance(thing, Food):
            return True
        return False
    def drink(self, thing):
        if isinstance(thing, Water):
            return True
        return False
def program(percepts):
    # Return reaction from outside
    for p in percepts:
        if isinstance(p, Food):
            return 'eat'
        elif isinstance(p, Water):
            return 'drink'
    return 'movedown'



#----------------------------------------------------------------------------------------------------------------------#


class Environment:
    """Abstract class representing an Environment. 'Real' Environment classes
    inherit from this. Your Environment will typically need to implement:
        percept:           Define the percept that an agent sees.
        execute_action:    Define the effects of executing an action.
                           Also update the agent.performance slot.
    The environment keeps a list of .things and .agents (which is a subset
    of .things). Each agent has a .performance slot, initialized to 0.
    Each thing has a .location slot, even though some environments may not
    need this."""

    def __init__(self):
        self.things = []
        self.agents = []

    def thing_classes(self):
        return []  # List of classes that can go into environment

    def percept(self, agent):
        """Return the percept that the agent sees at this point. (Implement this.)"""
        raise NotImplementedError
    def execute_action(self, agent, action):
        """Change the world to reflect this action. (Implement this.)"""
        raise NotImplementedError

    def default_location(self, thing):
        """Default location to place a new thing with unspecified location."""
        return None
    # Ngoại sinh 
    def exogenous_change(self):
        """If there is spontaneous(Tự phát) change in the world, override this."""
        pass

    def is_done(self):
        """By default, we're done when we can't find a live agent."""
        return not any(agent.is_alive() for agent in self.agents)

    def step(self):
        """Run the environment for one time step. If the
        actions and exogenous changes are independent, this method will
        do. If there are interactions between them, you'll need to
        override this method."""
        if not self.is_done():
            actions = []
            for agent in self.agents:
                if agent.alive:
                    actions.append(agent.program(self.percept(agent)))
                else:
                    actions.append("")
            for (agent, action) in zip(self.agents, actions):
                self.execute_action(agent, action)
            self.exogenous_change()

    def run(self, steps=1000):
        """Run the Environment for given number of time steps."""
        for step in range(steps):
            if self.is_done():
                return
            self.step()

    def list_things_at(self, location, tclass=Thing):
        """Return all things exactly at a given location."""
        if isinstance(location, numbers.Number):
            return [thing for thing in self.things
                    if thing.location == location and isinstance(thing, tclass)]
        return [thing for thing in self.things
                if all(x == y for x, y in zip(thing.location, location)) and isinstance(thing, tclass)]

    def some_things_at(self, location, tclass=Thing):
        """Return true if at least one of the things at location
        is an instance of class tclass (or a subclass)."""
        return self.list_things_at(location, tclass) != []

    def add_thing(self, thing, location=None):
        """Add a thing to the environment, setting its location. For
        convenience, if thing is an agent program we make a new agent
        for it. (Shouldn't need to override this.)"""
        if not isinstance(thing, Thing):
            thing = Agent(thing)
        if thing in self.things:
            print("Can't add the same thing twice")
        else:
            thing.location = location if location is not None else self.default_location(thing)
            self.things.append(thing)
            if isinstance(thing, Agent):
                thing.performance = 0
                self.agents.append(thing)

    def delete_thing(self, thing):
        """Remove a thing from the environment."""
        try:
            self.things.remove(thing)
        except ValueError as e:
            print(e)
            print("  in Environment delete_thing")
            print("  Thing to be removed: {} at {}".format(thing, thing.location))
            print("  from list: {}".format([(thing, thing.location) for thing in self.things]))
        if thing in self.agents:
            self.agents.remove(thing)
            

class Park(Environment):
    @override
    def percept(self, agent):
        things = self.list_things_at(agent.location)
        return things
    @override
    def execute_action(self, agent, action):
        if action == 'movedown':
            agent.movedown()
            print("BlindDog at: {}".format(agent.location))
        elif  action == 'eat':
            thing = self.list_things_at(agent.location, Food)
            agent.eat(thing[0])
            self.delete_thing(thing[0])
            print("SupperDog eat")
        elif action == 'drink':
            thing = self.list_things_at(agent.location, Water)
            agent.drink(thing[0])
            self.delete_thing(thing[0])
            print("SupperDog drink")

    @override
    def is_done(self):
        return super().is_done() or not any(isinstance(thing, Food) or isinstance(thing,Water) for thing in self.things)
if __name__ == '__main__':
   
    park = Park()
    dog = SuperDog(program)
    dogfood = Food()
    water = Water()

    park.add_thing(dog, 1)
    park.add_thing(dogfood, 5)
    park.add_thing(water, 7)
    park.run(8)

