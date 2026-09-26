

import typing

from ..core.api_error import ApiError
from ..types.documents_import_from502response import DocumentsImportFrom502Response


class BadGatewayError(ApiError):
    def __init__(self, body: DocumentsImportFrom502Response, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=502, headers=headers, body=body)
