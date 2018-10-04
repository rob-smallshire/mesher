from mesher.cgal_mesher import ConstrainedDelaunayTriangulation as CDT
from mesher.cgal_mesher import (
    Point, Mesher, make_conforming_delaunay, make_conforming_gabriel, Criteria, lloyd_optimize
)

def main():
    cdt = CDT()

    va = cdt.insert(Point(100, 269))
    vb = cdt.insert(Point(246, 269))
    vc = cdt.insert(Point(246, 223))
    vd = cdt.insert(Point(303, 223))
    ve = cdt.insert(Point(303, 298))
    vf = cdt.insert(Point(246, 298))
    vg = cdt.insert(Point(246, 338))
    vh = cdt.insert(Point(355, 338))
    vi = cdt.insert(Point(355, 519))
    vj = cdt.insert(Point(551, 519))
    vk = cdt.insert(Point(551, 445))
    vl = cdt.insert(Point(463, 445))
    vm = cdt.insert(Point(463, 377))
    vn = cdt.insert(Point(708, 377))
    vo = cdt.insert(Point(708, 229))
    vp = cdt.insert(Point(435, 229))
    vq = cdt.insert(Point(435, 100))
    vr = cdt.insert(Point(100, 100))

    cdt.insert_constraint(va, vb)
    cdt.insert_constraint(vb, vc)
    cdt.insert_constraint(vc, vd)
    cdt.insert_constraint(vd, ve)
    cdt.insert_constraint(ve, vf)
    cdt.insert_constraint(vf, vg)
    cdt.insert_constraint(vg, vh)
    cdt.insert_constraint(vh, vi)
    cdt.insert_constraint(vi, vj)
    cdt.insert_constraint(vj, vk)
    cdt.insert_constraint(vk, vl)
    cdt.insert_constraint(vl, vm)
    cdt.insert_constraint(vm, vn)
    cdt.insert_constraint(vn, vo)
    cdt.insert_constraint(vo, vp)
    cdt.insert_constraint(vp, vq)
    cdt.insert_constraint(vq, vr)
    cdt.insert_constraint(vr, va)

    vs = cdt.insert(Point(349, 236))
    vt = cdt.insert(Point(370, 236))
    vu = cdt.insert(Point(370, 192))
    vv = cdt.insert(Point(403, 192))
    vw = cdt.insert(Point(403, 158))
    vx = cdt.insert(Point(349, 158))

    cdt.insert_constraint(vs, vt)
    cdt.insert_constraint(vt, vu)
    cdt.insert_constraint(vu, vv)
    cdt.insert_constraint(vv, vw)
    cdt.insert_constraint(vw, vx)
    cdt.insert_constraint(vx, vs)

    vy = cdt.insert(Point(501, 336))
    vz = cdt.insert(Point(533, 336))
    v1 = cdt.insert(Point(519, 307))
    v2 = cdt.insert(Point(484, 307))

    cdt.insert_constraint(vy, vz)
    cdt.insert_constraint(vz, v1)
    cdt.insert_constraint(v1, v2)
    cdt.insert_constraint(v2, vy)

    print("Number of vertices:", cdt.number_of_vertices())

    mesher = Mesher(cdt)
    seeds = [
        Point(505, 325),
        Point(379, 172),
    ]
    mesher.seeds_from(seeds)

    make_conforming_delaunay(cdt)
    print("Number of vertices:", cdt.number_of_vertices())

    make_conforming_gabriel(cdt)
    print("Number of vertices:", cdt.number_of_vertices())

    mesher.criteria = Criteria(
        aspect_bound=0.125,
        size_bound=30
    )
    mesher.refine_mesh()
    print("Number of vertices:", cdt.number_of_vertices())

    lloyd_optimize(cdt, max_iteration_number=10)
    print("Number of vertices:", cdt.number_of_vertices())


if __name__ == '__main__':
    main()
