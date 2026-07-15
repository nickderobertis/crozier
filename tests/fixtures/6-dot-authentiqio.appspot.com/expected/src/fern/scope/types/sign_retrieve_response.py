

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SignRetrieveResponse(UniversalBaseModel):
    exp: typing.Optional[int] = None
    field: typing.Optional[str] = None
    sub: typing.Optional[str] = pydantic.Field(default=None)
    """
    base64safe encoded public signing key
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
