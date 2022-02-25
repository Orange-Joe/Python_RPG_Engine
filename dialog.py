import os
import sys
import colorama
import time
from collections import deque
import cursor

__author__ = "Orange-Joe"
__copyright__ = "Orange-Joe"
__version__ =  "1.0"

"""
This module has various functions pertaining to how various strings are printed in the terminal. For example, there is a settings function that allows
the user to select what colors will be used by the program. There are functions for printing out options, such as dialog choices, to the player, what
colors will be used when printing character dialog, and more. Some of the functions are for experimental purposes and may be best used from within the 
interpreter.
"""

# Foreground colors defined here in variables with shorter names for ease of coding. 
black = colorama.Fore.BLACK
red = colorama.Fore.RED
blue = colorama.Fore.BLUE
green = colorama.Fore.GREEN
yellow = colorama.Fore.YELLOW
cyan = colorama.Fore.CYAN
white = colorama.Fore.WHITE
magenta = colorama.Fore.MAGENTA
dim = colorama.Style.DIM
bright = colorama.Style.BRIGHT
normal = colorama.Style.NORMAL


# Background colors defined here in variables with shorter names for ease of coding.
bblack = colorama.Back.BLACK
bred = colorama.Back.RED
bblue = colorama.Back.BLUE
bgreen = colorama.Back.GREEN
byellow = colorama.Back.YELLOW
bcyan = colorama.Back.CYAN
bwhite = colorama.Back.WHITE
bmagenta = colorama.Back.MAGENTA
reset = colorama.Style.RESET_ALL

# Set automatic color reset. 
colorama.init(autoreset=True)


class Dialog:

    # 'Custom' determines whether or not to use user-generated chat.
    player_customized = False
    options_color = black + bright # Default options color
    description_color = blue + bright # Default description color
    chat_color = green
    choice_color = blue


    # Dictionary available colors available to the user. Called by interactive settings() function.
    colors = {'black': black + bright, 'red1': red + dim, 'red2': red, 'red': red,
    'red3': red + bright, 'green1': green + dim, 'green2': green, 'green3': green + bright, 'green': green,
    'yellow1': yellow + dim, 'yellow2': yellow, 'yellow3': yellow + bright, 'yellow': yellow,
    'normal2': normal + dim, 'normal2': normal, 'normal3': normal + bright, 'normal': normal,
    'blue1': blue + dim, 'blue2': blue, 'blue3': blue + bright, 'blue': blue,
    'magenta1': magenta + dim, 'magenta2': magenta, 'magenta3': magenta + bright, 'magenta': magenta,
    'cyan1': cyan + dim, 'cyan2': cyan, 'cyan3': cyan + bright, 'cyan': cyan,
    'white1,': white + dim, 'white2': white, 'white3': white + bright, 'white': white,
    'dim': dim, 'bblick': bblack, 'bred': bred, 'bgreen':bgreen, 'byellow':byellow, 'bblue':bblue, 'bmagenta':bmagenta, 'cyan':bcyan,'bwhite':bwhite, 'bright':bright}
  
    colors_list = [black + bright, red + dim, red, red + bright, green + dim, green, green + bright, yellow + dim, yellow, yellow + bright, normal + dim, normal, normal + bright, blue + dim, blue, blue + bright, magenta + dim, magenta, magenta + bright, cyan + dim, cyan, cyan + bright, white + dim, white, white + bright]

    # background_colors = [bblack, bred, bblue, bgreen, byellow, bmagenta, bcyan, bwhite] --- keeping this commented out for now. May implement later.


    # Various options for what determine a 'yes' or 'no' response during player prompts. 
    yes = ['1', 'y', 'yes', 'si', 'yeah', "let's do it", "go", "get on with it",
    "vamanos", "yah", 'ye', 'forward!', 'affirmative', 'yes please',
    'please and thank you', 'very much',
    'very much so', "yes, let's go!", 'sure']

    no = ['2', 'n', 'no', 'nah', 'no thanks', 'nope', 'get out of here',
    "i dont think so", "i don't think so"]

    done = ['done', 'quit', 'esc', 'b', 'q']


# This is an interactive function that allows the player to set up a custom color scheme for dialog options. 
# To see it in action, run python3 -i dialog.py in proper directory and call the function with Dialog.settings()
    def settings():

        response = ""

        os.system('clear')

        options = {"[1] ": "'Customize' color scheme", "[2] ": "'Return' settings to defaults", "[3] ":"'Back' to the main menu"}
    
        Dialog.default_dictionary(options)

        choice = input(":: ")

        if choice.lower() in ['3', 'back']:
            pass

        elif choice.lower() in ['', 'return', 'default']:

            Dialog.player_customized = False

            time.sleep(1)

            Dialog.settings()
            

        elif choice.lower() in ['1', 'customize']:

            Dialog.player_customized = True

            os.system('clear')

            sys.stdout.write(black + bright + '[Black]  ')
            sys.stdout.write(red + dim + '[Red1]   ')
            sys.stdout.write(red + '[Red2]  ')
            sys.stdout.write(red + bright  + '[Red3]\n')
            sys.stdout.write(green + dim + '[Green1]    ')
            sys.stdout.write(green + '[Green2]    ')
            sys.stdout.write(green + bright + '[Green3]\n')
            sys.stdout.write(yellow + dim + '[Yellow1]  ')
            sys.stdout.write(yellow + '[Yellow2]   ')
            sys.stdout.write(yellow + bright +  '[Yellow3]\n')
            sys.stdout.write(normal + dim  + '[Normal1]  ')
            sys.stdout.write(normal + '[Normal2]   ')
            sys.stdout.write(normal + bright + '[Normal3]\n')
            sys.stdout.write(blue + dim + '[Blue1]      ')
            sys.stdout.write(blue + '[Blue2]     ')
            sys.stdout.write(blue + bright + '[Blue3]\n')
            sys.stdout.write(magenta + dim + '[Magenta1] ')
            sys.stdout.write(magenta + '[Magenta2] ')
            sys.stdout.write(magenta + bright + '[Magenta3]\n')
            sys.stdout.write(cyan + dim +  '[Cyan1]      ')
            sys.stdout.write(cyan + '[Cyan2]     ')
            sys.stdout.write(cyan + bright +  '[Cyan3]\n')
            sys.stdout.write(white + dim + '[White1]    ')
            sys.stdout.write(white + '[White2]    ')
            sys.stdout.write(white + bright + '[White3]\n\n')

            choice = input("Choose your [option] color (ex: blue1).\n\n")
            print("\r")


            for choices, color in Dialog.colors.items():
                if choice in choices:
                    Dialog.options_color = color
                

            choice = input("\nChoose your 'description' color (ex: magenta1).\n\n")

            for choices, color in Dialog.colors.items():
                if choice in choices:
                    Dialog.description_color = color


            os.system('clear')

            Dialog.chat("Sample interface:", Dialog.description_color)

            choice_list = {"[Magic]: ": "Attack with magic", "[Meele]: ": "Attack with meele", "[Potions]: ": "Browse potions"}

            Dialog.default_dictionary(choice_list)
            time.sleep(.05)

            Dialog.chat("Are you okay with this choice?", Dialog.description_color)
               
            choice = input(":: " )
            if choice in Dialog.yes:
                pass

            elif choice in Dialog.no:

                Dialog.player_customized = False

                Dialog.settings()


