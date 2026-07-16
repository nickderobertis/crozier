

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Subscription(UniversalBaseModel):
    """
    Subscription entry
    """

    active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Is the subscription currently active
    """

    subscription_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    the unique id for this subscription record
    """

    subscription_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    The key value that the subscription references. E.g. a tag value or a repo name.
    """

    subscription_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of the subscription
    """

    subscription_value: typing.Optional[str] = pydantic.Field(default=None)
    """
    The value of the subscription target
    """

    user_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="userId"),
        pydantic.Field(alias="userId", description="The userId of the subscribed user"),
    ] = None
    """
    The userId of the subscribed user
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
