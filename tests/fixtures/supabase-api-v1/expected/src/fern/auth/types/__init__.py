



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_provider_body_attribute_mapping import CreateProviderBodyAttributeMapping
    from .create_provider_body_attribute_mapping_keys_value import CreateProviderBodyAttributeMappingKeysValue
    from .create_provider_body_attribute_mapping_keys_value_default import (
        CreateProviderBodyAttributeMappingKeysValueDefault,
    )
    from .create_provider_body_attribute_mapping_keys_value_default_zero import (
        CreateProviderBodyAttributeMappingKeysValueDefaultZero,
    )
    from .create_provider_body_name_id_format import CreateProviderBodyNameIdFormat
    from .create_provider_body_type import CreateProviderBodyType
    from .create_signing_key_body_algorithm import CreateSigningKeyBodyAlgorithm
    from .create_signing_key_body_private_jwk import (
        CreateSigningKeyBodyPrivateJwk,
        CreateSigningKeyBodyPrivateJwk_Ec,
        CreateSigningKeyBodyPrivateJwk_Oct,
        CreateSigningKeyBodyPrivateJwk_Okp,
        CreateSigningKeyBodyPrivateJwk_Rsa,
    )
    from .create_signing_key_body_private_jwk_ec import CreateSigningKeyBodyPrivateJwkEc
    from .create_signing_key_body_private_jwk_ec_alg import CreateSigningKeyBodyPrivateJwkEcAlg
    from .create_signing_key_body_private_jwk_ec_crv import CreateSigningKeyBodyPrivateJwkEcCrv
    from .create_signing_key_body_private_jwk_ec_key_ops_item import CreateSigningKeyBodyPrivateJwkEcKeyOpsItem
    from .create_signing_key_body_private_jwk_ec_use import CreateSigningKeyBodyPrivateJwkEcUse
    from .create_signing_key_body_private_jwk_oct import CreateSigningKeyBodyPrivateJwkOct
    from .create_signing_key_body_private_jwk_oct_alg import CreateSigningKeyBodyPrivateJwkOctAlg
    from .create_signing_key_body_private_jwk_oct_key_ops_item import CreateSigningKeyBodyPrivateJwkOctKeyOpsItem
    from .create_signing_key_body_private_jwk_oct_use import CreateSigningKeyBodyPrivateJwkOctUse
    from .create_signing_key_body_private_jwk_okp import CreateSigningKeyBodyPrivateJwkOkp
    from .create_signing_key_body_private_jwk_okp_alg import CreateSigningKeyBodyPrivateJwkOkpAlg
    from .create_signing_key_body_private_jwk_okp_crv import CreateSigningKeyBodyPrivateJwkOkpCrv
    from .create_signing_key_body_private_jwk_okp_key_ops_item import CreateSigningKeyBodyPrivateJwkOkpKeyOpsItem
    from .create_signing_key_body_private_jwk_okp_use import CreateSigningKeyBodyPrivateJwkOkpUse
    from .create_signing_key_body_private_jwk_rsa import CreateSigningKeyBodyPrivateJwkRsa
    from .create_signing_key_body_private_jwk_rsa_alg import CreateSigningKeyBodyPrivateJwkRsaAlg
    from .create_signing_key_body_private_jwk_rsa_e import CreateSigningKeyBodyPrivateJwkRsaE
    from .create_signing_key_body_private_jwk_rsa_key_ops_item import CreateSigningKeyBodyPrivateJwkRsaKeyOpsItem
    from .create_signing_key_body_private_jwk_rsa_use import CreateSigningKeyBodyPrivateJwkRsaUse
    from .create_signing_key_body_status import CreateSigningKeyBodyStatus
    from .update_auth_config_body_db_max_pool_size_unit import UpdateAuthConfigBodyDbMaxPoolSizeUnit
    from .update_auth_config_body_password_required_characters import UpdateAuthConfigBodyPasswordRequiredCharacters
    from .update_auth_config_body_security_captcha_provider import UpdateAuthConfigBodySecurityCaptchaProvider
    from .update_auth_config_body_sms_provider import UpdateAuthConfigBodySmsProvider
    from .update_provider_body_attribute_mapping import UpdateProviderBodyAttributeMapping
    from .update_provider_body_attribute_mapping_keys_value import UpdateProviderBodyAttributeMappingKeysValue
    from .update_provider_body_attribute_mapping_keys_value_default import (
        UpdateProviderBodyAttributeMappingKeysValueDefault,
    )
    from .update_provider_body_attribute_mapping_keys_value_default_zero import (
        UpdateProviderBodyAttributeMappingKeysValueDefaultZero,
    )
    from .update_provider_body_name_id_format import UpdateProviderBodyNameIdFormat
    from .update_signing_key_body_status import UpdateSigningKeyBodyStatus
