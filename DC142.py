

def file(path):
	with open(path, 'r') as f:
		
		n = int(f.readline().strip())
		world = [[c for c in line.strip('\n')] for line in f]

	return world, n


def print_world(world, n):
	for r in world:
		print(''.join(r))

def sparsemap(world, n):

	for r in range(n-1, 0, -1):
		for c in range(n):
			rabove = r - 1

			if world[r][c] in ('.', '#'):
				continue

			while rabove >=0 and world[rabove][c] == ' ':
				rabove -= 1

			if rabove < 0 or world[rabove][c] == "#":
				continue

			world[r][c] = '.';
			world[rabove][c] = ' ';


if __name__ == '__main__':
	world, n = file('dc142.txt')
	sparsemap(world, n)
	print_world(world, n)

