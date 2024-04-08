from typing import List


class Point3d:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Point3d(self.x + other.x, self.y + other.y, self.z + other.z)

    def __neg__(self):
        return Point3d(-self.x, -self.y, -self.z)

    def __sub__(self, other):
        return self.__add__(other.__neg__())

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Point3d(self.x * other, self.y * other, self.z * other)
        if isinstance(other, Point3d):
            return Point3d(self.x * other.x, self.y * other.y, self.z * other.z)
        raise

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __repr__(self):
        return f"[{self.x},{self.y},{self.z}]"

    def dot(self, other):
        p = self * other
        return p.x + p.y + p.z

    def cross(self, other):
        return Point3d(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

    def norm(self):
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5


class Triangle3d:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def __repr__(self):
        return f"Triangle[{self.p1}, {self.p2}, {self.p3}]"


######################################################


def determine_shadow_case(light: Point3d, vertices: List[Point3d]):
    z_coords = [v.z for v in vertices]
    light_z = light.z

    if all(z > light_z for z in z_coords):
        return 0.0

    if light_z > min(z_coords) and light_z < max(z_coords):
        return -1.0

    return False


def project_vertices_to_ground(light: Point3d, vertices: List[Point3d]):
    projected_points = []
    for vertex in vertices:
        a, b, c = light.x, light.y, light.z

        if vertex.z == c:
            t = -c / ((vertex.z - c) + 1e-10)  # Avoid division by zero
        else:
            t = -c / (vertex.z - c)
        x_proj = a + t * (vertex.x - a)
        y_proj = b + t * (vertex.y - b)
        projected_points.append(Point3d(x_proj, y_proj, 0))
    return projected_points


def cross_product(o, a, b):
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)


def find_convex_hull_points_no_np(points):
    start = min(points, key=lambda p: p.x)
    hull = [start]

    point = start
    while True:
        next_point = points[0] if points[0] != point else points[1]
        for p in points:
            if cross_product(point, next_point, p) < 0:
                next_point = p
        point = next_point
        if point == start:
            break
        hull.append(point)

    return hull


def calculate_polygon_area(points):
    n = len(points)
    area = 0.0

    for i in range(n):
        j = (i + 1) % n
        area += points[i].x * points[j].y
        area -= points[j].x * points[i].y

    area = abs(area) / 2.0
    return area


def solution(point1, point2, point3, point4, light_source):
    tent_vertices = [Point3d(*point) for point in [point1, point2, point3, point4]]
    light = Point3d(*light_source)

    det = determine_shadow_case(light, tent_vertices)
    if det:
        return f"{det:.6f}"
    projected_vertices = project_vertices_to_ground(light, tent_vertices)
    projected_vertices = find_convex_hull_points_no_np(projected_vertices)
    area = calculate_polygon_area(projected_vertices)
    return f"{area:.6f}"
