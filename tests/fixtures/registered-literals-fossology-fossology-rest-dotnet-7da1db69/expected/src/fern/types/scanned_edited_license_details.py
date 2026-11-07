

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ScannedEditedLicenseDetails(UniversalBaseModel):
    count: typing.Optional[int] = None
    unique: typing.Optional[int] = None
    rf_pk: typing.Optional[int] = None
    spdx_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
