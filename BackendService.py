class BackendService(object):
    """
    Template class for hosting specific plugins.
    """

    def __init__(self, app_guid: str):
        """
        Constructor.
        """
        self.app_guid = app_guid

    def set_existing_services(self, fcs_viewer, geometry_builder, document_builder) -> None: 
        """
        To any backend service connect we pass on the instances of the main operators.
        """

        self.fv = fcs_viewer
        self.gb = geometry_builder
        self.db = document_builder

    def get_available_callbacks(self) -> list:
        """
        List of available callbacks to be forwarded to the listeners of the cloud application.
        """
        raise NotImplementedError("`get_available_callbacks` needs to be implemented in the base class!")


    def run_command(self, command_name: str) -> bool:
        """
        Returns true, if the command was found and run (even if it failed).
        Return false otherwise.
        """
        raise NotImplementedError("`run_command` needs to be implemented in the base class!")
