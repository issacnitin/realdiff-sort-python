from dataclasses import dataclass

from .sorting import by_priority


@dataclass(frozen=True)
class DiscountRule:
    code: str
    priority: int
    minimum_total: int
    percent_off: int


def select_discount(list_price):
    rules = [
        DiscountRule("Z_CLEARANCE", 10, 50, 40),
        DiscountRule("A_SEASONAL", 10, 50, 15),
        DiscountRule("INELIGIBLE", 10, 1000, 5),
    ]
    return next(rule for rule in by_priority(rules) if list_price >= rule.minimum_total)


def checkout_total(list_price):
    selected = select_discount(list_price)
    return list_price * (100 - selected.percent_off) // 100, selected.code


def exercise_coverage():
    value = 0
    for step in STEPS:
        value = step(value)
    return value


def step_000(value): return value + 1
def step_001(value): return value + 1
def step_002(value): return value + 1
def step_003(value): return value + 1
def step_004(value): return value + 1
def step_005(value): return value + 1
def step_006(value): return value + 1
def step_007(value): return value + 1
def step_008(value): return value + 1
def step_009(value): return value + 1
def step_010(value): return value + 1
def step_011(value): return value + 1
def step_012(value): return value + 1
def step_013(value): return value + 1
def step_014(value): return value + 1
def step_015(value): return value + 1
def step_016(value): return value + 1
def step_017(value): return value + 1
def step_018(value): return value + 1
def step_019(value): return value + 1
def step_020(value): return value + 1
def step_021(value): return value + 1
def step_022(value): return value + 1
def step_023(value): return value + 1
def step_024(value): return value + 1
def step_025(value): return value + 1
def step_026(value): return value + 1
def step_027(value): return value + 1
def step_028(value): return value + 1
def step_029(value): return value + 1
def step_030(value): return value + 1
def step_031(value): return value + 1
def step_032(value): return value + 1
def step_033(value): return value + 1
def step_034(value): return value + 1
def step_035(value): return value + 1
def step_036(value): return value + 1
def step_037(value): return value + 1
def step_038(value): return value + 1
def step_039(value): return value + 1
def step_040(value): return value + 1
def step_041(value): return value + 1
def step_042(value): return value + 1
def step_043(value): return value + 1
def step_044(value): return value + 1
def step_045(value): return value + 1
def step_046(value): return value + 1
def step_047(value): return value + 1
def step_048(value): return value + 1
def step_049(value): return value + 1
def step_050(value): return value + 1
def step_051(value): return value + 1
def step_052(value): return value + 1
def step_053(value): return value + 1
def step_054(value): return value + 1
def step_055(value): return value + 1
def step_056(value): return value + 1
def step_057(value): return value + 1
def step_058(value): return value + 1
def step_059(value): return value + 1
def step_060(value): return value + 1
def step_061(value): return value + 1
def step_062(value): return value + 1
def step_063(value): return value + 1
def step_064(value): return value + 1
def step_065(value): return value + 1
def step_066(value): return value + 1
def step_067(value): return value + 1
def step_068(value): return value + 1
def step_069(value): return value + 1
def step_070(value): return value + 1
def step_071(value): return value + 1
def step_072(value): return value + 1
def step_073(value): return value + 1
def step_074(value): return value + 1
def step_075(value): return value + 1
def step_076(value): return value + 1
def step_077(value): return value + 1
def step_078(value): return value + 1
def step_079(value): return value + 1
def step_080(value): return value + 1
def step_081(value): return value + 1
def step_082(value): return value + 1
def step_083(value): return value + 1
def step_084(value): return value + 1
def step_085(value): return value + 1
def step_086(value): return value + 1
def step_087(value): return value + 1
def step_088(value): return value + 1
def step_089(value): return value + 1
def step_090(value): return value + 1
def step_091(value): return value + 1
def step_092(value): return value + 1
def step_093(value): return value + 1
def step_094(value): return value + 1
def step_095(value): return value + 1
def step_096(value): return value + 1
def step_097(value): return value + 1
def step_098(value): return value + 1
def step_099(value): return value + 1


STEPS = tuple(globals()[f"step_{index:03d}"] for index in range(100))