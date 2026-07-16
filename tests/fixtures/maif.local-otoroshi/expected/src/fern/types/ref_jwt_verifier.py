

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RefJwtVerifier(UniversalBaseModel):
    """
    Reference to a global JWT verifier
    """

    enabled: bool = pydantic.Field()
    """
    Is it enabled
    """

    id: str = pydantic.Field()
    """
    The id of the GlobalJWTVerifier
    """

    type: str = pydantic.Field()
    """
    A string with value 'ref'
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
