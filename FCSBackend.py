"""
22.10.15.3 - Hot fix to set_object_visibility method
22.10.15.2 - Visibility API
22.10.15.1 - First API version checking.
"""
# Versioning check
from PyFCS import check_api_compatibility, get_backend_api_version
FCS_PYTHON_API_VERSION = "22.10.15.2"
if not check_api_compatibility(FCS_PYTHON_API_VERSION):
    raise Exception(f"Incompatible backend API!\n"
                   f"Please make sure that a major version of {get_backend_api_version()} is used.")

# Operational libraries setup
global gb
global db
global fv

from GeometryBuilder import GeometryBuilder
gb = GeometryBuilder()

from PyFCS import DocumentBuilder
db = DocumentBuilder(gb.geom_engine)

from FCSViewer import FCSViewer
fv = FCSViewer(3000, db)