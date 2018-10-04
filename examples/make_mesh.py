import sys

from mesher.cgal_mesher import ConstrainedDelaunayTriangulation as CDT
from mesher.cgal_mesher import (
    Point,
    Mesher,
    make_conforming_delaunay,
    make_conforming_gabriel,
    Criteria,
    lloyd_optimize
)


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    edge_filename = argv[0]
    mesh_filename = argv[1]
    mesh_size = float(argv[2])

    cdt = CDT()
    with open(edge_filename, 'rt') as edge_file:
        for line in edge_file:
            ax, ay, bx, by = map(float, line.split())
            a = cdt.insert(Point(ax, ay))
            b = cdt.insert(Point(bx, by))
            cdt.insert_constraint(a, b)

    make_conforming_delaunay(cdt)
    make_conforming_gabriel(cdt)

    mesher = Mesher(cdt)
    mesher.criteria = Criteria(
        aspect_bound=0.125,
        size_bound=mesh_size
    )
    mesher.refine_mesh()

    lloyd_optimize(cdt, time_limit=0.5)

    point_to_index_map = {
        vertex.point: index
        for index, vertex in enumerate(cdt.finite_vertices())
    }

    triangles = (
        tuple(
            point_to_index_map[face.vertex_handle(i).point]
            for i in range(3)
        )
        for face in cdt.finite_faces()
    )

    with open(mesh_filename, 'wt') as mesh_file:
        print(cdt.number_of_vertices(), file=mesh_file)
        for point in point_to_index_map:
            print(point.x, point.y, file=mesh_file)

        print(cdt.number_of_faces(), file=mesh_file)
        for triangle in triangles:
            print(' '.join(map(str, triangle)), file=mesh_file)


if __name__ == "__main__":
    main()
