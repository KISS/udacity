class Group(object):
  def __init__(self, _name):
    self.name = _name
    self.groups = []
    self.users = []

  def add_group(self, group):
    self.groups.append(group)

  def add_user(self, user):
    self.users.append(user)

  def get_groups(self):
    return self.groups

  def get_users(self):
    return self.users

  def get_name(self):
    return self.name


def is_user_in_group(user, group):
  """
  Return True if user is in the group, False otherwise.

  Args:
    user(str): user name/id
    group(class:Group): group to check user membership against
  """
  # sort user list in-place
  group.users.sort()
  found = False

  # run binary search on group users
  found = binary_search(group.users, user, 0, len(group.users))

  # return early if our user belongs to our group
  if found:
    return found

  # traverse all subgroups of our current group to see if our user belongs to one of them (therefore making them a user of our parent group)
  for g in group.groups:
    found = is_user_in_group(user, g)
  return found

def binary_search(arr, target, start_index, end_index):
  if start_index >= end_index:
    return False

  mid = (start_index + end_index) // 2

  if arr[mid] == target:
    return True
  # compare first character to determine which side of the array to traverse next
  elif arr[mid][0] < target[0]:
    return binary_search(arr, target, mid + 1, end_index)
  else:
    return binary_search(arr, target, start_index, mid - 1)


# Set up groups
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Testing
print(is_user_in_group(sub_child_user, sub_child))    # Returns True
print(is_user_in_group(sub_child_user, parent))       # Returns True
print(is_user_in_group("xyz", sub_child))             # Returns False, user doesn't exist
print(is_user_in_group("xyz", parent))                # Returns False, user doesn't exist

# Add new user to child group
child.add_user("xyz")
print(is_user_in_group("xyz", sub_child))             # Returns False, user isn't in this group
print(is_user_in_group("xyz", child))                 # Returns True
print(is_user_in_group("xyz", parent))                # Returns True