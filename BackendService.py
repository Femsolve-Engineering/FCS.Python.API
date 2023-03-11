
from FCSViewer import FCSViewer
from FCSViewer import GeometryBuilder, gb
from FCSViewer import DocumentBuilder

class BackendService(object):
    """
    Template class for hosting specific plugins.
    """

    def __init__(self, app_guid: str):
        """
        Constructor.
        """
        self.app_guid = app_guid
        self.fv: FCSViewer
        self.db: DocumentBuilder
        self.gb: GeometryBuilder

    def set_existing_services(self, fcs_viewer: FCSViewer) -> None: 
        """
        To any backend service connect we pass on the instances of the main operators.
        """

        # ToDo: Set session services
        self.gb = gb # Only need a single instance right now
        self.fv = fcs_viewer
        self.db = self.fv.document_builder

    def run_command(self, command_name: str, command_args: dict={}) -> dict:
        """
        Returns true, if the command was found and run (even if it failed).
        Return false otherwise.
        """

        log = self.fv.get_logger()
        log.set_logging_context(self.app_guid)
        result = None

        try:
            command_ptr = getattr(self, command_name)
            result = command_ptr(command_args)
        except AttributeError:
            log.err(f'Could not find {command_name}!')
        except Exception as ex:
            log.err(f'Something failed: {ex.args}!')
        finally: 
            log.set_logging_context('')

        return result

#--------------------------------------------------------------------------------------------------
# Pure virtual methods that require implementation
#--------------------------------------------------------------------------------------------------

    def get_available_callbacks(self) -> list:
        """
        List of available callbacks to be forwarded to the listeners of the cloud application.
        """
        raise NotImplementedError("`get_available_callbacks` needs to be implemented in the base class!")
