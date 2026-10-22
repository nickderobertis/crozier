

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .suppression_object import SuppressionObject


class Suppression(UniversalBaseModel):
    object: SuppressionObject = pydantic.Field()
    """
    Object type identifier
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the suppression
    """

    created_at: dt.datetime = pydantic.Field()
    """
    When the suppression was created
    """

    email: str = pydantic.Field()
    """
    Suppressed email address
    """

    domain: str = pydantic.Field()
    """
    Domain for which the email is suppressed
    """

    reason: str = pydantic.Field()
    """
    Reason for suppression
    """

    expires_at: dt.datetime = pydantic.Field()
    """
    When the suppression expires
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