_dynamic_imports: typing.Dict[str, str] = {
    "CreateProviderBodyAttributeMapping": ".create_provider_body_attribute_mapping",
    "CreateProviderBodyAttributeMappingKeysValue": ".create_provider_body_attribute_mapping_keys_value",
    "CreateProviderBodyAttributeMappingKeysValueDefault": ".create_provider_body_attribute_mapping_keys_value_default",
    "CreateProviderBodyAttributeMappingKeysValueDefaultZero": ".create_provider_body_attribute_mapping_keys_value_default_zero",
    "CreateProviderBodyNameIdFormat": ".create_provider_body_name_id_format",
    "CreateProviderBodyType": ".create_provider_body_type",
    "CreateSigningKeyBodyAlgorithm": ".create_signing_key_body_algorithm",
    "CreateSigningKeyBodyPrivateJwk": ".create_signing_key_body_private_jwk",
    "CreateSigningKeyBodyPrivateJwkEc": ".create_signing_key_body_private_jwk_ec",
    "CreateSigningKeyBodyPrivateJwkEcAlg": ".create_signing_key_body_private_jwk_ec_alg",
    "CreateSigningKeyBodyPrivateJwkEcCrv": ".create_signing_key_body_private_jwk_ec_crv",
    "CreateSigningKeyBodyPrivateJwkEcKeyOpsItem": ".create_signing_key_body_private_jwk_ec_key_ops_item",
    "CreateSigningKeyBodyPrivateJwkEcUse": ".create_signing_key_body_private_jwk_ec_use",
    "CreateSigningKeyBodyPrivateJwkOct": ".create_signing_key_body_private_jwk_oct",
    "CreateSigningKeyBodyPrivateJwkOctAlg": ".create_signing_key_body_private_jwk_oct_alg",
    "CreateSigningKeyBodyPrivateJwkOctKeyOpsItem": ".create_signing_key_body_private_jwk_oct_key_ops_item",
    "CreateSigningKeyBodyPrivateJwkOctUse": ".create_signing_key_body_private_jwk_oct_use",
    "CreateSigningKeyBodyPrivateJwkOkp": ".create_signing_key_body_private_jwk_okp",
    "CreateSigningKeyBodyPrivateJwkOkpAlg": ".create_signing_key_body_private_jwk_okp_alg",
    "CreateSigningKeyBodyPrivateJwkOkpCrv": ".create_signing_key_body_private_jwk_okp_crv",
    "CreateSigningKeyBodyPrivateJwkOkpKeyOpsItem": ".create_signing_key_body_private_jwk_okp_key_ops_item",
    "CreateSigningKeyBodyPrivateJwkOkpUse": ".create_signing_key_body_private_jwk_okp_use",
    "CreateSigningKeyBodyPrivateJwkRsa": ".create_signing_key_body_private_jwk_rsa",
    "CreateSigningKeyBodyPrivateJwkRsaAlg": ".create_signing_key_body_private_jwk_rsa_alg",
    "CreateSigningKeyBodyPrivateJwkRsaE": ".create_signing_key_body_private_jwk_rsa_e",
    "CreateSigningKeyBodyPrivateJwkRsaKeyOpsItem": ".create_signing_key_body_private_jwk_rsa_key_ops_item",
    "CreateSigningKeyBodyPrivateJwkRsaUse": ".create_signing_key_body_private_jwk_rsa_use",
    "CreateSigningKeyBodyPrivateJwk_Ec": ".create_signing_key_body_private_jwk",
    "CreateSigningKeyBodyPrivateJwk_Oct": ".create_signing_key_body_private_jwk",
    "CreateSigningKeyBodyPrivateJwk_Okp": ".create_signing_key_body_private_jwk",
    "CreateSigningKeyBodyPrivateJwk_Rsa": ".create_signing_key_body_private_jwk",
    "CreateSigningKeyBodyStatus": ".create_signing_key_body_status",
    "UpdateAuthConfigBodyDbMaxPoolSizeUnit": ".update_auth_config_body_db_max_pool_size_unit",
    "UpdateAuthConfigBodyPasswordRequiredCharacters": ".update_auth_config_body_password_required_characters",
    "UpdateAuthConfigBodySecurityCaptchaProvider": ".update_auth_config_body_security_captcha_provider",
    "UpdateAuthConfigBodySmsProvider": ".update_auth_config_body_sms_provider",
    "UpdateProviderBodyAttributeMapping": ".update_provider_body_attribute_mapping",
    "UpdateProviderBodyAttributeMappingKeysValue": ".update_provider_body_attribute_mapping_keys_value",
    "UpdateProviderBodyAttributeMappingKeysValueDefault": ".update_provider_body_attribute_mapping_keys_value_default",
    "UpdateProviderBodyAttributeMappingKeysValueDefaultZero": ".update_provider_body_attribute_mapping_keys_value_default_zero",
    "UpdateProviderBodyNameIdFormat": ".update_provider_body_name_id_format",
    "UpdateSigningKeyBodyStatus": ".update_signing_key_body_status",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "CreateProviderBodyAttributeMapping",
    "CreateProviderBodyAttributeMappingKeysValue",
    "CreateProviderBodyAttributeMappingKeysValueDefault",
    "CreateProviderBodyAttributeMappingKeysValueDefaultZero",
    "CreateProviderBodyNameIdFormat",
    "CreateProviderBodyType",
    "CreateSigningKeyBodyAlgorithm",
    "CreateSigningKeyBodyPrivateJwk",
    "CreateSigningKeyBodyPrivateJwkEc",
    "CreateSigningKeyBodyPrivateJwkEcAlg",
    "CreateSigningKeyBodyPrivateJwkEcCrv",
    "CreateSigningKeyBodyPrivateJwkEcKeyOpsItem",
    "CreateSigningKeyBodyPrivateJwkEcUse",
    "CreateSigningKeyBodyPrivateJwkOct",
    "CreateSigningKeyBodyPrivateJwkOctAlg",
    "CreateSigningKeyBodyPrivateJwkOctKeyOpsItem",
    "CreateSigningKeyBodyPrivateJwkOctUse",
    "CreateSigningKeyBodyPrivateJwkOkp",
    "CreateSigningKeyBodyPrivateJwkOkpAlg",
    "CreateSigningKeyBodyPrivateJwkOkpCrv",
    "CreateSigningKeyBodyPrivateJwkOkpKeyOpsItem",
    "CreateSigningKeyBodyPrivateJwkOkpUse",
    "CreateSigningKeyBodyPrivateJwkRsa",
    "CreateSigningKeyBodyPrivateJwkRsaAlg",
    "CreateSigningKeyBodyPrivateJwkRsaE",
    "CreateSigningKeyBodyPrivateJwkRsaKeyOpsItem",
    "CreateSigningKeyBodyPrivateJwkRsaUse",
    "CreateSigningKeyBodyPrivateJwk_Ec",
    "CreateSigningKeyBodyPrivateJwk_Oct",
    "CreateSigningKeyBodyPrivateJwk_Okp",
    "CreateSigningKeyBodyPrivateJwk_Rsa",
    "CreateSigningKeyBodyStatus",
    "UpdateAuthConfigBodyDbMaxPoolSizeUnit",
    "UpdateAuthConfigBodyPasswordRequiredCharacters",
    "UpdateAuthConfigBodySecurityCaptchaProvider",
    "UpdateAuthConfigBodySmsProvider",
    "UpdateProviderBodyAttributeMapping",
    "UpdateProviderBodyAttributeMappingKeysValue",
    "UpdateProviderBodyAttributeMappingKeysValueDefault",
    "UpdateProviderBodyAttributeMappingKeysValueDefaultZero",
    "UpdateProviderBodyNameIdFormat",
    "UpdateSigningKeyBodyStatus",
]
