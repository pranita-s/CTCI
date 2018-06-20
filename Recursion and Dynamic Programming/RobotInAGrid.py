# TIME - O(2 ** (r+c)) (r+c) -- total number of steps

def RobotInAGrid_master(grid, offlimits):
	R = len(Grid)
	C = len(Grid[0])
	path = []
	if RobotInAGrid(R-1,C-1,offlimits,path):
		return path
	return None
	

def RobotInAGrid(curr_r, curr_c, offlimits, path):
	if curr_r < 0 or curr_c < 0 or (curr_r,curr_c) in offlimits:
		return False

		
	if (curr_r == 0 and curr_c == 0) or RobotInAGrid(curr_r-1,curr_c,offlimits, path) or 
	/ RobotInAGrid(curr_r,curr_c-1,offlimits,path):
		path.append((curr_r,curr_c))
		return True
	
	return False
	
	
# DYNAMIC PROGRAMMING

# TIME -  O(rc)

def RobotInAGrid(R,C,offlimits):
	path = []

	if helper(R-1,C-1,offlimits,path):
		return path
	return None
	

def helper(curr_r,curr_c,offlimits,path):
	if curr_r <0 or curr_c <0 or (curr_r,curr_c) in offlimits:
		return False

	point = (curr_r,curr_c)
	
	if point in offlimits:
		return False
	
	if point == (0,0) or helper(curr_r-1,curr_c,offlimits,path) or helper(curr_r,curr_c-1,offlimits,path):
		path.append(point)
		return True
	
	offlimits.append(point)
	return False
	
	
	
offlimits = [(1,1),(1,3),(3,2)]

print(RobotInAGrid(4,5,offlimits))
	
	


