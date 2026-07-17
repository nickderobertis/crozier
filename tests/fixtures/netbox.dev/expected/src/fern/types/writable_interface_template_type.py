

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WritableInterfaceTemplateType(enum.StrEnum):
    VIRTUAL = "virtual"
    BRIDGE = "bridge"
    LAG = "lag"
    ONE_HUNDRED_BASE_FX = "100base-fx"
    ONE_HUNDRED_BASE_LFX = "100base-lfx"
    ONE_HUNDRED_BASE_TX = "100base-tx"
    ONE_HUNDRED_BASE_T1 = "100base-t1"
    ONE_THOUSAND_BASE_T = "1000base-t"
    TWO5GBASE_T = "2.5gbase-t"
    FIVE_GBASE_T = "5gbase-t"
    TEN_GBASE_T = "10gbase-t"
    TEN_GBASE_CX4 = "10gbase-cx4"
    ONE_THOUSAND_BASE_X_GBIC = "1000base-x-gbic"
    ONE_THOUSAND_BASE_X_SFP = "1000base-x-sfp"
    TEN_GBASE_X_SFPP = "10gbase-x-sfpp"
    TEN_GBASE_X_XFP = "10gbase-x-xfp"
    TEN_GBASE_X_XENPAK = "10gbase-x-xenpak"
    TEN_GBASE_XX2 = "10gbase-x-x2"
    TWENTY_FIVE_GBASE_X_SFP28 = "25gbase-x-sfp28"
    FIFTY_GBASE_X_SFP56 = "50gbase-x-sfp56"
    FORTY_GBASE_X_QSFPP = "40gbase-x-qsfpp"
    FIFTY_GBASE_X_SFP28 = "50gbase-x-sfp28"
    ONE_HUNDRED_GBASE_X_CFP = "100gbase-x-cfp"
    ONE_HUNDRED_GBASE_X_CFP2 = "100gbase-x-cfp2"
    TWO_HUNDRED_GBASE_X_CFP2 = "200gbase-x-cfp2"
    ONE_HUNDRED_GBASE_X_CFP4 = "100gbase-x-cfp4"
    ONE_HUNDRED_GBASE_X_CPAK = "100gbase-x-cpak"
    ONE_HUNDRED_GBASE_X_QSFP28 = "100gbase-x-qsfp28"
    TWO_HUNDRED_GBASE_X_QSFP56 = "200gbase-x-qsfp56"
    FOUR_HUNDRED_GBASE_X_QSFPDD = "400gbase-x-qsfpdd"
    FOUR_HUNDRED_GBASE_X_OSFP = "400gbase-x-osfp"
    EIGHT_HUNDRED_GBASE_X_QSFPDD = "800gbase-x-qsfpdd"
    EIGHT_HUNDRED_GBASE_X_OSFP = "800gbase-x-osfp"
    ONE_THOUSAND_BASE_KX = "1000base-kx"
    TEN_GBASE_KR = "10gbase-kr"
    TEN_GBASE_KX4 = "10gbase-kx4"
    TWENTY_FIVE_GBASE_KR = "25gbase-kr"
    FORTY_GBASE_KR4 = "40gbase-kr4"
    FIFTY_GBASE_KR = "50gbase-kr"
    ONE_HUNDRED_GBASE_KP4 = "100gbase-kp4"
    ONE_HUNDRED_GBASE_KR2 = "100gbase-kr2"
    ONE_HUNDRED_GBASE_KR4 = "100gbase-kr4"
    IEEE80211A = "ieee802.11a"
    IEEE80211G = "ieee802.11g"
    IEEE80211N = "ieee802.11n"
    IEEE80211AC = "ieee802.11ac"
    IEEE80211AD = "ieee802.11ad"
    IEEE80211AX = "ieee802.11ax"
    IEEE80211AY = "ieee802.11ay"
    IEEE802151 = "ieee802.15.1"
    OTHER_WIRELESS = "other-wireless"
    GSM = "gsm"
    CDMA = "cdma"
    LTE = "lte"
    SONET_OC3 = "sonet-oc3"
    SONET_OC12 = "sonet-oc12"
    SONET_OC48 = "sonet-oc48"
    SONET_OC192 = "sonet-oc192"
    SONET_OC768 = "sonet-oc768"
    SONET_OC1920 = "sonet-oc1920"
    SONET_OC3840 = "sonet-oc3840"
    ONE_GFC_SFP = "1gfc-sfp"
    TWO_GFC_SFP = "2gfc-sfp"
    FOUR_GFC_SFP = "4gfc-sfp"
    EIGHT_GFC_SFPP = "8gfc-sfpp"
    SIXTEEN_GFC_SFPP = "16gfc-sfpp"
    THIRTY_TWO_GFC_SFP28 = "32gfc-sfp28"
    SIXTY_FOUR_GFC_QSFPP = "64gfc-qsfpp"
    ONE_HUNDRED_TWENTY_EIGHT_GFC_QSFP28 = "128gfc-qsfp28"
    INFINIBAND_SDR = "infiniband-sdr"
    INFINIBAND_DDR = "infiniband-ddr"
    INFINIBAND_QDR = "infiniband-qdr"
    INFINIBAND_FDR10 = "infiniband-fdr10"
    INFINIBAND_FDR = "infiniband-fdr"
    INFINIBAND_EDR = "infiniband-edr"
    INFINIBAND_HDR = "infiniband-hdr"
    INFINIBAND_NDR = "infiniband-ndr"
    INFINIBAND_XDR = "infiniband-xdr"
    T1 = "t1"
    E1 = "e1"
    T3 = "t3"
    E3 = "e3"
    XDSL = "xdsl"
    DOCSIS = "docsis"
    GPON = "gpon"
    XG_PON = "xg-pon"
    XGS_PON = "xgs-pon"
    NG_PON2 = "ng-pon2"
    EPON = "epon"
    TEN_G_EPON = "10g-epon"
    CISCO_STACKWISE = "cisco-stackwise"
    CISCO_STACKWISE_PLUS = "cisco-stackwise-plus"
    CISCO_FLEXSTACK = "cisco-flexstack"
    CISCO_FLEXSTACK_PLUS = "cisco-flexstack-plus"
    CISCO_STACKWISE80 = "cisco-stackwise-80"
    CISCO_STACKWISE160 = "cisco-stackwise-160"
    CISCO_STACKWISE320 = "cisco-stackwise-320"
    CISCO_STACKWISE480 = "cisco-stackwise-480"
    CISCO_STACKWISE1T = "cisco-stackwise-1t"
    JUNIPER_VCP = "juniper-vcp"
    EXTREME_SUMMITSTACK = "extreme-summitstack"
    EXTREME_SUMMITSTACK128 = "extreme-summitstack-128"
    EXTREME_SUMMITSTACK256 = "extreme-summitstack-256"
    EXTREME_SUMMITSTACK512 = "extreme-summitstack-512"
    OTHER = "other"

    def visit(
        self,
        virtual: typing.Callable[[], T_Result],
        bridge: typing.Callable[[], T_Result],
        lag: typing.Callable[[], T_Result],
        one_hundred_base_fx: typing.Callable[[], T_Result],
        one_hundred_base_lfx: typing.Callable[[], T_Result],
        one_hundred_base_tx: typing.Callable[[], T_Result],
        one_hundred_base_t1: typing.Callable[[], T_Result],
        one_thousand_base_t: typing.Callable[[], T_Result],
        two5gbase_t: typing.Callable[[], T_Result],
        five_gbase_t: typing.Callable[[], T_Result],
        ten_gbase_t: typing.Callable[[], T_Result],
        ten_gbase_cx4: typing.Callable[[], T_Result],
        one_thousand_base_x_gbic: typing.Callable[[], T_Result],
        one_thousand_base_x_sfp: typing.Callable[[], T_Result],
        ten_gbase_x_sfpp: typing.Callable[[], T_Result],
        ten_gbase_x_xfp: typing.Callable[[], T_Result],
        ten_gbase_x_xenpak: typing.Callable[[], T_Result],
        ten_gbase_xx2: typing.Callable[[], T_Result],
        twenty_five_gbase_x_sfp28: typing.Callable[[], T_Result],
        fifty_gbase_x_sfp56: typing.Callable[[], T_Result],
        forty_gbase_x_qsfpp: typing.Callable[[], T_Result],
        fifty_gbase_x_sfp28: typing.Callable[[], T_Result],
        one_hundred_gbase_x_cfp: typing.Callable[[], T_Result],
        one_hundred_gbase_x_cfp2: typing.Callable[[], T_Result],
        two_hundred_gbase_x_cfp2: typing.Callable[[], T_Result],
        one_hundred_gbase_x_cfp4: typing.Callable[[], T_Result],
        one_hundred_gbase_x_cpak: typing.Callable[[], T_Result],
        one_hundred_gbase_x_qsfp28: typing.Callable[[], T_Result],
        two_hundred_gbase_x_qsfp56: typing.Callable[[], T_Result],
        four_hundred_gbase_x_qsfpdd: typing.Callable[[], T_Result],
        four_hundred_gbase_x_osfp: typing.Callable[[], T_Result],
        eight_hundred_gbase_x_qsfpdd: typing.Callable[[], T_Result],
        eight_hundred_gbase_x_osfp: typing.Callable[[], T_Result],
        one_thousand_base_kx: typing.Callable[[], T_Result],
        ten_gbase_kr: typing.Callable[[], T_Result],
        ten_gbase_kx4: typing.Callable[[], T_Result],
        twenty_five_gbase_kr: typing.Callable[[], T_Result],
        forty_gbase_kr4: typing.Callable[[], T_Result],
        fifty_gbase_kr: typing.Callable[[], T_Result],
        one_hundred_gbase_kp4: typing.Callable[[], T_Result],
        one_hundred_gbase_kr2: typing.Callable[[], T_Result],
        one_hundred_gbase_kr4: typing.Callable[[], T_Result],
        ieee80211a: typing.Callable[[], T_Result],
        ieee80211g: typing.Callable[[], T_Result],
        ieee80211n: typing.Callable[[], T_Result],
        ieee80211ac: typing.Callable[[], T_Result],
        ieee80211ad: typing.Callable[[], T_Result],
        ieee80211ax: typing.Callable[[], T_Result],
        ieee80211ay: typing.Callable[[], T_Result],
        ieee802151: typing.Callable[[], T_Result],
        other_wireless: typing.Callable[[], T_Result],
        gsm: typing.Callable[[], T_Result],
        cdma: typing.Callable[[], T_Result],
        lte: typing.Callable[[], T_Result],
        sonet_oc3: typing.Callable[[], T_Result],
        sonet_oc12: typing.Callable[[], T_Result],
        sonet_oc48: typing.Callable[[], T_Result],
        sonet_oc192: typing.Callable[[], T_Result],
        sonet_oc768: typing.Callable[[], T_Result],
        sonet_oc1920: typing.Callable[[], T_Result],
        sonet_oc3840: typing.Callable[[], T_Result],
        one_gfc_sfp: typing.Callable[[], T_Result],
        two_gfc_sfp: typing.Callable[[], T_Result],
        four_gfc_sfp: typing.Callable[[], T_Result],
        eight_gfc_sfpp: typing.Callable[[], T_Result],
        sixteen_gfc_sfpp: typing.Callable[[], T_Result],
        thirty_two_gfc_sfp28: typing.Callable[[], T_Result],
        sixty_four_gfc_qsfpp: typing.Callable[[], T_Result],
        one_hundred_twenty_eight_gfc_qsfp28: typing.Callable[[], T_Result],
        infiniband_sdr: typing.Callable[[], T_Result],
        infiniband_ddr: typing.Callable[[], T_Result],
        infiniband_qdr: typing.Callable[[], T_Result],
        infiniband_fdr10: typing.Callable[[], T_Result],
        infiniband_fdr: typing.Callable[[], T_Result],
        infiniband_edr: typing.Callable[[], T_Result],
        infiniband_hdr: typing.Callable[[], T_Result],
        infiniband_ndr: typing.Callable[[], T_Result],
        infiniband_xdr: typing.Callable[[], T_Result],
        t1: typing.Callable[[], T_Result],
        e1: typing.Callable[[], T_Result],
        t3: typing.Callable[[], T_Result],
        e3: typing.Callable[[], T_Result],
        xdsl: typing.Callable[[], T_Result],
        docsis: typing.Callable[[], T_Result],
        gpon: typing.Callable[[], T_Result],
        xg_pon: typing.Callable[[], T_Result],
        xgs_pon: typing.Callable[[], T_Result],
        ng_pon2: typing.Callable[[], T_Result],
        epon: typing.Callable[[], T_Result],
        ten_g_epon: typing.Callable[[], T_Result],
        cisco_stackwise: typing.Callable[[], T_Result],
        cisco_stackwise_plus: typing.Callable[[], T_Result],
        cisco_flexstack: typing.Callable[[], T_Result],
        cisco_flexstack_plus: typing.Callable[[], T_Result],
        cisco_stackwise80: typing.Callable[[], T_Result],
        cisco_stackwise160: typing.Callable[[], T_Result],
        cisco_stackwise320: typing.Callable[[], T_Result],
        cisco_stackwise480: typing.Callable[[], T_Result],
        cisco_stackwise1t: typing.Callable[[], T_Result],
        juniper_vcp: typing.Callable[[], T_Result],
        extreme_summitstack: typing.Callable[[], T_Result],
        extreme_summitstack128: typing.Callable[[], T_Result],
        extreme_summitstack256: typing.Callable[[], T_Result],
        extreme_summitstack512: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WritableInterfaceTemplateType.VIRTUAL:
            return virtual()
        if self is WritableInterfaceTemplateType.BRIDGE:
            return bridge()
        if self is WritableInterfaceTemplateType.LAG:
            return lag()
        if self is WritableInterfaceTemplateType.ONE_HUNDRED_BASE_FX:
            return one_hundred_base_fx()
        if self is WritableInterfaceTemplateType.ONE_HUNDRED_BASE_LFX:
            return one_hundred_base_lfx()
        if self is WritableInterfaceTemplateType.ONE_HUNDRED_BASE_TX:
            return one_hundred_base_tx()
        if self is WritableInterfaceTemplateType.ONE_HUNDRED_BASE_T1:
            return one_hundred_base_t1()
        if self is WritableInterfaceTemplateType.ONE_THOUSAND_BASE_T:
            return one_thousand_base_t()
        if self is WritableInterfaceTemplateType.TWO5GBASE_T:
            return two5gbase_t()
        if self is WritableInterfaceTemplateType.FIVE_GBASE_T:
            return five_gbase_t()
        if self is WritableInterfaceTemplateType.TEN_GBASE_T:
            return ten_gbase_t()
        if self is WritableInterfaceTemplateType.TEN_GBASE_CX4:
            return ten_gbase_cx4()
        if self is WritableInterfaceTemplateType.ONE_THOUSAND_BASE_X_GBIC:
            return one_thousand_base_x_gbic()
        if self is WritableInterfaceTemplateType.ONE_THOUSAND_BASE_X_SFP:
            return one_thousand_base_x_sfp()
        if self is WritableInterfaceTemplateType.TEN_GBASE_X_SFPP:
            return ten_gbase_x_sfpp()
        if self is WritableInterfaceTemplateType.TEN_GBASE_X_XFP:
            return ten_gbase_x_xfp()
        if self is WritableInterfaceTemplateType.TEN_GBASE_X_XENPAK:
            return ten_gbase_x_xenpak()
        if self is WritableInterfaceTemplateType.TEN_GBASE_XX2:
            return ten_gbase_xx2()
        if self is WritableInterfaceTemplateType.TWENTY_FIVE_GBASE_X_SFP28:
            return twenty_five_gbase_x_sfp28()
        if self is WritableInterfaceTemplateType.FIFTY_GBASE_X_SFP56:
            return fifty_gbase_x_sfp56()
        if self is WritableInterfaceTemplateType.FORTY_GBASE_X_QSFPP:
            return forty_gbase_x_qsfpp()
        if self is WritableInterfaceTemplateType.FIFTY_GBASE_X_SFP28:
            return fifty_gbase_x_sfp28()
        if self is WritableInterfaceTemplateType.ONE_HUNDRED_GBASE_X_CFP:
            return one_hundred_gbase_x_cfp()
        if self is WritableInterfaceTemplateType.ONE_HUNDRED_GBASE_X_CFP2:
            return one_hundred_gbase_x_cfp2()
        if self is WritableInterfaceTemplateType.TWO_HUNDRED_GBASE_X_CFP2:
            return two_hundred_gbase_x_cfp2()
        if self is WritableInterfaceTemplateType.ONE_HUNDRED_GBASE_X_CFP4:
            return one_hundred_gbase_x_cfp4()
        if self is WritableInterfaceTemplateType.ONE_HUNDRED_GBASE_X_CPAK:
            return one_hundred_gbase_x_cpak()
        if self is WritableInterfaceTemplateType.ONE_HUNDRED_GBASE_X_QSFP28:
            return one_hundred_gbase_x_qsfp28()
        if self is WritableInterfaceTemplateType.TWO_HUNDRED_GBASE_X_QSFP56:
            return two_hundred_gbase_x_qsfp56()
        if self is WritableInterfaceTemplateType.FOUR_HUNDRED_GBASE_X_QSFPDD:
            return four_hundred_gbase_x_qsfpdd()
        if self is WritableInterfaceTemplateType.FOUR_HUNDRED_GBASE_X_OSFP:
            return four_hundred_gbase_x_osfp()
        if self is WritableInterfaceTemplateType.EIGHT_HUNDRED_GBASE_X_QSFPDD:
            return eight_hundred_gbase_x_qsfpdd()
        if self is WritableInterfaceTemplateType.EIGHT_HUNDRED_GBASE_X_OSFP:
            return eight_hundred_gbase_x_osfp()
        if self is WritableInterfaceTemplateType.ONE_THOUSAND_BASE_KX:
            return one_thousand_base_kx()
        if self is WritableInterfaceTemplateType.TEN_GBASE_KR:
            return ten_gbase_kr()
        if self is WritableInterfaceTemplateType.TEN_GBASE_KX4:
            return ten_gbase_kx4()
        if self is WritableInterfaceTemplateType.TWENTY_FIVE_GBASE_KR:
            return twenty_five_gbase_kr()
        if self is WritableInterfaceTemplateType.FORTY_GBASE_KR4:
            return forty_gbase_kr4()
        if self is WritableInterfaceTemplateType.FIFTY_GBASE_KR:
            return fifty_gbase_kr()
        if self is WritableInterfaceTemplateType.ONE_HUNDRED_GBASE_KP4:
            return one_hundred_gbase_kp4()
        if self is WritableInterfaceTemplateType.ONE_HUNDRED_GBASE_KR2:
            return one_hundred_gbase_kr2()
        if self is WritableInterfaceTemplateType.ONE_HUNDRED_GBASE_KR4:
            return one_hundred_gbase_kr4()
        if self is WritableInterfaceTemplateType.IEEE80211A:
            return ieee80211a()
        if self is WritableInterfaceTemplateType.IEEE80211G:
            return ieee80211g()
        if self is WritableInterfaceTemplateType.IEEE80211N:
            return ieee80211n()
        if self is WritableInterfaceTemplateType.IEEE80211AC:
            return ieee80211ac()
        if self is WritableInterfaceTemplateType.IEEE80211AD:
            return ieee80211ad()
        if self is WritableInterfaceTemplateType.IEEE80211AX:
            return ieee80211ax()
        if self is WritableInterfaceTemplateType.IEEE80211AY:
            return ieee80211ay()
        if self is WritableInterfaceTemplateType.IEEE802151:
            return ieee802151()
        if self is WritableInterfaceTemplateType.OTHER_WIRELESS:
            return other_wireless()
        if self is WritableInterfaceTemplateType.GSM:
            return gsm()
        if self is WritableInterfaceTemplateType.CDMA:
            return cdma()
        if self is WritableInterfaceTemplateType.LTE:
            return lte()
        if self is WritableInterfaceTemplateType.SONET_OC3:
            return sonet_oc3()
        if self is WritableInterfaceTemplateType.SONET_OC12:
            return sonet_oc12()
        if self is WritableInterfaceTemplateType.SONET_OC48:
            return sonet_oc48()
        if self is WritableInterfaceTemplateType.SONET_OC192:
            return sonet_oc192()
        if self is WritableInterfaceTemplateType.SONET_OC768:
            return sonet_oc768()
        if self is WritableInterfaceTemplateType.SONET_OC1920:
            return sonet_oc1920()
        if self is WritableInterfaceTemplateType.SONET_OC3840:
            return sonet_oc3840()
        if self is WritableInterfaceTemplateType.ONE_GFC_SFP:
            return one_gfc_sfp()
        if self is WritableInterfaceTemplateType.TWO_GFC_SFP:
            return two_gfc_sfp()
        if self is WritableInterfaceTemplateType.FOUR_GFC_SFP:
            return four_gfc_sfp()
        if self is WritableInterfaceTemplateType.EIGHT_GFC_SFPP:
            return eight_gfc_sfpp()
        if self is WritableInterfaceTemplateType.SIXTEEN_GFC_SFPP:
            return sixteen_gfc_sfpp()
        if self is WritableInterfaceTemplateType.THIRTY_TWO_GFC_SFP28:
            return thirty_two_gfc_sfp28()
        if self is WritableInterfaceTemplateType.SIXTY_FOUR_GFC_QSFPP:
            return sixty_four_gfc_qsfpp()
        if self is WritableInterfaceTemplateType.ONE_HUNDRED_TWENTY_EIGHT_GFC_QSFP28:
            return one_hundred_twenty_eight_gfc_qsfp28()
        if self is WritableInterfaceTemplateType.INFINIBAND_SDR:
            return infiniband_sdr()
        if self is WritableInterfaceTemplateType.INFINIBAND_DDR:
            return infiniband_ddr()
        if self is WritableInterfaceTemplateType.INFINIBAND_QDR:
            return infiniband_qdr()
        if self is WritableInterfaceTemplateType.INFINIBAND_FDR10:
            return infiniband_fdr10()
        if self is WritableInterfaceTemplateType.INFINIBAND_FDR:
            return infiniband_fdr()
        if self is WritableInterfaceTemplateType.INFINIBAND_EDR:
            return infiniband_edr()
        if self is WritableInterfaceTemplateType.INFINIBAND_HDR:
            return infiniband_hdr()
        if self is WritableInterfaceTemplateType.INFINIBAND_NDR:
            return infiniband_ndr()
        if self is WritableInterfaceTemplateType.INFINIBAND_XDR:
            return infiniband_xdr()
        if self is WritableInterfaceTemplateType.T1:
            return t1()
        if self is WritableInterfaceTemplateType.E1:
            return e1()
        if self is WritableInterfaceTemplateType.T3:
            return t3()
        if self is WritableInterfaceTemplateType.E3:
            return e3()
        if self is WritableInterfaceTemplateType.XDSL:
            return xdsl()
        if self is WritableInterfaceTemplateType.DOCSIS:
            return docsis()
        if self is WritableInterfaceTemplateType.GPON:
            return gpon()
        if self is WritableInterfaceTemplateType.XG_PON:
            return xg_pon()
        if self is WritableInterfaceTemplateType.XGS_PON:
            return xgs_pon()
        if self is WritableInterfaceTemplateType.NG_PON2:
            return ng_pon2()
        if self is WritableInterfaceTemplateType.EPON:
            return epon()
        if self is WritableInterfaceTemplateType.TEN_G_EPON:
            return ten_g_epon()
        if self is WritableInterfaceTemplateType.CISCO_STACKWISE:
            return cisco_stackwise()
        if self is WritableInterfaceTemplateType.CISCO_STACKWISE_PLUS:
            return cisco_stackwise_plus()
        if self is WritableInterfaceTemplateType.CISCO_FLEXSTACK:
            return cisco_flexstack()
        if self is WritableInterfaceTemplateType.CISCO_FLEXSTACK_PLUS:
            return cisco_flexstack_plus()
        if self is WritableInterfaceTemplateType.CISCO_STACKWISE80:
            return cisco_stackwise80()
        if self is WritableInterfaceTemplateType.CISCO_STACKWISE160:
            return cisco_stackwise160()
        if self is WritableInterfaceTemplateType.CISCO_STACKWISE320:
            return cisco_stackwise320()
        if self is WritableInterfaceTemplateType.CISCO_STACKWISE480:
            return cisco_stackwise480()
        if self is WritableInterfaceTemplateType.CISCO_STACKWISE1T:
            return cisco_stackwise1t()
        if self is WritableInterfaceTemplateType.JUNIPER_VCP:
            return juniper_vcp()
        if self is WritableInterfaceTemplateType.EXTREME_SUMMITSTACK:
            return extreme_summitstack()
        if self is WritableInterfaceTemplateType.EXTREME_SUMMITSTACK128:
            return extreme_summitstack128()
        if self is WritableInterfaceTemplateType.EXTREME_SUMMITSTACK256:
            return extreme_summitstack256()
        if self is WritableInterfaceTemplateType.EXTREME_SUMMITSTACK512:
            return extreme_summitstack512()
        if self is WritableInterfaceTemplateType.OTHER:
            return other()
