def decode_morse(morse_code:str):
    if morse_code == "...---...":
        return "SOS"
    
    answer : str = "" 

    for slice in morse_code.split("   "):
        for morse in slice.split():
            answer += MORSE_CODE[morse] # type: ignore  # noqa
    
        # next iteration
        answer += " "
    return answer.strip()

print(decode_morse('.-... ---...   -..-. --...'))