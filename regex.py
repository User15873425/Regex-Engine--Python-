def match_equal(rule, text):
    if rule == '':
        return True
    if text == '':
        return rule == '$'
    if rule[0] == '\\':
        rule = rule[1:]
        escape = True
    else:
        escape = False
    if len(rule) > 1:
        if rule[1] == '?':
            return match_equal(rule[2:], text) or match_equal(rule[0] + rule[2:], text)
        if rule[1] == '*':
            return match_equal(rule[2:], text) or match_equal(rule, text[1:])
        if rule[1] == '+':
            return match_equal(rule[0] + rule.replace('+', '*', 1), text)
    return match_equal(rule[1:], text[1:]) if rule[0] == text[0] or not escape and rule[0] == '.' else False


def match_unequal(rule, text):
    return match_equal(rule, text) or text != '' and match_unequal(rule, text[1:])


def match(rule, text):
    return match_equal(rule[1:], text) if rule.startswith('^') else match_unequal(rule, text)


print(match(*input().split('|')))
