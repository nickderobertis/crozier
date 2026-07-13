

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CardGeneratedCvc2Read(UniversalBaseModel):
    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the cvc code's creation.
    """

    cvc2: typing.Optional[str] = pydantic.Field(default=None)
    """
    The cvc2 code.
    """

    expiry_time: typing.Optional[str] = pydantic.Field(default=None)
    """
    Expiry time of the cvc2.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the cvc code.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the cvc2. Can be AVAILABLE, USED, EXPIRED, BLOCKED.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of generated cvc2. Can be STATIC or GENERATED.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the cvc code's last update.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
