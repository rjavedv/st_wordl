"""
19-01-2025

Utility functions for wordle solver
Testing wordle logic 

Rashid Javed
https://github.com/rjavedv
"""

##import search_dict as sd
import json


outfilename = 'words/words_sorted.json'
word_len = 5
global_list = []

def read_from_file(outfilename: str) -> dict:
    with open(outfilename, 'r') as file:
        worddict = json.load(file)    
    return worddict

def update_out_list(gsstr: str, clstr: str, outlist: list, wordlist: list, word_len: int) -> list:
    if outlist:
        local_list = outlist.copy()
    else:
        local_list = wordlist.copy()
    
    for ctr in range(word_len):
        charval = gsstr[ctr]
        charcol = clstr[ctr]
        if charcol == 'B':      #Black/grey
            local_list = delete_black_chars(charval, ctr, local_list)
        elif charcol == 'Y':     #Yellow
            local_list =  handle_yellow_chars(charval, ctr, local_list)
        elif charcol == 'G':
            local_list = handle_green_chars(charval, ctr, local_list)
        else:
            # what to do here???
            pass

    return local_list

def delete_black_chars(bcharval: str, bcharpos: int, wlist: list) -> list:
    temp_list = []
    for lword in wlist:
        try:
            dummy = lword.index(bcharval)
            temp_list.append(lword)
        except ValueError:
            pass            
    
    for tword in temp_list:
        wlist.remove(tword)
    
    return wlist

def handle_yellow_chars(ycharval: str, ycharpos: int, wlist: list) -> list:
    temp_list = []
    for lword in wlist:
        try:
            if lword[ycharpos] == ycharval or lword.count(ycharval) == 0:
                temp_list.append(lword)
        except ValueError:
            pass

    for tword in temp_list:
        wlist.remove(tword)        

    return wlist

def handle_green_chars(gcharval: str, gcharpos: int, wlist: list) -> list:
    temp_list = []
    for lword in wlist:
        try:
            if lword[gcharpos] != gcharval:
                temp_list.append(lword)
        except ValueError:
            pass
    for tword in temp_list:
        wlist.remove(tword)

    return wlist

def format_char_color(rbout: str, inp_char: str) -> str:
    lchar = inp_char.upper()
    if 'Grey' in rbout:
        clr_str = rbout.replace('Grey', lchar)
    elif 'Yellow' in rbout:
        clr_str = rbout.replace('Yellow', lchar)        
    elif 'Green' in rbout:
        clr_str = rbout.replace('Green', lchar)            
    else:
        clr_str = ''
    return clr_str

def build_clr_char(rbout: str, clrstr: str) -> str:
    clr_char = ''
    if 'Grey' in rbout:
        clr_char = 'B'
    elif 'Yellow' in rbout:
        clr_char = 'Y'
    elif 'Green' in rbout:
        clr_char = 'G'
    else:
        clr_char = ''
#   return ''.join(clrstr, clr_char)
    return clrstr + clr_char

def set_global_list(local_list: list, global_list: list) -> list:
    if local_list:
        global_list = local_list.copy()
        return global_list
    
def get_global_list(local_list: list, global_list: list) -> list:
    if global_list:
        local_list = global_list.copy()
        return local_list

def init_global_list(gl_list: list) -> list:
    gl_list.clear()
    return gl_list

def make_df_list(inp_list:list) -> list:
    row_list = []
    main_list = []
    ctr = 0
    if inp_list:
        for item in inp_list:
            row_list.append(item)
            ctr = ctr + 1
            if ctr == 5:
                main_list.append(row_list.copy())
                ctr = 0
                row_list.clear()

        if row_list:
            main_list.append(row_list)
    return main_list

def make_color_string(guess_str: str, guess_clr: str) -> str:
    ret_str = ''
    buff_str = ''
    for idx, clr in enumerate(guess_clr):
        char = guess_str[idx].upper()
        if clr == 'B':
            buff_str = ':grey[' + char + ']'
        elif clr == 'Y':
            buff_str = ':orange[' + char + ']'
        elif clr == 'G':
            buff_str = ':green[' + char + ']'            
        else:
            buff_str = ''
        ret_str = ret_str + buff_str
    return ret_str
        

## Main
if __name__ == '__main__':
    worddict = read_from_file(outfilename)
    word_len = 5
    word_list = worddict.get(str(word_len))
    out_list = []
    str_list = str()


    guess_str = 'clear'
    guess_clr = 'BBBBB'
    out_list = update_out_list(guess_str, guess_clr, out_list, word_list, word_len)
    print('OUTLIST =', out_list)

    # guess_str = 'forge'
    # guess_clr = 'YBYYY'
    # out_list = update_out_list(guess_str, guess_clr, out_list, word_list, word_len)
    # print('OUTLIST =', out_list)
    df_list = []
    df_list = make_df_list(out_list)

    print(df_list)