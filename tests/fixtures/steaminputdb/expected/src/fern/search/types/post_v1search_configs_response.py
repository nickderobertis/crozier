

import typing

from ...types.c_published_file_query_files_response import CPublishedFileQueryFilesResponse
from ...types.configs_response import ConfigsResponse

PostV1SearchConfigsResponse = typing.Union[ConfigsResponse, CPublishedFileQueryFilesResponse]
