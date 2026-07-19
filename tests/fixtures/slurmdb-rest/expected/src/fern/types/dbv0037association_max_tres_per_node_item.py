

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Dbv0037AssociationMaxTresPerNodeItem(UniversalBaseModel):
    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    TRES type
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    TRES name (optional)
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    database id
    """

    count: typing.Optional[int] = pydantic.Field(default=None)
    """
    count of TRES
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
