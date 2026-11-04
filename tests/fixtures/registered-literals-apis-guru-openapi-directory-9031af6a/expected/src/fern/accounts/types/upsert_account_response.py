

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .upsert_account_response_meta import UpsertAccountResponseMeta


class UpsertAccountResponse(UniversalBaseModel):
    meta: UpsertAccountResponseMeta
    message: str
    rejected: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    If validation fails, specifies the property name and error message
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
