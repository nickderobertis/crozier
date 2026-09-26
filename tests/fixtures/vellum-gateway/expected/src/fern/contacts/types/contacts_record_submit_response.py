

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ContactsRecordSubmitResponse(UniversalBaseModel):
    accepted: bool
    error: typing.Optional[str] = None
    duplicate: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Another client answered this form first. Nothing is wrong, but none of this submission's values were written.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
