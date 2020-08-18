import os

def find_files(suffix, path):
  """
  Find all files beneath path with file name suffix.

  Note that a path may contain further subdirectories
  and those subdirectories may also contain further subdirectories.

  There are no limits to the depth the subdirectories can be.

  Args:
    suffix(str): suffix of the file name to be found
    path(str): path of the file system

  Returns:
    a list of paths
  """
  # initialize our output list
  paths = list()

  # verify we're searching in an accessible directory
  if os.path.isdir(path):
    # get a list of all files/subdirectories in our current directory
    items = os.listdir(path=path)

    # iterate through each file/subdirectory
    for item in items:
      # build our path to the current file/subdirectory being reviewed
      new_path = os.path.join(path, item)

      # if item is a file with the suffix we're searching for, add its path to our output list
      if os.path.isfile(new_path) and new_path.endswith(suffix):
        paths.append(new_path)
      elif os.path.isdir(new_path):
        # if item is a subdirectory, search for all files within this subdirectory that match our search criteria and append the paths to these files to our output
        p = find_files(suffix, new_path)
        paths += p

  return paths


print(find_files(".c", "./testdir"))   # returns 4 paths: ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']

print(find_files(".x", "./testdir"))   # returns 0 paths because no files exist in our path with a .x suffix

print(find_files(".c", "./rand"))      # returns 0 paths because the path doesn't exist or isn't reachable