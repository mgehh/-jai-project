import openai

openai.api_key = "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"
file = open("Backend/code.txt", "r")
file_contents = file.read()  # Read the contents of the file

def generate_song(prompt, model="text-davinci-001"):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=50,
        temperature=0.6,
        n=1,
        stop=None,
    )

    generated_text = response.choices[0].text.strip()
    return generated_text

prompt = "You are a mean MIT professor grading a computer science assignment. Please grade the assignment on these 4 criteria. Code Functionality and Example, README, Notes and Comments, Creativity and Presentation. Grade the 4 criteria for the computer science assignment on the scale from 1 - 7. Just give me the the grades on the four criteria, no further explanation needed, just the numbers of the 4 criteria. Here is the assignment I want you to grade on the criteria I gave you at the start: "
generated_song = generate_song(prompt + file_contents)  # Pass the file contents as a string
print(generated_song)
