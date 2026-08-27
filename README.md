# RealDiff Python sort-stability demo

RealDiff runs the same tests on both sides of this pull request and reports the runtime values that changed.

## How it works

1. Check out the base and pull-request revisions.
2. Attach Python 3.12's `sys.monitoring` callbacks before either test run.
3. Run the same pytest suite on both, recording observed function arguments and return values.
4. Diff those execution traces instead of inferring behavior from the source diff.

This is not mutation testing, static analysis, or coverage. No production code or test is mutated, RealDiff does not generate tests, and it observes only code this test suite executes.

## Worked example

The pull request replaces Python's stable `sorted` call with a heap, avoiding the sorted-list path. In this block, `-` is the base, `+` is the proposal, and the important added operation is `heapq.heapify(heap)`; `_PriorityItem.__lt__` compares only priority:

```diff
-return sorted(rules, key=lambda rule: rule.priority)
+heap = [_PriorityItem(rule) for rule in rules]
+heapq.heapify(heap)
+return [heapq.heappop(heap).rule for _ in range(len(heap))]
```

Both implementations order by priority, so the edit looks like a local allocation/performance refactor. `sorted` preserves declaration order and selects `Z_CLEARANCE`. A heap does not preserve insertion order for equal keys, and this fixture deterministically selects `A_SEASONAL`.

The following block labels the exact values RealDiff observed before and after the edit:

```text
BASE  select_discount(100) -> Z_CLEARANCE
PR    select_discount(100) -> A_SEASONAL
BASE  checkout_total(100) -> (60, Z_CLEARANCE)
PR    checkout_total(100) -> (85, A_SEASONAL)
```

Neither pricing function is in the diff; only `src/sorting.py` changed. All three tests execute the path. The two broad total assertions still pass because 85 is discounted and does not exceed 100. Only `test_clearance_wins_current_ties`, which checks the exact selected code, reacts.

## Why the finding is focused

RealDiff runs the base more than once and subtracts observations that disagree with themselves, removing timestamps, GUIDs, hash-order variation, and similar self-noise.

The changed rule affects its callers, but RealDiff collapses that propagation and reports the first changed behavior in unedited `src/pricing.py`.

## Run it

The command below runs the demo's three tests:

```bash
python -m pytest
```