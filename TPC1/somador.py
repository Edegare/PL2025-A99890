import sys

def process_text(text):
    sum = 0
    on = True
    current_number = ""
    
    i = 0
    while i < len(text):
        char = text[i]
        
        if char.isdigit():
            current_number += char  
        else:
            if current_number: 
                if on:
                    sum += int(current_number)
                current_number = "" 
            
            if text[i:i+3].lower() == "off":
                on = False
                i += 2  
            elif text[i:i+2].lower() == "on":
                on = True
                i += 1  
            elif char == "=":
                print(sum)
        
        i += 1
    
    if current_number and on:
            sum += int(current_number)
    print("FIM:", sum)

if __name__ == "__main__":
    input_text = sys.stdin.read()
    process_text(input_text)