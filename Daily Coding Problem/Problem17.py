def longest_file_path(system):
	paths = []
	for key, node in root.items():
		if node == True:
			paths.append(key)
		else:
			paths.append(key + '/' + longest_path((node)))	

	paths = [path for path in paths if '.' in path]
	if paths:
		return max(paths, key = lambda path: len(path))	
	else:
		return ''


def build_fs(input):
	fs = {}
	files = input.split('\n')

	# create a dictionary to represent file system, split by newlines
	# current_path keeps track of last path if we need to return
	current_path = []
	for f in files:
		indent = 0
		while '\t' in f[:2]:
			indent += 1
			f = f[1:]

		current_node = fs
		for subdir in current_path[:indent]:
			current_node = current_node[subdir]

		# When at correct place to put dictionary/file, if has a '.' then it's a file, else dictionary
		if '.' in f:
			current_node[f] = True
		else:
			current_node[f] = {}

		current_path = current_path[:indentation]
		current_path.append(f)
	return fs

def longest_absolute_path(s):
	return len(longest_file_path(build_fs(s)))