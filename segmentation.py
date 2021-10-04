from PIL import Image, ImageStat
import numpy


def converged(centroids, old_centroids):
	if len(old_centroids) == 0:
		return False


	if len(centroids) <= 5:
		a = 1
	elif len(centroids) <= 10:
		a = 2
	else:
		a = 4

	for i in range(0, len(centroids)):
		cent = centroids[i]
		old_cent = old_centroids[i]

		if ((int(old_cent[0]) - a) <= cent[0] <= (int(old_cent[0]) + a)) and ((int(old_cent[1]) - a) <= cent[1] <= (int(old_cent[1]) + a)) and ((int(old_cent[2]) - a) <= cent[2] <= (int(old_cent[2]) + a)):
			continue
		else:
			return False

	return True

#end converged

def getMin(pixel, centroids):
	minDist = 9999
	minIndex = 0

	for i in range(0, len(centroids)):
		d = numpy.sqrt(int((centroids[i][0] - pixel[0]))**2 + int((centroids[i][1] - pixel[1]))**2 + int((centroids[i][2] - pixel[2]))**2)
		if d < minDist:
			minDist = d
			minIndex = i

	return minIndex

#end getMin


def assignPixels(centroids):
	clusters = {}

	for x in range(0, img_width):
		for y in range(0, img_height):
			p = px[x, y]
			minIndex = getMin(px[x, y], centroids)

			try:
				clusters[minIndex].append(p)
			except KeyError:
				clusters[minIndex] = [p]

	return clusters

#end assignPixels


def adjustCentroids(centroids, clusters):
	new_centroids = []
	keys = sorted(clusters.keys())
	#print(keys)

	for k in keys:
		n = numpy.mean(clusters[k], axis=0)
		new = (int(n[0]), int(n[1]), int(n[2]))
		print(str(k) + ": " + str(new))
		new_centroids.append(new)

	return new_centroids

#end adjustCentroids


def startKmeans(someK):
	centroids = []
	old_centroids = []
	rgb_range = ImageStat.Stat(img).extrema
	i = 1

	#Initializes someK number of centroids for the clustering
	for k in range(0, someK):

		cent = px[numpy.random.randint(0, img_width), numpy.random.randint(0, img_height)]
		centroids.append(cent)
	

	print("Centroids Initialized. Starting Assignments")

	while not converged(centroids, old_centroids) and i <= 20:
		print("Iteration #" + str(i))
		i += 1

		old_centroids = centroids 								#Make the current centroids into the old centroids
		clusters = assignPixels(centroids) 						#Assign each pixel in the image to their respective centroids
		centroids = adjustCentroids(old_centroids, clusters) 	#Adjust the centroids to the center of their assigned pixels
	print("Convergence Reached!")
	print(centroids)
	return centroids

#end startKmeans


def drawWindow(result):
	img = Image.new('RGB', (img_width, img_height), "white")
	p = img.load()

	for x in range(img.size[0]):
		for y in range(img.size[1]):
			RGB_value = result[getMin(px[x, y], result)]
			p[x, y] = RGB_value

	img.show()
num_input = str(input("Enter image number: "))
k_input = int(input("Enter K value: "))


img = Image.open("lissage.bmp")
img_width, img_height = img.size
px = img.load()

result = startKmeans(k_input)
drawWindow(result)

# save the smoothed image
img.save("Segmentation.bmp")