# Simplified character dialog option. Example output: [Player] Let's continue.
    def char_talk(name, text):
        Dialog.default(f"[{name}] {text}")


    # Print choices for the user to make in dictionary key, value format.   
    # If the player has not customized their colors, the function 'standard dictionary' will be called. I know, the function names don't make sense. 
    def default_dictionary(choices_dict):

        if Dialog.player_customized is False:
            
            Dialog.standard_dictionary(choices_dict)

        elif Dialog.player_customized is True:

            for options, description in choices_dict.items():
                
                for c in options:
                    
                    sys.stdout.write(Dialog.options_color + c)
                    sys.stdout.flush()

                sys.stdout.write(" ")
                
                for c in description:

                    sys.stdout.write(Dialog.description_color + c)
                    sys.stdout.flush()

                print("")
            print("")
    
    
    # Player choices will be printed in black+bright and blue+bright if player does not set custom options. 
    def standard_dictionary(choices_dict):

        for option, description in choices_dict.items():

            for c in option:

                sys.stdout.write(black+bright + c)
                sys.stdout.flush()

            sys.stdout.write(" ")

            for c in description:

                sys.stdout.write(blue + bright + c)
                sys.stdout.flush()
            print("")
    
        print("")


    # Choose your own colors for dictionary menus. Used in code when you don't want to use the default or standard options.
    def dictionary_choices(choices_dict, options_color, description_color):

        #Iterates through the passed dictionary and prints options and descriptions with defined color variables.  
        for options, description in choices_dict.items():

            #'c' stands for characters.
            for c in options:
                sys.stdout.write(options_color + c)
                sys.stdout.flush()
                time.sleep(.025)

            for c in description:
                sys.stdout.write(description_color + c)
                sys.stdout.flush()
                time.sleep(.025)

            print("\n")


    # Print a list with either the standard or player-defaulted color. 
    def default_list(list):
        
        for text in list:
            for c in text:
                sys.stdout.write(Dialog.description_color + c)
                sys.stdout.flush()

            print("\n")


    # Choose your own colors for list menus on a case-by-case basis.
    def list_display(list, description_color):

        #Same as above but processes a list with a single defined color Colorama variable.
        for text in list:
            for c in text:
                sys.stdout.write(description_color + c)
                sys.stdout.flush()
                time.sleep(.025)

            print("\n")


    # Print a string with the standard or player-defaulted color. 
    def default(text):
        for c in text:
            sys.stdout.write(Dialog.description_color + c)
            sys.stdout.flush()

        print("\n")


    # Print a string with your chosen color. Output is incremented by .025 of a second by default. 
    def chat(text, text_color):

        for c in text:
            sys.stdout.write(text_color + c)
            sys.stdout.flush()
            time.sleep(.025)

        print("\n")


    # nl = 'newline'. Choose your own color for text with no new line statement at the end. Must enter '\n' in text. Output incremented by .025 of a second.
    def chat_no_nl(text, text_color):

        for c in text:
            sys.stdout.write(text_color + c)
            sys.stdout.flush()
            time.sleep(.025)


    # Similar to 'chat' function, but output is not incremented.
    def quick_chat(text, text_color):
        
        for c in text:
            sys.stdout.write(text_color + c)
            sys.stdout.flush()

        print("\n")


    # Same as above but will not print a new line. 
    def qc_no_nl(text, text_color):

        for c in text:
            sys.stdout.write(text_color + c)
            sys.stdout.flush()


# Function that sets a delay before next action is performed.
def zzz(sleep_time):
    time.sleep(sleep_time)


# Print possible colors.
def possible_colors():
    sys.stdout.write(black + bright + '[Black]  ')
    sys.stdout.write(red + dim + '[Red1]   ')
    sys.stdout.write(red + '[Red2]  ')
    sys.stdout.write(red + bright  + '[Red3]\n')
    sys.stdout.write(green + dim + '[Green1]    ')
    sys.stdout.write(green + '[Green2]    ')
    sys.stdout.write(green + bright + '[Green3]\n')
    sys.stdout.write(yellow + dim + '[Yellow1]  ')
    sys.stdout.write(yellow + '[Yellow2]   ')
    sys.stdout.write(yellow + bright +  '[Yellow3]\n')
    sys.stdout.write(normal + dim  + '[Normal1]  ')
    sys.stdout.write(normal + '[Normal2]   ')
    sys.stdout.write(normal + bright + '[Normal3]\n')
    sys.stdout.write(blue + dim + '[Blue1]      ')
    sys.stdout.write(blue + '[Blue2]     ')
    sys.stdout.write(blue + bright + '[Blue3]\n')
    sys.stdout.write(magenta + dim + '[Magenta1] ')
    sys.stdout.write(magenta + '[Magenta2] ')
    sys.stdout.write(magenta + bright + '[Magenta3]\n')
    sys.stdout.write(cyan + dim +  '[Cyan1]      ')
    sys.stdout.write(cyan + '[Cyan2]     ')
    sys.stdout.write(cyan + bright +  '[Cyan3]\n')
    sys.stdout.write(white + dim + '[White1]    ')
    sys.stdout.write(white + '[White2]    ')
    sys.stdout.write(white + bright + '[White3]\n\n')


# Using the arrow variable in the charset_colors function creates a nice looking visual effect.
arrow = ['⟿','⟿','⟿','⟿','⟿','⟿','⟿','⟿','⟿','⟿','⟿','⟿','⟿','⟿','⟿','⟿','⟿','⟿','⟿','⟿','⟿','⟿','⟿','⟿']
def charset_colors(set):
    cursor.hide()
    for i in range(10000000):
        Dialog.colors_list = deque(Dialog.colors_list)
        Dialog.colors_list.rotate(1)
        Dialog.colors_list = deque(Dialog.colors_list)
        for i in set:
            for color in Dialog.colors_list:
                sys.stdout.write(color + i)
                sys.stdout.flush()
            time.sleep(.01)
            os.system('clear')    
    cursor.show()


# Print a list of map objects (unicode characters) with suggested uses.
def map_objects():

    objects = {'▩': 'For storing items or plundering loot. Perhaps full of surprises?',
'☤': 'A place for healing.', '☘': 'Want to pick up herbalism?',
'⚱': 'If this were Skyrim there would definitely be gold', '♨': "What's cookin', doc?",
'♂, ♀': "Choose your character's gender.", "✍": 'Write a note in your journal.', '☮': 'Choose peace.', '⚔': 'Choose violence.',
'☢': "Choose the 'nuclear' option.", '☯': 'Choose balance',
'☕': 'Drink some tea.', '⌛': 'Wait.', '⚡': 'Lightning magic',
'☠': 'Death, danger, poison?', '∢, ∡': 'Chart course', "⦵": 'Create roation effect with this and similar options.', '⦸': "Create rotation effect with this and similar options.", "◵, ◴, ◶, ◷": 'And these.', '⥀': 'Undo last map change.', '⥁': 'Redo last map change.', '⌕': 'Examine.'}
    
    for key, item in objects.items():
        sys.stdout.write('   ' + key + '  ::  '+ item + '\n')


# Function that prints a rotating timer.
def timer():
    cursor.hide()
    while True:
        clock = ['◴',  '◷', '◶', '◵']
        for i in clock:
            print(i)
            time.sleep(.5)
            os.system('clear')
command = 'dblue + K'


def check(r):
    indices = []
    if ' ' in r:
        print('space found in command')
        while ' ' in r:
            r = list(r)
            r.remove(' ')
            r = ''.join(r)
    print(r)
    while '+' in r:
        check = r.find('+')
        print(check)
        if check != -1:
            "'+' found in command"
            indices.append(check)
            print(indices)
            r_list = list(r.strip(''))
            r_list.pop(check)
            r = ''.join(r_list)
        print(r)
    return r


