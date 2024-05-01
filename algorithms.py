from vectors import Vector


def kmeans(k, vectors):
    # Find range to initialize centroids
    dimension = 0
    maximum = 1
    minimum = 0
    for vector in vectors:
        dimension = vector.dim
        if vector.maximum() > maximum:
            maximum = vector.maximum()
        if vector.minimum() < minimum:
            minimum = vector.minimum()

    # Initialize centroids
    centroids = []
    cluster_labels = []
    for i in range(k):
        centroids.append(Vector.rand(dimension, [minimum, maximum]))

    for i in range(100):
        cluster_labels = find_closest_centroid(vectors, centroids)
        centroids = calculate_centroids(k, vectors, cluster_labels)

    return cluster_labels


# Function that recalculates closest cluster for each vector
def find_closest_centroid(vectors, centroids):
    clusters = []
    for vector in vectors:
        closest_distance = int("inf")
        closest_cluster = 0
        for i in range(len(centroids)):
            if (vector - centroids[i]).norm() ** 2 < closest_distance:
                closest_distance = (vector - centroids[i]).norm() ** 2
                closest_cluster = i
        clusters.append(closest_cluster)
    return clusters


# Function that recalculates the mean of each cluster to be used as centroid
def calculate_centroids(k, vectors, clusters):
    centroids = []
    for i in range(k):
        sum = Vector([0 for k in range(len(k))])
        count = 0
        for j in range(len(vectors)):
            if clusters[j] == i:
                sum += vectors[j]
                count += 1
        mean_vector = sum * (1 / count)
        centroids.append(mean_vector)

    return centroids
