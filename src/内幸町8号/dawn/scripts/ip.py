import telnetlib
import datetime
##### Define variable
host = input("Please input DPU IP : ")
comment = input("Add any comment in the file name : ")
user = "user"
password = "password"
date = datetime.datetime.today().strftime("%y%m%d-%H%M")
file_name_form = 'showRun_{}_{}_{}.txt'
file_name = file_name_form.format(host, date, comment)
##### Connect to Target node via telnet
tn = telnetlib.Telnet(host, 23)
#### Enable debug trace
# tn.set_debuglevel(1)
tn.read_until(b"Login: ")
tn.write(user.encode('ascii') + b"\n")
tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")
tn.read_until(b"#")
tn.write(b"show version" + b'\n')
output_1 = tn.read_until(b"#").decode('ascii')
tn.write(b"\n")
tn.read_until(b"#")
tn.write(b"show running-config" + b'\n')
output_2 = tn.read_until(b"#").decode('ascii')
tn.write(b"exit" + b'\n')
tn.close()
f = open(file_name, mode='w', newline="")
f.write("##### Node version" + "\r\n")
f.write(output_1)
f.write("\r\n" + "##### Running Config" + "\r\n")
f.write(output_2)
f.close()
print("### Done!!! ", file_name, "is created.")