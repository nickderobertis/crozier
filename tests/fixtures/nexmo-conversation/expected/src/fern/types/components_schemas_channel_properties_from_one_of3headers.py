

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ComponentsSchemasChannelPropertiesFromOneOf3Headers(UniversalBaseModel):
    """
    Details of the Websocket you want to connect to
    """

    customer_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is an example header. You can provide any headers you may need
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
