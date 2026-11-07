

import typing

from ...types.server_upload import ServerUpload
from ...types.url_upload import UrlUpload
from ...types.vcs_upload import VcsUpload

CreateUploadRequestLocation = typing.Union[VcsUpload, UrlUpload, ServerUpload]
