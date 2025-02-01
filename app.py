"""
18-01-2025
frontend for wordle solver

Rashid Javed
https://github.com/rjavedv
"""
import streamlit as st
import wrd_lib as wl

### Set page Config
st.set_page_config(
    page_title='Wordle Helper', 
    page_icon=':brain:',
    menu_items={
        'Get Help': 'https://github.com/rjavedv/st_wordl',
        'Report a bug': 'mailto:rjaved@zoho.com',
        'About': '## Wordle Helper!  created by Rashid Javed'
    }    
    )

@st.cache_data
def get_word_dict():
    return wl.read_from_file(wl.outfilename)

worddict = get_word_dict()
word_len = wl.word_len

@st.cache_data
def get_word_list(word_len: int) -> list:
    return worddict.get(str(word_len))

word_list = get_word_list(word_len)

out_list = []
str_list = ''
last_str = ''
used_words = []
out_list = wl.get_global_list(out_list, wl.global_list)

if not 'gused_words' in st.session_state:
    st.session_state['gused_words'] = []

## these always need to initialize
df_list = []

def validate_guess_str(gsstr: str) -> bool:
    if len(gsstr) != word_len:
        return False
    return True

def validate_guess_clr(clstr: str) -> bool:
    colors = 'BYG'
    if len(clstr) != word_len:
        return False
    for char in clstr:
        if char not in colors:
            return False
    return True

def build_clr_str(rbout1: str, rbout2: str, rbout3: str, rbout4: str, rbout5: str) -> str:
    local_Str = ''

    local_Str = wl.build_clr_char(rbout1, local_Str)
    local_Str = wl.build_clr_char(rbout2, local_Str)
    local_Str = wl.build_clr_char(rbout3, local_Str)
    local_Str = wl.build_clr_char(rbout4, local_Str)        
    local_Str = wl.build_clr_char(rbout5, local_Str)    

    return local_Str

## Initialize

st.title('Wordle Helper')
st.write('Press Initialze Button to restart the App. You need to do it for a new session')
#st.write('Word Len = ', word_len)
init_app = st.button('Initialize')

if init_app:
    out_list = []
    str_list = ''
    last_str = ''
    used_words = []
    guess_str = ''
    guess_clr = ''
    wl.init_global_list(wl.global_list)
    st.session_state['gused_words'] = []
    st.session_state['rb1'] = ":grey[Grey]"
    st.session_state['rb2'] = ":grey[Grey]"
    st.session_state['rb3'] = ":grey[Grey]"
    st.session_state['rb4'] = ":grey[Grey]"
    st.session_state['rb5'] = ":grey[Grey]"            
    st.session_state['ti1'] = ""

st.divider()

### main logic of app
#st.write('Main logic part')

# clr1 = 'green'
# clr2 = 'orange'
# defclr = 'grey'
# strone = f':{clr1}[t] a :{clr2}[b] l e'
# st.subheader(strone)
# st.subheader('Color guide to fill')
# st.write("**:grey[B = Black ]**")
# st.write("**:orange[Y = Yellow ]**")
# st.write("**:green[G = Green]**")

# st.subheader('Examples : ')
# st.image('sample1.png')
# st.write('First Row: Word = CLEAR, Colors = BBYYB')
# st.write('Second Row: Word = GATED, Colors = BGBYB')
# st.write('Third Row: Word = CLEAR, Colors = GGGGG')

guess_str = st.text_input('Input word and press Enter Key to continue:',key='ti1').lower()
guess_clr = ''   #st.text_input('Enter Colors').upper()


#################################
# if guess_str:
#     for char in guess_str:
#         acol1, acol2 = st.columns([0.3,0.7])
#         formatted_str = '**' + char + '**'
#         acol1.write(formatted_str)
#         acol2.radio(label=formatted_str, options=["Grey", "Yellow", "Green"], index=0, horizontal=True)

#################################
st.write('**Choose the color for each character of the word**')
col1, col2, col3, col4, col5 = st.columns(5, border=True)
rbtitle = 'WC'
#col1, col2, col3, col4, col5 = st.columns([0.2, 0.2 ,0.2 ,0.2, 0.2], border=True, vertical_alignment="top")
with col1:
    st.write('1')
    clr1 = st.radio(
    rbtitle,
#   ["**:grey[Grey]**", "**:orange[Yellow]**", "**:green[Green]**"],
    [":grey[Grey]", ":orange[Yellow]", ":green[Green]"],    
    index=0, key='rb1', label_visibility="collapsed", horizontal=True)
    if validate_guess_str(guess_str):
        st.subheader(wl.format_char_color(clr1,guess_str[0]))  

with col2:
    st.write('2')
    clr2 = st.radio(
    rbtitle,
    [":grey[Grey]", ":orange[Yellow]", ":green[Green]"],
    index=0, key='rb2', label_visibility="collapsed", horizontal=True)
    if validate_guess_str(guess_str):
        st.subheader(wl.format_char_color(clr2,guess_str[1]))

with col3:
    st.write('3')
    clr3 = st.radio(
    rbtitle,
    [":grey[Grey]", ":orange[Yellow]", ":green[Green]"],
    index=0, key='rb3', label_visibility="collapsed", horizontal=True )
    if validate_guess_str(guess_str):
        st.subheader(wl.format_char_color(clr3,guess_str[2]))

with col4:
    st.write('4')
    clr4 = st.radio(
    rbtitle,
    [":grey[Grey]", ":orange[Yellow]", ":green[Green]"],
    index=0, key='rb4', label_visibility="collapsed", horizontal=True  )
    if validate_guess_str(guess_str):
        st.subheader(wl.format_char_color(clr4,guess_str[3]))

with col5:
    st.write('5')
    clr5 = st.radio(
    rbtitle,
    [":grey[Grey]", ":orange[Yellow]", ":green[Green]"],
    index=0, key='rb5', label_visibility="collapsed", horizontal=True  )
    if validate_guess_str(guess_str):
        st.subheader(wl.format_char_color(clr5,guess_str[4]))

guess_clr = build_clr_str(clr1, clr2, clr3, clr4, clr5)

submit_btn = st.button('Submit')

if submit_btn:
    if validate_guess_str(guess_str) and validate_guess_clr(guess_clr):
        #st.write(guess_str)
        #st.write(guess_clr)
        out_list = wl.update_out_list(guess_str, guess_clr, out_list, word_list, word_len)
        if out_list:
            str_list = ' ,'.join(out_list)
            df_list = wl.make_df_list(out_list)
            wl.global_list = wl.set_global_list(out_list, wl.global_list)
            last_str = wl.make_color_string(guess_str, guess_clr)
            used_words = st.session_state.gused_words
            used_words.append(last_str)
            st.session_state.gused_words = used_words.copy()
        else:
            wl.init_global_list(wl.global_list)
    else:
        st.write('Validate error in above input')    


#st.write('guess_clr=',guess_clr)
#st.write('guess_str=',guess_str)
st.write('Words already used:')
used_words = st.session_state['gused_words']
for word in used_words:
    st.subheader(word)

### output
#st.write('output part')
#st.divider()
# st.write(str_list)
#st.write(out_list)

# st.dataframe(df_list)    #, columns=("col %d" % i for i in range(5)))

st.divider()
st.write('**Suggested Word List:**')
#st.write(st.session_state)
st.table(df_list)
st.divider()

st.write('*:blue[Developed By: Rashid Javed]*')
