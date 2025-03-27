from ollama import chat

def main():
    model_name = "llama3.1:8b"  # I like using 8b since deepseek models fail to follow instructions. 
    system_prompt = (
        "You are a BASIC interpreter. Your job is to take BASIC code as input, execute it, "
        "and then return the output. For any code provided, simulate the behavior of a BASIC interpreter. This means never ever write any explanations. Only show the final result (which might be an empty string sometimes).Only display an internal representation with arrows and variable names. If the code trying to be run isnt supported, just return a Module Error saying there is no module that has that function. If the user inputs a prompt that isnt code, return a syntax error. "
        "and display the results or errors as appropriate. DO NOT RETURN ANY FINAL ANSWER BESIDES THE ACTUAL ANSWER. For example PRINT(1+1) should return 2 not 'The output would be 2'."
    )

    print("Welcome to the Llama BASIC Interpreter (via Ollama)!")
    print("Enter BASIC code below. Type 'exit' or 'quit' to stop.")

    while True:
        user_input = input("BASIC> ")
        if user_input.strip().lower() in {"exit", "quit"}:
            print("Exiting BASIC interpreter.")
            break

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Input BASIC Code:\n{user_input}\n\nOutput:"}
        ]

        response = chat(model=model_name, messages=messages)
        result = response.get("message", {}).get("content", "").strip()

        print(result)

if __name__ == "__main__":
    main()
