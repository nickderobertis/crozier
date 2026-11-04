

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BadRequestErrorBodyErrorsParameters(UniversalBaseModel):
    """
    All query-, header- and path- parameters that seemed incorrect
    """

    header: typing.Optional[typing.Dict[str, str]] = None
    path: typing.Optional[typing.Dict[str, str]] = None
    query: typing.Optional[typing.Dict[str, str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
