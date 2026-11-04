

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .attributes import Attributes
from .resource_type import ResourceType


class MembershipResource(UniversalBaseModel):
    """
    Information about the resource the membership is in.
    """

    id: str = pydantic.Field()
    """
    ID of the resource the membership is in.
    """

    type: ResourceType
    name: str = pydantic.Field()
    """
    Display name of the resource.
    """

    logo: typing.Optional[str] = pydantic.Field(default=None)
    """
    Logo fo the resource.
    """

    created_at: dt.datetime = pydantic.Field()
    """
    The timestamp of when the membership resource was created.
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    The timestamp of when the membership resource was last updated.
    """

    attributes: typing.Optional[Attributes] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
