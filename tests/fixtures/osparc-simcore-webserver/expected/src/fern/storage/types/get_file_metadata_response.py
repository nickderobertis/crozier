

import typing

from ...types.envelope_file_meta_data_get import EnvelopeFileMetaDataGet
from ...types.file_meta_data import FileMetaData

GetFileMetadataResponse = typing.Union[FileMetaData, EnvelopeFileMetaDataGet]
