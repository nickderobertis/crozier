

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IdNumberType(enum.StrEnum):
    """
    A globally unique and human readable ID type, specific to the country and document category. For more context on this field, see [Hybrid Input Validation](https://plaid.com/docs/identity-verification/hybrid-input-validation).
    """

    AR_DNI = "ar_dni"
    AU_DRIVERS_LICENSE = "au_drivers_license"
    AU_PASSPORT = "au_passport"
    BR_CPF = "br_cpf"
    CA_SIN = "ca_sin"
    CL_RUN = "cl_run"
    CN_RESIDENT_CARD = "cn_resident_card"
    CO_NIT = "co_nit"
    DK_CPR = "dk_cpr"
    EG_NATIONAL_ID = "eg_national_id"
    ES_DNI = "es_dni"
    ES_NIE = "es_nie"
    HK_HKID = "hk_hkid"
    IN_PAN = "in_pan"
    IT_CF = "it_cf"
    JO_CIVIL_ID = "jo_civil_id"
    JP_MY_NUMBER = "jp_my_number"
    KE_HUDUMA_NAMBA = "ke_huduma_namba"
    KW_CIVIL_ID = "kw_civil_id"
    MX_CURP = "mx_curp"
    MX_RFC = "mx_rfc"
    MY_NRIC = "my_nric"
    NG_NIN = "ng_nin"
    NZ_DRIVERS_LICENSE = "nz_drivers_license"
    OM_CIVIL_ID = "om_civil_id"
    PH_PSN = "ph_psn"
    PL_PESEL = "pl_pesel"
    RO_CNP = "ro_cnp"
    SA_NATIONAL_ID = "sa_national_id"
    SE_PIN = "se_pin"
    SG_NRIC = "sg_nric"
    TR_TC_KIMLIK = "tr_tc_kimlik"
    US_SSN = "us_ssn"
    US_SSN_LAST4 = "us_ssn_last_4"
    ZA_SMART_ID = "za_smart_id"

    def visit(
        self,
        ar_dni: typing.Callable[[], T_Result],
        au_drivers_license: typing.Callable[[], T_Result],
        au_passport: typing.Callable[[], T_Result],
        br_cpf: typing.Callable[[], T_Result],
        ca_sin: typing.Callable[[], T_Result],
        cl_run: typing.Callable[[], T_Result],
        cn_resident_card: typing.Callable[[], T_Result],
        co_nit: typing.Callable[[], T_Result],
        dk_cpr: typing.Callable[[], T_Result],
        eg_national_id: typing.Callable[[], T_Result],
        es_dni: typing.Callable[[], T_Result],
        es_nie: typing.Callable[[], T_Result],
        hk_hkid: typing.Callable[[], T_Result],
        in_pan: typing.Callable[[], T_Result],
        it_cf: typing.Callable[[], T_Result],
        jo_civil_id: typing.Callable[[], T_Result],
        jp_my_number: typing.Callable[[], T_Result],
        ke_huduma_namba: typing.Callable[[], T_Result],
        kw_civil_id: typing.Callable[[], T_Result],
        mx_curp: typing.Callable[[], T_Result],
        mx_rfc: typing.Callable[[], T_Result],
        my_nric: typing.Callable[[], T_Result],
        ng_nin: typing.Callable[[], T_Result],
        nz_drivers_license: typing.Callable[[], T_Result],
        om_civil_id: typing.Callable[[], T_Result],
        ph_psn: typing.Callable[[], T_Result],
        pl_pesel: typing.Callable[[], T_Result],
        ro_cnp: typing.Callable[[], T_Result],
        sa_national_id: typing.Callable[[], T_Result],
        se_pin: typing.Callable[[], T_Result],
        sg_nric: typing.Callable[[], T_Result],
        tr_tc_kimlik: typing.Callable[[], T_Result],
        us_ssn: typing.Callable[[], T_Result],
        us_ssn_last4: typing.Callable[[], T_Result],
        za_smart_id: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IdNumberType.AR_DNI:
            return ar_dni()
        if self is IdNumberType.AU_DRIVERS_LICENSE:
            return au_drivers_license()
        if self is IdNumberType.AU_PASSPORT:
            return au_passport()
        if self is IdNumberType.BR_CPF:
            return br_cpf()
        if self is IdNumberType.CA_SIN:
            return ca_sin()
        if self is IdNumberType.CL_RUN:
            return cl_run()
        if self is IdNumberType.CN_RESIDENT_CARD:
            return cn_resident_card()
        if self is IdNumberType.CO_NIT:
            return co_nit()
        if self is IdNumberType.DK_CPR:
            return dk_cpr()
        if self is IdNumberType.EG_NATIONAL_ID:
            return eg_national_id()
        if self is IdNumberType.ES_DNI:
            return es_dni()
        if self is IdNumberType.ES_NIE:
            return es_nie()
        if self is IdNumberType.HK_HKID:
            return hk_hkid()
        if self is IdNumberType.IN_PAN:
            return in_pan()
        if self is IdNumberType.IT_CF:
            return it_cf()
        if self is IdNumberType.JO_CIVIL_ID:
            return jo_civil_id()
        if self is IdNumberType.JP_MY_NUMBER:
            return jp_my_number()
        if self is IdNumberType.KE_HUDUMA_NAMBA:
            return ke_huduma_namba()
        if self is IdNumberType.KW_CIVIL_ID:
            return kw_civil_id()
        if self is IdNumberType.MX_CURP:
            return mx_curp()
        if self is IdNumberType.MX_RFC:
            return mx_rfc()
        if self is IdNumberType.MY_NRIC:
            return my_nric()
        if self is IdNumberType.NG_NIN:
            return ng_nin()
        if self is IdNumberType.NZ_DRIVERS_LICENSE:
            return nz_drivers_license()
        if self is IdNumberType.OM_CIVIL_ID:
            return om_civil_id()
        if self is IdNumberType.PH_PSN:
            return ph_psn()
        if self is IdNumberType.PL_PESEL:
            return pl_pesel()
        if self is IdNumberType.RO_CNP:
            return ro_cnp()
        if self is IdNumberType.SA_NATIONAL_ID:
            return sa_national_id()
        if self is IdNumberType.SE_PIN:
            return se_pin()
        if self is IdNumberType.SG_NRIC:
            return sg_nric()
        if self is IdNumberType.TR_TC_KIMLIK:
            return tr_tc_kimlik()
        if self is IdNumberType.US_SSN:
            return us_ssn()
        if self is IdNumberType.US_SSN_LAST4:
            return us_ssn_last4()
        if self is IdNumberType.ZA_SMART_ID:
            return za_smart_id()
