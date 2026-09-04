

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DisbursementRepayment(UniversalBaseModel):
    basis_points: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="basisPoints"),
        pydantic.Field(
            alias="basisPoints",
            description="The percentage of your user's incoming net volume that is deducted for repaying the grant. The percentage expressed in [basis points](https://www.investopedia.com/terms/b/basispoint.asp).",
        ),
    ]
    """
    The percentage of your user's incoming net volume that is deducted for repaying the grant. The percentage expressed in [basis points](https://www.investopedia.com/terms/b/basispoint.asp).
    """

    update_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="updateDescription"), pydantic.Field(alias="updateDescription")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
