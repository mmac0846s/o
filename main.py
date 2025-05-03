from flask import Flask, request, jsonify
from g4f.client import Client
import time

app = Flask(__name__)
client = Client()

@app.route('/make_scripts', methods=['POST'])
def make_scripts():
    data = request.get_json(force=True)
    if not data or 'script' not in data or not data['script']:
        return jsonify({'fixed_script': ''})
    script_content = data['script']
    start_time = time.time()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Make a bunch of scripts that might be in the ServerScriptService of the game the user says. Make at least 50-100 scripts. Dont say anything else but the scripts path. Make at least 50-100 scripts. Put some in folders sometimes. Remove .lua too since its a normal luau script. Dont name a folder 'folder' tho. Add game before the script path like real roblox would be like. Do periods and not slashes for the path. without adding ``` as we handle that. Make sure the Folders have names according to the scripts. Make sure there arent spaces between the paths. DONT PUT THEM ALL IN FOLDERS LEAVE SOME JUST IN ServerScriptService OR SERVERSTORAGE NOT INSIDE A FOLDER. Sometimes the user might send some replicatedstorage events makes some of the script names related to the events."},
            {"role": "user", "content": script_content}
        ]
    )
    end_time = time.time()
    elapsed_time = end_time - start_time

    print("done uhhhhhhhhhhhhhhhhhhhh';-;  making script name")
    fixed_script = response.choices[0].message.content
    formatted_script = (
        f"{fixed_script}"
    )
    return jsonify({'fixed_script': formatted_script})
@app.route('/generate_script', methods=['POST'])
def generate_script():
    data = request.get_json(force=True)

    if not data or 'script' not in data or not data['script']:
        return jsonify({'fixed_script': ''})

    script_content = data['script']

    start_time = time.time()

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Make a fake script based off of the path the user gives u. Dont say anything else only the script source. without adding ``` as we handle that. Make it at least 500 lines. Dont add any messages like -- or anything. Remember it is a server script with server capabilities. The user may send some replicatedstorage events, and models the user will put :: ClassName after. use them to build the sources of the script (DO NOT USE periods for events path use ['EVENTNAME']). Do not add anything that could only run from a plugin script or a localscript. Dont add anything like -- Script: script name -- Location: location.  MAKE IT LIKE A REAL SCRIPT THOOOOOO DONT PUT EXAMPLES PUT THINGS THAT MIGHT ACTUALLY BE IN THE GAME. "},
            {"role": "user", "content": script_content}
        ]
    )

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("booya")

    fixed_script = response.choices[0].message.content
    formatted_script = (
        f"{fixed_script}"
    )
    return jsonify({'fixed_script': formatted_script})
@app.route('/get_remote', methods=['POST'])
def get_remote():
    data = request.get_json(force=True)

    if not data or 'script' not in data or not data['script']:
        return jsonify({'fixed_script': ''})

    script_content = data['script']

    start_time = time.time()

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "The user will give you all remote events in the game. Tell them which one is the one to redeem codes in game. Only respond with the name of the remote event and nothing else. Only output one. Look for something like Redeem or anything with Code in it. If you cant find one just say the remote event path."},
            {"role": "user", "content": script_content}
        ]
    )

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("booya")

    fixed_script = response.choices[0].message.content
    formatted_script = (
        f"{fixed_script}"
    )
    return jsonify({'fixed_script': formatted_script})
@app.route('/get_codes', methods=['POST'])
def get_codes():
    data = request.get_json(force=True)

    if not data or 'script' not in data or not data['script']:
        return jsonify({'fixed_script': ''})

    script_content = data['script']

    start_time = time.time()

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Find real codes for the game the user sends on Roblox. Put the real codes first and then make some fake realistic codes. Only respond with the codes and nothing else. DONT PUT REAL OR FAKE IN THEM. DONT PUT EXPIRED EITHER. JUST THE CODES AND NOTHING ELSE. Generate at least 140 fake codes. Put the real codes first!!"},
            {"role": "user", "content": script_content}
        ]
    )

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("booya CODESSS!!")

    fixed_script = response.choices[0].message.content
    formatted_script = (
        f"{fixed_script}"
    )
    return jsonify({'fixed_script': formatted_script})
if __name__ == '__main__':
    print("HELLO")
    app.run(debug=True)
