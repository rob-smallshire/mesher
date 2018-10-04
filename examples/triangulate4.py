from mesher.cgal_mesher import ConstrainedDelaunayTriangulation as CDT
from mesher.cgal_mesher import Point

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

if __name__ == '__main__':
    main()