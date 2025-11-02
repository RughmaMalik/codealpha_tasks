import re

def extract_emails(input_file, output_file):
    # Open and read the input file
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regular expression pattern for finding emails
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    # Find all emails in the text
    emails = re.findall(email_pattern, content)

    # Remove duplicates by converting to a set
    unique_emails = sorted(set(emails))

    # Write all found emails to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        for email in unique_emails:
            file.write(email + '\n')

    print(f"✅ {len(unique_emails)} email(s) extracted successfully!")
    print(f"Saved to: {output_file}")


# ------------------- MAIN PROGRAM -------------------
input_file = "sample_text.txt"     # Input file with text
output_file = "extracted_emails.txt"  # Output file to save emails

extract_emails(input_file, output_file)
