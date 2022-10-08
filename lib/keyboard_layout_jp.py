#ASCII_TO_KEYCODEJP

#from adafruit_hid.keycode import Keycode
from keycode_jp import KeycodeJP

class KeyboardLayoutJP():
    ASCII_TO_KEYCODEJP = [
        [0x00],  # NULL
        [0x00],  # SOH
        [0x00],  # STX
        [0x00],  # ETX
        [0x00],  # EOT
        [0x00],  # ENQ
        [0x00],  # ACK
        [0x00],  # BEL \a
        [KeycodeJP.BACKSPACE],  # BS BACKSPACE \b (called DELETE in the usb.org document)
        [KeycodeJP.TAB],  # TAB \t
        [0x00],  # LF \n (called Return or ENTER in the usb.org document)
        [0x00],  # LF \n (called Return or ENTER in the usb.org document)
        [0x00],  # VT \v
        [0x00],  # FF \f
        [KeycodeJP.ENTER],  # CR \r
        [0x00],  # SO
        [0x00],  # SI
        [0x00],  # DLE
        [0x00],  # DC1
        [0x00],  # DC2
        [0x00],  # DC3
        [0x00],  # DC4
        [0x00],  # NAK
        [0x00],  # SYN
        [0x00],  # ETB
        [0x00],  # CAN
        [0x00],  # EM
        [0x00],  # SUB
        [KeycodeJP.ESCAPE],  # ESC
        [0x00],  # FS
        [0x00],  # GS
        [0x00],  # RS
        [0x00],  # US
        [KeycodeJP.SPACEBAR],  # SPACE
        [KeycodeJP.ONE, KeycodeJP.SHIFT],  # !
        [KeycodeJP.TWO, KeycodeJP.SHIFT],  # "
        [KeycodeJP.THREE, KeycodeJP.SHIFT], # #
        [KeycodeJP.FOUR, KeycodeJP.SHIFT],  # $
        [KeycodeJP.FIVE, KeycodeJP.SHIFT],  # %
        [KeycodeJP.SIX, KeycodeJP.SHIFT],  # &
        [KeycodeJP.SEVEN, KeycodeJP.SHIFT],  # '
        [KeycodeJP.EIGHT, KeycodeJP.SHIFT],  # (
        [KeycodeJP.NINE, KeycodeJP.SHIFT],  # )
        [KeycodeJP.COLON, KeycodeJP.SHIFT],  # *
        [KeycodeJP.SEMICOLON, KeycodeJP.SHIFT],  # +
        [KeycodeJP.COMMA],  # ,
        [KeycodeJP.MINUS],  # -
        [KeycodeJP.PERIOD],  # .
        [KeycodeJP.FORWARD_SLASH],  # /
        [KeycodeJP.ZERO],  # 0
        [KeycodeJP.ONE],  # 1
        [KeycodeJP.TWO],  # 2
        [KeycodeJP.THREE],  # 3
        [KeycodeJP.FOUR],  # 4
        [KeycodeJP.FIVE],  # 5
        [KeycodeJP.SIX],  # 6
        [KeycodeJP.SEVEN],  # 7
        [KeycodeJP.EIGHT],  # 8
        [KeycodeJP.NINE],  # 9
        [KeycodeJP.COLON],  # :
        [KeycodeJP.SEMICOLON],  # ;
        [KeycodeJP.COMMA, KeycodeJP.SHIFT],  # <
        [KeycodeJP.MINUS, KeycodeJP.SHIFT],  # =
        [KeycodeJP.PERIOD, KeycodeJP.SHIFT],  # >
        [KeycodeJP.FORWARD_SLASH, KeycodeJP.SHIFT],  # ?
        [KeycodeJP.ATSIGN],  # @
        [KeycodeJP.A, KeycodeJP.SHIFT],  # A
        [KeycodeJP.B, KeycodeJP.SHIFT],  # B
        [KeycodeJP.C, KeycodeJP.SHIFT],  # C
        [KeycodeJP.D, KeycodeJP.SHIFT],  # D
        [KeycodeJP.E, KeycodeJP.SHIFT],  # E
        [KeycodeJP.F, KeycodeJP.SHIFT],  # F
        [KeycodeJP.G, KeycodeJP.SHIFT],  # G
        [KeycodeJP.H, KeycodeJP.SHIFT],  # H
        [KeycodeJP.I, KeycodeJP.SHIFT],  # I
        [KeycodeJP.J, KeycodeJP.SHIFT],  # J
        [KeycodeJP.K, KeycodeJP.SHIFT],  # K
        [KeycodeJP.L, KeycodeJP.SHIFT],  # L
        [KeycodeJP.M, KeycodeJP.SHIFT],  # M
        [KeycodeJP.N, KeycodeJP.SHIFT],  # N
        [KeycodeJP.O, KeycodeJP.SHIFT],  # O
        [KeycodeJP.P, KeycodeJP.SHIFT],  # P
        [KeycodeJP.Q, KeycodeJP.SHIFT],  # Q
        [KeycodeJP.R, KeycodeJP.SHIFT],  # R
        [KeycodeJP.S, KeycodeJP.SHIFT],  # S
        [KeycodeJP.T, KeycodeJP.SHIFT],  # T
        [KeycodeJP.U, KeycodeJP.SHIFT],  # U
        [KeycodeJP.V, KeycodeJP.SHIFT],  # V
        [KeycodeJP.W, KeycodeJP.SHIFT],  # W
        [KeycodeJP.X, KeycodeJP.SHIFT],  # X
        [KeycodeJP.Y, KeycodeJP.SHIFT],  # Y
        [KeycodeJP.Z, KeycodeJP.SHIFT],  # Z
        [KeycodeJP.LEFT_BRACKET],  # [
        [KeycodeJP.INTERNATIONAL1],  # \ backslash
        [KeycodeJP.RIGHT_BRACKET],  # ]
        [KeycodeJP.CIRCUMFLEX],  # ^
        [KeycodeJP.INTERNATIONAL1, KeycodeJP.SHIFT],  # _
        [KeycodeJP.ATSIGN, KeycodeJP.SHIFT],  # `
        [KeycodeJP.A],  # a
        [KeycodeJP.B],  # b
        [KeycodeJP.C],  # c
        [KeycodeJP.D],  # d
        [KeycodeJP.E],  # e
        [KeycodeJP.F],  # f
        [KeycodeJP.G],  # g
        [KeycodeJP.H],  # h
        [KeycodeJP.I],  # i
        [KeycodeJP.J],  # j
        [KeycodeJP.K],  # k
        [KeycodeJP.L],  # l
        [KeycodeJP.M],  # m
        [KeycodeJP.N],  # n
        [KeycodeJP.O],  # o
        [KeycodeJP.P],  # p
        [KeycodeJP.Q],  # q
        [KeycodeJP.R],  # r
        [KeycodeJP.S],  # s
        [KeycodeJP.T],  # t
        [KeycodeJP.U],  # u
        [KeycodeJP.V],  # v
        [KeycodeJP.W],  # w
        [KeycodeJP.X],  # x
        [KeycodeJP.Y],  # y
        [KeycodeJP.Z],  # z
        [KeycodeJP.LEFT_BRACKET, KeycodeJP.SHIFT],  # {
        [KeycodeJP.INTERNATIONAL3, KeycodeJP.SHIFT],  # |
        [KeycodeJP.RIGHT_BRACKET, KeycodeJP.SHIFT],  # }
        [KeycodeJP.CIRCUMFLEX, KeycodeJP.SHIFT],  # ~
        [0x00],  # DEL DELETE (called Forward Delete in usb.org document)
    ]
