

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class EndpointDisabledEventData(UniversalBaseModel):
    """
    Sent when an endpoint has been automatically disabled after continuous failures.
    """

    app_id: typing_extensions.Annotated[str, FieldMetadata(alias="appId"), pydantic.Field(alias="appId")]
    app_uid: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="appUid"), pydantic.Field(alias="appUid")
    ] = None
    endpoint_id: typing_extensions.Annotated[str, FieldMetadata(alias="endpointId"), pydantic.Field(alias="endpointId")]
    endpoint_uid: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="endpointUid"), pydantic.Field(alias="endpointUid")
    ] = None
    fail_since: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="failSince"), pydantic.Field(alias="failSince")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
