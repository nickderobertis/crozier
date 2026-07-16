

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PowerPortTypeValue(str, enum.Enum):
    IEC60320C6 = "iec-60320-c6"
    IEC60320C8 = "iec-60320-c8"
    IEC60320C14 = "iec-60320-c14"
    IEC60320C16 = "iec-60320-c16"
    IEC60320C20 = "iec-60320-c20"
    IEC60320C22 = "iec-60320-c22"
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
    NEMA115P = "nema-1-15p"
    NEMA515P = "nema-5-15p"
    NEMA520P = "nema-5-20p"
    NEMA530P = "nema-5-30p"
    NEMA550P = "nema-5-50p"
    NEMA615P = "nema-6-15p"
    NEMA620P = "nema-6-20p"
    NEMA630P = "nema-6-30p"
    NEMA650P = "nema-6-50p"
    NEMA1030P = "nema-10-30p"
    NEMA1050P = "nema-10-50p"
    NEMA1420P = "nema-14-20p"
    NEMA1430P = "nema-14-30p"
    NEMA1450P = "nema-14-50p"
    NEMA1460P = "nema-14-60p"
    NEMA1515P = "nema-15-15p"
    NEMA1520P = "nema-15-20p"
    NEMA1530P = "nema-15-30p"
    NEMA1550P = "nema-15-50p"
    NEMA1560P = "nema-15-60p"
    NEMA_L115P = "nema-l1-15p"
    NEMA_L515P = "nema-l5-15p"
    NEMA_L520P = "nema-l5-20p"
    NEMA_L530P = "nema-l5-30p"
    NEMA_L550P = "nema-l5-50p"
    NEMA_L615P = "nema-l6-15p"
    NEMA_L620P = "nema-l6-20p"
    NEMA_L630P = "nema-l6-30p"
    NEMA_L650P = "nema-l6-50p"
    NEMA_L1030P = "nema-l10-30p"
    NEMA_L1420P = "nema-l14-20p"
    NEMA_L1430P = "nema-l14-30p"
    NEMA_L1450P = "nema-l14-50p"
    NEMA_L1460P = "nema-l14-60p"
    NEMA_L1520P = "nema-l15-20p"
    NEMA_L1530P = "nema-l15-30p"
    NEMA_L1550P = "nema-l15-50p"
    NEMA_L1560P = "nema-l15-60p"
    NEMA_L2120P = "nema-l21-20p"
    NEMA_L2130P = "nema-l21-30p"
    NEMA_L2230P = "nema-l22-30p"
    CS6361C = "cs6361c"
    CS6365C = "cs6365c"
    CS8165C = "cs8165c"
    CS8265C = "cs8265c"
    CS8365C = "cs8365c"
    CS8465C = "cs8465c"
    ITA_C = "ita-c"
    ITA_E = "ita-e"
    ITA_F = "ita-f"
    ITA_EF = "ita-ef"
    ITA_G = "ita-g"
    ITA_H = "ita-h"
    ITA_I = "ita-i"
    ITA_J = "ita-j"
    ITA_K = "ita-k"
    ITA_L = "ita-l"
    ITA_M = "ita-m"
    ITA_N = "ita-n"
    ITA_O = "ita-o"
    USB_A = "usb-a"
    USB_B = "usb-b"
    USB_C = "usb-c"
    USB_MINI_A = "usb-mini-a"
    USB_MINI_B = "usb-mini-b"
    USB_MICRO_A = "usb-micro-a"
    USB_MICRO_B = "usb-micro-b"
    USB_MICRO_AB = "usb-micro-ab"
    USB3B = "usb-3-b"
    USB3MICRO_B = "usb-3-micro-b"
    DC_TERMINAL = "dc-terminal"
    SAF_D_GRID = "saf-d-grid"
    NEUTRIK_POWERCON20 = "neutrik-powercon-20"
    NEUTRIK_POWERCON32 = "neutrik-powercon-32"
    NEUTRIK_POWERCON_TRUE1 = "neutrik-powercon-true1"
    NEUTRIK_POWERCON_TRUE1TOP = "neutrik-powercon-true1-top"
    UBIQUITI_SMARTPOWER = "ubiquiti-smartpower"
    HARDWIRED = "hardwired"
    OTHER = "other"

    def visit(
        self,
        iec60320c6: typing.Callable[[], T_Result],
        iec60320c8: typing.Callable[[], T_Result],
        iec60320c14: typing.Callable[[], T_Result],
        iec60320c16: typing.Callable[[], T_Result],
        iec60320c20: typing.Callable[[], T_Result],
        iec60320c22: typing.Callable[[], T_Result],
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
        nema115p: typing.Callable[[], T_Result],
        nema515p: typing.Callable[[], T_Result],
        nema520p: typing.Callable[[], T_Result],
        nema530p: typing.Callable[[], T_Result],
        nema550p: typing.Callable[[], T_Result],
        nema615p: typing.Callable[[], T_Result],
        nema620p: typing.Callable[[], T_Result],
        nema630p: typing.Callable[[], T_Result],
        nema650p: typing.Callable[[], T_Result],
        nema1030p: typing.Callable[[], T_Result],
        nema1050p: typing.Callable[[], T_Result],
        nema1420p: typing.Callable[[], T_Result],
        nema1430p: typing.Callable[[], T_Result],
        nema1450p: typing.Callable[[], T_Result],
        nema1460p: typing.Callable[[], T_Result],
        nema1515p: typing.Callable[[], T_Result],
        nema1520p: typing.Callable[[], T_Result],
        nema1530p: typing.Callable[[], T_Result],
        nema1550p: typing.Callable[[], T_Result],
        nema1560p: typing.Callable[[], T_Result],
        nema_l115p: typing.Callable[[], T_Result],
        nema_l515p: typing.Callable[[], T_Result],
        nema_l520p: typing.Callable[[], T_Result],
        nema_l530p: typing.Callable[[], T_Result],
        nema_l550p: typing.Callable[[], T_Result],
        nema_l615p: typing.Callable[[], T_Result],
        nema_l620p: typing.Callable[[], T_Result],
        nema_l630p: typing.Callable[[], T_Result],
        nema_l650p: typing.Callable[[], T_Result],
        nema_l1030p: typing.Callable[[], T_Result],
        nema_l1420p: typing.Callable[[], T_Result],
        nema_l1430p: typing.Callable[[], T_Result],
        nema_l1450p: typing.Callable[[], T_Result],
        nema_l1460p: typing.Callable[[], T_Result],
        nema_l1520p: typing.Callable[[], T_Result],
        nema_l1530p: typing.Callable[[], T_Result],
        nema_l1550p: typing.Callable[[], T_Result],
        nema_l1560p: typing.Callable[[], T_Result],
        nema_l2120p: typing.Callable[[], T_Result],
        nema_l2130p: typing.Callable[[], T_Result],
        nema_l2230p: typing.Callable[[], T_Result],
        cs6361c: typing.Callable[[], T_Result],
        cs6365c: typing.Callable[[], T_Result],
        cs8165c: typing.Callable[[], T_Result],
        cs8265c: typing.Callable[[], T_Result],
        cs8365c: typing.Callable[[], T_Result],
        cs8465c: typing.Callable[[], T_Result],
        ita_c: typing.Callable[[], T_Result],
        ita_e: typing.Callable[[], T_Result],
        ita_f: typing.Callable[[], T_Result],
        ita_ef: typing.Callable[[], T_Result],
        ita_g: typing.Callable[[], T_Result],
        ita_h: typing.Callable[[], T_Result],
        ita_i: typing.Callable[[], T_Result],
        ita_j: typing.Callable[[], T_Result],
        ita_k: typing.Callable[[], T_Result],
        ita_l: typing.Callable[[], T_Result],
        ita_m: typing.Callable[[], T_Result],
        ita_n: typing.Callable[[], T_Result],
        ita_o: typing.Callable[[], T_Result],
        usb_a: typing.Callable[[], T_Result],
        usb_b: typing.Callable[[], T_Result],
        usb_c: typing.Callable[[], T_Result],
        usb_mini_a: typing.Callable[[], T_Result],
        usb_mini_b: typing.Callable[[], T_Result],
        usb_micro_a: typing.Callable[[], T_Result],
        usb_micro_b: typing.Callable[[], T_Result],
        usb_micro_ab: typing.Callable[[], T_Result],
        usb3b: typing.Callable[[], T_Result],
        usb3micro_b: typing.Callable[[], T_Result],
        dc_terminal: typing.Callable[[], T_Result],
        saf_d_grid: typing.Callable[[], T_Result],
        neutrik_powercon20: typing.Callable[[], T_Result],
        neutrik_powercon32: typing.Callable[[], T_Result],
        neutrik_powercon_true1: typing.Callable[[], T_Result],
        neutrik_powercon_true1top: typing.Callable[[], T_Result],
        ubiquiti_smartpower: typing.Callable[[], T_Result],
        hardwired: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PowerPortTypeValue.IEC60320C6:
            return iec60320c6()
        if self is PowerPortTypeValue.IEC60320C8:
            return iec60320c8()
        if self is PowerPortTypeValue.IEC60320C14:
            return iec60320c14()
        if self is PowerPortTypeValue.IEC60320C16:
            return iec60320c16()
        if self is PowerPortTypeValue.IEC60320C20:
            return iec60320c20()
        if self is PowerPortTypeValue.IEC60320C22:
            return iec60320c22()
        if self is PowerPortTypeValue.IEC60309PNE4H:
            return iec60309pne4h()
        if self is PowerPortTypeValue.IEC60309PNE6H:
            return iec60309pne6h()
        if self is PowerPortTypeValue.IEC60309PNE9H:
            return iec60309pne9h()
        if self is PowerPortTypeValue.IEC603092PE4H:
            return iec603092pe4h()
        if self is PowerPortTypeValue.IEC603092PE6H:
            return iec603092pe6h()
        if self is PowerPortTypeValue.IEC603092PE9H:
            return iec603092pe9h()
        if self is PowerPortTypeValue.IEC603093PE4H:
            return iec603093pe4h()
        if self is PowerPortTypeValue.IEC603093PE6H:
            return iec603093pe6h()
        if self is PowerPortTypeValue.IEC603093PE9H:
            return iec603093pe9h()
        if self is PowerPortTypeValue.IEC603093PNE4H:
            return iec603093pne4h()
        if self is PowerPortTypeValue.IEC603093PNE6H:
            return iec603093pne6h()
        if self is PowerPortTypeValue.IEC603093PNE9H:
            return iec603093pne9h()
        if self is PowerPortTypeValue.NEMA115P:
            return nema115p()
        if self is PowerPortTypeValue.NEMA515P:
            return nema515p()
        if self is PowerPortTypeValue.NEMA520P:
            return nema520p()
        if self is PowerPortTypeValue.NEMA530P:
            return nema530p()
        if self is PowerPortTypeValue.NEMA550P:
            return nema550p()
        if self is PowerPortTypeValue.NEMA615P:
            return nema615p()
        if self is PowerPortTypeValue.NEMA620P:
            return nema620p()
        if self is PowerPortTypeValue.NEMA630P:
            return nema630p()
        if self is PowerPortTypeValue.NEMA650P:
            return nema650p()
        if self is PowerPortTypeValue.NEMA1030P:
            return nema1030p()
        if self is PowerPortTypeValue.NEMA1050P:
            return nema1050p()
        if self is PowerPortTypeValue.NEMA1420P:
            return nema1420p()
        if self is PowerPortTypeValue.NEMA1430P:
            return nema1430p()
        if self is PowerPortTypeValue.NEMA1450P:
            return nema1450p()
        if self is PowerPortTypeValue.NEMA1460P:
            return nema1460p()
        if self is PowerPortTypeValue.NEMA1515P:
            return nema1515p()
        if self is PowerPortTypeValue.NEMA1520P:
            return nema1520p()
        if self is PowerPortTypeValue.NEMA1530P:
            return nema1530p()
        if self is PowerPortTypeValue.NEMA1550P:
            return nema1550p()
        if self is PowerPortTypeValue.NEMA1560P:
            return nema1560p()
        if self is PowerPortTypeValue.NEMA_L115P:
            return nema_l115p()
        if self is PowerPortTypeValue.NEMA_L515P:
            return nema_l515p()
        if self is PowerPortTypeValue.NEMA_L520P:
            return nema_l520p()
        if self is PowerPortTypeValue.NEMA_L530P:
            return nema_l530p()
        if self is PowerPortTypeValue.NEMA_L550P:
            return nema_l550p()
        if self is PowerPortTypeValue.NEMA_L615P:
            return nema_l615p()
        if self is PowerPortTypeValue.NEMA_L620P:
            return nema_l620p()
        if self is PowerPortTypeValue.NEMA_L630P:
            return nema_l630p()
        if self is PowerPortTypeValue.NEMA_L650P:
            return nema_l650p()
        if self is PowerPortTypeValue.NEMA_L1030P:
            return nema_l1030p()
        if self is PowerPortTypeValue.NEMA_L1420P:
            return nema_l1420p()
        if self is PowerPortTypeValue.NEMA_L1430P:
            return nema_l1430p()
        if self is PowerPortTypeValue.NEMA_L1450P:
            return nema_l1450p()
        if self is PowerPortTypeValue.NEMA_L1460P:
            return nema_l1460p()
        if self is PowerPortTypeValue.NEMA_L1520P:
            return nema_l1520p()
        if self is PowerPortTypeValue.NEMA_L1530P:
            return nema_l1530p()
        if self is PowerPortTypeValue.NEMA_L1550P:
            return nema_l1550p()
        if self is PowerPortTypeValue.NEMA_L1560P:
            return nema_l1560p()
        if self is PowerPortTypeValue.NEMA_L2120P:
            return nema_l2120p()
        if self is PowerPortTypeValue.NEMA_L2130P:
            return nema_l2130p()
        if self is PowerPortTypeValue.NEMA_L2230P:
            return nema_l2230p()
        if self is PowerPortTypeValue.CS6361C:
            return cs6361c()
        if self is PowerPortTypeValue.CS6365C:
            return cs6365c()
        if self is PowerPortTypeValue.CS8165C:
            return cs8165c()
        if self is PowerPortTypeValue.CS8265C:
            return cs8265c()
        if self is PowerPortTypeValue.CS8365C:
            return cs8365c()
        if self is PowerPortTypeValue.CS8465C:
            return cs8465c()
        if self is PowerPortTypeValue.ITA_C:
            return ita_c()
        if self is PowerPortTypeValue.ITA_E:
            return ita_e()
        if self is PowerPortTypeValue.ITA_F:
            return ita_f()
        if self is PowerPortTypeValue.ITA_EF:
            return ita_ef()
        if self is PowerPortTypeValue.ITA_G:
            return ita_g()
        if self is PowerPortTypeValue.ITA_H:
            return ita_h()
        if self is PowerPortTypeValue.ITA_I:
            return ita_i()
        if self is PowerPortTypeValue.ITA_J:
            return ita_j()
        if self is PowerPortTypeValue.ITA_K:
            return ita_k()
        if self is PowerPortTypeValue.ITA_L:
            return ita_l()
        if self is PowerPortTypeValue.ITA_M:
            return ita_m()
        if self is PowerPortTypeValue.ITA_N:
            return ita_n()
        if self is PowerPortTypeValue.ITA_O:
            return ita_o()
        if self is PowerPortTypeValue.USB_A:
            return usb_a()
        if self is PowerPortTypeValue.USB_B:
            return usb_b()
        if self is PowerPortTypeValue.USB_C:
            return usb_c()
        if self is PowerPortTypeValue.USB_MINI_A:
            return usb_mini_a()
        if self is PowerPortTypeValue.USB_MINI_B:
            return usb_mini_b()
        if self is PowerPortTypeValue.USB_MICRO_A:
            return usb_micro_a()
        if self is PowerPortTypeValue.USB_MICRO_B:
            return usb_micro_b()
        if self is PowerPortTypeValue.USB_MICRO_AB:
            return usb_micro_ab()
        if self is PowerPortTypeValue.USB3B:
            return usb3b()
        if self is PowerPortTypeValue.USB3MICRO_B:
            return usb3micro_b()
        if self is PowerPortTypeValue.DC_TERMINAL:
            return dc_terminal()
        if self is PowerPortTypeValue.SAF_D_GRID:
            return saf_d_grid()
        if self is PowerPortTypeValue.NEUTRIK_POWERCON20:
            return neutrik_powercon20()
        if self is PowerPortTypeValue.NEUTRIK_POWERCON32:
            return neutrik_powercon32()
        if self is PowerPortTypeValue.NEUTRIK_POWERCON_TRUE1:
            return neutrik_powercon_true1()
        if self is PowerPortTypeValue.NEUTRIK_POWERCON_TRUE1TOP:
            return neutrik_powercon_true1top()
        if self is PowerPortTypeValue.UBIQUITI_SMARTPOWER:
            return ubiquiti_smartpower()
        if self is PowerPortTypeValue.HARDWIRED:
            return hardwired()
        if self is PowerPortTypeValue.OTHER:
            return other()
