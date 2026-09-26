

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_versions_list404response_code import DocVersionsList404ResponseCode
from .doc_versions_list404response_name import DocVersionsList404ResponseName


class DocVersionsList404Response(UniversalBaseModel):
    name: DocVersionsList404ResponseName
    code: DocVersionsList404ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
