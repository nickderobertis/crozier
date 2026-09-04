

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .verified_claim_detail_claims import VerifiedClaimDetailClaims
from .verified_claim_detail_verification import VerifiedClaimDetailVerification


class VerifiedClaimDetail(UniversalBaseModel):
    """
    Verified claim detail that can be requested by the RP

    **How should OP beahve when requested verified claims cannot be fulfilled? **
    Refer : https://openid.net/specs/openid-connect-4-identity-assurance-1_0.html#section-6.5


    ** Sample requests: **
    The RP MUST set fields one step deeper into the structure if it wants to obtain evidence. One or more entries in the evidence array are used as filter criteria and templates for all entries in the result array.

    If multiple entries are present in evidence, these filters are linked by a logical OR.

    Eg: The following example shows that the RP wants to obtain an attestation based on the German Anti Money Laundering Law (trust framework de_aml) and limited to End-Users who were identified in a bank branch in person (physical in person proofing - method pipp) using either an idcard or a passport.

    {
      "userinfo": {
        "verified_claims": {
          "verification": {
            "trust_framework": {
              "value": "de_aml"
            },
            "evidence": [
              {
                "type": {
                  "value": "document"
                },
                "method": {
                  "value": "pipp"
                },
                "document_details": {
                  "type": {
                    "values": [
                      "idcard",
                      "passport"
                    ]
                  }
                }
              }
            ]
          },
          "claims": {
            "given_name": null,
            "birthdate": null
          }
        }
      }
    }


    The following is an example of a request for Claims where the verification process of the data is not allowed to be older than 63113852 seconds:

    {
      "userinfo": {
        "verified_claims": {
          "verification": {
            "trust_framework": {
              "value": "jp_aml"
            },
            "time": {
              "max_age": 63113852
            }
          },
          "claims": {
            "given_name": null,
            "birthdate": null
          }
        }
      }
    }

    **NOTE:** eKYC working group has documented some of the predefined values  for trust frameworks, documents, methods, validation methods or verification methods in the below wikipage.
    https://bitbucket.org/openid/ekyc-ida/wiki/identifiers
    Values is NOT restricted to list in the wiki page, This is left to adopters of the technical specification, e.g., implementers, identity schemes, or jurisdictions.
    """

    verification: VerifiedClaimDetailVerification = pydantic.Field()
    """
    Object that contains data about the verification process.
    """

    claims: VerifiedClaimDetailClaims = pydantic.Field()
    """
    Object that is the container for the Verified Claims about the End-User.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
