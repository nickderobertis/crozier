

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PreprintsCitationReadResponseAttributes(UniversalBaseModel):
    """
    The properties of the citation style entity.
    """

    citation: typing.Optional[str] = pydantic.Field(default=None)
    """
    The complete entity citation in the requested style.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