# Non-comprehensive list of unicode characters. Can be useful to print these in interpreter mode when map building. 
charset = ['૱', '꠸', '┯', '┰', '┱', '┲', '❗', '►', '◄', 'Ă', 'ă', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Ǖ', 'ǖ', 'Ꞁ', '¤', '\xad', 'Ð', '¢', '℥', 'Ω', '℧', 'K', 'ℶ', 'ℷ', 'ℸ', 'ⅇ', '⅊', '⚌', '⚍', '⚎', '⚏', '⚭', '⚮', '⌀', '⏑', '⏒', '⏓', '⏔', '⏕', '⏖', '⏗', '⏘', '⏙', '⏠', '⏡', '⏦', 'ᶀ', 'ᶁ', 'ᶂ', 'ᶃ', 'ᶄ', 'ᶆ', 'ᶇ', 'ᶈ', 'ᶉ', 'ᶊ', 'ᶋ', 'ᶌ', 'ᶍ', 'ᶎ', 'ᶏ', 'ᶐ', 'ᶑ', 'ᶒ', 'ᶓ', 'ᶔ', 'ᶕ', 'ᶖ', 'ᶗ', 'ᶘ', 'ᶙ', 'ᶚ', 'ᶸ', 'ᵯ', 'ᵰ', 'ᵴ', 'ᵶ', 'ᵹ', 'ᵼ', 'ᵽ', 'ᵾ', 'ᵿ', '\u2000', '\u2001', '\u200c', '\u200d', '\u200e', '\u200f', '\u202f', '⁁', '⁊', '\u205f', '\u206a', '\u206b', '\u206c', '\u206d', '\u206e', '\u206f', '⸜', '⸝', '¶', '¥', '£', '⅕', '⅙', '⅛', '⅔', '⅖', '⅗', '⅘', '⅜', '⅚', '⅐', '⅝', '↉', '⅓', '⅑', '⅒', '⅞', '←', '↑', '→', '↓', '↔', '↕', '↖', '↗', '↘', '↙', '↚', '↛', '↜', '↝', '↞', '↟', '↠', '↡', '↢', '↣', '↤', '↥', '↦', '↧', '↨', '↩', '↪', '↫', '↬', '↭', '↮', '↯', '↰', '↱', '↲', '↳', '↴', '↵', '↶', '↷', '↸', '↹', '↺', '↻', '↼', '↽', '↾', '↿', '⇀', '⇁', '⇂', '⇃', '⇄', '⇅', '⇆', '⇇', '⇈', '⇉', '⇊', '⇋', '⇌', '⇍', '⇎', '⇏', '⇐', '⇑', '⇒', '⇓', '⇔', '⇕', '⇖', '⇗', '⇘', '⇙', '⇚', '⇛', '⇜', '⇝', '⇞', '⇟', '⇠', '⇡', '⇢', '⇣', '⇤', '⇥', '⇦', '⇨', '⇩', '⇪', '⇧', '⇫', '⇬', '⇭', '⇮', '⇯', '⇰', '⇱', '⇲', '⇳', '⇴', '⇵', '⇶', '⇷', '⇸', '⇹', '⇺', '⇻', '⇼', '⇽', '⇾', '⇿', '⟰', '⟱', '⟲', '⟳', '⟴', '⟵', '⟶', '⟷', '⟸', '⟹', '⟺', '⟻', '⟼', '⟽', '⟾', '⟿', '⤀', '⤁', '⤂', '⤃', '⤄', '⤅', '⤆', '⤇', '⤈', '⤉', '⤊', '⤋', '⤌', '⤍', '⤎', '⤏', '⤐', '⤑', '⤒', '⤓', '⤔', '⤕', '⤖', '⤗', '⤘', '⤙', '⤚', '⤛', '⤜', '⤝', '⤞', '⤟', '⤠', '⤡', '⤢', '⤣', '⤤', '⤥', '⤦', '⤧', '⤨', '⤩', '⤪', '⤫', '⤬', '⤭', '⤮', '⤯', '⤰', '⤱', '⤲', '⤳', '⤴', '⤵', '⤶', '⤷', '⤸', '⤹', '⤺', '⤻', '⤼', '⤽', '⤾', '⤿', '⥀', '⥁', '⥂', '⥃', '⥄', '⥅', '⥆', '⥇', '⥈', '⥉', '⥊', '⥋', '⥌', '⥍', '⥎', '⥏', '⥐', '⥑', '⥒', '⥓', '⥔', '⥕', '⥖', '⥗', '⥘', '⥙', '⥚', '⥛', '⥜', '⥝', '⥞', '⥟', '⥠', '⥡', '⥢', '⥣', '⥤', '⥥', '⥦', '⥧', '⥨', '⥩', '⥪', '⥫', '⥬', '⥭', '⥮', '⥯', '⥰', '⥱', '⥲', '⥳', '⥴', '⥵', '⥶', '⥷', '⥸', '⥹', '⥺', '⥻', '⥼', '⥽', '⥾', '⥿', '➔', '➘', '➙', '➚', '➛', '➜', '➝', '➞', '➝', '➞', '➟', '➠', '➡', '➢', '➣', '➤', '➥', '➦', '➧', '➨', '➩', '➩', '➪', '➫', '➬', '➭', '➮', '➯', '➱', '➲', '➳', '➴', '➵', '➶', '➷', '➸', '➹', '➺', '➻', '➼', '➽', '➾', '⬀', '⬁', '⬂', '⬃', '⬄', '⬅', '⬆', '⬇', '⬈', '⬉', '⬊', '⬋', '⬌', '⬍', '⬎', '⬏', '⬐', '⬑', '☇', '☈', '⏎', '⍃', '⍄', '⍅', '⍆', '⍇', '⍈', '⍐', '⍗', '⍌', '⍓', '⍍', '⍔', '⍏', '⍖', '♾', '⎌', '☊', '☋', '☌', '☍', '⌃', '⌄', '⌤', '⌅', '⌆', '⌇', '⚋', '⚊', '⌌', '⌍', '⌎', '⌏', '⌐', '⌑', '⌔', '⌕', '⌗', '⌙', '⌢', '⌣', '⌯', '⌬', '⌭', '⌮', '⌖', '⌰', '⌱', '⌲', '⌳', '⌴', '⌵', '⌶', '⌷', '⌸', '⌹', '⌺', '⌻', '⌼', '⍯', '⍰', '⌽', '⌾', '⌿', '⍀', '⍁', '⍂', '⍉', '⍊', '⍋', '⍎', '⍏', '⍑', '⍒', '⍕', '⍖', '⍘', '⍙', '⍚', '⍛', '⍜', '⍝', '⍞', '⍠', '⍟', '⍡', '⍢', '⍣', '⍤', '⍥', '⍨', '⍩', '⍦', '⍧', '⍬', '⍿', '⍪', '⍮', '⍫', '⍱', '⍲', '⍭', '⍳', '⍴', '⍵', '⍶', '⍷', '⍸', '⍹', '⍺', '⍼', '⍽', '⍾', '⎀', '⎁', '⎂', '⎃', '⎄', '⎅', '⎆', '⎉', '⎊', '⎋', '⎍', '⎎', '⎏', '⎐', '⎑', '⎒', '⎓', '⎔', '⎕', '⏣', '⌓', '⏥', '⏢', '⎖', '⎲', '⎳', '⎴', '⎵', '⎶', '⎸', '⎹', '⎺', '⎻', '⎼', '⎽', '⎾', '⎿', '⏀', '⏁', '⏂', '⏃', '⏄', '⏅', '⏆', '⏇', '⏈', '⏉', '⏉', '⏋', '⏌', '⏍', '⏐', '⏤', '⏚', '⏛', 'Ⓝ', 'ℰ', 'ⓦ', '!', '\u2003', '\u2003', '\u2003', '⌘', '«', '»', '‹', '›', '‘', '’', '“', '”', '„', '‚', '❝', '❞', '£', '¥', '€', '$', '¢', '¬', '¶', '@', '§', '®', '©', '™', '°', '×', 'π', '±', '√', '‰', 'Ω', '∞', '≈', '÷', '~', '≠', '¹', '²', '³', '½', '¼', '¾', '‐', '–', '—', '|', '⁄', '\\', '[', ']', '{', '}', '†', '‡', '…', '·', '•', '●', '\uf8ff', '⌥', '⌃', '⇧', '↩', '¡', '¿', '‽', '⁂', '∴', '∵', '◊', '※', '←', '→', '↑', '↓', '☜', '☞', '☝', '☟', '✔', '★', '☆', '♺', '☼', '☂', '☺', '☹', '☃', '✉', '✿', '✄', '✈', '✌', '✎', '♠', '♦', '♣', '♥', '♪', '♫', '♯', '♀', '♂', 'α', 'ß', 'Á', 'á', 'À', 'à', 'Å', 'å', 'Ä', 'ä', 'Æ', 'æ', 'Ç', 'ç', 'É', 'é', 'È', 'è', 'Ê', 'ê', 'Í', 'í', 'Ì', 'ì', 'Î', 'î', 'Ñ', 'ñ', 'Ó', 'ó', 'Ò', 'ò', 'Ô', 'ô', 'Ö', 'ö', 'Ø', 'ø', 'Ú', 'ú', 'Ù', 'ù', 'Ü', 'ü', 'Ž', 'ž', '₳', '฿', '￠', '€', '₡', '¢', '₢', '₵', '₫', '￡', '£', '₤', '₣', 'ƒ', '₲', '₭', '₥', '₦', '₱', '＄', '$', '₮', '₩', '￦', '¥', '￥', '₴', '₰', '¤', '៛', '₪', '₯', '₠', '₧', '₨', '௹', '﷼', '㍐', '৲', '৳', '~', 'ƻ', 'Ƽ', 'ƽ', '¹', '¸', '¬', '¨', 'ɂ', 'ǁ', '¯', 'Ɂ', 'ǂ', '¡', '´', '°', 'ꟾ', '¦', '}', '{', '|', '.', ',', '·', ']', ')', '[', '/', '_', '\\', '¿', 'º', '§', '"', '*', '-', '+', '(', '!', '&', '%', '$', '¼', '¾', '½', '¶', '©', '®', '@', 'ẟ', 'Ɀ', '`', 'Ȿ', '^', '꜠', '꜡', 'ỻ', "'", '=', ':', ';', '<', 'ꞌ', 'Ꞌ', '꞊', 'ꞁ', 'ꞈ', '꞉', '>', '?', '÷', 'ℾ', 'ℿ', '℔', '℩', '℉', '⅀', '℈', 'þ', 'ð', 'Þ', 'µ', 'ª', 'ꝋ', 'ꜿ', 'Ꜿ', 'ⱽ', 'ⱺ', 'ⱹ', 'ⱷ', 'ⱶ', 'Ⱶ', 'ⱴ', 'ⱱ', 'Ɒ', 'ⱦ', 'ȶ', 'ȴ', 'ȣ', 'Ȣ', 'ȡ', 'ȝ', 'Ȝ', 'ț', 'ȋ', 'Ȋ', 'ȉ', 'Ȉ', 'ǯ', 'Ǯ', 'ǃ', 'ǀ', 'ƿ', 'ƾ', 'ƺ', 'ƹ', 'Ƹ', 'Ʒ', 'Ʋ', 'ư', 'ƪ', 'ƣ', 'Ƣ', 'Ɵ', 'ƛ', 'Ɩ', 'ƕ', 'ƍ', 'ſ', 'ỽ', '⸀', '⸁', '⸂', '⸃', '⸄', '⸅', '⸆', '⸇', '⸈', '⸉', '⸊', '⸋', '⸌', '⸍', '⸎', '⸏', '⸐', '⸑', '⸒', '⸔', '⸕', '▲', '▼', '◀', '▶', '◢', '◣', '◥', '◤', '△', '▽', '◿', '◺', '◹', '◸', '▴', '▾', '◂', '▸', '▵', '▿', '◃', '▹', '◁', '▷', '◅', '▻', '◬', '⟁', '⧋', '⧊', '⊿', '∆', '∇', '◭', '◮', '⧩', '⧨', '⌔', '⟐', '◇', '◆', '◈', '⬖', '⬗', '⬘', '⬙', '⬠', '⬡', '⎔', '⋄', '◊', '⧫', '⬢', '⬣', '▰', '▪', '◼', '▮', '◾', '▗', '▖', '■', '∎', '▃', '▄', '▅', '▆', '▇', '█', '▌', '▐', '▍', '▎', '▉', '▊', '▋', '❘', '❙', '❚', '▀', '▘', '▝', '▙', '▚', '▛', '▜', '▟', '▞', '░', '▒', '▓', '▂', '▁', '▬', '▔', '▫', '▯', '▭', '▱', '◽', '□', '◻', '▢', '⊞', '⊡', '⊟', '⊠', '▣', '▤', '▥', '▦', '⬚', '▧', '▨', '▩', '⬓', '◧', '⬒', '◨', '◩', '◪', '⬔', '⬕', '❏', '❐', '❑', '❒', '⧈', '◰', '◱', '◳', '◲', '◫', '⧇', '⧅', '⧄', '⍁', '⍂', '⟡', '⧉', '⚬', '○', '⚪', '◌', '◍', '◎', '◯', '❍', '◉', '⦾', '⊙', '⦿', '⊜', '⊖', '⊘', '⊚', '⊛', '⊝', '●', '⚫', '⦁', '◐', '◑', '◒', '◓', '◔', '◕', '⦶', '⦸', '◵', '◴', '◶', '◷', '⊕', '⊗', '⦇', '⦈', '⦉', '⦊', '❨', '❩', '⸨', '⸩', '◖', '◗', '❪', '❫', '❮', '❯', '❬', '❭', '❰', '❱', '⊏', '⊐', '⊑', '⊒', '◘', '◙', '◚', '◛', '◜', '◝', '◞', '◟', '◠', '◡', '⋒', '⋓', '⋐', '⋑', '╰', '╮', '╭', '╯', '⌒', '╳', '✕', '╱', '╲', '⧸', '⧹', '⌓', '◦', '❖', '✖', '✚', '✜', '⧓', '⧗', '⧑', '⧒', '⧖', '_', '⚊', '╴', '╼', '╾', '‐', '⁃', '‑', '‒', '-', '–', '⎯', '—', '―', '╶', '╺', '╸', '─', '━', '┄', '┅', '┈', '┉', '╌', '╍', '═', '≣', '≡', '☰', '☱', '☲', '☳', '☴', '☵', '☶', '☷', '╵', '╷', '╹', '╻', '│', '▕', '▏', '┃', '┆', '┇', '┊', '╎', '┋', '╿', '╽', '┌', '┍', '┎', '┏', '┐', '┑', '┒', '┓', '└', '┕', '┖', '┗', '┘', '┙', '┚', '┛', '├', '┝', '┞', '┟', '┠', '┡', '┢', '┣', '┤', '┥', '┦', '┧', '┨', '┩', '┪', '┫', '┬', '┭', '┮', '┳', '┴', '┵', '┶', '┷', '┸', '┹', '┺', '┻', '┼', '┽', '┾', '┿', '╀', '╁', '╂', '╃', '╄', '╅', '╆', '╇', '╈', '╉', '╊', '╋', '╏', '║', '╔', '╒', '╓', '╕', '╖', '╗', '╚', '╘', '╙', '╛', '╜', '╝', '╞', '╟', '╠', '╡', '╢', '╣', '╤', '╥', '╦', '╧', '╨', '╩', '╪', '╫', '╬', '⌞', '⌟', '⌜', '⌝', '⌊', '⌋', '⌉', '⌈', '⌋', '₯', 'ἀ', 'ἁ', 'ἂ', 'ἃ', 'ἄ', 'ἅ', 'ἆ', 'ἇ', 'Ἀ', 'Ἁ', 'Ἂ', 'Ἃ', 'Ἄ', 'Ἅ', 'Ἆ', 'Ἇ', 'ἐ', 'ἑ', 'ἒ', 'ἓ', 'ἔ', 'ἕ', 'Ἐ', 'Ἑ', 'Ἒ', 'Ἓ', 'Ἔ', 'Ἕ', 'ἠ', 'ἡ', 'ἢ', 'ἣ', 'ἤ', 'ἥ', 'ἦ', 'ἧ', 'Ἠ', 'Ἡ', 'Ἢ', 'Ἣ', 'Ἤ', 'Ἥ', 'Ἦ', 'Ἧ', 'ἰ', 'ἱ', 'ἲ', 'ἳ', 'ἴ', 'ἵ', 'ἶ', 'ἷ', 'Ἰ', 'Ἱ', 'Ἲ', 'Ἳ', 'Ἴ', 'Ἵ', 'Ἶ', 'Ἷ', 'ὀ', 'ὁ', 'ὂ', 'ὃ', 'ὄ', 'ὅ', 'Ὀ', 'Ὁ', 'Ὂ', 'Ὃ', 'Ὄ', 'Ὅ', 'ὐ', 'ὑ', 'ὒ', 'ὓ', 'ὔ', 'ὕ', 'ὖ', 'ὗ', 'Ὑ', 'Ὓ', 'Ὕ', 'Ὗ', 'ὠ', 'ὡ', 'ὢ', 'ὣ', 'ὤ', 'ὥ', 'ὦ', 'ὧ', 'Ὠ', 'Ὡ', 'Ὢ', 'Ὣ', 'Ὤ', 'Ὥ', 'Ὦ', 'Ὧ', 'ὰ', 'ά', 'ὲ', 'έ', 'ὴ', 'ή', 'ὶ', 'ί', 'ὸ', 'ό', 'ὺ', 'ύ', 'ὼ', 'ώ', 'ᾀ', 'ᾁ', 'ᾂ', 'ᾃ', 'ᾄ', 'ᾅ', 'ᾆ', 'ᾇ', 'ᾈ', 'ᾉ', 'ᾊ', 'ᾋ', 'ᾌ', 'ᾍ', 'ᾎ', 'ᾏ', 'ᾐ', 'ᾑ', 'ᾒ', 'ᾓ', 'ᾔ', 'ᾕ', 'ᾖ', 'ᾗ', 'ᾘ', 'ᾙ', 'ᾚ', 'ᾛ', 'ᾜ', 'ᾝ', 'ᾞ', 'ᾟ', 'ᾠ', 'ᾡ', 'ᾢ', 'ᾣ', 'ᾤ', 'ᾥ', 'ᾦ', 'ᾧ', 'ᾨ', 'ᾩ', 'ᾪ', 'ᾫ', 'ᾬ', 'ᾭ', 'ᾮ', 'ᾯ', 'ᾰ', 'ᾱ', 'ᾲ', 'ᾳ', 'ᾴ', 'ᾶ', 'ᾷ', 'Ᾰ', 'Ᾱ', 'Ὰ', 'Ά', 'ᾼ', '᾽', 'ι', '᾿', '῀', '῁', 'ῂ', 'ῃ', 'ῄ', 'ῆ', 'ῇ', 'Ὲ', 'Έ', 'Ὴ', 'Ή', 'ῌ', '῍', '῎', '῏', 'ῐ', 'ῑ', 'ῒ', 'ΐ', 'ῖ', 'ῗ', 'Ῐ', 'Ῑ', 'Ὶ', 'Ί', '῝', '῞', '῟', 'ῠ', 'ῡ', 'ῢ', 'ΰ', 'ῤ', 'ῥ', 'ῦ', 'ῧ', 'Ῠ', 'Ῡ', 'Ὺ', 'Ύ', 'Ῥ', '῭', '΅', '`', 'ῲ', 'ῳ', 'ῴ', 'ῶ', 'ῷ', 'Ὸ', 'Ό', 'Ὼ', 'Ώ', 'ῼ', '´', '῾', 'Ͱ', 'ͱ', 'Ͳ', 'ͳ', 'ʹ', '͵', 'Ͷ', 'ͷ', 'ͺ', 'ͻ', 'ͼ', 'ͽ', ';', '΄', '΅', 'Ά', '·', 'Έ', 'Ή', 'Ί', 'Ό', 'Ύ', 'Ώ', 'ΐ', 'Α', 'Β', 'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ', 'Μ', 'Ν', 'Ξ', 'Ο', 'Π', 'Ρ', 'Σ', 'Τ', 'Υ', 'Φ', 'Χ', 'Ψ', 'Ω', 'Ϊ', 'Ϋ', 'ά', 'έ', 'ή', 'ί', 'ΰ', 'α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν', 'ξ', 'ο', 'π', 'ρ', 'ς', 'σ', 'τ', 'υ', 'φ', 'χ', 'ψ', 'ω', 'ϊ', 'ϋ', 'ό', 'ύ', 'ώ', 'ϐ', 'ϑ', 'ϒ', 'ϓ', 'ϔ', 'ϕ', 'ϖ', 'ϗ', 'Ϙ', 'ϙ', 'Ϛ', 'ϛ', 'Ϝ', 'ϝ', 'Ϟ', 'ϟ', 'Ϡ', 'ϡ', 'Ϣ', 'ϣ', 'Ϥ', 'ϥ', 'Ϧ', 'ϧ', 'Ϩ', 'ϩ', 'Ϫ', 'ϫ', 'Ϭ', 'ϭ', 'Ϯ', 'ϯ', 'ϰ', 'ϱ', 'ϲ', 'ϳ', 'ϴ', 'ϵ', '϶', 'Ϸ', 'ϸ', 'Ϲ', 'Ϻ', 'ϻ', 'ϼ', 'Ͻ', 'Ͼ', 'Ͽ', 'Ⓐ', 'ⓐ', '⒜', 'A', 'a', 'Ạ', 'ạ', 'Ả', 'ả', 'Ḁ', 'ḁ', 'Â', 'Ã', 'Ǎ', 'ǎ', 'Ấ', 'ấ', 'Ầ', 'ầ', 'Ẩ', 'ẩ', 'Ȃ', 'ȃ', 'Ẫ', 'ẫ', 'Ậ', 'ậ', 'À', 'Á', 'Ắ', 'ắ', 'Ằ', 'ằ', 'Ẳ', 'ẳ', 'Ẵ', 'ẵ', 'Ặ', 'ặ', 'Ā', 'ā', 'Ą', 'ą', 'Ǟ', 'Ȁ', 'ȁ', 'Å', 'Ǻ', 'ǻ', 'Ä', 'ä', 'ǟ', 'Ǡ', 'ǡ', 'â', 'á', 'å', 'ã', 'à', 'ẚ', 'Ȧ', 'ȧ', 'Ⱥ', 'Å', 'ⱥ', 'Æ', 'æ', 'Ǽ', 'Ǣ', 'ǣ', 'Ɐ', 'Ꜳ', 'ꜳ', 'Ꜹ', 'Ꜻ', 'Ɑ', 'ꜹ', 'ꜻ', 'ª', '℀', '⅍', '℁', 'Ⓑ', 'ⓑ', '⒝', 'B', 'b', 'Ḃ', 'ḃ', 'Ḅ', 'ḅ', 'Ḇ', 'ḇ', 'Ɓ', 'Ƀ', 'ƀ', 'ƃ', 'Ƃ', 'Ƅ', 'ƅ', 'ℬ', 'Ⓒ', 'ⓒ', '⒞', 'C', 'c', 'Ḉ', 'ḉ', 'Ć', 'ć', 'Ĉ', 'ĉ', 'Ċ', 'ċ', 'Č', 'č', 'Ç', 'ç', 'Ƈ', 'ƈ', 'Ȼ', 'ȼ', 'ℂ', '℃', 'ℭ', 'Ɔ', '℅', '℆', '℄', 'Ꜿ', 'ꜿ', 'Ⓓ', 'ⓓ', '⒟', 'D', 'd', 'Ḋ', 'ḋ', 'Ḍ', 'ḍ', 'Ḏ', 'ḏ', 'Ḑ', 'ḑ', 'Ḓ', 'ḓ', 'Ď', 'ď', 'Ɗ', 'Ƌ', 'ƌ', 'Ɖ', 'Đ', 'đ', 'ȡ', 'ⅅ', 'ⅆ', 'Ǳ', 'ǲ', 'ǳ', 'Ǆ', 'ǅ', 'ǆ', 'ȸ', 'Ⓔ', 'ⓔ', '⒠', 'E', 'e', 'Ḕ', 'ḕ', 'Ḗ', 'ḗ', 'Ḙ', 'ḙ', 'Ḛ', 'ḛ', 'Ḝ', 'ḝ', 'Ẹ', 'ẹ', 'Ẻ', 'ẻ', 'Ế', 'ế', 'Ẽ', 'ẽ', 'Ề', 'ề', 'Ể', 'ể', 'Ễ', 'ễ', 'Ệ', 'ệ', 'Ē', 'ē', 'Ĕ', 'ĕ', 'Ė', 'ė', 'Ę', 'ę', 'Ě', 'ě', 'È', 'è', 'É', 'é', 'Ê', 'ê', 'Ë', 'ë', 'Ȅ', 'ȅ', 'Ȩ', 'ȩ', 'Ȇ', 'ȇ', 'Ǝ', 'ⱸ', 'Ɇ', 'ℇ', 'ℯ', '℮', 'Ɛ', 'ℰ', 'Ə', 'ǝ', 'ⱻ', 'ɇ', 'Ⓕ', 'ⓕ', '⒡', 'F', 'f', 'Ḟ', 'ḟ', 'Ƒ', 'ƒ', 'ꜰ', 'Ⅎ', 'ⅎ', 'ꟻ', 'ℱ', '℻', 'Ⓖ', 'ⓖ', '⒢', 'G', 'g', 'Ɠ', 'Ḡ', 'ḡ', 'Ĝ', 'ĝ', 'Ğ', 'ğ', 'Ġ', 'ġ', 'Ģ', 'ģ', 'Ǥ', 'ǥ', 'Ǧ', 'ǧ', 'Ǵ', 'ℊ', '⅁', 'ǵ', 'Ⓗ', 'ⓗ', '⒣', 'H', 'h', 'Ḣ', 'ḣ', 'Ḥ', 'ḥ', 'Ḧ', 'ḧ', 'Ḩ', 'ḩ', 'Ḫ', 'ḫ', 'ẖ', 'Ĥ', 'ĥ', 'Ȟ', 'ȟ', 'Ħ', 'ħ', 'Ⱨ', 'ⱨ', 'Ꜧ', 'ℍ', 'Ƕ', 'ℏ', 'ℎ', 'ℋ', 'ℌ', 'ꜧ', 'Ⓘ', 'ⓘ', '⒤', 'I', 'i', 'Ḭ', 'ḭ', 'Ḯ', 'ḯ', 'Ĳ', 'ĳ', 'ì', 'í', 'î', 'ï', 'Ì', 'Í', 'Î', 'Ï', 'Ĩ', 'ĩ', 'Ī', 'ī', 'Ĭ', 'ĭ', 'Į', 'į', 'ı', 'Ɨ', 'ƚ', 'Ỻ', 'Ǐ', 'ǐ', 'ⅈ', 'ⅉ', 'ℹ', 'ℑ', 'ℐ', 'Ⓙ', 'ⓙ', '⒥', 'J', 'j', 'Ĵ', 'ĵ', 'ȷ', 'ⱼ', 'Ɉ', 'ɉ', 'ǰ', 'Ⓚ', 'ⓚ', '⒦', 'K', 'k', 'Ḱ', 'ḱ', 'Ḳ', 'ḳ', 'Ḵ', 'ḵ', 'Ķ', 'ķ', 'Ƙ', 'ƙ', 'Ꝁ', 'ꝁ', 'Ꝃ', 'ꝃ', 'Ꝅ', 'ꝅ', 'Ǩ', 'ǩ', 'Ⱪ', 'ⱪ', 'ĸ', 'Ⓛ', 'ⓛ', '⒧', 'L', 'l', 'Ḷ', 'ḷ', 'Ḹ', 'ḹ', 'Ḻ', 'ḻ', 'Ḽ', 'ḽ', 'Ĺ', 'ĺ', 'Ļ', 'ļ', 'Ľ', 'İ', 'ľ', 'Ŀ', 'ŀ', 'Ł', 'ł', 'Ỉ', 'ỉ', 'Ị', 'ị', 'Ƚ', 'Ⱡ', 'Ꝉ', 'ꝉ', 'ⱡ', 'Ɫ', 'ꞁ', 'ℒ', 'Ǉ', 'ǈ', 'ǉ', '⅃', '⅂', 'ℓ', 'ȉ', 'Ȉ', 'Ȋ', 'ȋ', 'Ⓜ', 'ⓜ', '⒨', 'M', 'm', 'Ḿ', 'ḿ', 'Ṁ', 'ṁ', 'Ṃ', 'ṃ', 'ꟿ', 'ꟽ', 'Ɱ', 'Ʃ', 'Ɯ', 'ℳ', 'Ⓝ', 'ⓝ', '⒩', 'N', 'n', 'Ṅ', 'ṅ', 'Ṇ', 'ṇ', 'Ṉ', 'ṉ', 'Ṋ', 'ṋ', 'Ń', 'ń', 'Ņ', 'ņ', 'Ň', 'ň', 'Ǹ', 'ǹ', 'Ŋ', 'Ɲ', 'ñ', 'ŉ', 'Ñ', 'Ƞ', 'ƞ', 'ŋ', 'Ǌ', 'ǋ', 'ǌ', 'ȵ', 'ℕ', '№', 'O', 'o', 'Ṍ', 'ṍ', 'Ṏ', 'ṏ', 'Ṑ', 'ṑ', 'Ṓ', 'ṓ', 'Ȫ', 'ȫ', 'Ȭ', 'ȭ', 'Ȯ', 'ȯ', 'Ȱ', 'ȱ', 'Ǫ', 'ǫ', 'Ǭ', 'ǭ', 'Ọ', 'ọ', 'Ỏ', 'ỏ', 'Ố', 'ố', 'Ồ', 'ồ', 'Ổ', 'ổ', 'Ỗ', 'ỗ', 'Ộ', 'ộ', 'Ớ', 'ớ', 'Ờ', 'ờ', 'Ở', 'ở', 'Ỡ', 'ỡ', 'Ợ', 'ợ', 'Ơ', 'ơ', 'Ō', 'ō', 'Ŏ', 'ŏ', 'Ő', 'ő', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö', 'Ǒ', 'Ȍ', 'ȍ', 'Ȏ', 'ȏ', 'Œ', 'œ', 'Ø', 'Ǿ', 'Ꝋ', 'ǽ', 'ǿ', 'ℴ', '⍥', '⍤', 'Ⓞ', 'ⓞ', '⒪', 'ò', 'ó', 'ô', 'õ', 'ö', 'ǒ', 'ø', 'Ꝏ', 'ꝏ', 'Ⓟ', 'ⓟ', '⒫', '℗', 'P', 'p', 'Ṕ', 'ṕ', 'Ṗ', 'ṗ', 'Ƥ', 'ƥ', 'Ᵽ', 'ℙ', 'Ƿ', 'ꟼ', '℘', 'Ⓠ', 'ⓠ', '⒬', 'Q', 'q', 'Ɋ', 'ɋ', 'ℚ', '℺', 'ȹ', 'Ⓡ', 'ⓡ', '⒭', 'R', 'r', 'Ŕ', 'ŕ', 'Ŗ', 'ŗ', 'Ř', 'ř', 'Ṙ', 'ṙ', 'Ṛ', 'ṛ', 'Ṝ', 'ṝ', 'Ṟ', 'ṟ', 'Ȑ', 'ȑ', 'Ȓ', 'ȓ', 'ɍ', 'Ɍ', 'Ʀ', 'Ɽ', '℞', 'Ꝛ', 'ꝛ', 'ℜ', 'ℛ', '℟', 'ℝ', 'Ⓢ', 'ⓢ', '⒮', 'S', 's', 'Ṡ', 'ṡ', 'Ṣ', 'ṣ', 'Ṥ', 'ṥ', 'Ṧ', 'ṧ', 'Ṩ', 'ṩ', 'Ś', 'ś', 'Ŝ', 'ŝ', 'Ş', 'ş', 'Š', 'š', 'Ș', 'ș', 'ȿ', 'ꜱ', 'Ƨ', 'ƨ', 'ẞ', 'ß', 'ẛ', 'ẜ', 'ẝ', '℠', 'Ⓣ', 'ⓣ', '⒯', 'T', 't', 'Ṫ', 'ṫ', 'Ṭ', 'ṭ', 'Ṯ', 'ṯ', 'Ṱ', 'ṱ', 'Ţ', 'ţ', 'Ť', 'ť', 'Ŧ', 'ŧ', 'Ƭ', 'Ʈ', 'ẗ', 'Ț', 'Ⱦ', 'ƫ', 'ƭ', 'ț', 'ⱦ', 'ȶ', '℡', '™', 'Ⓤ', 'ⓤ', '⒰', 'U', 'u', 'Ṳ', 'ṳ', 'Ṵ', 'ṵ', 'Ṷ', 'ṷ', 'Ṹ', 'ṹ', 'Ṻ', 'ṻ', 'Ụ', 'Ủ', 'ủ', 'Ứ', 'Ừ', 'ụ', 'ứ', 'Ử', 'ử', 'ừ', 'ữ', 'Ữ', 'Ự', 'ự', 'Ũ', 'ũ', 'Ū', 'ū', 'Ŭ', 'ŭ', 'Ů', 'ů', 'Ű', 'ű', 'Ǚ', 'ǚ', 'Ǘ', 'ǘ', 'Ǜ', 'ǜ', 'Ų', 'ų', 'Ǔ', 'ǔ', 'Ȕ', 'ȕ', 'Û', 'û', 'Ȗ', 'ȗ', 'Ù', 'ù', 'Ü', 'ü', 'Ư', 'ú', 'Ʉ', 'ư', 'Ʋ', 'Ʊ', 'Ⓥ', 'ⓥ', '⒱', 'V', 'v', 'Ṽ', 'ṽ', 'Ṿ', 'ṿ', 'Ỽ', 'Ʌ', '℣', 'ⱱ', 'ⱴ', 'ⱽ', 'Ⓦ', 'ⓦ', '⒲', 'W', 'w', 'Ẁ', 'ẁ', 'Ẃ', 'ẃ', 'Ẅ', 'ẅ', 'Ẇ', 'ẇ', 'Ẉ', 'ẉ', 'Ŵ', 'ŵ', 'ẘ', 'Ⱳ', 'ⱳ', 'Ⓧ', 'ⓧ', '⒳', 'X', 'x', 'Ẋ', 'ẋ', 'Ẍ', 'ẍ', 'ℵ', '×', 'Ⓨ', 'ⓨ', '⒴', 'y', 'Y', 'Ẏ', 'ẏ', 'Ỿ', 'ỿ', 'ẙ', 'Ỳ', 'ỳ', 'Ỵ', 'ỵ', 'Ỷ', 'ỷ', 'Ỹ', 'ỹ', 'Ŷ', 'ŷ', 'Ƴ', 'ƴ', 'Ÿ', 'ÿ', 'Ý', 'ý', 'Ɏ', 'ɏ', 'Ȳ', 'Ɣ', '⅄', 'ȳ', 'ℽ', 'Ⓩ', 'ⓩ', '⒵', 'Z', 'z', 'Ẑ', 'ẑ', 'Ẓ', 'ẓ', 'Ẕ', 'ẕ', 'Ź', 'ź', 'Ż', 'ż', 'Ž', 'ž', 'Ȥ', 'ȥ', 'Ⱬ', 'ⱬ', 'Ƶ', 'ƶ', 'ɀ', 'ℨ', 'ℤ', '⟀', '⟁', '⟂', '⟃', '⟄', '⟇', '⟈', '⟉', '⟊', '⟐', '⟑', '⟒', '⟓', '⟔', '⟕', '⟖', '⟗', '⟘', '⟙', '⟚', '⟛', '⟜', '⟝', '⟞', '⟟', '⟠', '⟡', '⟢', '⟣', '⟤', '⟥', '⟦', '⟧', '⟨', '⟩', '⟪', '⟫', '⦀', '⦁', '⦂', '⦃', '⦄', '⦅', '⦆', '⦇', '⦈', '⦉', '⦊', '⦋', '⦌', '⦍', '⦎', '⦏', '⦐', '⦑', '⦒', '⦓', '⦔', '⦕', '⦖', '⦗', '⦘', '⦙', '⦚', '⦛', '⦜', '⦝', '⦞', '⦟', '⦠', '⦡', '⦢', '⦣', '⦤', '⦥', '⦦', '⦧', '⦨', '⦩', '⦪', '⦫', '⦬', '⦭', '⦮', '⦯', '⦰', '⦱', '⦲', '⦳', '⦴', '⦵', '⦶', '⦷', '⦸', '⦹', '⦺', '⦻', '⦼', '⦽', '⦾', '⦿', '⧀', '⧁', '⧂', '⧃', '⧄', '⧅', '⧆', '⧇', '⧈', '⧉', '⧊', '⧋', '⧌', '⧍', '⧎', '⧏', '⧐', '⧑', '⧒', '⧓', '⧔', '⧕', '⧖', '⧗', '⧘', '⧙', '⧚', '⧛', '⧜', '⧝', '⧞', '⧟', '⧡', '⧢', '⧣', '⧤', '⧥', '⧦', '⧧', '⧨', '⧩', '⧪', '⧫', '⧬', '⧭', '⧮', '⧯', '⧰', '⧱', '⧲', '⧳', '⧴', '⧵', '⧶', '⧷', '⧸', '⧹', '⧺', '⧻', '⧼', '⧽', '⧾', '⧿', '∀', '∁', '∂', '∃', '∄', '∅', '∆', '∇', '∈', '∉', '∊', '∋', '∌', '∍', '∎', '∏', '∐', '∑', '−', '∓', '∔', '∕', '∖', '∗', '∘', '∙', '√', '∛', '∜', '∝', '∞', '∟', '∠', '∡', '∢', '∣', '∤', '∥', '∦', '∧', '∨', '∩', '∪', '∫', '∬', '∭', '∮', '∯', '∰', '∱', '∲', '∳', '∴', '∵', '∶', '∷', '∸', '∹', '∺', '∻', '∼', '∽', '∾', '∿', '≀', '≁', '≂', '≃', '≄', '≅', '≆', '≇', '≈', '≉', '≊', '≋', '≌', '≍', '≎', '≏', '≐', '≑', '≒', '≓', '≔', '≕', '≖', '≗', '≘', '≙', '≚', '≛', '≜', '≝', '≞', '≟', '≠', '≡', '≢', '≣', '≤', '≥', '≦', '≧', '≨', '≩', '≪', '≫', '≬', '≭', '≮', '≯', '≰', '≱', '≲', '≳', '≴', '≵', '≶', '≷', '≸', '≹', '≺', '≻', '≼', '≽', '≾', '≿', '⊀', '⊁', '⊂', '⊃', '⊄', '⊅', '⊆', '⊇', '⊈', '⊉', '⊊', '⊋', '⊌', '⊍', '⊎', '⊏', '⊐', '⊑', '⊒', '⊓', '⊔', '⊕', '⊖', '⊗', '⊘', '⊙', '⊚', '⊛', '⊜', '⊝', '⊞', '⊟', '⊠', '⊡', '⊢', '⊣', '⊤', '⊥', '⊦', '⊧', '⊨', '⊩', '⊪', '⊫', '⊬', '⊭', '⊮', '⊯', '⊰', '⊱', '⊲', '⊳', '⊴', '⊵', '⊶', '⊷', '⊸', '⊹', '⊺', '⊻', '⊼', '⊽', '⊾', '⊿', '⋀', '⋁', '⋂', '⋃', '⋄', '⋅', '⋆', '⋇', '⋈', '⋉', '⋊', '⋋', '⋌', '⋍', '⋎', '⋏', '⋐', '⋑', '⋒', '⋓', '⋔', '⋕', '⋖', '⋗', '⋘', '⋙', '⋚', '⋛', '⋜', '⋝', '⋞', '⋟', '⋠', '⋡', '⋢', '⋣', '⋤', '⋥', '⋦', '⋧', '⋨', '⋩', '⋪', '⋫', '⋬', '⋭', '⋮', '⋯', '⋰', '⋱', '⋲', '⋳', '⋴', '⋵', '⋶', '⋷', '⋸', '⋹', '⋺', '⋻', '⋼', '⋽', '⋾', '⋿', '✕', '✖', '✚', '◀', '▶', '❝', '❞', '\uf8ff', '★', '☆', '☼', '☂', '☺', '☹', '✄', '✈', '✌', '✎', '♪', '♫', '☀', '☁', '☔', '⚡', '❆', '☽', '☾', '✆', '✔', '☯', '☮', '☠', '⚑', '☬', '✄', '✏', '♰', '✡', '✰', '✺', '⚢', '⚣', '♕', '♛', '♚', '♬', 'ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', '↺', '↻', '⇖', '⇗', '⇘', '⇙', '⟵', '⟷', '⟶', '⤴', '⤵', '⤶', '⤷', '➫', '➬', '€', '₤', '＄', '₩', '₪', '⟁', '⟐', '◆', '⎔', '░', '▢', '⊡', '▩', '⟡', '◎', '◵', '⊗', '❖', 'Ω', 'β', 'Φ', 'Σ', 'Ξ', '⟁', '⦻', '⧉', '⧭', '⧴', '∞', '≌', '⊕', '⋍', '⋰', '⋱', '✖', '⓵', '⓶', '⓷', '⓸', '⓹', '⓺', '⓻', '⓼', '⓽', '⓾', 'ᴕ', '⸨', '⸩', '❪', '❫', '⓵', '⓶', '⓷', '⓸', '⓹', '⓺', '⓻', '⓼', '⓽', '⓾', '⒈', '⒉', '⒊', '⒋', '⒌', '⒍', '⒎', '⒏', '⒐', '⒑', '⒒', '⒓', '⒔', '⒕', '⒖', '⒗', '⒘', '⒙', '⒚', '⒛', '⓪', '①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧', '⑨', '⑩', '➀', '➁', '➂', '➃', '➄', '➅', '➆', '➇', '➈', '➉', '⑪', '⑫', '⑬', '⑭', '⑮', '⑯', '⑰', '⑱', '⑲', '⑳', '⓿', '❶', '❷', '❸', '❹', '❺', '❻', '❼', '❽', '❾', '❿', '➊', '➋', '➌', '➍', '➎', '➏', '➐', '➑', '➒', '➓', '⓫', '⓬', '⓭', '⓮', '⓯', '⓰', '⓱', '⓲', '⓳', '⓴', '⑴', '⑵', '⑶', '⑷', '⑸', '⑹', '⑺', '⑻', '⑼', '⑽', '⑾', '⑿', '⒀', '⒁', '⒂', '⒃', '⒄', '⒅', '⒆', '⒇', 'ᶅ', 'ᶛ', 'ᶜ', 'ᶝ', 'ᶞ', 'ᶟ', 'ᶠ', 'ᶡ', 'ᶢ', 'ᶣ', 'ᶤ', 'ᶥ', 'ᶦ', 'ᶧ', 'ᶨ', 'ᶩ', 'ᶪ', 'ᶫ', 'ᶬ', 'ᶭ', 'ᶮ', 'ᶯ', 'ᶰ', 'ᶱ', 'ᶲ', 'ᶳ', 'ᶴ', 'ᶵ', 'ᶶ', 'ᶷ', 'ᶹ', 'ᶺ', 'ᶻ', 'ᶼ', 'ᶽ', 'ᶾ', 'ᶿ', 'ᴀ', 'ᴁ', 'ᴂ', 'ᴃ', 'ᴄ', 'ᴅ', 'ᴆ', 'ᴇ', 'ᴈ', 'ᴉ', 'ᴊ', 'ᴋ', 'ᴌ', 'ᴍ', 'ᴎ', 'ᴏ', 'ᴐ', 'ᴑ', 'ᴒ', 'ᴓ', 'ᴔ', 'ᴕ', 'ᴖ', 'ᴗ', 'ᴘ', 'ᴙ', 'ᴚ', 'ᴛ', 'ᴜ', 'ᴝ', 'ᴞ', 'ᴟ', 'ᴠ', 'ᴡ', 'ᴢ', 'ᴣ', 'ᴤ', 'ᴥ', 'ᴦ', 'ᴧ', 'ᴨ', 'ᴩ', 'ᴪ', 'ᴫ', 'ᴬ', 'ᴭ', 'ᴮ', 'ᴯ', 'ᴰ', 'ᴱ', 'ᴲ', 'ᴳ', 'ᴴ', 'ᴵ', 'ᴶ', 'ᴷ', 'ᴸ', 'ᴹ', 'ᴺ', 'ᴻ', 'ᴼ', 'ᴽ', 'ᴾ', 'ᴿ', 'ᵀ', 'ᵁ', 'ᵂ', 'ᵃ', 'ᵄ', 'ᵅ', 'ᵆ', 'ᵇ', 'ᵈ', 'ᵉ', 'ᵊ', 'ᵋ', 'ᵌ', 'ᵍ', 'ᵎ', 'ᵏ', 'ᵐ', 'ᵑ', 'ᵒ', 'ᵓ', 'ᵔ', 'ᵕ', 'ᵖ', 'ᵗ', 'ᵘ', 'ᵙ', 'ᵚ', 'ᵛ', 'ᵜ', 'ᵝ', 'ᵞ', 'ᵟ', 'ᵠ', 'ᵡ', 'ᵢ', 'ᵣ', 'ᵤ', 'ᵥ', 'ᵦ', 'ᵧ', 'ᵨ', 'ᵩ', 'ᵪ', 'ᵫ', 'ᵬ', 'ᵭ', 'ᵮ', 'ᵱ', 'ᵲ', 'ᵳ', 'ᵵ', 'ᵷ', 'ᵸ', 'ᵺ', 'ᵻ', '᷋', '᷌', '᷍', '᷎', '᷏', 'ᷓ', 'ᷔ', 'ᷕ', 'ᷖ', 'ᷗ', 'ᷘ', 'ᷙ', 'ᷛ', 'ᷜ', 'ᷝ', 'ᷞ', 'ᷟ', 'ᷠ', 'ᷡ', 'ᷢ', 'ᷣ', 'ᷤ', 'ᷥ', 'ᷦ', '‘', '’', '‛', '‚', '“', '”', '„', '‟', '«', '»', '‹', '›', 'Ꞌ', '"', '❛', '❜', '❝', '❞', '<', '>', '@', '‧', '¨', '․', '꞉', ':', '⁚', '⁝', '⁞', '‥', '…', '⁖', '⸪', '⸬', '⸫', '⸭', '⁛', '⁘', '⁙', '⁏', ';', '⦂', '⁃', '‐', '‑', '‒', '-', '–', '⎯', '—', '―', '_', '⁓', '⸛', '⸞', '⸟', 'ⸯ', '¬', '/', '\\', '⁄', '\\', '⁄', '|', '⎜', '¦', '‖', '‗', '†', '‡', '·', '•', '⸰', '°', '‣', '⁒', '%', '‰', '‱', '&', '⅋', '§', '÷', '+', '±', '=', '꞊', '′', '″', '‴', '⁗', '‵', '‶', '‷', '‸', '*', '⁑', '⁎', '⁕', '※', '⁜', '⁂', '!', '‼', '¡', '?', '¿', '⸮', '⁇', '⁉', '⁈', '‽', '⸘', '¼', '½', '¾', '²', '³', '©', '®', '™', '℠', '℻', '℅', '℁', '⅍', '℄', '¶', '⁋', '❡', '⁌', '⁍', '⸖', '⸗', '⸚', '⸓', '(', ')', '[', ']', '{', '}', '⸨', '⸩', '❨', '❩', '❪', '❫', '⸦', '⸧', '❬', '❭', '❮', '❯', '❰', '❱', '❴', '❵', '❲', '❳', '⦗', '⦘', '⁅', '⁆', '〈', '〉', '⏜', '⏝', '⏞', '⏟', '⸡', '⸠', '⸢', '⸣', '⸤', '⸥', '⎡', '⎤', '⎣', '⎦', '⎨', '⎬', '⌠', '⌡', '⎛', '⎠', '⎝', '⎞', '⁀', '⁔', '‿', '⁐', '‾', '⎟', '⎢', '⎥', '⎪', 'ꞁ', '⎮', '⎧', '⎫', '⎩', '⎭', '⎰', '⎱', '✈', '☀', '☼', '☁', '☂', '☔', '⚡', '❄', '❅', '❆', '☃', '☉', '☄', '★', '☆', '☽', '☾', '⌛', '⌚', '☇', '☈', '⌂', '⌁', '⏧', '✆', '☎', '☏', '☑', '✓', '✔', '⎷', '⍻', '✖', '✗', '✘', '☒', '✕', '☓', '☕', '♿', '✌', '☚', '☛', '☜', '☝', '☞', '☟', '☹', '☺', '☻', '☯', '⚘', '☮', '✝', '⚰', '⚱', '⚠', '☠', '☢', '⚔', '⚓', '⎈', '⚒', '⚑', '⚐', '☡', '❂', '⚕', '⚖', '⚗', '✇', '☣', '⚙', '☤', '⚚', '⚛', '⚜', '☥', '☦', '☧', '☨', '☩', '†', '☪', '☫', '☬', '☭', '✁', '✂', '✃', '✄', '✍', '✎', '✏', '✐', '\uf802', '✑', '✒', '✉', '✙', '✚', '✜', '✛', '♰', '♱', '✞', '✟', '✠', '✡', '☸', '✢', '✣', '✤', '✥', '✦', '✧', '✩', '✪', '✫', '✬', '✭', '✮', '✯', '✰', '✲', '✱', '✳', '✴', '✵', '✶', '✷', '✸', '✹', '✺', '✻', '✼', '✽', '✾', '❀', '✿', '❁', '❃', '❇', '❈', '❉', '❊', '❋', '⁕', green + dim + '☘', '❦', '❧', '☙', '❢', '❣', '♀', '♂', '⚲', '⚢', '⚣', '⚤', '⚥', '⚦', '⚧', '⚨', '⚩', '☿', '♁', '⚯', '♔', '♕', '♖', '♗', '♘', '♙', '♚', '♛', '♜', '♝', '♞', '♟', '☖', '☗', '♠', '♣', '♦', '♥', '❤', '❥', '♡', '♢', '♤', '♧', '⚀', '⚁', '⚂', '⚃', '⚄', '⚅', '⚇', '⚆', '⚈', '⚉', '♨', '♩', '♪', '♫', '♬', '♭', '♮', '♯', '\uf8ff', '⌨', '⏏', '⎗', '⎘', '⎙', '⎚', '⌥', '⎇', '⌘', '⌦', '⌫', '⌧', '♲', '♳', '♴', '♵', '♶', '♷', '♸', '♹', '♺', '♻', '♼', '♽', '⁌', '⁍', '⎌', '⌇', '⌲', '⍝', '⍟', '⍣', '⍤', '⍥', '⍨', '⍩', '⎋', '♃', '♄', '♅', '♆', '♇', '♈', '♉', '♊', '♋', '♌', '♍', '♎', '♏', '♐', '♑', '♒', '♓', '⏚', '⏛']
