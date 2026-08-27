import heapq


class _PriorityItem:
    def __init__(self, rule):
        self.rule = rule

    def __lt__(self, other):
        return self.rule.priority < other.rule.priority


def by_priority(rules):
    heap = [_PriorityItem(rule) for rule in rules]
    heapq.heapify(heap)
    return [heapq.heappop(heap).rule for _ in range(len(heap))]