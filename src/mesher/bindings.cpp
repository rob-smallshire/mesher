#include <vector>
#include <string>
#include <cstdarg>
#include <cstring>

#include <boost/lexical_cast.hpp>

#include <pybind11/pybind11.h>

namespace py = pybind11;

#include <CGAL/Exact_predicates_inexact_constructions_kernel.h>
#include <CGAL/Constrained_Delaunay_triangulation_2.h>
#include <CGAL/Delaunay_mesher_2.h>
#include <CGAL/Delaunay_mesh_face_base_2.h>
#include <CGAL/Delaunay_mesh_vertex_base_2.h>
#include <CGAL/Delaunay_mesh_size_criteria_2.h>

using K = CGAL::Exact_predicates_inexact_constructions_kernel;
using Vb = CGAL::Delaunay_mesh_vertex_base_2<K>;
using Fb = CGAL::Delaunay_mesh_face_base_2<K>;
using Tds = CGAL::Triangulation_data_structure_2<Vb, Fb>;
using CDT = CGAL::Constrained_Delaunay_triangulation_2<K, Tds>;

using Vertex_handle = CDT::Vertex_handle;
using Point = CDT::Point;

PYBIND11_MODULE(cgal_mesher, m)
{
    py::class_<Point>(m, "Point")
            .def(py::init<double, double>(), py::arg("x"), py::arg("y"))
            .def(py::init<int, int>(),  py::arg("x"), py::arg("y"))
            .def_property_readonly("x", &Point::x)
            .def_property_readonly("y", &Point::y)
            .def("__repr__",
            [](const Point &p) {
                std::string r("Point(");
                r += boost::lexical_cast<std::string>(p.x());
                r += ", ";
                r += boost::lexical_cast<std::string>(p.y());
                r += ")";
                return r;
            })
            ;

    //py:class_<CDT>("m", "ConstrainedDelaunayTriangulation2")
    //    .def
}
