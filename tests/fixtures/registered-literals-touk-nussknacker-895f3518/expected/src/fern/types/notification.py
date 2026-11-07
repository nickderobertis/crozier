

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .data_to_refresh import DataToRefresh
from .notification_type import NotificationType


class Notification(UniversalBaseModel):
    id: str
    scenario_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="scenarioName"), pydantic.Field(alias="scenarioName")
    ] = None
    message: str
    type: typing.Optional[NotificationType] = None
    to_refresh: typing_extensions.Annotated[
        typing.Optional[typing.List[DataToRefresh]], FieldMetadata(alias="toRefresh"), pydantic.Field(alias="toRefresh")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
