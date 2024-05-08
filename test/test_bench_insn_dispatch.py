import pytest

def basic(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 3
    elif x == 4:
        return 4
    elif x == 5:
        return 5
    elif x == 6:
        return 6
    elif x == 7:
        return 7
    elif x == 8:
        return 8
    elif x == 9:
        return 9
    elif x == 10:
        return 10
    elif x == 11:
        return 11
    elif x == 12:
        return 12
    elif x == 13:
        return 13
    elif x == 14:
        return 14
    elif x == 15:
        return 15
    elif x == 16:
        return 16
    elif x == 17:
        return 17
    elif x == 18:
        return 18
    elif x == 19:
        return 19
    elif x == 20:
        return 20
    elif x == 21:
        return 21
    elif x == 22:
        return 22
    elif x == 23:
        return 23
    elif x == 24:
        return 24
    elif x == 25:
        return 25
    elif x == 26:
        return 26
    elif x == 27:
        return 27
    elif x == 28:
        return 28
    elif x == 29:
        return 29
    elif x == 30:
        return 30
    elif x == 31:
        return 31
    elif x == 32:
        return 32
    elif x == 33:
        return 33
    elif x == 34:
        return 34
    elif x == 35:
        return 35
    elif x == 36:
        return 36
    elif x == 37:
        return 37
    elif x == 38:
        return 38
    elif x == 39:
        return 39
    elif x == 40:
        return 40
    elif x == 41:
        return 41
    elif x == 42:
        return 42
    elif x == 43:
        return 43
    elif x == 44:
        return 44
    elif x == 45:
        return 45
    elif x == 46:
        return 46
    elif x == 47:
        return 47
    elif x == 48:
        return 48
    elif x == 49:
        return 49
    elif x == 50:
        return 50
    elif x == 51:
        return 51
    elif x == 52:
        return 52
    elif x == 53:
        return 53
    elif x == 54:
        return 54
    elif x == 55:
        return 55
    elif x == 56:
        return 56
    elif x == 57:
        return 57
    elif x == 58:
        return 58
    elif x == 59:
        return 59
    elif x == 60:
        return 60
    elif x == 61:
        return 61
    elif x == 62:
        return 62
    elif x == 63:
        return 63
    elif x == 64:
        return 64
    elif x == 65:
        return 65
    elif x == 66:
        return 66
    elif x == 67:
        return 67
    elif x == 68:
        return 68
    elif x == 69:
        return 69
    elif x == 70:
        return 70
    elif x == 71:
        return 71
    elif x == 72:
        return 72
    elif x == 73:
        return 73
    elif x == 74:
        return 74
    elif x == 75:
        return 75
    elif x == 76:
        return 76
    elif x == 77:
        return 77
    elif x == 78:
        return 78
    elif x == 79:
        return 79
    elif x == 80:
        return 80
    elif x == 81:
        return 81
    elif x == 82:
        return 82
    elif x == 83:
        return 83
    elif x == 84:
        return 84
    elif x == 85:
        return 85
    elif x == 86:
        return 86
    elif x == 87:
        return 87
    elif x == 88:
        return 88
    elif x == 89:
        return 89
    elif x == 90:
        return 90
    elif x == 91:
        return 91
    elif x == 92:
        return 92
    elif x == 93:
        return 93
    elif x == 94:
        return 94
    elif x == 95:
        return 95
    elif x == 96:
        return 96
    elif x == 97:
        return 97
    elif x == 98:
        return 98
    elif x == 99:
        return 99
    elif x == 100:
        return 100
    elif x == 101:
        return 101
    elif x == 102:
        return 102
    elif x == 103:
        return 103
    elif x == 104:
        return 104
    elif x == 105:
        return 105
    elif x == 106:
        return 106
    elif x == 107:
        return 107
    elif x == 108:
        return 108
    elif x == 109:
        return 109
    elif x == 110:
        return 110
    elif x == 111:
        return 111
    elif x == 112:
        return 112
    elif x == 113:
        return 113
    elif x == 114:
        return 114
    elif x == 115:
        return 115
    elif x == 116:
        return 116
    elif x == 117:
        return 117
    elif x == 118:
        return 118
    elif x == 119:
        return 119
    elif x == 120:
        return 120
    elif x == 121:
        return 121
    elif x == 122:
        return 122
    elif x == 123:
        return 123
    elif x == 124:
        return 124
    elif x == 125:
        return 125
    elif x == 126:
        return 126
    elif x == 127:
        return 127
    elif x == 128:
        return 128
    else:
        raise ValueError(x)
    

# Create a dictionary to hold references to the functions
function_registry = {}

# Define the decorator that registers each function
def register(n):
    def decorator(func):
        function_registry[n] = func
        return func
    return decorator

# Assuming the decorator `register` and the dictionary `function_registry` are already defined as shown earlier

@register(1)
def return1():
    return 1

@register(2)
def return2():
    return 2

@register(3)
def return3():
    return 3

@register(4)
def return4():
    return 4

@register(5)
def return5():
    return 5

@register(6)
def return6():
    return 6

@register(7)
def return7():
    return 7

@register(8)
def return8():
    return 8

@register(9)
def return9():
    return 9

@register(10)
def return10():
    return 10

@register(11)
def return11():
    return 11

@register(12)
def return12():
    return 12

@register(13)
def return13():
    return 13

@register(14)
def return14():
    return 14

@register(15)
def return15():
    return 15

@register(16)
def return16():
    return 16

@register(17)
def return17():
    return 17

@register(18)
def return18():
    return 18

@register(19)
def return19():
    return 19

@register(20)
def return20():
    return 20

@register(21)
def return21():
    return 21

@register(22)
def return22():
    return 22

@register(23)
def return23():
    return 23

@register(24)
def return24():
    return 24

@register(25)
def return25():
    return 25

@register(26)
def return26():
    return 26

@register(27)
def return27():
    return 27

@register(28)
def return28():
    return 28

@register(29)
def return29():
    return 29

@register(30)
def return30():
    return 30

@register(31)
def return31():
    return 31

@register(32)
def return32():
    return 32

@register(33)
def return33():
    return 33

@register(34)
def return34():
    return 34

@register(35)
def return35():
    return 35

@register(36)
def return36():
    return 36

@register(37)
def return37():
    return 37

@register(38)
def return38():
    return 38

@register(39)
def return39():
    return 39

@register(40)
def return40():
    return 40

@register(41)
def return41():
    return 41

@register(42)
def return42():
    return 42

@register(43)
def return43():
    return 43

@register(44)
def return44():
    return 44

@register(45)
def return45():
    return 45

@register(46)
def return46():
    return 46

@register(47)
def return47():
    return 47

@register(48)
def return48():
    return 48

@register(49)
def return49():
    return 49

@register(50)
def return50():
    return 50

@register(51)
def return51():
    return 51

@register(52)
def return52():
    return 52

@register(53)
def return53():
    return 53

@register(54)
def return54():
    return 54

@register(55)
def return55():
    return 55

@register(56)
def return56():
    return 56

@register(57)
def return57():
    return 57

@register(58)
def return58():
    return 58

@register(59)
def return59():
    return 59

@register(60)
def return60():
    return 60

@register(61)
def return61():
    return 61

@register(62)
def return62():
    return 62

@register(63)
def return63():
    return 63

@register(64)
def return64():
    return 64

@register(65)
def return65():
    return 65

@register(66)
def return66():
    return 66

@register(67)
def return67():
    return 67

@register(68)
def return68():
    return 68

@register(69)
def return69():
    return 69

@register(70)
def return70():
    return 70

@register(71)
def return71():
    return 71

@register(72)
def return72():
    return 72

@register(73)
def return73():
    return 73

@register(74)
def return74():
    return 74

@register(75)
def return75():
    return 75

@register(76)
def return76():
    return 76

@register(77)
def return77():
    return 77

@register(78)
def return78():
    return 78

@register(79)
def return79():
    return 79

@register(80)
def return80():
    return 80

@register(81)
def return81():
    return 81

@register(82)
def return82():
    return 82

@register(83)
def return83():
    return 83

@register(84)
def return84():
    return 84

@register(85)
def return85():
    return 85

@register(86)
def return86():
    return 86

@register(87)
def return87():
    return 87

@register(88)
def return88():
    return 88

@register(89)
def return89():
    return 89

@register(90)
def return90():
    return 90

@register(91)
def return91():
    return 91

@register(92)
def return92():
    return 92

@register(93)
def return93():
    return 93

@register(94)
def return94():
    return 94

@register(95)
def return95():
    return 95

@register(96)
def return96():
    return 96

@register(97)
def return97():
    return 97

@register(98)
def return98():
    return 98

@register(99)
def return99():
    return 99

@register(100)
def return100():
    return 100

@register(101)
def return101():
    return 101

@register(102)
def return102():
    return 102

@register(103)
def return103():
    return 103

@register(104)
def return104():
    return 104

@register(105)
def return105():
    return 105

@register(106)
def return106():
    return 106

@register(107)
def return107():
    return 107

@register(108)
def return108():
    return 108

@register(109)
def return109():
    return 109

@register(110)
def return110():
    return 110

@register(111)
def return111():
    return 111

@register(112)
def return112():
    return 112

@register(113)
def return113():
    return 113

@register(114)
def return114():
    return 114

@register(115)
def return115():
    return 115

@register(116)
def return116():
    return 116

@register(117)
def return117():
    return 117

@register(118)
def return118():
    return 118

@register(119)
def return119():
    return 119

@register(120)
def return120():
    return 120

@register(121)
def return121():
    return 121

@register(122)
def return122():
    return 122

@register(123)
def return123():
    return 123

@register(124)
def return124():
    return 124

@register(125)
def return125():
    return 125

@register(126)
def return126():
    return 126

@register(127)
def return127():
    return 127

@register(128)
def return128():
    return 128

def fancy(x):
    return function_registry[x]()


@pytest.mark.benchmark
@pytest.mark.parametrize("x", [16, 32, 64, 128])
def test_basic(benchmark, x):
    benchmark(basic, x)


@pytest.mark.benchmark
@pytest.mark.parametrize("x", [16, 32, 64, 128])
def test_fancy(benchmark, x):
    benchmark(fancy, x)

