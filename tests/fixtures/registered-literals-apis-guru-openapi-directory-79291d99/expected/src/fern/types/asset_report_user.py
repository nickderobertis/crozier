

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AssetReportUser(UniversalBaseModel):
    """
    The user object allows you to provide additional information about the user to be appended to the Asset Report. All fields are optional. The `first_name`, `last_name`, and `ssn` fields are required if you would like the Report to be eligible for Fannie Mae’s Day 1 Certainty™ program.
    """

    client_user_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    An identifier you determine and submit for the user.
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's email address.
    """

    first_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's first name. Required for the Fannie Mae Day 1 Certainty™ program.
    """

    last_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's last name.  Required for the Fannie Mae Day 1 Certainty™ program.
    """

    middle_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's middle name
    """

    phone_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's phone number, in E.164 format: +{countrycode}{number}. For example: "+14151234567". Phone numbers provided in other formats will be parsed on a best-effort basis.
    """

    ssn: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's Social Security Number. Required for the Fannie Mae Day 1 Certainty™ program.
    
    Format: "ddd-dd-dddd"
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
