

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PowerOutletTypeValue(str, enum.Enum):
    IEC60320C5 = "iec-60320-c5"
    IEC60320C7 = "iec-60320-c7"
    IEC60320C13 = "iec-60320-c13"
    IEC60320C15 = "iec-60320-c15"
    IEC60320C19 = "iec-60320-c19"
    IEC60320C21 = "iec-60320-c21"
    IEC60309PNE4H = "iec-60309-p-n-e-4h"
    IEC60309PNE6H = "iec-60309-p-n-e-6h"
    IEC60309PNE9H = "iec-60309-p-n-e-9h"
    IEC603092PE4H = "iec-60309-2p-e-4h"
    IEC603092PE6H = "iec-60309-2p-e-6h"
    IEC603092PE9H = "iec-60309-2p-e-9h"
    IEC603093PE4H = "iec-60309-3p-e-4h"
    IEC603093PE6H = "iec-60309-3p-e-6h"
    IEC603093PE9H = "iec-60309-3p-e-9h"
    IEC603093PNE4H = "iec-60309-3p-n-e-4h"
    IEC603093PNE6H = "iec-60309-3p-n-e-6h"
    IEC603093PNE9H = "iec-60309-3p-n-e-9h"
    NEMA115R = "nema-1-15r"
    NEMA515R = "nema-5-15r"
    NEMA520R = "nema-5-20r"
    NEMA530R = "nema-5-30r"
    NEMA550R = "nema-5-50r"
    NEMA615R = "nema-6-15r"
    NEMA620R = "nema-6-20r"
    NEMA630R = "nema-6-30r"
    NEMA650R = "nema-6-50r"
    NEMA1030R = "nema-10-30r"
    NEMA1050R = "nema-10-50r"
    NEMA1420R = "nema-14-20r"
    NEMA1430R = "nema-14-30r"
    NEMA1450R = "nema-14-50r"
    NEMA1460R = "nema-14-60r"
    NEMA1515R = "nema-15-15r"
    NEMA1520R = "nema-15-20r"
    NEMA1530R = "nema-15-30r"
    NEMA1550R = "nema-15-50r"
    NEMA1560R = "nema-15-60r"
    NEMA_L115R = "nema-l1-15r"
    NEMA_L515R = "nema-l5-15r"
    NEMA_L520R = "nema-l5-20r"
    NEMA_L530R = "nema-l5-30r"
    NEMA_L550R = "nema-l5-50r"
    NEMA_L615R = "nema-l6-15r"
    NEMA_L620R = "nema-l6-20r"
    NEMA_L630R = "nema-l6-30r"
    NEMA_L650R = "nema-l6-50r"
    NEMA_L1030R = "nema-l10-30r"
    NEMA_L1420R = "nema-l14-20r"
    NEMA_L1430R = "nema-l14-30r"
    NEMA_L1450R = "nema-l14-50r"
    NEMA_L1460R = "nema-l14-60r"
    NEMA_L1520R = "nema-l15-20r"
    NEMA_L1530R = "nema-l15-30r"
    NEMA_L1550R = "nema-l15-50r"
    NEMA_L1560R = "nema-l15-60r"
    NEMA_L2120R = "nema-l21-20r"
    NEMA_L2130R = "nema-l21-30r"
    NEMA_L2230R = "nema-l22-30r"
    CS6360C = "CS6360C"
    CS6364C = "CS6364C"
    CS8164C = "CS8164C"
    CS8264C = "CS8264C"
    CS8364C = "CS8364C"
    CS8464C = "CS8464C"
    ITA_E = "ita-e"
    ITA_F = "ita-f"
    ITA_G = "ita-g"
    ITA_H = "ita-h"
    ITA_I = "ita-i"
    ITA_J = "ita-j"
    ITA_K = "ita-k"
    ITA_L = "ita-l"
    ITA_M = "ita-m"
    ITA_N = "ita-n"
    ITA_O = "ita-o"
    ITA_MULTISTANDARD = "ita-multistandard"
    USB_A = "usb-a"
    USB_MICRO_B = "usb-micro-b"
    USB_C = "usb-c"
    DC_TERMINAL = "dc-terminal"
    HDOT_CX = "hdot-cx"
    SAF_D_GRID = "saf-d-grid"
    NEUTRIK_POWERCON20A = "neutrik-powercon-20a"
    NEUTRIK_POWERCON32A = "neutrik-powercon-32a"
    NEUTRIK_POWERCON_TRUE1 = "neutrik-powercon-true1"
    NEUTRIK_POWERCON_TRUE1TOP = "neutrik-powercon-true1-top"
    UBIQUITI_SMARTPOWER = "ubiquiti-smartpower"
    HARDWIRED = "hardwired"
    OTHER = "other"

    def visit(
        self,
        iec60320c5: typing.Callable[[], T_Result],
        iec60320c7: typing.Callable[[], T_Result],
        iec60320c13: typing.Callable[[], T_Result],
        iec60320c15: typing.Callable[[], T_Result],
        iec60320c19: typing.Callable[[], T_Result],
        iec60320c21: typing.Callable[[], T_Result],
        iec60309pne4h: typing.Callable[[], T_Result],
        iec60309pne6h: typing.Callable[[], T_Result],
        iec60309pne9h: typing.Callable[[], T_Result],
        iec603092pe4h: typing.Callable[[], T_Result],
        iec603092pe6h: typing.Callable[[], T_Result],
        iec603092pe9h: typing.Callable[[], T_Result],
        iec603093pe4h: typing.Callable[[], T_Result],
        iec603093pe6h: typing.Callable[[], T_Result],
        iec603093pe9h: typing.Callable[[], T_Result],
        iec603093pne4h: typing.Callable[[], T_Result],
        iec603093pne6h: typing.Callable[[], T_Result],
        iec603093pne9h: typing.Callable[[], T_Result],
        nema115r: typing.Callable[[], T_Result],
        nema515r: typing.Callable[[], T_Result],
        nema520r: typing.Callable[[], T_Result],
        nema530r: typing.Callable[[], T_Result],
        nema550r: typing.Callable[[], T_Result],
        nema615r: typing.Callable[[], T_Result],
        nema620r: typing.Callable[[], T_Result],
        nema630r: typing.Callable[[], T_Result],
        nema650r: typing.Callable[[], T_Result],
        nema1030r: typing.Callable[[], T_Result],
        nema1050r: typing.Callable[[], T_Result],
        nema1420r: typing.Callable[[], T_Result],
        nema1430r: typing.Callable[[], T_Result],
        nema1450r: typing.Callable[[], T_Result],
        nema1460r: typing.Callable[[], T_Result],
        nema1515r: typing.Callable[[], T_Result],
        nema1520r: typing.Callable[[], T_Result],
        nema1530r: typing.Callable[[], T_Result],
        nema1550r: typing.Callable[[], T_Result],
        nema1560r: typing.Callable[[], T_Result],
        nema_l115r: typing.Callable[[], T_Result],
        nema_l515r: typing.Callable[[], T_Result],
        nema_l520r: typing.Callable[[], T_Result],
        nema_l530r: typing.Callable[[], T_Result],
        nema_l550r: typing.Callable[[], T_Result],
        nema_l615r: typing.Callable[[], T_Result],
        nema_l620r: typing.Callable[[], T_Result],
        nema_l630r: typing.Callable[[], T_Result],
        nema_l650r: typing.Callable[[], T_Result],
        nema_l1030r: typing.Callable[[], T_Result],
        nema_l1420r: typing.Callable[[], T_Result],
        nema_l1430r: typing.Callable[[], T_Result],
        nema_l1450r: typing.Callable[[], T_Result],
        nema_l1460r: typing.Callable[[], T_Result],
        nema_l1520r: typing.Callable[[], T_Result],
        nema_l1530r: typing.Callable[[], T_Result],
        nema_l1550r: typing.Callable[[], T_Result],
        nema_l1560r: typing.Callable[[], T_Result],
        nema_l2120r: typing.Callable[[], T_Result],
        nema_l2130r: typing.Callable[[], T_Result],
        nema_l2230r: typing.Callable[[], T_Result],
        cs6360c: typing.Callable[[], T_Result],
        cs6364c: typing.Callable[[], T_Result],
        cs8164c: typing.Callable[[], T_Result],
        cs8264c: typing.Callable[[], T_Result],
        cs8364c: typing.Callable[[], T_Result],
        cs8464c: typing.Callable[[], T_Result],
        ita_e: typing.Callable[[], T_Result],
        ita_f: typing.Callable[[], T_Result],
        ita_g: typing.Callable[[], T_Result],
        ita_h: typing.Callable[[], T_Result],
        ita_i: typing.Callable[[], T_Result],
        ita_j: typing.Callable[[], T_Result],
        ita_k: typing.Callable[[], T_Result],
        ita_l: typing.Callable[[], T_Result],
        ita_m: typing.Callable[[], T_Result],
        ita_n: typing.Callable[[], T_Result],
        ita_o: typing.Callable[[], T_Result],
        ita_multistandard: typing.Callable[[], T_Result],
        usb_a: typing.Callable[[], T_Result],
        usb_micro_b: typing.Callable[[], T_Result],
        usb_c: typing.Callable[[], T_Result],
        dc_terminal: typing.Callable[[], T_Result],
        hdot_cx: typing.Callable[[], T_Result],
        saf_d_grid: typing.Callable[[], T_Result],
        neutrik_powercon20a: typing.Callable[[], T_Result],
        neutrik_powercon32a: typing.Callable[[], T_Result],
        neutrik_powercon_true1: typing.Callable[[], T_Result],
        neutrik_powercon_true1top: typing.Callable[[], T_Result],
        ubiquiti_smartpower: typing.Callable[[], T_Result],
        hardwired: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PowerOutletTypeValue.IEC60320C5:
            return iec60320c5()
        if self is PowerOutletTypeValue.IEC60320C7:
            return iec60320c7()
        if self is PowerOutletTypeValue.IEC60320C13:
            return iec60320c13()
        if self is PowerOutletTypeValue.IEC60320C15:
            return iec60320c15()
        if self is PowerOutletTypeValue.IEC60320C19:
            return iec60320c19()
        if self is PowerOutletTypeValue.IEC60320C21:
            return iec60320c21()
        if self is PowerOutletTypeValue.IEC60309PNE4H:
            return iec60309pne4h()
        if self is PowerOutletTypeValue.IEC60309PNE6H:
            return iec60309pne6h()
        if self is PowerOutletTypeValue.IEC60309PNE9H:
            return iec60309pne9h()
        if self is PowerOutletTypeValue.IEC603092PE4H:
            return iec603092pe4h()
        if self is PowerOutletTypeValue.IEC603092PE6H:
            return iec603092pe6h()
        if self is PowerOutletTypeValue.IEC603092PE9H:
            return iec603092pe9h()
        if self is PowerOutletTypeValue.IEC603093PE4H:
            return iec603093pe4h()
        if self is PowerOutletTypeValue.IEC603093PE6H:
            return iec603093pe6h()
        if self is PowerOutletTypeValue.IEC603093PE9H:
            return iec603093pe9h()
        if self is PowerOutletTypeValue.IEC603093PNE4H:
            return iec603093pne4h()
        if self is PowerOutletTypeValue.IEC603093PNE6H:
            return iec603093pne6h()
        if self is PowerOutletTypeValue.IEC603093PNE9H:
            return iec603093pne9h()
        if self is PowerOutletTypeValue.NEMA115R:
            return nema115r()
        if self is PowerOutletTypeValue.NEMA515R:
            return nema515r()
        if self is PowerOutletTypeValue.NEMA520R:
            return nema520r()
        if self is PowerOutletTypeValue.NEMA530R:
            return nema530r()
        if self is PowerOutletTypeValue.NEMA550R:
            return nema550r()
        if self is PowerOutletTypeValue.NEMA615R:
            return nema615r()
        if self is PowerOutletTypeValue.NEMA620R:
            return nema620r()
        if self is PowerOutletTypeValue.NEMA630R:
            return nema630r()
        if self is PowerOutletTypeValue.NEMA650R:
            return nema650r()
        if self is PowerOutletTypeValue.NEMA1030R:
            return nema1030r()
        if self is PowerOutletTypeValue.NEMA1050R:
            return nema1050r()
        if self is PowerOutletTypeValue.NEMA1420R:
            return nema1420r()
        if self is PowerOutletTypeValue.NEMA1430R:
            return nema1430r()
        if self is PowerOutletTypeValue.NEMA1450R:
            return nema1450r()
        if self is PowerOutletTypeValue.NEMA1460R:
            return nema1460r()
        if self is PowerOutletTypeValue.NEMA1515R:
            return nema1515r()
        if self is PowerOutletTypeValue.NEMA1520R:
            return nema1520r()
        if self is PowerOutletTypeValue.NEMA1530R:
            return nema1530r()
        if self is PowerOutletTypeValue.NEMA1550R:
            return nema1550r()
        if self is PowerOutletTypeValue.NEMA1560R:
            return nema1560r()
        if self is PowerOutletTypeValue.NEMA_L115R:
            return nema_l115r()
        if self is PowerOutletTypeValue.NEMA_L515R:
            return nema_l515r()
        if self is PowerOutletTypeValue.NEMA_L520R:
            return nema_l520r()
        if self is PowerOutletTypeValue.NEMA_L530R:
            return nema_l530r()
        if self is PowerOutletTypeValue.NEMA_L550R:
            return nema_l550r()
        if self is PowerOutletTypeValue.NEMA_L615R:
            return nema_l615r()
        if self is PowerOutletTypeValue.NEMA_L620R:
            return nema_l620r()
        if self is PowerOutletTypeValue.NEMA_L630R:
            return nema_l630r()
        if self is PowerOutletTypeValue.NEMA_L650R:
            return nema_l650r()
        if self is PowerOutletTypeValue.NEMA_L1030R:
            return nema_l1030r()
        if self is PowerOutletTypeValue.NEMA_L1420R:
            return nema_l1420r()
        if self is PowerOutletTypeValue.NEMA_L1430R:
            return nema_l1430r()
        if self is PowerOutletTypeValue.NEMA_L1450R:
            return nema_l1450r()
        if self is PowerOutletTypeValue.NEMA_L1460R:
            return nema_l1460r()
        if self is PowerOutletTypeValue.NEMA_L1520R:
            return nema_l1520r()
        if self is PowerOutletTypeValue.NEMA_L1530R:
            return nema_l1530r()
        if self is PowerOutletTypeValue.NEMA_L1550R:
            return nema_l1550r()
        if self is PowerOutletTypeValue.NEMA_L1560R:
            return nema_l1560r()
        if self is PowerOutletTypeValue.NEMA_L2120R:
            return nema_l2120r()
        if self is PowerOutletTypeValue.NEMA_L2130R:
            return nema_l2130r()
        if self is PowerOutletTypeValue.NEMA_L2230R:
            return nema_l2230r()
        if self is PowerOutletTypeValue.CS6360C:
            return cs6360c()
        if self is PowerOutletTypeValue.CS6364C:
            return cs6364c()
        if self is PowerOutletTypeValue.CS8164C:
            return cs8164c()
        if self is PowerOutletTypeValue.CS8264C:
            return cs8264c()
        if self is PowerOutletTypeValue.CS8364C:
            return cs8364c()
        if self is PowerOutletTypeValue.CS8464C:
            return cs8464c()
        if self is PowerOutletTypeValue.ITA_E:
            return ita_e()
        if self is PowerOutletTypeValue.ITA_F:
            return ita_f()
        if self is PowerOutletTypeValue.ITA_G:
            return ita_g()
        if self is PowerOutletTypeValue.ITA_H:
            return ita_h()
        if self is PowerOutletTypeValue.ITA_I:
            return ita_i()
        if self is PowerOutletTypeValue.ITA_J:
            return ita_j()
        if self is PowerOutletTypeValue.ITA_K:
            return ita_k()
        if self is PowerOutletTypeValue.ITA_L:
            return ita_l()
        if self is PowerOutletTypeValue.ITA_M:
            return ita_m()
        if self is PowerOutletTypeValue.ITA_N:
            return ita_n()
        if self is PowerOutletTypeValue.ITA_O:
            return ita_o()
        if self is PowerOutletTypeValue.ITA_MULTISTANDARD:
            return ita_multistandard()
        if self is PowerOutletTypeValue.USB_A:
            return usb_a()
        if self is PowerOutletTypeValue.USB_MICRO_B:
            return usb_micro_b()
        if self is PowerOutletTypeValue.USB_C:
            return usb_c()
        if self is PowerOutletTypeValue.DC_TERMINAL:
            return dc_terminal()
        if self is PowerOutletTypeValue.HDOT_CX:
            return hdot_cx()
        if self is PowerOutletTypeValue.SAF_D_GRID:
            return saf_d_grid()
        if self is PowerOutletTypeValue.NEUTRIK_POWERCON20A:
            return neutrik_powercon20a()
        if self is PowerOutletTypeValue.NEUTRIK_POWERCON32A:
            return neutrik_powercon32a()
        if self is PowerOutletTypeValue.NEUTRIK_POWERCON_TRUE1:
            return neutrik_powercon_true1()
        if self is PowerOutletTypeValue.NEUTRIK_POWERCON_TRUE1TOP:
            return neutrik_powercon_true1top()
        if self is PowerOutletTypeValue.UBIQUITI_SMARTPOWER:
            return ubiquiti_smartpower()
        if self is PowerOutletTypeValue.HARDWIRED:
            return hardwired()
        if self is PowerOutletTypeValue.OTHER:
            return other()
