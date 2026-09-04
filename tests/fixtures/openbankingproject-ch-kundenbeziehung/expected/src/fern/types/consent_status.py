

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .consent_status_status import ConsentStatusStatus
from .data_category import DataCategory


class ConsentStatus(UniversalBaseModel):
    consent_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="consentId"), pydantic.Field(alias="consentId")
    ] = None
    status: typing.Optional[ConsentStatusStatus] = None
    approved_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="approvedAt"), pydantic.Field(alias="approvedAt")
    ] = None
    revoked_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="revokedAt"), pydantic.Field(alias="revokedAt")
    ] = None
    data_categories: typing_extensions.Annotated[
        typing.Optional[typing.List[DataCategory]],
        FieldMetadata(alias="dataCategories"),
        pydantic.Field(alias="dataCategories"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
