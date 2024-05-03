import random
class Vector:
    # Initialize a vector object with elements and a length
    def __init__(self, lst):
        # Confirm list is valid
        for element in lst:
            if isinstance(element, int) or isinstance(element, float):
                element = element * 1.0
            else:
                raise TypeError("Vector contents must be of type 'int' or 'float'")
        # Initialize vector
        self.vect = lst
        self.dim = len(lst)

    # Create random vector of length n
    @staticmethod
    def rand(n, range=[0, 1]):
        values = []
        for i in range(n):
            values.append(random.uniform(range[0], range[1]))
        return Vector(values)

    # Convert vector to string for easy readability
    def __str__(self):
        str_value = " Ʌ\n"
        for a in self.vect:
            str_value += format(a, ".2f") + "\n"
        return str_value + " V"

    # Overload the indexing operator
    def __getitem__(self, key):
        return self.vect[key]

    # Overload multiplication operator
    def __mul__(self, other):
        # Inner product of two vectors
        if isinstance(other, self.__class__):
            if self.dim == other.dim:
                result = 0
                for a, b in zip(self.vect, other.vect):
                    result += a * b
                return result
            else:
                raise TypeError("Vectors must be the same length")
        # Scalar multiplication
        elif isinstance(other, float):
            self.vect = [i * other for i in self.vect]
            return self

    # Addition operator for two equally sized vectors
    def __add__(self, other):
        if self.dim == other.dim:
            new_vect = []
            for a, b in zip(self.vect, other.vect):
                new_vect.append(a + b)
            return Vector(new_vect)
        else:
            raise TypeError("Vectors must be the same length")

    # Subtraction operator for two equally sized vectors
    def __sub__(self, other):
        if self.dim == other.dim:
            new_vect = []
            for a, b in zip(self.vect, other.vect):
                new_vect.append(a - b)
            return Vector(new_vect)
        else:
            raise TypeError("Vectors must be the same length")

    # Calculate the Euclidean norm of the vector
    def norm(self):
        return (sum([a**2 for a in self.vect])) ** (1 / 2)

    # Calculate the average value of the vector
    def avg(self):
        return sum(self.vect) / self.dim

    # Calculate the standard deviation of the vector
    def std(self):
        inside = 0
        avg = self.avg()
        for element in self.vect:
            inside += (element - avg) ** 2
        return (inside / 2) ** (1 / 2)

    # Return maximum value in the vector
    def maximum(self):
        return max(self.vect)

    # Return minimum value in the vector
    def minimum(self):
        return min(self.vect)


# Special vector where elements are other Vectors
class BlockVector:
    def __init__(self, lst):
        dims = []
        # Confirm list is valid
        for element in lst:
            if not isinstance(element, Vector):
                raise TypeError("Block vector contents must be of type 'Vector'")
            else:
                dims.append(len(element.vect))

        # Initialize vector
        self.vect = lst
        self.dim = dims

    # Overload multiplication operator
    def __mul__(self, other):
        # Inner product of two vectors
        if isinstance(other, self.__class__):
            # Check dimensions
            if self.dim == other.dim:
                result = 0
                for a, b in zip(self.vect, other.vect):
                    result += a * b
                return result
            else:
                raise TypeError("Block vectors must be the same length")
        # Scalar multiplication
        elif isinstance(other, float):
            self.vect = [i * other for i in self.vect]
            return self

    # Euclidean Norm for block vectors
    def norm(self):
        return (sum([(element.norm()) ** 2 for element in self.vect])) ** (1 / 2)
