# Python API to Femsolve Cloud Services
Provides Python methods bound to high-performance libraries for fast delivery of engineering applications.

## Setup
### Windows
Make sure you have Python 3.11 installed. Find the installation directory of Python 3.11 and create the required
environment for it using the following commands. Open a CMD in the root directory of the Python API. 
Step 1: Create environment:
`%USERPROFILE%\AppData\Local\Programs\Python\Python311\python.exe -m venv envFCS`
Step 2: Activate the environment:
`.\envFCS\Scripts\activate`
Step 3: Install packages
`pip install -r requirements.txt`
Step 4: Deactivate if finished (optional)
`deactivate`


### Linux
Make sure you have Python 3.11 installed. You can typically use `python3.11` to refer to Python 3.11 on Linux. Open a terminal in the root directory of the Python API.
Step 1: Create environment:
`python3.11 -m venv envFCS`
Step 2: Activate the environment:
`source envFCS/bin/activate`
Step 3: Install packages:
`pip install -r requirements.txt`
Step 4: Deactivate if finished (optional):
`deactivate`

## Version Log
- 23.4.7.11  - Do not close document after saving it.
- 23.4.7.10  - Upgraded Python 3.6 to 3.11 support. Documented in README file the setup.
- 23.4.7.9   - Hotfix based on most recent testings of STH analysis
- 23.4.7.8   - Added 'is_shape_null' to check if the shape stored in the GEOM object it not null (result of failed import/operations)
- 23.4.7.3   - Added 'is_null' method to check if GEOM object is not null (result of invalid operation)
- 23.4.7.2   - Adaptation to HealingOperations ('get_free_boundary', 'fill_holes')
- 23.4.7.1   - Adaptation to 'make_pipe_bi_normal_along_vector'
- 23.4.7.0   - Backend services added
- 22.11.1.12 - Added container item methods for grouping objects
- 22.11.1.11 - Import STEP by hierarchy method added
- 22.11.1.10 - Added STL size estimation methods, exporting STLs with set size possible
- 22.11.1.9  - Invalid ID guards before methods
- 22.11.1.8  - Disabled visibility API methods (temporarily)
- 22.11.1.7  - MakePartition API hotfix
- 22.11.1.6  - MakePartition API update
- 22.11.1.5  - Avoid failure if no viewer is attached
- 22.11.1.4  - Remove colouring logs
- 22.11.1.3  - Projection method naming change.
- 22.11.1.2  - Shape tools extended (HLR projection)
- 22.11.1.1  - Removal from document added 
- 22.11.1    - Doc Hierarchy methods: add_to_document_under added
- 22.10.15.3 - Hot fix to set_object_visibility method
- 22.10.15.2 - Visibility API
- 22.10.15.1 - First API version checking.
