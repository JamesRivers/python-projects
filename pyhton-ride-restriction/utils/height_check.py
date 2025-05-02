def check_height(height):
    if height < 120:
        return "You are not allowed to ride."
    elif 120 <= height < 140:
        return "You are allowed to ride but must be accompanied by an adult."
    else:
        return "You are allowed to ride alone."