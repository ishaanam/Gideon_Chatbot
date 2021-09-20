
import webbrowser
from method_of_communication import communicate_better 

#opens all of the links you need for a class, found this one especially helpful helpful during zoom school
def find_links(sentence):
    print(sentence)
    links = {
        #replace empty strings with links
        'science' : {
            'google classroom' : '',
            'acman' : '',
            'zoom' : '',
            'site' : ''
            },
        'spanish' : {
            'google classroom' : '',
            'acman' : '',
            'site' : '',
            'site' : '',
            'zoom' : ''
            },
        'PE' : {
            'acman' : '',
            'zoom' : ''
            },
        'latin' : {
            'google classroom' : '',
            'acman' : '',
            'zoom' : '',
            'site' : ''
            },
        'english' : {
            'acman' : '',
            'zoom password' : '',
            'zoom' : '',
            'site' : '',
            'google classroom' : ''
            },
        'math' : {
            'google classroom' : '',
            'acman' : '',
            'zoom' : ''
            },
        'history' : {
            'google classroom' : '',
            'acman' : '',
            'zoom' : ''
            },
        'health' : {
            'acman' : '',
            'zoom' : ''
            },
        'cs' : {
            'zoom' : '',
            'acman' : ''
            },
        'prepare' : {
            'acman' : '',
            'zoom' : ''
            }
        }

    my_classes = links.keys()
    
    for word in sentence:
        if word in my_classes:
            next_class = word


    print("Do you need zoom(yes/no)?")
    is_remote = communicate_better()
    

    #excludes zoom, just pulls up your other links
    if is_remote == "yes":
        print("\n")
        print(next_class + ': ')
        l = links[next_class]
        for key in l:
            zoom = l[key]
            if key == 'zoom' or key == 'google classroom' or key == 'acman' or key=="site":
                webbrowser.open(zoom, new=2)
            elif key == 'zoom password':
                print(key + " :" + zoom)    
        print("Gideon: I hope you enjoy " + next_class + "!")

    #opens all links listed in dictionary, including zoom
    elif is_remote == "no":
        print("\n")
        print(next_class + ': ')
        l = links[next_class]
        for key in l:
            zoom = l[key]
            if key == 'google classroom' or key == 'acman' or key=="site":
                webbrowser.open(zoom, new=2)
            elif key == 'zoom password':
                print(key + " :" + zoom)
            
        print("Gideon: I hope you enjoy " + next_class + "!")
