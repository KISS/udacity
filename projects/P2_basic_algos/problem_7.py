# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
  def __init__(self, route_handler_msg):
    # initialize the trie with a root node and a handler, this is the root path or home page node
    self.root = RouteTrieNode("/")
    self.handler = route_handler_msg

  def insert(self, paths, handler_msg):
    # recursively add nodes, assigning the handler to only the leaf (deepest) node of this path
    curr = self.root
    # iterate through each path, adding a path to the Trie if it doesn't exist, until we've built all paths
    for path in paths:
      if path not in curr.children:
        curr.children[path] = RouteTrieNode("")
      curr = curr.children[path]
    # set leaf path handler
    curr.handler = handler_msg

  def find(self, paths):
    # starting at the root, navigate the Trie to find a match for the path
    # return the handler for a match, or None for no match
    if not paths:
      return self.handler

    curr = self.root
    for path in paths:
      if path not in curr.children:
        return None
      curr = curr.children[path]
    return curr.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
  def __init__(self, route_handler_msg):
    self.children = dict()
    self.handler = route_handler_msg

  def insert(self, path):
    new_node = RouteTrieNode(path)
    self.children[new_node]

# The Router class will wrap the Trie and handle requests
class Router:
  def __init__(self, route_handler_msg, error_msg="404: Page Not Found"):
    # create a new RouteTrie for holding our routes
    self.routes = RouteTrie(route_handler_msg)
    self.not_found = error_msg

  def add_handler(self, path, handler_msg):
    # split the path and pass the pass parts as a list to the RouteTrie
    path_parts = self.split_path(path)
    self.routes.insert(path_parts, handler_msg)

  def lookup(self, path):
    # lookup path (by parts) and return the associated handler
    path_parts = self.split_path(path)
    handler = self.routes.find(path_parts)
    return handler if handler else self.not_found

  def split_path(self, path):
    path_parts = list()
    s = ""
    for char in path:
      if char != "/":
        s += char
      if s != "" and char == "/":
        path_parts.append(s)
        s = ""
    if s != "":
      path_parts.append(s)
    return path_parts


# Test 1: home
# create the router and add a route
router_one = Router("root handler", "not found handler")
router_one.add_handler("/home/", "home handler")  # add a route

# some lookups with the expected output
print(router_one.lookup("/")) # should print 'root handler'
print(router_one.lookup("/home")) # should print 'home handler'
print(router_one.lookup("/home/careers")) # should print 'not found handler'


# Test 2: home/about
# create the router and add a route
router_two = Router("root 2 handler")
router_two.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print("\n")
print(router_two.lookup("/")) # should print 'root 2 handler'
print(router_two.lookup("/home")) # should print '404: Page Not Found'
print(router_two.lookup("/home/about")) # should print 'about handler'
print(router_two.lookup("/home/about/")) # should print 'about handler'


# Test 3: home/about/me
# create the router and add a route
router_three = Router("root 3 handler")
router_three.add_handler("/home/about/", "about handler")  # add a route
router_three.add_handler("/home/about/me/", "about me handler")  # add a route

# some lookups with the expected output
print("\n")
print(router_three.lookup("/")) # should print 'root 3 handler'
print(router_three.lookup("/home")) # should print '404: Page Not Found'
print(router_three.lookup("/home/about/")) # should print 'about handler'
print(router_three.lookup("/home/about/me")) # should print 'about me handler'