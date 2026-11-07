

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListOfId4Ns(UniversalBaseModel):
    """
    A list of id4ns
    """

    id4ns: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of id4ns.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
