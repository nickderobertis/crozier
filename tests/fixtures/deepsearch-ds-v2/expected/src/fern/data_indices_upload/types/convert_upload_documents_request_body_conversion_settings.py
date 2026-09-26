

import typing

from ...types.partial_direct_conversion_parameters import PartialDirectConversionParameters
from ...types.project_data_index_conversion_settings_input import ProjectDataIndexConversionSettingsInput

ConvertUploadDocumentsRequestBodyConversionSettings = typing.Union[
    ProjectDataIndexConversionSettingsInput, PartialDirectConversionParameters
]
