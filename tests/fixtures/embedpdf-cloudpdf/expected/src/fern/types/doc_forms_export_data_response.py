

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_forms_export_data_response_code import DocFormsExportDataResponseCode
from .doc_forms_export_data_response_name import DocFormsExportDataResponseName


class DocFormsExportDataResponse(UniversalBaseModel):
    name: DocFormsExportDataResponseName
    code: DocFormsExportDataResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
