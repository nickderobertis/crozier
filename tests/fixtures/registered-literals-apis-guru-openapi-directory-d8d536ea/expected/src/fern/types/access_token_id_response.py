

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AccessTokenIdResponse(UniversalBaseModel):
    issue_address: typing_extensions.Annotated[
        str, FieldMetadata(alias="issueAddress"), pydantic.Field(alias="issueAddress", description="Ip address.")
    ]
    """
    Ip address.
    """

    issued_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="issuedDate"),
        pydantic.Field(alias="issuedDate", description="Date when access token was created."),
    ]
    """
    Date when access token was created.
    """

    object: str = pydantic.Field()
    """
    Name of the object.
    """

    token_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="tokenId"),
        pydantic.Field(alias="tokenId", description="Unique Id for the access token."),
    ]
    """
    Unique Id for the access token.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
