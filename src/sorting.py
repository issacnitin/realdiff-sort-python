def by_priority(rules):
    return sorted(rules, key=lambda rule: rule.priority)