

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RecordsReplaceMetadataRequestPropertiesAgreementDate(UniversalBaseModel):
    """
    The date of the agreement.
    """

    type: typing.Optional[str] = None
    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    UTC date (e.g. `2018-05-08T00:00:00-07:00`)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
