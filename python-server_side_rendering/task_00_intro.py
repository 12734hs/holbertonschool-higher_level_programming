def generate_invitations(template, attendees):
    if not isinstance(template, str) \
    or not isinstance(attendees, list) \
    or not all(isinstance(i, dict) for i in attendees):
        raise ValueError("Invalid input types")

    if not template:
        print("Template is empty, no output files generated.")
        return None

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return None

    for index, dct in enumerate(attendees):
        result = template
        for k in dct.keys():
            value = 'N/A' if dct[k] is None else dct[k]
            result = result.replace(f"{{{k}}}", value)

        with open(f'output_{index+1}.txt', 'w') as file:
            file.write(result)

    return 1


with open('template.txt', 'r') as file:
    result = file.read()


example = 'df'
sample = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]


generate_invitations(result,sample)