from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def summarize_transcript(file_path, course = "", topic = ""):
    if course != "":
        course = "This lecture is for a course on "+course+"."
    if topic != "":
        topic = "This lecture is focused on "+topic+"."
    try:
        # Read the transcript from a text file
        with open(file_path, 'r', encoding='utf-8') as file:
            transcript = file.read()
        
        print("Processing the transcript...")
        # Process the transcript with the OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Specify the engine/model directly here
            messages=[
                {"role": "system", "content": "Please summarize the following lecture into key points and important concepts. Do not alter any of the information in the input file when creatng the key points and important concepts. {course} {topic}"},
                {"role": "user", "content": transcript}
            ]
        )
        summary = response.choices[0].message.content
        # Extract the summary from the API response
        #summary = response['choices'][0]['text'].strip()
        
        # Write the summary to a text document
        with open('summarized_notes.txt', 'w', encoding='utf-8') as summary_file:
            summary_file.write(summary)
        
        print("Summarized Notes have been saved to 'summarized_notes.txt'.")
    
    except client.APIError as e:  # Updated exception handling
        print(f"An error occurred with the OpenAI API: {str(e)}")
    except FileNotFoundError:
        print("The file was not found. Please check the file path.")
    except Exception as e:
        # Handle other exceptions
        print(f"An unexpected error occurred: {e}")

# Example usage
#file_path = "lecture_transcript.txt"  
#file_path = "compellingCharacters.txt"
file_path = "reef.txt"

summarize_transcript(file_path, "Marine Biology and Ecology", "Ecotourism, Recreation, and Reefs")
