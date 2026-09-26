

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_forms_get404response_code import DocFormsGet404ResponseCode
from .doc_forms_get404response_name import DocFormsGet404ResponseName


class DocFormsGet404Response(UniversalBaseModel):
    name: DocFormsGet404ResponseName
    code: DocFormsGet404ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
