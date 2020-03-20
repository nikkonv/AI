
# the main idea is create an GA to create a robot population 
# each robot in a final instance 
class Robot:
	def __init__(self, height, width, depth, toforward, tobackward, toleft, toright, detect_obstacle, detect_circles, detect_squares, colisions):
		self.height = height
		self.width = width
		self.depth = depth
		self.toforward = toforward
		self.tobackward = tobackward
		self.toleft = toleft
		self.toright = toright
		self.detect_obstacle = detect_obstacle
		self.detect_circles = detect_circles
		self.detect_squares = detect_squares
		self.colisions = colisions

if __name__ == '__main__':
	
	r = Robot(1.5,.5,.5,True,True,False,False,True,False,False,0)
	r.height = 1.7
	print(r.height)