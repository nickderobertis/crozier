

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Identifier(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier string. DOIs should start `10.`.
    """

    scheme: typing.Optional[str] = pydantic.Field(default=None)
    """
    A keyword indicating the scheme from which the identifier is drawn. Valid keywords may be obtained from the `id_schemes` endpoint.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
