

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class OrganisationConformanceTest(UniversalBaseModel):
    api_family_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="ApiFamilyType"),
        pydantic.Field(
            alias="ApiFamilyType",
            description="The family type of the resource url to be tested (for example channels_branches)",
        ),
    ]
    """
    The family type of the resource url to be tested (for example channels_branches)
    """

    resource_url: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="ResourceUrl"),
        pydantic.Field(
            alias="ResourceUrl",
            description="The url of the API to be tested (for example, https://matls-api.mockbank.poc.raidiam.io/open-banking/products-services/v1/personal-accounts)",
        ),
    ]
    """
    The url of the API to be tested (for example, https://matls-api.mockbank.poc.raidiam.io/open-banking/products-services/v1/personal-accounts)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
