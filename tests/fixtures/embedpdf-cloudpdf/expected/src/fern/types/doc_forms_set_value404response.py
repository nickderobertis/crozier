

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_forms_set_value404response_code import DocFormsSetValue404ResponseCode
from .doc_forms_set_value404response_name import DocFormsSetValue404ResponseName


class DocFormsSetValue404Response(UniversalBaseModel):
    name: DocFormsSetValue404ResponseName
    code: DocFormsSetValue404ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
