

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConnectV1ConnectorExpansionId(UniversalBaseModel):
    """
    The ID of connector.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the connector.
    """

    id_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of the value in the `id` property.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
