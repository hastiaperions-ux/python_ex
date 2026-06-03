import re
emails = ["abc@gmail.com", "123$tt*@xyz.com", "good@bad@uk.in", 
"nasa@usa12.space", "no-reply@domain.in", "ramha$numan@saketa.lok", 
"ruhi.mohan@exter123.c45", "fake@fake123.fakercom"] 

pattern= r'^[a-zA-Z._-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$'
    
valid = []
invalid = []

for email in emails:
    if re.match(pattern,email):
        valid.append(email)
    else:
        invalid.append(email)


print(f"valid emails : {valid}")
print(f"invalid emails : {invalid}")
