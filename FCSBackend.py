
global gb
global db
global fv

from GeometryBuilder import GeometryBuilder
gb = GeometryBuilder()

from PyFCS import DocumentBuilder
db = DocumentBuilder(gb.geom_engine)

from FCSViewer import FCSViewer
fv = FCSViewer(3000, db)