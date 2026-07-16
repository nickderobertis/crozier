

import typing

from .local_jwt_verifier import LocalJwtVerifier
from .ref_jwt_verifier import RefJwtVerifier

ImportExportServiceDescriptorsItemJwtVerifier = typing.Union[LocalJwtVerifier, RefJwtVerifier]
