
# Platform specific environment settings
import sys
import os 
if sys.platform == "linux":
    filepath = os.path.dirname(os.path.abspath(__file__))
    added_path = f"{filepath}/../x64/Debug/"
    print(added_path)
    sys.path.append(added_path)
    print("Updated Python path for Linux!")

from FCSBackend import gb
from FCSBackend import fv
from FCSBackend import db
from PyFCS import ColourSelection

# Prepare a document 
db.set_document_name("PyFCSProject")

# Primitives test
torus = gb.make_torus_r_r(10.0,5.0)
cyl = gb.make_cylinder_r_h_a(5.0,10.0,2.0)

torus_id = fv.add_to_document(torus, "Torus")
fv.set_specific_object_colour(torus_id, 255, 0, 100)

cyl_id = fv.add_to_document(cyl, "Cylinder")
fv.set_specific_object_colour(cyl_id, 255, 255, 0)

vertex1_id = db.get_geom_object_by_id(17) # (5, 0, 10)
vertex2_id = db.get_geom_object_by_id(7) # (15, 0, 0)
list_distance = gb.closest_points(vertex1_id, vertex2_id)
print(f"Closest points : {list_distance}")
