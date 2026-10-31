

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Alert(UniversalBaseModel):
    """
    Information about a particular alert.
    """

    uuid_: typing_extensions.Annotated[
        str, FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid", description="The UUID of this individual alert.")
    ]
    """
    The UUID of this individual alert.
    """

    device: str = pydantic.Field()
    """
    The UUID of the device which published this alert.
    """

    type: str = pydantic.Field()
    """
    A UUID identifying the category of alert this represents. These UUIDs should be registered in the ConfigDB with at least a human-readable name in the General Info app.
    """

    metric: str = pydantic.Field()
    """
    The path to the metric sub-tree within the device's metrics which represents this alert. Metrics here should conform to the Alert schema. Do not attach any significance to the metric names used; alerts must be identified by their type and their Links.
    """

    active: bool = pydantic.Field()
    """
    Is this alert currently active?
    """

    last_change: dt.datetime = pydantic.Field()
    """
    The time this alert last changed status.
    """

    links: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Link UUIDs linking from this alert.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
