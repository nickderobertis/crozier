

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_forms_import_data404response_code import DocFormsImportData404ResponseCode
from .doc_forms_import_data404response_name import DocFormsImportData404ResponseName


class DocFormsImportData404Response(UniversalBaseModel):
    name: DocFormsImportData404ResponseName
    code: DocFormsImportData404ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
