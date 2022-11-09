
# Versioning check
from PyFCS import check_api_compatibility, get_backend_api_version
FCS_PYTHON_API_VERSION = "22.11.1.1"
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