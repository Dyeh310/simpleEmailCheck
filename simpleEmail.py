def emailCheck(email):
    com = ''
    if len(email) > 30:
        return False
    for i in range (0, len(email)):
        if '@' not in email:
            return False
    if '.com' in email:
        return True
    else:
        return False


while (True):
    print('Please enter your email (no more than 30 characters)')
    email = input()
    if emailCheck(email) == False:
        print('That is not correct')
    else:
        print('That is correct')
        break

