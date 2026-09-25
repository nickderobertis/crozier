

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_realm_export_consents_response_export_consents_item import GetRealmExportConsentsResponseExportConsentsItem


class GetRealmExportConsentsResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    export_consents: typing.Optional[typing.List[GetRealmExportConsentsResponseExportConsentsItem]] = pydantic.Field(
        default=None
    )
    """
    An array of objects where each object contains a user ID, whether the
    user has consented for their private data to be exported, and their
    email visibility policy.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
