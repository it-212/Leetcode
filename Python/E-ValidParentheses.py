class Solution:
    def isValid(self, string: str) -> bool:

        parentheses = { "}":"{", "]":"[", ")":"("}
        right = ")]}"
        str_cpy = string[:]

        i = 0
        while(str_cpy != ""):
            print("String copy: %s" %str_cpy)
            if(i >= len(str_cpy)):
                return False
            print("String[i]: %s" %str_cpy[i])
            if(str_cpy[i] in right):
                if(i != 0 and parentheses[str_cpy[i]]==str_cpy[i-1] ):
                    if(len(str_cpy) <= 2):
                        return True
                    if(i == 1):
                        str_cpy = str_cpy[i+1:]
                    elif(i == len(str_cpy)-1):
                        str_cpy = str_cpy[:i-1]
                    else:
                        str_cpy = str_cpy[:i-1] + str_cpy[i+1:]
                    i-=2
                else:
                    return False
            i+=1
        
        return True

if __name__=='__main__':
    examples =         ["([]","(()(", "()", "(){}[]", "(]", "([{()()}])", "()({)(})", "((({(})))"]
    expected_output = ["false", "false", "true", "true", "false", "true", "false", "false"]
    
    for i in range(len(examples)):
        out = "true" if Solution().isValid(examples[i]) else "false"
        print("Example %d: %s" % (i+1,examples[i]))
        print("Output: %s" %out)
        if(out!=expected_output[i]):
            print("Expected output: %s" %expected_output[i])
            print("ERROR")
        print()

    
