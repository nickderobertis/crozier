

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CaseDocumentOrderPacerOptions(UniversalBaseModel):
    """
    **Applicable for PACER cases.**
    """

    pacer_client_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pacerClientCode"),
        pydantic.Field(
            alias="pacerClientCode",
            description="PACER Client Code. This is mandatory if your setting in PACER website is set to True for required client code.",
        ),
    ] = None
    """
    PACER Client Code. This is mandatory if your setting in PACER website is set to True for required client code.
    """

    pacer_user_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="pacerUserId"),
        pydantic.Field(
            alias="pacerUserId",
            description="Your PACER credentials username. This is mandatory when a PACER Case is being requested in the API. For Non PACER cases this is not mandatory. Suppose your request consists of Non PACER and PACER Cases then this needs to be passed becuase you are requesting a PACER case too.",
        ),
    ]
    """
    Your PACER credentials username. This is mandatory when a PACER Case is being requested in the API. For Non PACER cases this is not mandatory. Suppose your request consists of Non PACER and PACER Cases then this needs to be passed becuase you are requesting a PACER case too.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
