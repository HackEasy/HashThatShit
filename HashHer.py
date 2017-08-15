#Coded By The M4d Sc13nT15t
#Can You Hear Those Voices?
#Look Into My Eyes Can You See The Pain
#The Chaos I Bring, Youll Never Forget My Name
#The Troubles, The Pain, The Panic, The Fear
#We're Not Santa, But We Will Be Around All Year
from termcolor import colored

print colored("""
	 
                         _.---.                           
                       .' :.--."-.                        
                     .'.-";.--.`. \                       
                   .'.' :\:-./;`.  ;                  ;   
                .-" / .-'-   -';   :                 /    
               (/   .:: ._  _. :\ \;;              .'     
               :  .'j ;'._` _.`: ;/ :             :       
 \             ; / : `;  o   o  :':  :`-           ;       
  "-.          ::   \ :\  s   /; ;   \            :       
     `.       / ; ;  `.\  ==  / /:\ \ `._          \      
       \     :  : :   ;\`.__.' : ; `.`.; `          ;     
 "-.    ;    ;. ; ;  /  ;\  ;   \: \ `(            /:     
    `.  :  `-: " / .'   : \      )\ "--`._.      .' ;     
      \ ;   (;  / /   .';`     .(  "-.___;.     /  /      
       y     :-' :   / /      (  `.( __.-' \   : .'       
    .-"    .t \  ;  :-(        `-. `"-.)    ;  ;/       .-
  .'     .'  \ :-: :              \ "-.`.   :  :       (  
 /     .'     \;  t.\        :     `.  ) ;  :   \       `-
      :  _     ;  : `      : ;       )/ /   ;    "-.      
      :.'/ /"l :  ;(o)     ; :    (o)^-:    ;       ""--..
      ' / /  :/ ; '.      /   \      / ;    ;     .-"     
 \     : :      :   ;----'     `----'  ;    ;    /        
  ;  / ; ;       ;  ;     .'  `.       ;    ;_.-"         
  : :  : :       :  :        ;  \      ;    ;            /
  ; ;   \ \       ;  ;       :        /    :           .' 
 /  :    `.`.     :  :       ;       :     ;        .-"/  
     \     `."-.   ; :               ;    /      .-" .'   
      `--.   "-."-.: ;  :    c    ; :    /      /  .'     
         :      "-."t.  ;         : ;   /      :  (       
          \        j+."-.         ;/   /-.      \  \      
    "-.    "-.    /  \ -."-.      /   /   `,     ;  ;     
       `.     `. :    \  "-.`..-./   /\     \   /   :     
         \      \;     t.  .`;-' `  /  ;      .'    ;     
          ;     :       \`-;":---  ;   :    .'     /      
          :     ;        ;  "-`+-+'    :  .'     .'       
          ;    :         :     ; ;      \/      /         
"-.      :     :          ;   / /        \     :          
_  \     ;     ;          :_.'.'          \    ;          
 "-.;   :      ;          :`-';            \   :          
    :   ;\     ;          :>  :             ;   \         
     \  : `.   ;          :>   ;            :    `-     .'
         \  "-.;          :>   :             ;        ./  
          `._.-;          ;     \            :      .':   
 "-.           ;          ;      \            ;    /  ;   
    \_..---..  ;         :_       \           :._.'  :    
 `.  "-.     "-:         ; "-.  .-"`.          ;     ;    
   \    `-._.._:        :     `.     `.        :    /    _
    "-.        ""---..__;-.     \      `.     . ; .'  .-" 
       ""--..            "-;     ;    .-"""    """   /    
             "-.            `.   :           `-.___.'   
""","red")


print colored ("[+] C0d3d By Th3 M4d Sc13nT15t & Th3 M4d Ch3m15t ","blue")


import re
import hashlib

key_string = raw_input( "Enter What You Would Like To Hide With An MD5 Hash ", )

input_str = raw_input("Could Your Provide A Little Info?: ")

print colored("""
                         .\   / _\   .\          >> Your Hash <<                
                        /_ \   ||   / _\     >> Has Been Generated <<                                
                         ||    ||    ||
                  ; ,     \`.__||__.'/           >> You Should <<                          
          |\     /( ;\_.;  `./|  __.'       >> Be On Your Way Now.. <<                       
          ' `.  _|_\/_;-'_ .' '||
           \ _/`       `.-\_ / ||      _
       , _ _`; ,--.   ,--. ;'_ _|,     |
       '`''\| /  ,-\ | _,-\ |/''`'  _  |
        \ .-- \__\_/ /` )_/ --. /   |  |       _
        /    .         -'  .    \ --|--|--.  .' \
       |     /             \     |  |  |   \ |---'
    .   .  -' `-..____...-' `-  .   |  |    |\  _
 .'`'.__ `._      `-..-''    _.'|   |  | _  | `-'      _
  \ .--.`.  `-..__    _,..-'   L|   |    |             |
   '    \ \      _,| |,_      /_7)  |    |   _       _ |  _
         \ \    /       \ _.-'/||        | .' \     _| |  |
          \ \  /.'|   |`.__.'` ||     .--| |--- _   /| |  |
           \ `//_/     \       ||    /   | \  _ \  / | |  |
            `/ \|       |      ||   |    |  `-'  \/  | '--|      _
             `"`'.  _  .'      ||    `--'|                |   .--/
                  \ | /        ||                         '--'
                   |'|  mx     'J  >>> Th3 M4d Sc13nT15t & M4d Ch3m15t <<<
                .-.|||.-.                  >>> Made Me Do It <<<
""","blue")
print colored ("Your Generated Input Has Been Hashed:","white"), input_str
print hashlib.md5( key_string ).hexdigest()

