# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BulkEnrollmentOperationError(Model):
    """Bulk enrollment operation error.

    All required parameters must be populated in order to send to Azure.

    :param registration_id: Required. Device registration id.
    :type registration_id: str
    :param error_code: Required. Error code
    :type error_code: int
    :param error_status: Required. Error status
    :type error_status: str
    """

    _validation = {
        "registration_id": {"required": True},
        "error_code": {"required": True},
        "error_status": {"required": True},
    }

    _attribute_map = {
        "registration_id": {"key": "registrationId", "type": "str"},
        "error_code": {"key": "errorCode", "type": "int"},
        "error_status": {"key": "errorStatus", "type": "str"},
    }

    def __init__(
        self, *, registration_id: str, error_code: int, error_status: str, **kwargs
    ) -> None:
        super(BulkEnrollmentOperationError, self).__init__(**kwargs)
        self.registration_id = registration_id
        self.error_code = error_code
        self.error_status = error_status