def alphabet_position(letter):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    Caps="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    position=0
    for i in range(0,len(alphabet)):
        if alphabet[i]==letter:
            position=i
        if Caps[i]==letter:
            position=i
    return position

def rotate_character(char,rot):
    result=''
    if char.isalpha() is False:
        result=char
        return result
    start=alphabet_position(char)
    rotation=start+rot
    if rotation>25:
        rotation=rotation%26
    else:
        rotation=rotation
    rot_alpha="abcdefghijklmnopqrstuvwxyz"
    result=rot_alpha[rotation]
    if char.isupper():
        result=result.upper()
    return result


def encrypt(text,rot):
    encrypted_string=''
    for i in text:
        shifted=rotate_character(i,int(rot))
        encrypted_string+=shifted
    return encrypted_string
