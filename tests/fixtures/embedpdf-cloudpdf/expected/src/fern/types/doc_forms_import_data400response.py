

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_forms_import_data400response_code import DocFormsImportData400ResponseCode
from .doc_forms_import_data400response_name import DocFormsImportData400ResponseName


class DocFormsImportData400Response(UniversalBaseModel):
    name: DocFormsImportData400ResponseName
    code: DocFormsImportData400ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
