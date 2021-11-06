def correct_output(Wrong_input):
    if len(Wrong_input)<=1:
        return Wrong_input
    elif Wrong_input[0]==Wrong_input[1]:
        return correct_output(Wrong_input[1:])
    else:
        return Wrong_input[0] + correct_output(Wrong_input[1:])


while True:
    Wrong_input=input()
    if Wrong_input=='*':
        break
    if Wrong_input=='':
        continue
    print(correct_output(Wrong_input))