from rich.console import Console
from rich.markup import escape
from k_amino import Client as SA_Client
from pymino import Client as Py_Client
import time
import threading

console = Console()
sa_client = SA_Client()
py_client = Py_Client(
    device_key="E7309ECC0953C6FA60005B2765F99DBBC965C8E9", 
    signature_key="DFA5ED192DDA6E88A12FE12130DC6206B1251E44", 
    service_key="ZTFjNjVmNTBkNWY1ZmI0OQ=="
)

email = "evetupto@gmail.com"
password = "kingshado111"
sa_client.login(email=email, password=password)

py_email = input("Enter pymino email: ")
py_password = input("Enter pymino password: ")

while True:
    try:
        py_client.login(email=py_email, password=py_password)
        break
    except Exception as e:
        console.print(escape(f"Login error with pymino: {e}. Retrying..."))
        time.sleep(2)

def collect_user_ids(sa_client):
    user_ids = []
    start = 0
    try:
        for i in range(3):  
            users = sa_client.get_all_users(start=start, size=50)
            start += 150
            for user_id, chat_request in zip(users.userId, users.privilegeOfChatInviteRequest):
                user_ids.append(user_id)
    except Exception as e:
        console.print(escape(f"Failed to get users: {e}"))
    return user_ids

def edit_chat_with_retry(py_client, chat_id, title, announcement, viewOnly, max_retries=2):
    retries = 0
    while retries < max_retries:
        try:
            py_client.edit_chat(
                chatId=chat_id,
                title=title,
                announcement=announcement,
                viewOnly=viewOnly
            )
            console.print(f"Edited chat settings: Title='{title}', Announcement='{announcement}', ViewOnly={viewOnly}")
            break
        except Exception as e:
            console.print(escape(f"Error editing chat settings: {e}. Retrying..."))
            retries += 1
            time.sleep(6)
    if retries == max_retries:
        console.print(escape(f"Failed to edit chat settings after {max_retries} attempts."))

def create_group_chats(py_client, sa_client, message1, message2):
    console.print("Creating 100 group chats...")
    for i in range(115):
        user_ids = []

        def fetch_user_ids():
            nonlocal user_ids
            user_ids = collect_user_ids(sa_client)
        
        thread = threading.Thread(target=fetch_user_ids)
        thread.start()
        thread.join()

        if not user_ids:
            console.print(escape("No users found. Retrying..."))
            time.sleep(6)
            continue

        try:
            message = message1 if i % 2 == 0 else message2
            chat_thread = py_client.start_chat(userId=user_ids, message=message)
            chat_id = chat_thread.chatId
            console.print(escape(f"Group chat created. Thread ID: {chat_id}"))
            console.print(f"Number of invites in chat {chat_id}: {len(user_ids)}")

            # Edit chat settings with retry
            edit_chat_with_retry(
                py_client=py_client,
                chat_id=chat_id,
                title="🩸 Roll play 🩸",
                announcement="http://aminoapps.com/c/Tslyh502",
                viewOnly=True
            )

        except Exception as e:
            if "blocked" in str(e).lower():
                console.print(escape(f"User blocked you: {e}. Skipping user."))
            else:
                console.print(escape(f"Error creating group chat: {e}"))
        time.sleep(2)

def main():
    # Read profile content from text.txt
    with open('text.txt', 'r') as file:
        profile_content = file.read()

    # Edit profile with the content from text.txt
    py_client.edit_profile(content=profile_content)
    console.print("Profile content updated with text from text.txt.")

    message1 = """
    [cu]Roll play 🥵💋💋
[c]
[c]┉ ┅━━━━━━━━━━┅ ┉
[ic] sex community
[ic] Put a lollipop in my pussy
[c]┉ ┅━━━━━━━━━━┅ ┉
[c]
[c]⏜͡︵͡⏜︵⏜͡︵͡⏜︵⏜͡︵͡
[bc]http://aminoapps.com/c/Tslyh502
[c]︶͜⏝ׅ︶͜  ͝ ︶͜⏝ׅ︶͜  ͝ ︶͜⏝ׅ︶͜  ͝ ︶͜"""
    message2 = """
[cu]Roll play 🥵💋💋
[c]
[c]┉ ┅━━━━━━━━━━┅ ┉
[ic] sex community
[ic] Put a lollipop in my pussy
[c]┉ ┅━━━━━━━━━━┅ ┉
[c]
[c]⏜͡︵͡⏜︵⏜͡︵͡⏜︵⏜͡︵͡
[bc]http://aminoapps.com/c/Tslyh502
[c]︶͜⏝ׅ︶͜  ͝ ︶͜⏝ׅ︶͜  ͝ ︶͜⏝ׅ︶͜  ͝ ︶͜"""

    create_group_chats(py_client, sa_client, message1, message2)

if __name__ == '__main__':
    main()