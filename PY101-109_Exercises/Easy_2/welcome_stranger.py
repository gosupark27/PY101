def greetings(full_name, job):
    return (f'Hello, {" ".join(full_name)}! Nice to have a ' 
            f'{" ".join([job.get('title'), job.get('occupation')])} around.')

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)