####################################################################################
#                                                                                  #
# flashcards.py -- basic script to assist in studying new vocab words by           #
#                  displaying a definition and prompting the user for the word     #
#                                                                                  #
# Author: Colton Acosta                                                            #
# Date: 6/22/2022                                                                  #
#                                                                                  #
####################################################################################


####################################################################################
# Imports/Globals                                                                  #
####################################################################################
import os
import random

WORD_INDEX = 0
DEF_INDEX  = 1
ANSWER_CORRECT   = True
ANSWER_INCORRECT = False
NEXT_WORD_INDEX  = 0


####################################################################################
# Objects                                                                          #
####################################################################################
class VocabWords:

    def __init__( self ):
        self.vocab_source_file    = None
        self.vocab_words_and_defs = {}
        self.incorrect_words      = []

    def set_source_file( self, filename ):
        if ( os.path.exists( filename ) ):
            self.vocab_source_file = filename
        else:
            print( "Error: file \""+filename+"\" does not exist")
    
    def load_words( self ):
        with open( self.vocab_source_file, "r" ) as file:
            source_lines = file.readlines()
        for line in source_lines:
            word_and_def = line.split( ":" )
            word         = word_and_def[ WORD_INDEX ]
            definition   = word_and_def[ DEF_INDEX  ].strip()
            self.vocab_words_and_defs[word] = definition
        self.incorrect_words = list( self.vocab_words_and_defs )
        random.shuffle( self.incorrect_words )
    
    def get_num_incorrect_words( self ):
        return len( self.incorrect_words )

    def get_next_word( self ):
        return self.incorrect_words[0] 

    def display_next_def( self ):
        word = self.get_next_word() 
        print( self.vocab_words_and_defs[word] )

    def get_user_input( self ):
        return input( ">" )

    def check_user_input( self, word, user_input ):
        if ( word != user_input ):
            return ANSWER_INCORRECT
        else:
            return ANSWER_CORRECT
        
    def remove_word( self ):
        self.incorrect_words.pop( NEXT_WORD_INDEX )

    def send_word_to_back( self ):
        word = self.incorrect_words.pop( NEXT_WORD_INDEX )
        self.incorrect_words.append( word )


## VocabWords ##


####################################################################################
# Main Loop                                                                        #
####################################################################################
def main():
    vocab_words_and_defs = VocabWords()
    vocab_words_and_defs.set_source_file( "pride_and_prejudice.txt" )
    vocab_words_and_defs.load_words()

    while ( vocab_words_and_defs.get_num_incorrect_words() > 0 ):
        word = vocab_words_and_defs.get_next_word()
        vocab_words_and_defs.display_next_def()
        user_input = vocab_words_and_defs.get_user_input()
        is_answer_correct = vocab_words_and_defs.check_user_input( word, user_input )
        if ( is_answer_correct == ANSWER_CORRECT ):
            vocab_words_and_defs.remove_word()
            print( "Correct\n")
        else:
            vocab_words_and_defs.send_word_to_back()
            print( "Incorrect. Correct answer is \""+word+"\"\n")

    print( "End of List" )

## main ## 


####################################################################################
# Procedures                                                                       #
####################################################################################


####################################################################################
# Run the script                                                                   #
####################################################################################
if __name__ == "__main__":
    main()


####################################################################################
# EOF                                                                              #
####################################################################################