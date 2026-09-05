

import typing

from ...types.envelope_any_url import EnvelopeAnyUrl
from ...types.envelope_file_upload_schema import EnvelopeFileUploadSchema

UploadFileResponse = typing.Union[EnvelopeFileUploadSchema, EnvelopeAnyUrl]
